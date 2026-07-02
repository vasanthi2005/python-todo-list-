tasks=[]
def add_task():
    task=input("Enter your task:")
    tasks.append(task)
    print("Task added succesfully")
    for index,value in enumerate(tasks,start=1):
        print("Current tasks:")
        print(f'{index}.{value}')

def view_task():
    if len(tasks)==0:
        print("No tasks to show")
    else:
        for index,value in enumerate(tasks, start=1):
            print(f"{index}. {value}")

def delete_task():
    task=int(input("Enter the task number to delete:"))
    if 1<=task<=len(tasks):
        tasks.pop(task-1)
        print("Task deleted successfully")
    else:
        print("Invalid task number")

def exit_program():
    print("Thank you for using the To-Do List!")
        
while True:
    print("TO DO LIST")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")
    number=int(input("Enter your choice:"))
    if number==1:
        add_task()
    elif number==2:
        view_task()
    elif number==3:
        delete_task()
    else:
        exit_program()
        break
