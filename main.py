print(r'''
    ___        __        ___                 
   / _ | ___  / /____ __/ (_)__  ___ ___ ___ 
  / __ |/ _ \/ __/ -_) _  / / _ \/ _ `/ -_) _ \
 /_/ |_/_//_/\__/\__/\_,_/_/_//_/\_, /\__/_//_/
                                /___/           
       AutoRecon-Pi by Adeet Shanbhag
''')

from modules import scan, whois_lookup, dns_enum, http_analyzer, subdomain_finder

target = input("Enter target domain or IP: ")

scan.run_nmap(target)
whois_lookup.get_whois(target)
dns_enum.dns_lookup(target)
http_analyzer.check_headers(target)
subdomain_finder.find_subdomains(target)
