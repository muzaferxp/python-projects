#===============TODO==================

#list (database)

tasks = []


#create task
def create_task():
    task_title = input("Enter Task : ")
    task_status = "pending"

    task_dict = {
        "id" : len(tasks) + 1,
        "title" : task_title,
        "status" : task_status
    }
    tasks.append(task_dict)

    print("tasks added successfully")
    


#Get all tasks
def get_all_tasks():
    for task in tasks:
        print(task['id'] , task['title']  ,task['status']   )


#Edit task (mark as done)


#change status
def edit_task(id):
    title = input("Enter title: ")
    for i in range(len(tasks)):
        task = tasks[i]

        if id == task['id']:
            task['title'] = title
            tasks[i] = task


#change status
def mark_as_done(id):
    for i in range(len(tasks)):
        task = tasks[i]

        if id == task['id']:
            task['status'] = "completed"
            tasks[i] = task


#Delete task

#change status
def delete_task(id):
    for i in range(len(tasks)):
        task = tasks[i]

        if id == task['id']:
            tasks.remove(task)
            return True



def main():
    print("\n\n\n\n\n\n\n\nselect below option")
    print("1. create task")
    print("2. get all tasks")
    print("3. edit task")
    print("4. mark as done")
    print("5. delete task")
    print("6. Exit")

    option = input("Type (1,2,3 or 4): ")

    if option == "1":
        create_task()
        get_all_tasks()
    elif option == "2":
        get_all_tasks()
    elif option == "3":
        id = int(input("Enter id: "))
        edit_task(id)
        get_all_tasks()
    
    elif option == "4":
        id = int(input("Enter id: "))
        mark_as_done(id)
        get_all_tasks()
    elif option == "5":
        id = int(input("Enter id: "))
        delete_task(id)
        get_all_tasks()
    else:

        return True

    main()


main()