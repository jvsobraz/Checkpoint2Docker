FROM python:3.8-slim-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -ms /bin/bash newuser
RUN chown -R newuser:newuser /app

USER newuser

CMD bash -c "sleep 10000000000000000000000000000000000000000000000000000000 && python main.py"
