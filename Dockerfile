FROM python:3.12-slim

WORKDIR Simple-DjangoApp/AnimeView

COPY requirements.txt .

RUN pip3 install -r requirements.txt 

COPY . .

WORKDIR AnimeView

RUN python manage.py migrate 

CMD [ "python3","manage.py","runserver","0.0.0.0:8000" ]

EXPOSE 8000