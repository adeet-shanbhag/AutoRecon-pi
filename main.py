#!/usr/bin/env python3
# AutoRecon-Pi - Automated Reconnaissance Tool

import argparse
import os
from modules import scan, whois_lookup, dns_enum, http_analyzer, subdomain_finder

BANNER = r"""
   ___         __        ____                      
  / _ | ___ __/ /____ __/ __/_ _____  ___ ________ 
 / __ |/ -_) _  / -_) \ / _// // / _ \/ _ `/ __/ -_)
/_/ |_|\__/\_,_/\__/_\_\/_/ \_,_/_//_/\_,_/_/  \__/ 
             AutoRecon-Pi by Adeet Shanbhag
"""

def save_output(output, filepath):
    with open(filepath, "a") as f:
        f.write(output + "\n\n")

def main():
    parser = argparse.ArgumentParser(description="AutoRecon-Pi: Automated recon script")
    parser.add_argument("--target", help="Target domain or IP", required=True)
    parser.add_argument("--output", help="Output report file", default="report.txt")
    args = parser.parse_args()

    os.system("clear")
    print(BANNER)
    print(f"[*] Starting recon on: {args.target}\n")

    # Clear old report
    with open(args.output, "w") as f:
        f.write(BANNER + "\n")

    # Run modules and save output
    save_output(scan.run_nmap(args.target), args.output)
    save_output(whois_lookup.get_whois(args.target), args.output)
    save_output(dns_enum.dns_lookup(args.target), args.output)
    save_output(http_analyzer.check_headers(args.target), args.output)
    save_output(subdomain_finder.find_subdomains(args.target), args.output)

    print(f"\n[✔] Recon complete. Report saved to: {args.output}")

if __name__ == "__main__":
    main()
