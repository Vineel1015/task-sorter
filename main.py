# import modules
import uuid
import sys

# constants
TASK_LIST = []

# create a task object that has taskID, taskName, taskDate

class taskObject:

  def __init__(self, task_name, task_date, ):
    self.task_name = task_name
    self.task_date = task_date
    self.taskID = uuid.uuid4()

  def __str__(self):
    return self.task_name

#initial prompt user will recieve

def initial_prompt():
  print('''
    == TO-DO LIST ==
    [1] show tasks
    [2] add tasks
    [3] complete task
    [4] exit
        ''')
  while True:
    try:
      user_input = int(input("Your choice: "))
      return user_input
    except Exception as e:
        print("Error Detected: "+e)
    

#prints a list of tasks that are yet to be done

def show_tasks(task_list):
  print("[YOUR TASKS]")
  if len(task_list) >= 1:
    for item in task_list:
      print(f'{item.taskID}|{item.task_name}|{item.task_date}')
  else:
    print("Empty List")

#adds a task
def add_task(task_list): 
  print(["ADD TASK"])
  task_name = str(input("What is the task?"))
  task_date = str(input("What is the deadline"))
  task_list.append(taskObject(task_name,task_date))

#completes and removes the task for the task list
def complete_task(task_list):
  if len(task_list) >= 1:
    for item in task_list:
      print(f'{item.taskID} | {item.task_name} | {item.task_date}')
    taskID_to_delete = input("Enter id to complete: ")
    try:
      taskID_to_delete_uuid = uuid.UUID(taskID_to_delete.replace(" ", ""))
      for item in task_list:
        if item.taskID == taskID_to_delete_uuid:
          index = task_list.index(item)
          del task_list[index]
          break
      else:
        print("Task ID not found")
    except Exception as e:
      print("Error Detected: "+e)
  else:
    print("Empty List")


while True:
  # prompts the user
  user_input = initial_prompt()
  
  try:
    if user_input == 1:
      show_tasks(TASK_LIST)
    elif user_input == 2:
      add_task(TASK_LIST)
    elif user_input == 3:
      complete_task(TASK_LIST)
    elif user_input == 4:
      sys.exit(1)

  except Exception as e:
    print("Error detected: " + e)
  
      
