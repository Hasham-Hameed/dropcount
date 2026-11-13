# DropCount

A tiny web app that analyzes a text file. Drop a file onto the page and it instantly shows the number of **characters**, **words** and **lines**.

**Live demo:** https://dropcount-kohl.vercel.app

## Features
- Drag and drop a file or tap to choose one (works on phones too)
- Returns characters, words and lines
- Rejects non-text files with a clear error message
- Responsive layout

## Tech Stack
- **Backend:** Python, FastAPI
- **Frontend:** HTML, CSS, vanilla JavaScript
- **Hosting:** Vercel

## How it works
1. The page sends the dropped file to the `/analyze` endpoint using `fetch` and `FormData`.
2. FastAPI reads the file, decodes it as UTF-8 and counts characters, words and lines.
3. The result is returned as JSON and shown on the page.

## Run locally
```bash
git clone https://github.com/Hasham-Hameed/dropcount.git
cd dropcount
pip install -r requirements.txt
uvicorn main:app --reload
```
Then open http://127.0.0.1:8000

## Project structure
```
dropcount/
  main.py            # FastAPI backend
  requirements.txt
  public/
    index.html       # frontend
```

## Author
Hasham Hameed, [GitHub](https://github.com/Hasham-Hameed)
