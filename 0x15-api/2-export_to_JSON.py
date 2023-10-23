import json
import requests
import sys

# API endpoint for fetching user data
url = 'https://jsonplaceholder.typicode.com/users/'

# Check if a user ID was provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 export_to_JSON.py <USER_ID>")
    sys.exit(1)

user_id = sys.argv[1]

# Fetch the user data using the provided user_id
response = requests.get(url + user_id)

if response.status_code != 200:
    print(f"Failed to fetch user data for user ID {user_id}")
    sys.exit(1)

user_data = response.json()
username = user_data['username']

# Fetch the tasks for the user
response = requests.get(url + user_id + '/todos')

if response.status_code != 200:
    print(f"Failed to fetch tasks for user ID {user_id}")
    sys.exit(1)

tasks = response.json()

# Create a dictionary to store the user's tasks
user_tasks = {
    user_id: [{"task": task['title'], "completed": task['completed'], "username": username} for task in tasks]
}

# Create a JSON file with the user's tasks
file_name = f"{user_id}.json"

with open(file_name, 'w') as json_file:
    json.dump(user_tasks, json_file, indent=4)

print(f"Tasks for user {user_id} have been exported to {file_name}")
)
