import json, re, glob

def extract_json_from_html(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
        m = re.search(r'<script[^>]*id=["\']data["\'][^>]*>([\s\S]*?)</script>', html, re.I)
        if not m:
            return {}
        return json.loads(m.group(1).strip())
    except Exception:
        return {}

def main():
    entries = []
    for file in glob.glob("*_withcover.html"):
        meta = extract_json_from_html(file)
        title = meta.get("album_title") or file.replace("_", " ")
        cover = meta.get("cover") or "image/placeholder.png"
        entries.append({"file": file, "title": title, "cover": cover})

    # Sort alphabetically by title (A–Z)
    entries.sort(key=lambda x: x.get("title","").lower())

    with open("albums.json", "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
