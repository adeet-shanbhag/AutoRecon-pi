import subprocess

def get_whois(target):
    try:
        result = subprocess.check_output(['whois', target], text=True)
        return f"\n🧾 WHOIS Info for {target}:\n{result}"
    except subprocess.CalledProcessError as e:
        return f"[!] WHOIS lookup failed: {e}"
    except FileNotFoundError:
        return "[!] 'whois' tool not found. Please install it to use this module."
