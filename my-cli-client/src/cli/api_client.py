import click
import requests

API_URL = "http://127.0.0.1:8000"


def test_connection():
    """Function to test connection to the server"""
    response = requests.get(f"{API_URL}/")
    if response.status_code == 200:
        return{"success": True, "message": response.json()}

def create_pipeline(name, description):
    """Function to create a new pipeline."""
    response = requests.post(f"{API_URL}/pipelines/", json={"name": name, "description": description})
    if response.status_code == 200:
        return {"success": True, "message": "Pipeline created successfully!", "data": response.json()}
    else:
        return {"success": False, "message": "Failed to create pipeline."}

def get_pipeline(pipeline_id):
    """Function to get a specific pipeline."""
    response = requests.get(f"{API_URL}/pipelines/{pipeline_id}")
    if response.status_code == 200:
        return {"success": True, "data": response.json()}
    else:
        return {"success": False, "message": "Failed to fetch pipeline details."}

def get_pipelines():
    """Function to get all pipelines"""
    response = requests.get(f"{API_URL}/pipelines/")
    if response.status_code == 200:
        return {"success": True, "data": response.json()}
    else:
        return {"success": False, "message": "Failed to fetch pipeline details."}



    
