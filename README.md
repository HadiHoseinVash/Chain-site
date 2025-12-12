Chain Site

This project is the web version of the Chain App. It is built with Django and uses PostgreSQL as the database. The project is fully Docker-based, so you can run it easily without installing Python or other tools on your system.

---

## About the Project

Chain Site is a Django web application that includes the backend and basic frontend of the Chain App. The project is prepared for development with Docker and docker-compose, and it includes all necessary configuration files.

---

## Requirements

Before running the project, make sure you have these installed:

- Docker
- Docker Compose

(You do not need Python if you use Docker.)

---

## How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/HadiHoseinVash/Chain-site.git
   cd Chain-site
2.	Create the environment file:
3.	cp .env.example .env
Edit the values inside .env if needed (for example database name, user, password).
4.	Build and start the containers:
5.	docker-compose up --build
6.	After the containers start, open the website:
7.	http://localhost:8000
The project is now running.

Project Structure
The project contains the following main parts:
•	A Django application inside the src folder
•	A Dockerfile for building the web container
•	A docker-compose.yml file to run the app and database
•	A requirements.txt file for Python dependencies

Technologies Used
•	Django
•	Python
•	PostgreSQL
•	Docker and Docker Compose
•	HTML, CSS, and JavaScript

Useful Docker Commands
Run the project:
docker-compose up
Rebuild the containers:
docker-compose up --build
Enter the Django container:
docker exec -it <container_name>  bash
Run database migrations:
docker-compose exec web python manage.py migrate

Contributing
Feel free to fork the project, make changes, and submit a pull request.
Devops523@gmail.com

License
This project is released under the MIT License.
