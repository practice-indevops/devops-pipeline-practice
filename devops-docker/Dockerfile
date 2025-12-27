
# 1. Use a small Python base image
FROM python:3.12-slim

# 2. Set working directory
WORKDIR /app

# 3. Install system deps (optional but common)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy dependency file first to leverage caching
COPY requirements.txt .

# 5. Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the app
COPY . .

# 7. Expose port (documentation only; not required to run)
EXPOSE 5000

# 8. Default command
CMD ["python", "app.py"]

