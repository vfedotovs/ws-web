# Docker Compose installation  

This installation method is for test setups and small-scale production setups.

## Requirements
- A host with at least 2 CPU cores and 2 GB of RAM
- Docker
- Docker Compose (Compose v2 is recommended)

## Preparation
To download the latest docker-compose.yml open your terminal and navigate to the directory of your choice. Run the following command:
```bash
git clone https://github.com/vfedotovs/sslv_web_scraper.git .
```

If this is a fresh Web Scraper installation, you need to generate a password and .env file.


Run the following commands to generate a password and write them to your .env file:
```bash
./gen_local_envs.sh
```

## Email configuration (optional but recommended)

It is also recommended to configure email credentials. These are used by Web Scraper to send you daily reports.
Edit .env file with your eamil settings  

# Startup

Afterward, run these commands to finish:
```bash
make build
make up
```

For an explanation about what each service in the docker compose file does, see Architecture.
