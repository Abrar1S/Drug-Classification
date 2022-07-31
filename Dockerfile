# start by pulling the python image
FROM tiangolo/uwsgi-nginx-flask:python3.8

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory & install python libs
WORKDIR /app
RUN pip install -r requirements.txt

# environment
ENV FLASK_APP=main.py

# copy code from current directory
COPY . /app

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]