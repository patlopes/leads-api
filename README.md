# Documentation

This API is responsible for managing leads:

Leads are forms that contain the following fields:
- first_name
- last_name
- email
- resume

# Design
## Initial Concept
<img src="https://github.com/patlopes/leads-api/blob/main/doc/backend-arch.jpg" alt="Design" width="500"/>
Before starting the project, I created a design that would guide me in the development of the API.
The idea was also to create a highly scalable and maintainable code.

In this concept we would have:
- API: responsible for managing the leads
- Keycloak: responsible for managing authentication and authorization
- Postgres: responsible for storing the leads
- Minio: responsible for storing the resumes (Minio is an S3 compatible storage)
- Celery: responsible for processing the emails

## Actual Design
<img src="https://github.com/patlopes/leads-api/blob/main/doc/backend-arch-as-is.jpg" alt="Design" width="500"/>
Given the deadline and the complexity of the project, I decided to simplify the design.
The final design is composed of:
- API: responsible for managing the leads and authentication
- Postgres: responsible for storing the leads
- Minio: responsible for storing the resumes
- API (BackgroundTasks): responsible for processing the emails

## Clean Architecture
<img src="https://github.com/patlopes/leads-api/blob/main/doc/clean-simplified.png" alt="Design" width="500"/>
I used the Clean Architecture to create the project structure.
The focus was to create a easy-to-maintain and scalable code.

folder structure:
```
.
├── app
│   ├── auth
├── data
│   ├── clients
│   ├── model
│   ├── repository
├── infrastructure
├── interface
│   ├── controllers
│   └── schemas
```
I explain more about each layer in there respective README.md

# How to run
## Requirements
- Docker
- Docker Compose

## Steps
1. Clone the repository
2. Create a .env file in the root of the project with the variables similar to the example.env file
3. For the signed urls to work, you need to add the following line to your /etc/hosts file:
```
127.0.0.1   object-storage
```
This is necessary for the signed urls to work correctly.
4. Run the following command on the project root folder:
```
docker-compose up --build
```
5. The API will be available at http://localhost:8000
6. The documentation will be available at http://localhost:8000/docs