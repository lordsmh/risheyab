import sublist3r
import subprocess
import argparse
import pyfiglet
import time

def display_banner():
    banner = pyfiglet.figlet_format("risheyab")
    print(banner)

def find_subdomains(domain, enable_bruteforce, dns_recon, output_file):
    print(f"Finding subdomains for: {domain}\n")
    start_time = time.time()
    
    # Sublist3r scan
    print("[*] Running Sublist3r...")
    subdomains = sublist3r.main(domain, threads=40, savefile=None, ports=None, silent=True, verbose=False, enable_bruteforce=enable_bruteforce, engines=None)
    print(f"[+] Sublist3r found {len(subdomains)} subdomains.\n")
    
    # DNSRecon scan
    if dns_recon:
        print("[*] Running DNSRecon...\n")
        try:
            dnsrecon_output = subprocess.check_output(["dnsrecon", "-d", domain, "-t", "brt"]).decode()
            dns_recon_count = 0
            for line in dnsrecon_output.splitlines():
                if "A" in line:
                    subdomain = line.split(" ")[-1]
                    if subdomain not in subdomains:
                        subdomains.append(subdomain)
                        dns_recon_count += 1
            print(f"[+] DNSRecon found {dns_recon_count} additional subdomains.\n")
        except subprocess.CalledProcessError as e:
            print(f"[-] Error running dnsrecon: {e}\n")
    
    # MassDNS validation
    print("[*] Validating subdomains with MassDNS...\n")
    with open("/home/smhmosavi/Desktop/resolvers.txt", "r") as f:
        resolvers = f.read().splitlines()
    
    with open("/tmp/subdomains.txt", "w") as f:
        for subdomain in subdomains:
            f.write(subdomain + "\n")
    
    valid_subdomains = []
    try:
        massdns_output = subprocess.check_output(["massdns", "-r", "/home/smhmosavi/Desktop/resolvers.txt", "-t", "A", "-o", "S", "/tmp/subdomains.txt"]).decode()
        for line in massdns_output.splitlines():
            if " A " in line:
                valid_subdomain = line.split(". ")[0]
                if valid_subdomain not in valid_subdomains:
                    valid_subdomains.append(valid_subdomain)
        print(f"[+] MassDNS validated {len(valid_subdomains)} subdomains.\n")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error running massdns: {e}")
        return
    
    # Output results
    if output_file:
        with open(output_file, "w") as f:
            for subdomain in valid_subdomains:
                f.write(subdomain + "\n")
        print(f"[+] Valid subdomains saved to {output_file}")
    else:
        print("\nValid subdomains:")
        for subdomain in valid_subdomains:
            print(subdomain)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\n[+] Scan completed in {elapsed_time:.2f} seconds.")

def main():
    display_banner()
    
    parser = argparse.ArgumentParser(description="Advanced Subdomain Finder")
    parser.add_argument("-d", "--domain", required=True, help="The domain to search for subdomains")
    parser.add_argument("-b", "--bruteforce", "-bf", action="store_true", help="Enable brute-force search with Sublist3r")
    parser.add_argument("--dnsrecon", "-dr", action="store_true", help="Enable DNSRecon search")
    parser.add_argument("-o", "--output", help="Output file to save valid subdomains")

    args = parser.parse_args()
    find_subdomains(args.domain, args.bruteforce, args.dnsrecon, args.output)

if __name__ == "__main__":
    main()
