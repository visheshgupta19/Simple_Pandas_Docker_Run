# Simple Pandas CSV Analyzer in Docker

This project is a lightweight Flask application that allows users to upload CSV files and receive basic data analysis results. The application is containerized using Docker and comes with a Makefile for easy building, running, and managing the Docker image. Additionally, a CI/CD pipeline is configured to automatically build and push the Docker image to Docker Hub.

## Project Structure

- Dockerfile
- Makefile
- app.py
- requirements.txt
- .gitignore
- .github/workflows/docker-ci.yml

## Dockerfile

The Dockerfile defines the environment for the Flask application:
- Uses Python 3.9 slim image for a lightweight environment.
- Sets `/app` as the working directory.
- Copies all project files into the container.
- Installs required Python packages from `requirements.txt`.
- Exposes port 5000 for the Flask app.
- Sets the `FLASK_APP` environment variable.
- Runs the Flask server on container start.

## Makefile

The Makefile simplifies Docker workflow:
- `make build` → builds the Docker image.
- `make run` → runs the container mapping host port 5003 to container port 5000.
- `make clean` → removes the Docker image.
- `make image_show` / `make container_show` → inspect images and containers.
- `make push` → pushes the image to Docker Hub.
- `make login` → logs into Docker Hub.

## Flask App

The Flask app provides a simple CSV upload and analysis interface:
- Upload CSV files via a web form.
- Generates basic numeric statistics using pandas.
- Displays results as an HTML table.
- Handles errors gracefully if CSV cannot be processed.

## .gitignore

Prevents sensitive environment variables from being committed:
- `.env`

## CI/CD Pipeline

The GitHub Actions pipeline automatically builds and pushes the Docker image on each push to the `main` branch:
- Checks out the code.
- Logs into Docker Hub using secrets.
- Builds the Docker image using `make build`.
- Pushes the image to Docker Hub.

## How to Use

1. Build the Docker image using `make build`.
2. Run the container using `make run` and access the app at `http://localhost:5003`.
3. Upload a CSV and view summary statistics.
4. Clean up images with `make clean`.
5. Push to Docker Hub with `make push`.

## Summary

This project demonstrates:
- Containerizing Python Flask applications with Docker.
- Using a Makefile to simplify Docker commands.
- Building a simple CSV analysis web app with Pandas.
- Automating Docker image builds and pushes with GitHub Actions CI/CD.

