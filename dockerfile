FROM python:3.9.1

WORKDIR /code
COPY . .
CMD python manage.py migrate && python manage.py collectstatic
RUN pip install -r requirements.txt
