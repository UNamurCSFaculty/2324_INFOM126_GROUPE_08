FROM python:3.8-slim-buster

# make the 'python-docker' the current working dirrectory
WORKDIR /python-docker

# copy project files and folder to the current dirrectory
COPY . .

# install project requirements
RUN pip3 install -r requirements.txt

# install production server
RUN pip3 install waitress

# expose flask API port
EXPOSE 5000

# set command for the image
CMD ["waitress-serve", "--port=5000", "--call", "api:create_app"]
