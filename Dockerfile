FROM python:3.10-slim

# Evita prompts interativos
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependências do sistema necessárias para OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENTRYPOINT ["python", "app.py"]