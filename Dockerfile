FROM python:3.12

WORKDIR /app

RUN apt update && apt install -y \
    wget \
    xvfb \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libgtk-3-0 \
    libgdk-pixbuf2.0-0 \
    libatk1.0-0 \
    libasound2 \
    libdbus-1-3 \
    libnss3 \
    libnspr4 \
    libgbm1 \
    && apt clean

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    playwright install chromium

COPY screenshot_script.py .

CMD xvfb-run -a python /app/screenshot_script.py
