FROM python:latest
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    libgdal-dev \
    binutils \
    libproj-dev \
    postgresql-client \
    wget \
    build-essential \
    cmake \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . /app/

CMD ["sh", "entrypoint.sh"]
