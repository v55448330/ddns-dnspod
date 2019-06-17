FROM python:3.7-alpine

WORKDIR /app

RUN pip install requests --no-cache-dir

ADD *.py /app/

CMD [ "python", "ddns.py" ]