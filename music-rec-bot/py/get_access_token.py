import requests
import os
from dotenv import load_dotenv

# This script generates a new access token from Spotify

# Load environment variables from .env file
load_dotenv()

# Spotify client ID and client secret
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Spotify API token endpoint
url = "https://accounts.spotify.com/api/token"

# Request body and headers
data = {
    "grant_type": "client_credentials"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Make the POST request with client credentials
response = requests.post(url, data=data, auth=(CLIENT_ID, CLIENT_SECRET))

# Check if the request was successful
if response.status_code == 200:
    token_data = response.json()
    access_token = token_data["access_token"]
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to get access token: {response.status_code}")
    print(response.json())
