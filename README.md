# EFS Volume Demonstration for Convox V2 ECS Racks

This repository showcases a Python application designed to illustrate the use of Amazon EFS volumes with V2 (ECS) racks on Convox, emphasizing the persistent storage capabilities for containerized applications.

> **Note for V2 Racks:** This sample app is specifically tailored for deployment on V2 ECS racks on Convox, highlighting the integration of EFS volumes for persistent storage solutions.

## Structure

- **convox.yml**: Service configuration file that includes the EFS volume (`my-vol`) mount setup at `/data`.
- **Dockerfile**: Creates the Docker environment for the app, using `python:3.9-slim` and copies the app file into the image.
- **app.py**: The application script which periodically writes to and updates files in the `/data` directory to demonstrate EFS volume usage.
