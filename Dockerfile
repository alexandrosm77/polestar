FROM python:3.7-alpine
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
ENTRYPOINT ["python3"]
RUN python manage.py migrate
RUN python manage.py import_csv positions.csv
CMD ["manage.py", "runserver", "0.0.0.0:8000"]