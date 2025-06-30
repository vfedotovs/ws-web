# 📘 MKDocs Setup Instructions

## 🧪 1. Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 📦 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

> Make sure `mkdocs`, `mkdocs-material`, and any plugins (e.g. `mkdocs-charts-plugin`) are listed in `requirements.txt`.

## ✅ 3. Verify MKDocs installation

```bash
which mkdocs
# Should point to .venv/bin/mkdocs
```

## 🏗️ 4. Build the documentation

```bash
mkdocs build
```

## 🌐 5. Serve documentation locally

```bash
mkdocs serve
```

Then open in your browser:

* [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* or [http://localhost:8000/](http://localhost:8000/)

## 🐳 6. Run with Docker (optional)

Build the image:

```bash
docker build -t mkdocs-site .
```

Serve with Docker Compose:

```bash
docker-compose up
```


## 🧹 7. Cleanup (optional)

```bash
deactivate
rm -rf .venv
```

