
FROM python:3.11.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

EXPOSE 8000

WORKDIR /URL_Checker

COPY req.txt /URL_Checker/req.txt
RUN pip install --no-cache-dir -r req.txt

COPY . /URL_Checker/