#!/usr/bin/python3
"""
This script exports user-specific task data to JSON format.
Usage: ./script.py <user_id>
"""

import requests
import sys
import json

def main():
    """
    The main function for retrieving user-specific data and exporting it to a JSON file.
    """
    id = sys.argv[1]  # Get the user ID from the command-line argument
    base_url = 'https://jsonplaceholder.typicode.com'
    user_endpoint = f'/users?id={id}'
    todos_endpoint = f'/todos?userId={id}'

    # Retrieve user information
    user_data = requests.get(f'{base_url}{user_endpoint}').json()
    username = user_data[0].get("username")

    # Retrieve user's task data
    todos_data = requests.get(f'{base_url}{todos_endpoint}').json()

    # Organize data into a dictionary
    user_tasks = {
        "username": username,
        "tasks": [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            for todo in todos_data
        ]
    }

    # Create a JSON file and write the data to it
    all_employees_data = {}
    all_employees_data[id] = user_tasks
    with open('todo_all_employees.json', 'a') as json_file:
        json.dump(all_employees_data, json_file)

if __name__ == "__main__":
    main()

