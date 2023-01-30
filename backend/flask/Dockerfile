FROM python:3.10-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./
RUN ["pip3", "install", "-r", "requirements.txt"]

ADD src /
ENTRYPOINT ["python3", "-W", "ignore", "-m"]