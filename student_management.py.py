import os
file_name="student,txt"
def calculate_marks(marks):
    if(marks>90):
        print("A")
    elif(marks>80):
         print("B+")
    elif(marks>70):
         print("C+")
    elif(marks>60):
         print("D+")
    else:
         return "E"
def view_student():
    if not os.path.exists(file_name):
        print("not found")
        return
    print("USN,name,marks,grade")
    with open(file_name,"r") as f:
          for line in f:
              print(USN,name,marks,grade)

def delete_student():
    key=input("enter USN to delete:")
    fount=False
    new_lines=[]
    if not os.path.exists(file_name):
        print("not found")
        return
    with open(file_name,"r") as f:
        for line in f:
            if USN!=key:
                new_lines.append(line)
            else:
                found=True

    with open(file_name,"w") as f:
        for line in new_lines:
            f.write(line)

delete_student()
                
    


