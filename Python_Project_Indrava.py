import os
import csv
import subprocess
path='C:/Python_Project_main-folder'
#All the Functions used Throughout the code
def createfile(name,lst):
    with open(f'{path}/{name}','a',newline='')as f:
        script= csv.writer(f)
        script.writerow(lst)
        print(f"{name} file has been UPDATED")

def percent(num):
    if stream.lower()=='cse' or stream.lower()=='cseai' or stream.lower()=='cseaiml' or stream.lower()=='cseiotcsbs':
        num=(num*100)//600
    elif stream.lower()=='it' or stream.lower()=='ece' or stream.lower()=='me':
        num=(num*100)//500
    return num
    

def grade(num):
    if num>=90:
        return("Outstanding Performance... You have passed the exam with grade A.")
    elif num<90 and num>=80:
        return("Excellent Performance... You have passed the exam with grade B.")
    elif num<80 and num>=70:
        return("Good Performance... You have passed the exam with grade C.")
    elif num<70 and num>=60:
        return("Your performance is average... Work hard... You have passed the exam with grade D.")
    elif num<60 and num>=50:
        return("Your performance is below average... There is massive scope of improvement... You have barely passed the exam with grade E.")
    else:
        return("Extremely poor performance... You have Failed the Exam and got F.")

def count(lst):
    num=0
    for i in lst:
        if str(type(i))=="<class 'int'>":
            num+=1
        else:
            pass
    return num
        

def add(lst):
    plus=0
    for i in lst:
        try:
            plus+=i
        except:
            pass
    return plus

def duplicate(file,attr,pos=0):
    with open(f'{path}/{file}','r') as f:
        reader = csv.reader(f)
        dup_lst=[]
        for i in reader:
            dup_lst+=[i[pos]]
    if attr in dup_lst:
        return True
    else:
        return False

def choice(stream):
    if stream.lower()=='cse' or stream.lower()=='cseai' or stream.lower()=='cseaiml' or stream.lower()=='cseiotcsbs':
        return ("C001:C002:C003:C004:C005:C006")
    elif stream.lower()=='it' or stream.lower()=='ece' or stream.lower()=='me':
        return ("C002:C003:C004:C005:C006")

def get_batch():
    with open(f'C:/Python_Project_main-folder/Batch.csv','r') as f:
        reader=csv.reader(f)
        rows=[row for row in reader]
        column=[]
        for i in range(len(rows)):
            if i==0:
                pass
            else:
                column+=[rows[i][0]]
    return column
def remove(string):
    with open(f'C:/Python_Project_main-folder/Student.csv','r+',newline='') as f:
        script=csv.reader(f)
        rows=[row for row in script]
        for i in rows:
            if i[0]==string:
                rows[rows.index(i)]=['','','','']   
            else:
                pass
        f.seek(0)
        f.truncate()
        writer=csv.writer(f)
        writer.writerows(rows)


#Creation of Folder and all the Modules recquired...    
try:
    os.makedirs(f'{path}/ReportCards')
    message=True
except:
    message=False

while message:
    createfile('Batch.csv',['Batch ID','Batch Name','Department Name','List of Courses','List of Students'])
    createfile('Course.csv',['Course ID','Course Name','Marks Obtained'])
    with open(f'{path}/Course.csv','a',newline='')as f:
        script= csv.writer(f)
        script.writerow(['C001','Python Programming'])
        script.writerow(['C002','Math'])
        script.writerow(['C003','Physics'])
        script.writerow(['C004','Chemistry'])
        script.writerow(['C005','Biology'])
        script.writerow(['C006','English'])
    createfile('Department.csv',['Department ID','Department Name','List of Batches'])
    with open(f'{path}/Department.csv','a',newline='')as f:
        script= csv.writer(f)
        script.writerow(['CSE','Computer Sience and Engineering'])
        script.writerow(['CSEAI','Computer Sience and Engineering and Artificial Intelligence'])
        script.writerow(['CSEAIML','Computer Sience and Engineering and Artificial Intelligence and Machine Learning'])
        script.writerow(['CSEIOTCSBS','Computer Sience and Engineering and Internet of Things and Business Studies'])
        script.writerow(['IT','Information Technology'])
        script.writerow(['ECE','Electrical and Communications Engineering'])
        script.writerow(['ME','Mechanical Engineering'])
    createfile('Student.csv',['Student ID','Name','Class Roll Number','Batch ID'])
    createfile('Examination.csv',['Course Name','Student ID','Marks'])
    break

print('\n','Computer Sience and Engineering : CSE','\n',
      'Computer Sience and Engineering and Artificial Intelligence : CSEAI','\n',
      'Computer Sience and Engineering and Artificial Intelligence and Machine Learning : CSEAIML','\n',
      'Computer Sience and Engineering and Internet of Things and Business Studies : CSEIOTCSBS','\n',
      'Information Technology : IT','\n',
      'Electrical and Communications Engineering : ECE','\n',
      'Mechanical Engineering : ME','\n')
