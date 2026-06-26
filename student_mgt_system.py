account={}
def create_account():
    print("\n =======Create_Account========")

    Name=input("Enter your full name=")
    email_id=input("Enter your email id=")
    password=input("Enter your password=")
    print("---------------------------------")
    print("create account sucessfully")
    print("---------------------------------")
    

    account[password]={
       "Name":Name,
       "email_id":email_id,
       "password":password
    }
    
    

student={}
def login():
    print("\n============Login=========")
    
    password=input("Enter your Password number=")
    if password in account:
          print("---------------------------------")
          print("Login successfully!!!")
 
          while True:
            print("\n MENU")

            print("1.Add")
            print("2.View")
            print("3.Search")
            print("4.Update")
            print("5.Delete")
            print("6.Exit")

            choice=int (input("Enter your choice="))
            if choice==1:
               print("------------Add the student information------------")
            # Stu_id=random.randint()
               
               roll_no=int(input("Enter student Roll number="))
               name=input("Enter student name=")
               age=int(input("Enter student Age="))
               course=input("Enter student course name=")
               contact_no=int(input("Enter contact number="))

               student[roll_no]={
                  "roll_no":roll_no,
                  "name":name,
                  "age":age,
                  "course":course,
                  "contact_no":contact_no
               }
            elif choice==2:
               print("----------- Student information-----------")
               for key, value in student[roll_no].items():
                  print("\n",key,":",value)

            elif choice==3:
               print("----------- Search student informatiion ------------")
               roll_no=int(input(" Enter Search student roll number= "))
               if roll_no in student:
                  for key, value in student[roll_no].items():
                     print(key,":",value)
               else:
                  print("student not found")

            elif choice==4:
               print("------------ Update student information -----------")
               roll_no=int(input("Enter roll number to update="))
               if roll_no in student:
                  student[roll_no]["roll_no"]=int(input("New Roll number="))
                  student[roll_no]["name"]=input("New name=")
                  student[roll_no]["age"]=input("New age=")
                  student[roll_no]["course"]=input("New course=")
                  student[roll_no]["contact_no"]=input("New contact_no=")
               else:
                  print("student not found")


            elif choice==5:
               print("------------ Delete student information -----------")
               roll_no=int(input(" Enter delete student roll number= "))
               if roll_no in student:
                  del student[roll_no]
                  print("Student deleted successfully")
               else:
                  print("Student not found")

            elif choice==6:
               print("thanks")
               break

            else:
               print("invalid choice")

    else:
       print("incrrect password")
      
   

print("========== WELLCOME TO STUDENT MGT SYSTEM ===========")
while True:
   
   print("1.create Account")
   print("2.Login")
   print("3.Exit")

   choice=int(input("Enter your choice="))
   
   if choice==1:
       create_account()

   elif choice==2:
      login()

   elif choice==3:
      print("Thank you for visit website!!")
      break


   else:
       print("invalid choice")
      