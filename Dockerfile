FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./myblog ./app

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]

# EXPOSE 8000

# CMD [ "gunicorn", "myblog.wsgi:application", "--bind 0.0.0.0:8000" ]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]