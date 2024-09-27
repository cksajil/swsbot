import yaml
import requests


# def load_api_key():
#     with open("api_key.yaml") as file:
#         config = yaml.safe_load(file)
#     return config


# config = load_api_key()


# API_TOKEN = config["api_key"]

RSS_TOKEN = "05a8c276b835fb33349a1aa46a0906fc1b2a9573f7bff2b579194bab71b88672"
PROJECT_ID = 144

BASE_URL = "https://openproject.icfoss.org/api/v3"  # Replace with your actual base URL
HEADERS = {"Authorization": f"Bearer {RSS_TOKEN}", "Content-Type": "application/json"}


def get_projects():
    url = f"{BASE_URL}/projects?access_token={RSS_TOKEN}"  # Include the token in the query parameters
    response = requests.get(url)

    print(f"Projects Test - Status Code: {response.status_code}")
    print(f"Response: {response.text}")  # Print the response text for debugging


# Run the test
get_projects()
