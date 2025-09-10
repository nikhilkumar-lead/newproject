todo_list=[]

while True:
    print("\n---------TO-DO LIST--------")
    print("1. Add list")
    print("2. view list")
    print("3. delete list")
    print("3. exit")
    choice=input("enter  your choice:")
    if choice =="1":
        task=input("enter your task")
        todo_list.append(task)
        print("task added")
    elif choice == "2":
        if not todo_list:
            print("no task yet")
        else:
            print("your task")
            for i, task in enumerate(todo_list, 1):

                print(f"{i}.{task}")
    elif choice == "3":
        if not todo_list:
            print("no tasks to delete ")
        else:
            print("your tasks :")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task number to delete :"))
                if 1 <= task_num <= len(todo_list):
                    removed_task = todo_list.pop(task_num - 1)
                    print(f"Task'{removed_task}'deleted successfully :")
                else:
                    print("invalid task number.")
            except ValueError:
                print("Please enter a valid number :")
    elif choice =="4":
        print("good bye")
        break
    else:
        print("invalid option try again")

