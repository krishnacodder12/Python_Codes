l=[]
def add_task():
    a=input("Enter your task for add:\n")
    l.append(a)

def remove_task():
    b=input("Enter your task for remove:\n ")
    l.remove(b)
    
def view_all_task():
    for i in l:
        print(i)
while(True):
    print("Avialables are:- add,remove,view")
    c=input("Choose your task:\n")
    if c=="add":
        add_task()
        print("Your task is added successfully Done")
    elif c=="remove":
        remove_task()
        print("Your task is removed successfully Done")

    elif c=="view":
        view_all_task()
        print("your task is listed successfully done")
        count=input("Do you want to continue?")
        if count=="no":
            print("bye")
            break
    else:
        print("You are choosing wrong task")


