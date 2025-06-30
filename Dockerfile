FROM python:3.9-slim-buster

# Install required tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /docs

# Install MkDocs and dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install mkdocs mkdocs-material mkdocs-charts-plugin

# Create a non-root user
RUN useradd -m mkdocs
USER mkdocs

# Default command
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]

