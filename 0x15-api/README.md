# 0x15. API

## Description
What you should learn from this project:

* What Bash scripting should not be used for
* What is an API
* What is a REST API
* What are microservices
* What is the CSV format
* What is the JSON format
* Pythonic Package and module name style
* Pythonic Class name style
* Pythonic Variable name style
* Pythonic Function name style
* Pythonic Constant name style
* Significance of CapWords or CamelCase in Python

## Requirements

- All files are created and executed on Ubuntu 14.04 LTS using Python3 (version 3.4.3)
- All Python code use the PEP 8 style (version 1.7.\*)

## Tasks

### [0. Gather data from an API](./0-gather_data_from_an_API.py)

- Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
  - You must use urllib or requests module
  - The script must accept an integer as a parameter, which is the employee ID
  - The script must display on the standard output the employee TODO list progress in this exact format:
    - First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
      - EMPLOYEE_NAME: name of the employee
      - NUMBER_OF_DONE_TASKS: number of completed tasks
      - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
    - Second and N next lines display the title of completed tasks: Tab TASK_TITLE (with 1 tabulation + 1 space before)


### [1. Export to CSV](./1-export_to_CSV.py)
* Using what you did in the task #0, extend your Python script to export data in the CSV format.
- Records all tasks that are owned by this employee
  - Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
  - File name must be: USER_ID.csv

### [2. Export to JSON](./2-export_to_JSON.py)
* Using what you did in the task #0, extend your Python script to export data in the JSON format.
- Records all tasks that are owned by this employee
  - Format must be: { "USER_ID": [ {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}
  - File name must be: USER_ID.json

### [3. Dictionary of list of dictionaries](./3-dictionary_of_list_of_dictionaries.py)
* Using what you did in the task #0, extend your Python script to export data in the JSON format.
  - Records all tasks from all employees
  - Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
  - File name must be: todo_all_employees.json

---

## Author
* **Van Phan** - [vdphan](https://github.com/vdphan)
