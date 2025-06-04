import requests

def check_headers(target):
    if not target.startswith("http"):
        target = "http://" + target
    try:
        response = requests.get(target, timeout=5)
        headers = "\n".join(f"{k}: {v}" for k, v in response.headers.items())
        return f"\n📡 HTTP Headers for {target}:\n{headers}"
    except requests.RequestException as e:
        return f"[!] HTTP header check failed: {e}"
