# app/Dockerfile
# Start with a base image
#FROM python:3-onbuild
# Copy our application code


#WORKDIR /var/app
#COPY . .
#COPY requirements.txt .
# Fetch app specific dependencies

#FROM python:3.8.5-slim-buster
FROM python:3.6-slim
COPY ./app.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./decryption.py /deploy/
WORKDIR /deploy/
RUN apt-get update && apt-get install -y gcc
RUN pip3 install -r requirements.txt
RUN pip3 install flask
RUN pip3 install gunicorn
RUN pip3 install --upgrade pip
RUN apt-get install -y gunicorn
RUN apt-get install -y python-gevent
#ENTRYPOINT ["python3"]

# Expose port
EXPOSE 5000
# Start the app
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]


