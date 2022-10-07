# Airplanes or Automobiles - Dockerized Flask Application

This is a Flask version of the image classification application, dockerized and deployed on Heroku - https://github.com/VincentLu91/airplanes_or_cars

This is a case study to compare between deployment methods based on the framework applied to each version - Streamlit and Flask.

Dockerized/Flask Heroku app link: https://airplanes-or-cars-docker-flask.herokuapp.com/

Docker repo: https://hub.docker.com/repository/docker/vincelu299/airplanes-or-cars-docker-flask

Like its Streamlit counterpart, it is limited to resizing images of a certain size - 224 * 224 * 3.

I have written up a blog post on the IG Content Generator in great detail here: https://vincentlu91.github.io/2020/07/06/Image-Classification-Planes-or-Automobiles.html

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

To use the data app, upload an image. Some examples include:

![airplane](https://user-images.githubusercontent.com/3411100/194626766-72180dec-c48f-4aa4-a607-11df01c1c8e8.jpg)

![car](https://user-images.githubusercontent.com/3411100/194626816-6684532d-c547-4749-b224-574fac0d939e.jpg)

![graphicstock-an-african-american-fat-man-holding-tray-with-fast-food-young-smiling-man-having-a-lunch-in-a-fast-food-restaurant-happy-plump-man-with-fast-food-vector-flat-design-illustration-square-layout_SXqB-sL8W_thumb](https://user-images.githubusercontent.com/3411100/194626830-7b99e260-e6f6-4493-b6c8-4e6ca53896e1.jpg)


Data app in action:

![Screen Shot 2022-10-07 at 2 49 40 PM](https://user-images.githubusercontent.com/3411100/194630287-f9a474e4-262f-4bd8-a258-0f69b568608b.jpg)
