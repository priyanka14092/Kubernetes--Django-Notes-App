FROM python:3.9-alpine3.15
WORKDIR /notes_app
COPY /requirements.txt /notes_app/
RUN pip install -r requirements.txt
COPY . /notes_app/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]