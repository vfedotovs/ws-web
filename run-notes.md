

# app folder is where compose needs files to execute
➜  st-pywalk tree
.
├── Dockerfile
├── Dockerfile-orig
├── app
│   ├── app.py
│   └── removed_ads_table_22_04_23.csv
├── app.py
├── docker-compose.yaml
├── removed_ads_table_22_04_23.csv
└── requirements.txt

# How to start web up using docker compose without building
2 directories, 8 files
➜  st-pywalk #docker compose up -d


# requires locally buit image
➜  st-pywalk cat docker-compose.yaml
version: '3.8'

services:
  sslv-st-web:
    image: st-web-3:latest-arm # Use the specified Docker image
    ports:
      - "8501:8501"
    volumes:
      - ./app:/app  # Mount your Streamlit app directory into the container
    environment:
      - STREAMLIT_SERVER_PORT=8501  # Set the port for the Streamlit server


