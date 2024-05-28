
import sublist3r
import subprocess
import os
import argparse
import pyfiglet

def display_banner():
    banner = pyfiglet.figlet_format("Lord_smh")
    print(banner)

def find_subdomains(domain, enable_bruteforce, dns_recon, output_file):

    subdomains = sublist3r.main(domain, 40, output=None, ports=None, silent=True, verbose=False, enable_bruteforce=enable_bruteforce, engines=None)
    
    if dns_recon:

        dnsrecon_output = subprocess.check_output(["dnsrecon", "-d", domain, "-t", "brt"]).decode()
        for line in dnsrecon_output.splitlines():
            if "A" in line:
                subdomain = line.split(" ")[-1]
                if subdomain not in subdomains:
                    subdomains.append(subdomain)
    
    with open("/tmp/subdomains.txt", "w") as f:
        for subdomain in subdomains:
            f.write(subdomain + "\n")
    
    massdns_output = subprocess.check_output(["massdns", "-r", "massdns/lists/resolvers.txt", "-t", "A", "-o", "S", "/tmp/subdomains.txt"]).decode()
    valid_subdomains = []
    for line in massdns_output.splitlines():
        if " A " in line:
            valid_subdomain = line.split(". ")[0]
            if valid_subdomain not in valid_subdomains:
                valid_subdomains.append(valid_subdomain)
    
    if output_file:
        with open(output_file, "w") as f:
            for subdomain in valid_subdomains:
                f.write(subdomain + "\n")
    else:
        for subdomain in valid_subdomains:
            print(subdomain)

def main():
    display_banner()
    
    parser = argparse.ArgumentParser(description="Advanced Subdomain Finder")
    parser.add_argument("domain", help="The domain to search for subdomains")
    parser.add_argument("-b", "--bruteforce", action="store_true", help="Enable brute-force search with Sublist3r")
    parser.add_argument("-d", "--dnsrecon", action="store_true", help="Enable DNSRecon search")
    parser.add_argument("-o", "--output", help="Output file to save valid subdomains")

    args = parser.parse_args()
    find_subdomains(args.domain, args.bruteforce, args.dnsrecon, args.output)

if __name__ == "__main__":
    main()

