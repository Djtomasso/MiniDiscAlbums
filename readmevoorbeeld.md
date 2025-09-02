# MiniDiscAlbums — Album Bibliotheek

Deze repository bevat een online bibliotheek van albums (tracklists) die automatisch zichtbaar worden via **GitHub Pages**.

## 📂 Structuur
- **index.html** → startpagina van de bibliotheek (laadt `albums.json`).
- **albums.json** → manifest met alle albums (wordt automatisch bijgewerkt via GitHub Actions).
- **image/** → map met albumhoezen + `placeholder.png` (fallback).
- **`*_withcover.html`** → losse albumpagina’s (één per album, met embedded tracklist).

## 🚀 Publiceren
1. Upload een nieuwe albumpagina (`*_withcover.html`) in de **root** van de repo.
2. Upload de bijbehorende hoes (`.png`) in de **image/** map.
3. Commit en push naar `main`.
4. De GitHub Action draait automatisch en past **albums.json** aan.
5. Binnen enkele minuten verschijnt het album op de online indexpagina.

## ⚙️ Automatische updates (GitHub Actions)
- Workflow-bestand: `.github/workflows/build-index.yml`
- Script: `.github/scripts/generate_albums.py`
- Deze zorgen dat `albums.json` **altijd up-to-date** is en alfabetisch gesorteerd wordt.

## 🔗 Online bekijken
De bibliotheek staat live op:  
`https://<jouw-gebruikersnaam>.github.io/MiniDiscAlbums/`

(voor jou: [https://djtomasso.github.io/MiniDiscAlbums/](https://djtomasso.github.io/MiniDiscAlbums/))

---

## 📖 Voorbeeld: nieuw album toevoegen

Stel je wilt het album **"Michael Jackson — Dangerous"** toevoegen.

1. Maak een CSV met de tracklist en genereer daar een HTML-pagina van (bijv.  
   `michael-jackson-dangerous_withcover.html`).  
   Deze bevat alle tracks + links (YouTube zoek + Wikipedia).

2. Maak een coverafbeelding, noem deze bijv.  
   `michael-jackson-dangerous.png`.

3. Upload de bestanden:
   - Zet `michael-jackson-dangerous_withcover.html` in de **root** van de repo.  
   - Zet `michael-jackson-dangerous.png` in de map **image/**.

4. Commit en push naar GitHub.

5. De GitHub Action draait automatisch en werkt `albums.json` bij.  
   Binnen een paar minuten staat het nieuwe album in de **indexpagina**.

---

## ℹ️ Handige tips
- Zet altijd de albumcover in `image/` en gebruik **dezelfde naam** als in de HTML (bijv. `image/eros-sempre-eros-una.png`).  
- Als een cover ontbreekt of fout is, toont de index automatisch `image/placeholder.png`.  
- Nieuwe albumpagina’s moeten de suffix **`_withcover.html`** hebben om opgenomen te worden.  
- De index sorteert albums **alfabetisch** op titel.

---

✍️ **Samengesteld door Tomasso 2025**
