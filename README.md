# Portrait
A simple app to demonstrate Facebook Login. 


### Getting started

This project was developed using Python(Django)/Js/HTML/CSS and makes use of a CDN for development.

##Docker
To develop and/or run this application, download and install [docker](https://www.docker.com/get-started) and [docker-compose](https://docs.docker.com/compose/install/) from their website before proceeding.

Run the command `docker-compose up` from the **root directory** i.e. where you have the `docker-compose.yml` file and you should be good to go.

`docker-compose down` or `CMD/ctrl + C` to stop the application.

`docker-compose build` to build the application and `docker-compose up --build`  to build and run the application in one commnand. :)

##Services
The application consists of two(2) services: Web and Database These services are coupled together using the `docker-compose.yml` file at the root of the application.

- Django comes with an `Admin` dashboard by default, so I took advantage of that to create an admin user for convinience. To view the admin dashboard after starting up the application, navigate to the `/admin` route and login using the details below
```
Username: devadmin
password: nimda
```

###### RUNNING THE APP
Once you have the application running locally using `docker-compose up` from the **root directory** navigate to the homepage `http://localhost:8000/` to take the app for a spin. `:)` the facebook app is in development mode and only recognises url originating from `http://localhost:8000/` and not `http://127.0.0.1:8000/` or `http://0.0.0.0:8000/`
