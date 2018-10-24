FROM python:3.6

ENV FLASK_APP app.py
ENV FLASK_ENV production
ENV FLASK_DEBUG 0

WORKDIR /app

ADD encuestas.db /app/
ADD EncuestasDatabase.py /app/
ADD app.py /app/
ADD requirements.txt /app/

RUN pip install -r requirements.txt
ENTRYPOINT ["flask", "run"]
CMD ["--host=0.0.0.0", "--port=8085"]

EXPOSE 8085