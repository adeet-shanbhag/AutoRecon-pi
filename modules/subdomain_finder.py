import subprocess

def find_subdomains(target):
    wordlist = "wordlists/subdomains.txt"  # Customize your wordlist path here
    try:
        with open(wordlist, 'r') as f:
            subdomains = f.read().splitlines()

        found = []
        for sub in subdomains:
            url = f"{sub}.{target}"
            try:
                subprocess.check_output(["ping", "-c", "1", url], stderr=subprocess.DEVNULL)
                found.append(url)
            except subprocess.CalledProcessError:
                pass

        if found:
            return f"\n🔎 Subdomains Found:\n" + "\n".join(found)
        else:
            return f"\n🔎 Subdomains Found:\nNo active subdomains found."

    except FileNotFoundError:
        return "[!] Subdomain wordlist not found. Please add wordlists/subdomains.txt"
