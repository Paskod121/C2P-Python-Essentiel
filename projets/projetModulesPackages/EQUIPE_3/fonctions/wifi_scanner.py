import subprocess

def run_wifi():
    print("\n=== Scanner WiFi ===")
    print("Scan en cours...")
    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "networks"],
            capture_output=True,
            text=True,
            encoding= 'utf-8')
        if result.returncode != 0:
            print("Erreur de scan")
            return
        lines = result.stdout.splitlines()
        ssids = []
        for line in lines:
            if "SSID" in line and ":" in line:
                ssid = line.split(":", 1)[1].strip()
                if ssid:
                    ssids.append(ssid)
        if ssids:
            for i, ssid in enumerate(ssids, 1):
                print(f"{i}. {ssid}")
            print(f"Total : {len(ssids)} réseaux")
        else:
            print("Aucun réseau détecté")
    except Exception as e:
        print("Erreur de scan")
