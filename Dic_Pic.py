# print("welcome to hotel management system")
# hotels={
#     'WEEK1':{"MONDAY":'beans',"tuesday":"chicken","wednesday":"rice"},
#     "WEEK2":{"MONDAY":'RICE',"tuesday":"BEAN","wednesday":"CHICKEN"},
#     "WEEK3":{"MONDAY":'RICE',"tuesday":"BEAN","wednesday":"CHICKEN"},
#     "WEEK4":{"MONDAY":'LADY FINGER',"tuesday":"BEAN","wednesday":"CHICKEN"},
#     "WEEK5":{"MONDAY":'RICE',"tuesday":"BEAN","wednesday":"CHICKEN"},
# }
# # print(f"all weeks timetable : {hotels}")

# select=input("ente a week")
# if select=="WEEK1":
#     print(f"First week menu {hotels["WEEK1"]}")
    
# select_day=input("select a day")
# if select_day=="MONDAY":
#     print(f"today only {hotels["WEEK1"]["MONDAY"]}")
    
# if select_day=="tuesday":
#     print(f"today only {hotels["WEEK1"]["tuesday"]}")
    
# if select_day=="wednesday":

#     print(f"today only {hotels["WEEK1"]["wednesday"]}")
    


# elif select=="WEEK2":
#     print(f"2ND week menu {hotels["WEEK2"]}")
    
# select_day=input("select a day")
# if select_day=="MONDAY":
#     print(f"today only {hotels["WEEK2"]["MONDAY"]}")
    
# elif select_day=="tuesday":
#     print(f"today only {hotels["WEEK2"]["tuesday"]}")
    
# elif select_day=="wednesday":
#     print(f"today only {hotels["WEEK2"]["wednesday"]}")

print("welcome to uet peshawar")
dept={"dept_Name":["computer science","mechanical engineering ","electrical engineering"],
      101:{"name":"ali","age":17}
      
      
      }
# dept.update({"mining engineering"})
# dept.pop("dept_id")
# dept.clear()
# dept.copy()
# len(dept)
# type(dept)

dept_NAME=input("enter your department name")
if dept_NAME=="Computer science":
    print("welcome to computer science")


    help_needed=input("what we can  help you")
if help_needed=="yes":
    regno=int(input("enter your registeration no"))
    if  regno==101:
        print(f" It is your detials : {dept[101]}")

        

   








    



