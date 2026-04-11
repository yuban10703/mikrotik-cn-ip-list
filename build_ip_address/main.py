import requests

URL = "https://github.com/DustinWin/ruleset_geodata/releases/download/sing-box-ruleset/cnip.json"
OUTPUT_FILE = "cn_ipv4_script.rsc"

def download_json(url):
    print(f"涓嬭浇 {url} ...")
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def generate_script(ip_list):
    lines = [
        '/log info "Loading CN ipv4 address list"',
        '/ip firewall address-list remove [/ip firewall address-list find list=CN]',
        '/ip firewall address-list'
    ]
    for ip in ip_list:
        if ":" in ip:
            continue
        lines.append(f':do {{ add address={ip} list=CN }} on-error={{}}')
    return "\n".join(lines)

def main():
    data = download_json(URL)
    ip_list = data.get("rules", {})[0].get("ip_cidr", {})
    if not ip_list:
        print("鏈壘鍒颁换浣?IP 缃戞銆?)
        return
    script = generate_script(ip_list)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(script)
    print(f"鑴氭湰宸蹭繚瀛樺埌 {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
