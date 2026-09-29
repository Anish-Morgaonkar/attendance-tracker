print("Welcome to the Attendance Tracker")
class_list = []

while True:
    student_name = input("Enter student name (or type 'quit' to stop): ")
    
    if student_name == 'quit':
        break  
        
    class_list.append(student_name)
    print(student_name + " was added")

print("Final Class List")
print(class_list)

attendance_record = {}
for student in class_list:
    attendance_record[student] = []

date=input("Enter today's date:")
while True:
    print("Daily Tasks" + date)
    print("1 View Attendance")
    print("2 Mark someone Present")
    print("3 marks someone absent")
    print("4 exit")
    print("5 change date")
    
    task = input("Which task to perform between(1-5)")
    
    if task == '1':
        total = len(class_list)
        for i in range(total):
            print(class_list[i] + " attendance:")
            for record in attendance_record[class_list[i]]:
                print("  " + record)
                
    elif task == '2':
        name_to_mark = input("Who is present today")
        
        if name_to_mark in class_list:
            attendance_record[name_to_mark].append(date + " -present")
            print(name_to_mark + " marked present")
        else:
            print("Name not found")
            
    elif task == '3':
        name_to_mark = input("Who is absent today: ")
        
        if name_to_mark in class_list:
            attendance_record[name_to_mark].append(date + " -absent")
            print(name_to_mark + " marked absent")
        else:
            print("Name not found")    
            
    elif task == '4':
        print("thanks")
        break
        
    elif task == '5':
        date = input("Enter new date:")
        print("Date changed")
        
    else:
        print("Wrong number type")