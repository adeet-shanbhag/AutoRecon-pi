import subprocess

def run_nmap(target):
    try:
        result = subprocess.check_output(['nmap', '-sV', '-T4', target], text=True)
        return f"\n🔍 Nmap Scan for {target}:\n{result}"
    except subprocess.CalledProcessError as e:
        return f"[!] Nmap scan failed: {e}"
    except FileNotFoundError:
        return "[!] Nmap is not installed. Please install it to use this module."
