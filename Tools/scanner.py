import socket
import nmap
import csv
import requests

def scanner_of_ports(ip, ports):
    """Open port scan with socket."""
    port_open = []
    print(f"Ports scan for the adress {ip}")
    for port in ports:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(1)  # Time limit for each connection
            result = client.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is open")
                port_open.append(port)
            client.close()
        except Exception as e:
            print(f"Error for the port {port}: {e}")
    return port_open

def scan_avanced(ip):
    """Avanced scan with Nmap."""
    nm = nmap.PortScanner()
    nm.scan(hosts=ip, arguments="-sV --script vuln")
    scan_results = []
    for host in nm.all_hosts():
        for protocol in nm[host].all_protocols():
            ports = nm[host][protocol].keys()
            for port in ports:
                service = nm[host][protocol][port]['name']
                state = nm[host][protocol][port]['state']
                vulnerabilities = nm[host][protocol][port].get('script', {})
                scan_results.append({
                    "host": host,
                    "port": port,
                    "service": service,
                    "status": state,
                    "vulnerabilities": vulnerabilities
                })
    return scan_results

def check_cve(service_name, version):
    """Checks vulnerabilities with the Vulners API."""
    api_url = "https://vulners.com/api/v3/search/lucene/"
    query = f"{service_name} {version}"
    try:
        response = requests.post(api_url, json={"query": query})
        if response.status_code == 200:
            data = response.json()
            if data['data']['total'] > 0:
                return [item['id'] for item in data['data']['search']]
        return []
    except Exception as e:
        print(f"Erreur API CVE: {e}")
        return []

def save_to_csv(results, filename="scan_results.csv"):
    """Save of the results in a CSV file."""
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Host", "Port", "Service", "Status", "Vulnerabilities"])
        for result in results:
            writer.writerow([
                result["host"],
                result["port"],
                result["service"],
                result["status"],
                ", ".join(result.get("vulnerabilities", []))
            ])
    print(f"CSV report saved in {filename}")



def main():
    ip = input("Enter the IP address to scan : ")
    ports = range(20, 1025)  # Ports to scan (20 to 1024)

    # Step 1 : Basic port scan
    ports_open = scanner_of_ports(ip, ports)

    # Step 2 : Avanced scan with Nmap
    scan_results = scan_avanced(ip)

    # Step 3 : Vulnerabilities analyze via CVE
    for result in scan_results:
        service_name = result.get("service", "")
        version = ""  # You can add a version scope if available
        result["vulnerabilities"] = check_cve(service_name, version)

    # Step 4 : Save of results
    save_to_csv(scan_results)
if __name__ == "__main__":
    main()
