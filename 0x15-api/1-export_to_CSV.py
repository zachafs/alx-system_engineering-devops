#!/usr/bin/python3
#better way to export file :

import re
import requests
import sys
import csv

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            emp_req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = emp_req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))

            # Define the CSV file name based on the user ID
            csv_file_name = '{}.csv'.format(id)

            with open(csv_file_name, mode='w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                # Write the CSV header
                csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

                # Write each task to the CSV file
                for task in completed_tasks:
                    csv_writer.writerow([id, emp_name, str(task.get('completed')), task.get('title')])

            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            print(f'CSV data has been saved to {csv_file_name}')

