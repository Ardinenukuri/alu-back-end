#!/usr/bin/python3
"""Module"""

import requests
import sys

# Specify the base URL of the API
base_url = "https://jsonplaceholder.typicode.com/"

# Define a function to retrieve an employee's TODO list progress
def get_employee_todo_progress(employee_id):
    # Send a GET request to retrieve the user's information
    user_response = requests.get(base_url + f"users/{employee_id}")
    user = user_response.json()
    employee_name = user["name"]

    # Send a GET request to retrieve the user's TODO list
    todo_response = requests.get(base_url + f"todos?userId={employee_id}")
    todo_list = todo_response.json()

    # Calculate the number of completed and non-completed tasks
    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task["completed"]]
    num_completed_tasks = len(completed_tasks)

    # Print the employee's TODO list progress in the required format
    print(f"Employee {employee_name} is done with {num_completed_tasks}/{total_tasks} tasks:")

    # Print the titles of the completed tasks
    for task in completed_tasks:
        print(f"\t {task['title']}")

# Get the employee ID from the command line argument
employee_id = int(sys.argv[1])

# Call the function to retrieve the employee's TODO list progress
get_employee_todo_progress(employee_id)

