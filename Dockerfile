FROM python:3.10

ENV DEBIAN_FRONTEND=noninteractive
# ENV PYTHONFAULTHANDLER=1
# ENV PYTHONUNBUFFERED=1
# ENV PYTHONHASHSEED=random
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PIP_DISABLE_PIP_VERSION_CHECK=on
# ENV PIP_DEFAULT_TIMEOUT=100

RUN apt-get update &&\
    apt-get install -y python3 python3-pip build-essential \
    zbar-tools libpq-dev python3-opencv

COPY requirements.txt /app/
WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

CMD python3 /app/bot.py