print("Please write all the stream name in short form as mentioned above and in capital letters only!!!")
print()
      

student_no=int(input("Enter the no. of students whose data you want to input : "))
print()
print('-'*50)
for i in range(student_no):
    name=input("Enter Student's Name : ")
    batch=input("Which batch they are in (e.g. 2022-26) : ")
    stream=input("Which Stream are you in : ")
    roll=input("What is your Class Roll Number : ")

    batch_id=stream+batch[2:4]
    student_id=batch_id+roll
    batch_name=stream+batch

    if duplicate('Student.csv',student_id,0):
        print("the student is already present in the directory")
        print(f"You can find your report card here : {path}/ReportCards/{student_id}_{name}.txt")
    else:
        print()
        print("The subjects are [Python,Math,Physics,Chemistry,Biology,English]")
        print('please enter the subjects marks in the above mentioned order in a list type and if you dont have a particular subject write there "null" (e.g. [100,100,"null",75,69,85])')
        print('Each Subject is ot of 100 marks')
        print()
        marks_lst=eval(input("Enter the Marks list : "))
        total_marks=add(marks_lst)
        print()
        
        with open(f"{path}/ReportCards/{student_id}_{''.join(name.split())}.txt",'w') as f:

            f.writelines([f'Name of the student : {name} \n',
                          f'Class Roll of the student : {roll} \n',
                          f'Stream of the student : {stream} \n',
                          f'Your Student ID is : {student_id}\n',
                          '\n',
                          f'Marks obtained in Math is : {marks_lst[1]} \n',
                          f'Marks obtained in Python is : {marks_lst[0]} \n',
                          f'Marks obtained in Physics is : {marks_lst[2]} \n',
                          f'Marks obtained in Chemistry is : {marks_lst[3]} \n',
                          f'Marks obtained in Biology is : {marks_lst[4]} \n',
                          f'Marks obtained in English is : {marks_lst[5]} \n',])
            f.write('\n')
            f.write(f'You have got {total_marks} in total with {percent(total_marks)}% out of 600 \n')
            f.write(grade(total_marks/count(marks_lst)))      
        createfile('Student.csv',[student_id,name,roll,batch_id])
        print(f"You can find your report card here : {path}/ReportCards/{student_id}_{''.join(name.split())}.txt")
        openpath=f"{path}/ReportCards/{student_id}_{''.join(name.split())}.txt"
        subprocess.run(['start',openpath], shell=True)

        ask=input("Do you want to remove this name from database now is the time (Y/N) : ")

        if ask.lower()=='n':
            if duplicate('Batch.csv',batch_id,0):
                with open(f'{path}/Batch.csv','r+',newline='') as f:
                    script=csv.reader(f)
                    rows=[row for row in script]
                    for i in rows:
                        if batch_id==i[0]:
                            rows[rows.index(i)][4]+=f':{student_id}'
                    f.seek(0)
                    f.truncate()
                    writer=csv.writer(f)
                    writer.writerows(rows)
                    
                print("Batch.csv has been updated")
            else:
                createfile('Batch.csv',[batch_id,batch_name,stream,choice(stream),student_id])

            with open(f'{path}/Course.csv','r+',newline='') as f:
                script=csv.reader(f)
                rows=[row for row in script]
                for i in range(len(rows)):
                    if i==0:
                        pass
                    else:
                        try:
                            rows[i][2]+=f'{student_id}:{marks_lst[i-1]}-'
                        except:
                            rows[i].append(f'{student_id}:{marks_lst[i-1]}-')
                f.seek(0)
                f.truncate()
                writer=csv.writer(f)
                writer.writerows(rows)
        else:
            remove(student_id)
            subprocess.call("TASKKILL /F /IM notepad.exe", shell=True)
            os.remove(openpath)
            print('Your details have been successfully removed from the directory')
    print('-'*50)
    print()

try:            
    with open(f'{path}/Department.csv','r+',newline='') as f:
        script=csv.reader(f)
        rows=[row for row in script]
        lst=get_batch()
        for i in lst:
            for j in rows:
                if i[0:-2]==j[0]:
                    try:
                        if i in j[2]:
                            pass
                        else:
                            rows[rows.index(j)][2]+=f'{i}:'
                    except:
                        rows[rows.index(j)].append(f'{i}:')
                    break
        f.seek(0)
        f.truncate()
        writer=csv.writer(f)
        writer.writerows(rows)
            
except:
    print("Nothing to add in Department.csv")



#Creation of the Graphs...

last=input("Press Enter to exit")
subprocess.call("TASKKILL /F /IM notepad.exe", shell=True)
