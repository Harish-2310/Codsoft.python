#Todo list

tasks = []

def addTask():
  task = input("Please enter a task:")
  tasks.append(task)
  print(f"Task '{task}' added to the List.")

def listTasks():
  if not tasks:
    print("There are no tasks currently.")
  else:
    print("Current Tasks:")
    for index, task in enumerate(tasks):
      print(f"Task # {index}. {task}")   

def deleteTask():
  listTasks()
  try:
    taskToDelete = int(input("Enter the # to delete:"))
    if taskToDelete >=0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} has been removed.")
    else:
      print(f"Task {taskToDelete} was not found.")  
  except:print("Invalid input.")

if __name__ == "__main__":
  print("Wecome to the Todo list app :)")

  while True:
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1.Add the new task")
    print("2.Delete a task")
    print("3.Lists task")
    print("4.Quit")

    choice = input("Enter your choice:")
    if(choice == "1"):
      addTask()
    elif(choice == "2"):
      deleteTask()  
    elif(choice == "3"):
      listTasks()
    elif(choice == "4"):
      break
    else:
      print("Invalid input. Please try again.")
print("Goodbye 👋👋")      

