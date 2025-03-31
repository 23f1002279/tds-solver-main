FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    poppler-utils \
    default-jre-headless \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY . .

# Expose any ports your application needs
EXPOSE 8080 8000 8001 8002 8003 

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Command to run the FastAPI application
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]
