FROM python:3.10-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update && apt-get install -y \
    gcc \
    libaio1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]

COPY requirements.txt ./
RUN ["pip3", "install", "-r", "requirements.txt"]

ADD src /
ENTRYPOINT ["python3", "-W", "ignore", "-m"]