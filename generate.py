import requests

sources = [
    # Listas públicas legales
    "https://iptv-org.github.io/iptv/index.m3u",
    "https://iptv-org.github.io/iptv/languages/spa.m3u"
]

output = "#EXTM3U\n\n"

for url in sources:
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            output += r.text + "\n"
    except:
        pass

# Guardar lista combinada
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(output)
