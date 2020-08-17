# Airplanes or Automobiles - Dockerized Flask Application

This is a Flask version of the image classification application, dockerized and deployed on Heroku - https://github.com/VincentLu91/airplanes_or_cars

This is a case study to compare between deployment methods based on the framework applied to each version - Streamlit and Flask.

Dockerized/Flask Heroku app link: https://airplanes-or-cars-docker-flask.herokuapp.com/

Docker repo: https://hub.docker.com/repository/docker/vincelu299/airplanes-or-cars-docker-flask

Like its Streamlit counterpart, it is limited to resizing images of a certain size - 224 * 224 * 3.

### You can also set up a Docker container to run the application

You can pull the docker image from the Docker Hub repository:
https://hub.docker.com/repository/docker/vincelu299/airplanes-or-cars-docker-flask

Then:
```
docker run -p 5000:5000 airplanes-or-cars-docker-flask:v1
```

Go to browser and enter: ```http://localhost:5000/```

### Alternatively, you can access the application in development environment

Libraries and their versions are included in requirements.txt. To install the virtual environment, run the following:
```
python3 -m venv env # or python -m venv env
source env/bin/activate
pip3 install -r requirements.txt # or pip install -r requirements.txt
```

At this point the environment should be set up with required libraries to run the application. To run the app, enter:
```
python app.py
```

Then in the browser, enter ```localhost:5000```.

Example of app in use:

![martymcfly](https://user-images.githubusercontent.com/3411100/89757005-0f109400-dab2-11ea-8338-69da014cabd1.png)
