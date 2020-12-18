FROM python:3.7.3

WORKDIR /code
COPY . .
CMD python manage.py migrate && python manage.py collectstatic
RUN pip install -r requirements.txt
