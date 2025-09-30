import os


TASK_FILE = "tasks.txt"
COMPLETED_FILE = "completed.txt"

def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename,"r") as f:
            return[line.strip() for line in f.readlines()]
    return []


def save_task(filename,tasklist):
    with open(filename,"w") as f:
        for task in tasklist:
            f.write(task + "\n")
            

tasks = load_tasks(TASK_FILE)
completed_task = load_tasks(COMPLETED_FILE)
print(completed_task)


print("Todo List")
print("1.To view the task")
print("2.To add a task")
print("3.To remove the task")
print("4.To mark the completed task")
print("5.exit")

tasks = []
completedTask = []

while True:
    try:
        choice = int(input("Enter the choice: "))
        if choice == 1:
            if tasks:
              for i,task in enumerate(tasks,start=1):
                 print(f"{i}.{task}")
            else:
                print("No tasks to view!")
        elif choice == 2:
            addtask = input("Enter the task: ")
            tasks.append(addtask)
            print("Task added sucessfully")
        elif choice == 3:
            if tasks:
                for i,task in enumerate(tasks,start=1):
                  print(f"{i}.{task}")
                removeIndex = int(input("Enter the task to remove: ")) - 1
                try:
                    if 0<= removeIndex < len(tasks):
                        removed = tasks.pop(removeIndex)
                        print(f"Removed task:{removed}")
                    else:
                      print("Invalid task number")
                except ValueError:
                        print("Enter a valid task number")
            else:
                print("No task to remove")
                
        elif choice == 4:
            if tasks:
                for i,task in enumerate(tasks,start=1):
                    print(f"{i}.{task}")
                completedIndex = int(input("Enter the completed task no: ")) - 1
                try:
                    if 0<= completedIndex < len(tasks):
                        completedTask.append(tasks[completedIndex])
                        print(f"Completed task is {tasks[completedIndex]}")
                    else:
                        print("invalid task number")
                except ValueError:
                        print("enter a valid task number")
            else:
                print("No task to add in completed list")
                       
        elif choice == 5:
             print("Exiting the todo list...byeee")
             break
    except ValueError:
        print("Enter a valid choice")
            
                
        