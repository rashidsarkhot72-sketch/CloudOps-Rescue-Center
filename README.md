\# CloudOps Rescue Center



A containerized cloud incident management application built using \*\*Python, Flask, Docker, Amazon ECR, and Amazon ECS Fargate\*\*.



\## Project Overview



CloudOps Rescue Center is designed to simulate a simple cloud operations and incident management system.



Users can submit incidents, while backend services process and manage the incident information.



The project demonstrates how a Flask application can be containerized with Docker and deployed to AWS ECS Fargate.



\## Architecture



```text

User

&#x20; │

&#x20; ▼

Frontend

&#x20; │

&#x20; ▼

Incident API

&#x20; │

&#x20; ▼

Notification Service

&#x20; │

&#x20; ▼

Docker Container

&#x20; │

&#x20; ▼

Amazon ECR

&#x20; │

&#x20; ▼

Amazon ECS Fargate

&#x20; │

&#x20; ▼

Running Flask Application

AWS Services Used

Amazon ECS – Runs the containerized application

AWS Fargate – Serverless compute for ECS containers

Amazon ECR – Stores the Docker container image

Amazon CloudWatch Logs – Monitors application logs

Amazon VPC – Provides network connectivity

Security Groups – Controls network access

Technologies Used

Python

Flask

Docker

AWS ECS Fargate

Amazon ECR

Amazon CloudWatch

Git

GitHub

Project Structure

CloudOps-Rescue-Center/

│

├── frontend/

│   └── index.html

│

├── incident-api/

│   ├── app.py

│   └── requirements.txt

│

├── notification-service/

│   ├── app.py

│   ├── Dockerfile

│   ├── requirements.txt

│   └── screenshots/

│

├── .gitignore

└── README.md

Docker Workflow



The application is containerized using Docker.



Flask Application

&#x20;      │

&#x20;      ▼

&#x20;  Dockerfile

&#x20;      │

&#x20;      ▼

&#x20;Docker Image

&#x20;      │

&#x20;      ▼

&#x20;    ECR

&#x20;      │

&#x20;      ▼

&#x20;ECS Fargate

&#x20;      │

&#x20;      ▼

&#x20;Running Container

ECS Deployment



The application is deployed using:



ECS Cluster: flask-ecs-cluster

ECS Service: flask-ecs-service

Task Definition: flask-ecs-task:1

Launch Type: Fargate

CPU: 0.25 vCPU

Memory: 0.5 GiB

Container Port: 5000

Application Verification



The Flask application successfully runs inside the ECS Fargate container.



The application returns:



Containerized Flask Application



Application is running successfully!

Monitoring



Application logs are available through Amazon CloudWatch Logs.



Example application activity:



GET / HTTP/1.1 200



This confirms that the Flask application received and successfully processed HTTP requests.



Screenshots



Project screenshots are available in:



notification-service/screenshots/



The screenshots demonstrate:



ECS cluster and service

Fargate task

Running ECS task

Flask application

ECS task status

ECS service

ECS networking

ECS logs

Deployment success

ECS cluster overview

ECR Docker image

ECS task definition

Key Learning



This project demonstrates the complete container deployment workflow:



Python Flask

&#x20;    ↓

Docker

&#x20;    ↓

Docker Image

&#x20;    ↓

Amazon ECR

&#x20;    ↓

Amazon ECS

&#x20;    ↓

AWS Fargate

&#x20;    ↓

Running Container

&#x20;    ↓

CloudWatch Logs

Author



Rashid Sarkhot



