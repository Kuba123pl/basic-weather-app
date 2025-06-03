# Basic Weather App

A simple weather API built with FastAPI. This application provides endpoints to get the current temperature and rain status for a given city using Open-Meteo and geocoding APIs.

## Features

- **Get current temperature for any city**  
  `/temperature/{city}` – Returns current temperature in the specified city.

- **Check rain status**  
  `/rain/{city}` – Returns current rain level and weather description for the specified city.

- **Health check endpoint**  
  `/health` – Returns API status.

## Architecture Overview

- **Frontend**  
  The frontend is hosted on **Azure App Service** for scalable and reliable web app delivery.

- **Backend**  
  The FastAPI backend is containerized using Docker and deployed on **Azure Container Apps** for managed, scalable API hosting.

- **Docker Image**  
  The backend is built as a Docker image. This image is published to **Azure Container Registry (ACR)** as part of the deployment workflow.

- **CI/CD Deployment**  
  Automated CI/CD pipelines are used to:
  - Build and push the Docker image to ACR
  - Deploy the backend container to Azure Container Apps
  - Deploy the frontend to Azure App Service

## Installation (Local Development)

1. Clone this repository:
   ```bash
   git clone https://github.com/Kuba123pl/basic-weather-app.git
   cd basic-weather-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Build and run locally with Docker:
   ```bash
   docker build -t weather-api .
   docker run -p 8000:8000 weather-api
   ```

## Usage

Run the API server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### Example requests

- Get temperature:  
  `GET http://127.0.0.1:8000/temperature/London`

- Check rain status:  
  `GET http://127.0.0.1:8000/rain/London`

## Project Structure

- `main.py`: FastAPI application setup and router inclusion.
- `api/routers/city.py`: Contains endpoints for temperature and rain data.
- `requirements.txt`: Required Python dependencies.

