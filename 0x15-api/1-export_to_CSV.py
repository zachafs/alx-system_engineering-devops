#!/usr/bin/python3
"""
This script exports user-specific task data to a CSV file.
Usage: ./script.py <user_id>
"""

import requests
import sys

def main():
    """
    The main function for retrieving user-specific data and exporting it to a CSV file.
    """
    id = sys.argv[1]  # Get the user ID from the command-line argument
    base_url = 'https://jsonplaceholder.typicode.com'
    user_endpoint = f'/users?id={id}'
    todos_endpoint = f'/todos?userId={id}'
    completed_todos_endpoint = f'{todos_endpoint}&completed=true'

    # Retrieve user information
    user_data = requests.get(f'{base_url}{user_endpoint}').json()
    name = user_data[0].get("name")
    username = user_data[0].get("username")

    # Retrieve user's task data
    todos_data = requests.get(f'{base_url}{todos_endpoint}').json()
    completed_todos_data = requests.get(f'{base_url}{completed_todos_endpoint}').json()
    completed_tasks_count = len(completed_todos_data)
    total_tasks_count = len(todos_data)

    # Export data into a CSV file
    with open(f'{id}.csv', 'w') as csv_file:
        for todo in todos_data:
            csv_data = f'"{id}","{username}","{todo.get("completed")}",'
            csv_data += f'"{todo.get("title")}"\n'
            csv_file.write(csv_data)

if __name__ == "__main__":
    main()


