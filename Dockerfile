FROM python:3.7-stretch

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

ENV PORT 5000

EXPOSE ${PORT}

WORKDIR /app/src

CMD [ "uwsgi", "--http=0.0.0.0:5000", "--wsgi-file=main.py", "--callable=app" ]
