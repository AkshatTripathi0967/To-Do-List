Tasks = {}
print("*****To Do List*****\nPress the respective number in front of the operation you want to perform")

def Add_task():
    Input_task = input("Enter the Task :")
    Tasks[Input_task]= "Undone"
def Show_Tasks():
    if len(Tasks)==0:
        print("No Undone Tasks")
    else:
        for key,value in Tasks.items():
           print(f"{key} : {value}")
def Mark_the_task():
    b= input("Enter the Task :")
    Tasks[b]= "Done"
def Delete():
    Input= input("Enter the Task :")
    del Tasks[Input]
while (True):
    print("Add Task : 1\nShow Tasks : 2\nMark the task Done : 3\nDelete : 4\nExit : 5")
    Number = int(input("Input the number : "))
    if Number == 1:
        Add_task()
        Show_Tasks()
    elif Number == 2:
        Show_Tasks()
    elif Number == 3:
        Mark_the_task()
        Show_Tasks()
    elif Number == 4:
        Delete()
        Show_Tasks()
    elif Number == 5:
        break
    else:
        print("Invalid Number")
        break


 


