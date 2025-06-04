import subprocess

def dns_lookup(target):
    try:
        result = subprocess.check_output(['nslookup', target], text=True)
        return f"\n🌐 DNS Lookup for {target}:\n{result}"
    except subprocess.CalledProcessError as e:
        return f"[!] DNS lookup failed: {e}"
    except FileNotFoundError:
        return "[!] 'nslookup' is not available. Please install or use a compatible DNS tool."
