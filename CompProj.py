import mysql.connector
import csv

# Connect to the database
passwd=input("To make sure it is you, please enter the password: ")
try:
    conobj=mysql.connector.connect(host="localhost",user="root",password=passwd, database="comp_proj")
    print("Connected Successfully!")
    cur=conobj.cursor()
except:
    print("Connection Failed! Try checking your password.")
    exit()


#Function Definitions

 
def addstudentrecord(): 
    query="select * from Student_file"
    cur.execute(query)
    entries=cur.fetchall()
    if len(entries)==0:
        ano=1000
    else:
        ano=entries[-1][0]+1

    
    Rno=int(input("Enter Roll Number: "))
    classs=int(input("Enter Class: "))
    section=input("Enter Section: ")
    name=input("Enter Name: ")
    dob=input("Enter Date of Birth in YYYY-MM-DD format: ")
    mname=input("Enter Mother's Name: ")
    fname=input("Enter Father's Name: ")
    phone=int(input("Enter Phone Number: "))
    gender=input("Enter gender (M or F): ")
    stream_code=(input("Enter Stream Code: "))
    query="insert into Student_file values({},{},{},'{}','{}','{}','{}','{}',{},'{}','{}')".format(ano,Rno,classs,section,name,dob,mname,fname,phone,gender,stream_code)
    cur.execute(query)
    conobj.commit()
    print("Record Inserted Successfully")
    print("Admission Number: ",ano)
    print("-----------------------------------------")
    choice=input("Do you want to add more records? (Y/N): ")
    if choice=="Y" or choice=="y":
        addstudentrecord()
    

def deletestudentrecord():
    ano=int(input("Enter Admission Number of the Student: "))
    query="select * from Student_file where Ano={}".format(ano)
    cur.execute(query)
    data=cur.fetchall()
    if data==[]:
        print("Record not found!")
        x=input("Press Enter to continue...")
        return
    choice=input("Are you sure you want to delete the record and marks? (Y/N): ")
    if choice=="Y" or choice=="y":
        query1="delete from Student_file where ano={}".format(ano)
        cur.execute(query1)
        query2="delete from Result_file where ano={}".format(ano)
        cur.execute(query2)
        conobj.commit()
        print("Record Deleted Successfully")
        print("-----------------------------------------")
        choice=input("Do you want to delete more records? (Y/N): ")
        if choice=="Y" or choice=="y":
            deletestudentrecord()
    else:
        print("Record Deletion Cancelled")
        print("-----------------------------------------")
    

def modifyrecord():
    ano=int(input("Enter Admission Number of the Student: "))
    check_query="select * from Student_file where Ano={}".format(ano)
    cur.execute(check_query)
    data=cur.fetchall()
    if data==[]:
        print("Record not found!")
        x=input("Press Enter to continue...")
        return
    print("1. Modify Roll Number")
    print("2. Modify Class")
    print("3. Modify Section")
    print("4. Modify Name")
    print("5. Modify Date of Birth")
    print("6. Modify Mother's Name")
    print("7. Modify Father's Name")
    print("8. Modify Phone Number")
    print("9. Modify gender")
    print("10. Modify Stream Code")
    choice=int(input("Enter your choice: "))
    if choice==1:
        Rno=int(input("Enter new Roll Number: "))
        query="update Student_file set Rno={} where ano={}".format(Rno,ano)
    elif choice==2:
        classs=int(input("Enter new Class: "))
        query="update Student_file set class={} where ano={}".format(classs,ano)
    elif choice==3:
        section=input("Enter new Section: ")
        query="update Student_file set Section='{}' where ano={}".format(section,ano)
    elif choice==4:
        name=input("Enter new Name: ")
        query="update Student_file set name='{}' where ano={}".format(name,ano)
    elif choice==5:
        dob=input("Enter new Date of Birth in YYYY-MM-DD format: ")
        query="update Student_file set Dob='{}' where ano={}".format(dob,ano)
    elif choice==6:
        mname=input("Enter new Mother's Name: ")
        query="update Student_file set Mname='{}' where ano={}".format(mname,ano)
    elif choice==7:
        fname=input("Enter new Father's Name: ")
        query="update Student_file set Fname='{}' where ano={}".format(fname,ano)
    elif choice==8:
        phone=int(input("Enter new Phone Number: "))
        query="update Student_file set phone={} where ano={}".format(phone,ano)
    elif choice==9:
        gender=input("Enter new gender (M or F): ")
        query="update Student_file set gender='{}' where ano={}".format(gender,ano)
    elif choice==10:
        stream_code=input("Enter new Stream Code: ")
        query="update Student_file set StreamCode='{}' where ano={}".format(stream_code,ano)
    cur.execute(query)
    conobj.commit()
    print("Record Modified Successfully!")
    print("-----------------------------------------")
    choice=input("Do you want to modify more records? (Y/N): ")
    if choice=="Y" or choice=="y":
        modifyrecord()



def enterMarks():
    ano=int(input("Enter Admission Number of the Student: "))
    check_Student_file_query="select * from Student_file where Ano={}".format(ano)
    cur.execute(check_Student_file_query)
    data1=cur.fetchall()
    if data1==[]:
        print("Record not found!")
        x=input("Press Enter to continue...")
        return
    check_Result_file_query="select * from Result_file where Ano={}".format(ano)
    cur.execute(check_Result_file_query)
    data2=cur.fetchall()
    if data2!=[]:
        print("Marks already entered for this student!")
        x=input("Press Enter to continue...")
        return
    query="select Rno from Student_file where Ano={}".format(ano)
    cur.execute(query)
    Rno=cur.fetchone()[0]
    query2="select name from Student_file where Ano={}".format(ano)
    cur.execute(query2)
    name=cur.fetchone()[0]
    query3="select StreamCode from Student_file where Ano={}".format(ano)
    cur.execute(query3)
    stream_code=cur.fetchone()[0]
    SE_Subjects=['Physics','Chemistry','Mathematics','Economics']
    SC_Subjects=['Physics','Chemistry','Mathematics','Computer Science']
    SB_Subjects=['Physics','Chemistry','Mathematics','Biology']
    CM_Subjects=['Economics','Accountancy','Business Studies','Mathematics']
    CI_Subjects=['Economics','Accountancy','Business Studies','Informatics Practices']
    HU_Subjects=['History','Geography','Economics','Political Science']

    if stream_code=="SE":
        subject2=SE_Subjects[0]
        subject3=SE_Subjects[1]
        subject4=SE_Subjects[2]
        subject5=SE_Subjects[3]
    elif stream_code=="SC":
        subject2=SC_Subjects[0]
        subject3=SC_Subjects[1]
        subject4=SC_Subjects[2]
        subject5=SC_Subjects[3]
    elif stream_code=="SB":
        subject2=SB_Subjects[0]
        subject3=SB_Subjects[1]
        subject4=SB_Subjects[2]
        subject5=SB_Subjects[3]
    elif stream_code=="CM":
        subject2=CM_Subjects[0]
        subject3=CM_Subjects[1]
        subject4=CM_Subjects[2]
        subject5=CM_Subjects[3]
    elif stream_code=="CI":
        subject2=CI_Subjects[0]
        subject3=CI_Subjects[1]
        subject4=CI_Subjects[2]
        subject5=CI_Subjects[3]
    elif stream_code=="HU":
        subject2=HU_Subjects[0]
        subject3=HU_Subjects[1]
        subject4=HU_Subjects[2]
        subject5=HU_Subjects[3]

    



    sub1mks=int(input("Enter Marks in English: "))
    grade1=input("Enter Grade in English: ")
    sub2mks=int(input(f"Enter Marks in {subject2}: "))
    grade2=input(f"Enter Grade in {subject2}: ")
    sub3mks=int(input(f"Enter Marks in {subject3}: "))
    grade3=input(f"Enter Grade in {subject3}: ")
    sub4mks=int(input(f"Enter Marks in {subject4}: "))
    grade4=input(f"Enter Grade in {subject4}: ")
    sub5mks=int(input(f"Enter Marks in {subject5}: "))
    grade5=input(f"Enter Grade in {subject5}: ")
    total=sub1mks+sub2mks+sub3mks+sub4mks+sub5mks
    avg=total/5
    L=[sub1mks,sub2mks,sub3mks,sub4mks,sub5mks]
    count_of_greater_than_33=0
    for i in L:
        if i>33:
            count_of_greater_than_33+=1
        if count_of_greater_than_33==5:
            if total>=60:
                div="I"
            elif total>=45:
                div="II"
            else:
                div="III"
        elif count_of_greater_than_33==4:
            div='CO'
        else:
            div='FA'

    query="insert into Result_file values({},{},'{}',{},'{}',{},'{}',{},'{}',{},'{}',{},'{}',{},{},'{}')".format(ano,Rno,name,sub1mks,grade1,sub2mks,grade2,sub3mks,grade3,sub4mks,grade4,sub5mks,grade5,total,avg,div)
    cur.execute(query)
    conobj.commit()
    print("Marks Entered Successfully!")
    print("-----------------------------------------")
    choice=input("Do you want to enter more marks? (Y/N): ")
    if choice=="Y" or choice=="y":
        enterMarks()

    

def viewStudentDetails():
    ano=int(input("Enter Admission Number of the Student: "))
    query="select * from Student_file where Ano={}".format(ano)
    cur.execute(query)
    details=cur.fetchall()
    if details==[]:
        print("Record not found!")
        x=input("Press Enter to continue...")
        return
    
    print("---------------------------------STUDENT DETAILS---------------------------------")
    print("Admission Number: ",ano)
    print("Roll Number: ",details[0][1])
    print("Class: ",details[0][2])
    print("Section: ",details[0][3])
    print("Name: ",details[0][4])
    print("Date of Birth: ",details[0][5])
    print("Mother's Name: ",details[0][6])
    print("Father's Name: ",details[0][7])
    print("Phone Number: ",details[0][8])
    print("Gender: ",details[0][9])
    print("Stream Code: ",details[0][10])
    print("---------------------------------------------------------------------------------")
    x=input("Press Enter to continue...")

def generateStreamWiseStudentInfo():
    stream_code=input("Enter Stream Code: ")
    if stream_code not in ['SE','SC','SB','CM','CI','HU']:
        print("Invalid Stream Code!")
        x=input("Press Enter to continue...")
        return
    
    query="select * from Student_file where StreamCode='{}'".format(stream_code)
    cur.execute(query)
    details=cur.fetchall()
    if details==[]:
        print("No records found for this Stream!")
        x=input("Press Enter to continue...")
        return
    print("=======================================================")
    for i in details:
        print("Admission Number: ",i[0])
        print("Roll Number: ",i[1])
        print("Class: ",i[2])
        print("Section: ",i[3])
        print("Name: ",i[4])
        print("Date of Birth: ",i[5])
        print("Mother's Name: ",i[6])
        print("Father's Name: ",i[7])
        print("Phone Number: ",i[8])
        print("Gender: ",i[9])
        print("Stream Code: ",i[10])
        print("=======================================================")
    x=input("Press Enter to continue...")
    

def generateStreamWiseResultList():
    stream_code=input("Enter Stream Code: ")
    if stream_code not in ['SE','SC','SB','CM','CI','HU']:
        print("Invalid Stream Code!")
        x=input("Press Enter to continue...")
        return
    query="select * from Result_file NATURAL JOIN Student_file where StreamCode='{}'".format(stream_code)
    cur.execute(query)
    details=cur.fetchall()
    if details==[]:
        print("No records found for this Stream!")
        x=input("Press Enter to continue...")
        return
    print("=======================================================")
    for i in details:
        print("Admission Number: ",i[0])
        print("Roll Number: ",i[1])
        print("Name: ",i[2])
        print("English: ",i[3],"-",i[4])
        if stream_code=="SE":
            print("Physics: ",i[5],"-",i[6])
            print("Chemistry: ",i[7],"-",i[8])
            print("Mathematics: ",i[9],"-",i[10])
            print("Economics: ",i[11],"-",i[12])
        elif stream_code=="SC":
            print("Physics: ",i[5],"-",i[6])
            print("Chemistry: ",i[7],"-",i[8])
            print("Mathematics: ",i[9],"-",i[10])
            print("Computer Science: ",i[11],"-",i[12])
           
        elif stream_code=="SB":
            print("Physics: ",i[5],"-",i[6])
            print("Chemistry: ",i[7],"-",i[8])
            print("Mathematics: ",i[9],"-",i[10])
            print("Biology: ",i[11],"-",i[12])
           
        elif stream_code=="CM":
            print("Economics: ",i[5],"-",i[6])
            print("Accountancy: ",i[7],"-",i[8])
            print("Business Studies: ",i[9],"-",i[10])
            print("Mathematics: ",i[11],"-",i[12])
            
        elif stream_code=="CI":
            print("Economics: ",i[5],"-",i[6])
            print("Accountancy: ",i[7],"-",i[8])
            print("Business Studies: ",i[9],"-",i[10])
            print("Informatics Practices: ",i[11],"-",i[12])
           
        elif stream_code=="HU":
            print("History: ",i[5],"-",i[6])
            print("Geography: ",i[7],"-",i[8])
            print("Economics: ",i[9],"-",i[10])
            print("Political Science: ",i[11],"-",i[12])
        print("Total Marks: ",i[13])
        print("Average: ",i[14])
        print("Division: ",i[15])
        print("=======================================================")
    x=input("Press Enter to continue...")
            



def generateMarkSheet():
    ano=int(input("Enter the Admission No: "))
    query1="select * from Student_file where ano={}".format(ano)
    cur.execute(query1)
    data1=cur.fetchall()
    query2="select * from Result_file where ano={}".format(ano)
    cur.execute(query2)
    data2=cur.fetchall()
    if data1==[] or data2==[]:
        print("Record not found!")
        x=input("Press Enter to continue...")
        return
    stream_code=data1[0][10]
    print("-----------------------------------------------------------")

    print("          SECOND TERMINAL EXAMINATION 2024          ")
    print("Admission No: ",ano,"               ","Roll No: ",data1[0][1])
    print("Name: ", data1[0][4],"               ","Class: ",data1[0][2],"-",data1[0][3])
    print("Stream: ",data1[0][10],"               ","DOB: ",data1[0][5])
    print("-----------------------------------------------------------")
    print("Subject      MAX     MARKS     GRADE")
    print("-----------------------------------------------------------")
    print("English      100     ",data2[0][3],"       ",data2[0][4])
    if stream_code=="SE":
        print("Physics      100     ",data2[0][5],"       ",data2[0][6])
        print("Chemistry    100     ",data2[0][7],"       ",data2[0][8])
        print("Mathematics  100     ",data2[0][9],"       ",data2[0][10])
        print("Economics    100     ",data2[0][11],"       ",data2[0][12])
    elif stream_code=="SC":
        print("Physics      100     ",data2[0][5],"       ",data2[0][6])
        print("Chemistry    100     ",data2[0][7],"       ",data2[0][8])
        print("Mathematics  100     ",data2[0][9],"       ",data2[0][10])
        print("Computer Sci 100     ",data2[0][11],"       ",data2[0][12])
    elif stream_code=="SB":
        print("Physics      100     ",data2[0][5],"       ",data2[0][6])
        print("Chemistry    100     ",data2[0][7],"       ",data2[0][8])
        print("Mathematics  100     ",data2[0][9],"       ",data2[0][10])
        print("Biology      100     ",data2[0][11],"       ",data2[0][12])
    elif stream_code=="CM":
        print("Economics    100     ",data2[0][5],"       ",data2[0][6])
        print("Accountancy  100     ",data2[0][7],"       ",data2[0][8])
        print("Business St  100     ",data2[0][9],"       ",data2[0][10])
        print("Mathematics  100     ",data2[0][11],"       ",data2[0][12])
    elif stream_code=="CI":
        print("Economics    100     ",data2[0][5],"       ",data2[0][6])
        print("Accountancy  100     ",data2[0][7],"       ",data2[0][8])
        print("Business St  100     ",data2[0][9],"       ",data2[0][10])
        print("Informatics  100     ",data2[0][11],"       ",data2[0][12])
    elif stream_code=="HU":
        print("History      100     ",data2[0][5],"       ",data2[0][6])
        print("Geography    100     ",data2[0][7],"       ",data2[0][8])
        print("Economics    100     ",data2[0][9],"       ",data2[0][10])
        print("Pol Science  100     ",data2[0][11],"       ",data2[0][12])
    print("-----------------------------------------------------------")
    percentage=(data2[0][13]/500)*100
    print("Total Marks: ",data2[0][13],"               ","Percentage: ",percentage,"               ","Division: ",data2[0][15])
    print("-----------------------------------------------------------")
    print("Class Teacher","               ","Principal")
    x=input("Press Enter to continue...")

def copyReportCardToCSV():
    ano=int(input("Enter Admission Number of the Student: "))
    check_Student_file_query="select * from Student_file where Ano={}".format(ano)
    cur.execute(check_Student_file_query)
    checkdata1=cur.fetchall()
    if checkdata1==[]:
        print("Record not found!")
        print("-----------------------------------------")
        x=input("Press Enter to continue...")
        return
    check_Result_file_query="select * from Result_file where Ano={}".format(ano)
    cur.execute(check_Result_file_query)
    checkdata2=cur.fetchall()
    if checkdata2==[]:
        print("Marks not entered for this student! Cannot generate Report Card!")
        print("-----------------------------------------")
        x=input("Press Enter to continue...")
        return
    
    filename="ReportCard"+str(ano)+".csv"
    file=open(filename,"w",newline="")
    cw=csv.writer(file,delimiter=",")
    query="select * from Student_file where Ano={}".format(ano)
    cur.execute(query)
    data=cur.fetchall()
    query2="select * from Result_file where Ano={}".format(ano)
    cur.execute(query2)
    data2=cur.fetchall()
    stream_code=data[0][10]
    cw.writerow(["SECOND TERMINAL EXAMINATION 2024"])
    cw.writerow([["Admission No: "],ano,"Roll No: ",data[0][1]])
    cw.writerow(["Name: ", data[0][4],"Class: ",data[0][2],data[0][3]])
    cw.writerow(["Stream: ",stream_code,"DOB: ",data[0][5]])
    cw.writerow(["Subject","MAX","MARKS","GRADE"])
    cw.writerow(["English",100,data2[0][3],data2[0][4]])
    if stream_code=="SE":
        cw.writerow(["Physics",100,data2[0][5],data2[0][6]])
        cw.writerow(["Chemistry",100,data2[0][7],data2[0][8]])
        cw.writerow(["Mathematics",100,data2[0][9],data2[0][10]])
        cw.writerow(["Economics",100,data2[0][11],data2[0][12]])
    elif stream_code=="SC":
        cw.writerow(["Physics",100,data2[0][5],data2[0][6]])
        cw.writerow(["Chemistry",100,data2[0][7],data2[0][8]])
        cw.writerow(["Mathematics",100,data2[0][9],data2[0][10]])
        cw.writerow(["Computer Science",100,data2[0][11],data2[0][12]])
    elif stream_code=="SB":
        cw.writerow(["Physics",100,data2[0][5],data2[0][6]])
        cw.writerow(["Chemistry",100,data2[0][7],data2[0][8]])
        cw.writerow(["Mathematics",100,data2[0][9],data2[0][10]])
        cw.writerow(["Biology",100,data2[0][11],data2[0][12]])
    elif stream_code=="CM":
        cw.writerow(["Economics",100,data2[0][5],data2[0][6]])
        cw.writerow(["Accountancy",100,data2[0][7],data2[0][8]])
        cw.writerow(["Business Studies",100,data2[0][9],data2[0][10]])
        cw.writerow(["Mathematics",100,data2[0][11],data2[0][12]])
    elif stream_code=="CI":
        cw.writerow(["Economics",100,data2[0][5],data2[0][6]])
        cw.writerow(["Accountancy",100,data2[0][7],data2[0][8]])
        cw.writerow(["Business Studies",100,data2[0][9],data2[0][10]])
        cw.writerow(["Informatics Practices",100,data2[0][11],data2[0][12]])
    elif stream_code=="HU":
        cw.writerow(["History",100,data2[0][5],data2[0][6]])
        cw.writerow(["Geography",100,data2[0][7],data2[0][8]])
        cw.writerow(["Economics",100,data2[0][9],data2[0][10]])
        cw.writerow(["Political Science",100,data2[0][11],data2[0][12]])
    cw.writerow(["Total Marks: ",data2[0][13],"Percentage: ",((data2[0][13]/500)*100),"Division: ",data2[0][15]])
    file.close()
    print("Report Card Copied to CSV Successfully!")
    x=input("Press Enter to continue...")


def advanced():
    query=input("Enter the query: ")
    try:
        cur.execute(query)
    except:
        print("An error occurred! Please check your query.")
        return
    if query.split()[0].lower()=="select":
        data=cur.fetchall()
        for i in data:
            print(i)
    else:
        conobj.commit()
        print("Query Executed Successfully!")

#Main Code

while True:
    print("***********************************WELCOME TO THE EXAM MANAGEMENT SYSTEM***********************************")
    print("1. Add Student Record")
    print("2. Delete Student Record")
    print("3. Modify Student Record")
    print("4. Enter Marks")
    print("5. View Student Details")
    print("6. Generate Stream Wise Student Information")
    print("7. Generate Stream Wise Result List")
    print("8. Generate Mark Sheet")
    print("9. Copy Report Card to CSV")
    print("10. Advanced")
    print("11. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        addstudentrecord()
    elif choice==2:
        deletestudentrecord()
    elif choice==3:
        modifyrecord()
    elif choice==4:
        enterMarks()
    elif choice==5:
        viewStudentDetails()
    elif choice==6:
        generateStreamWiseStudentInfo()
    elif choice==7:
        generateStreamWiseResultList()
    elif choice==8:
        generateMarkSheet()
    elif choice==9:
        copyReportCardToCSV()
    elif choice==10:
        advanced()
    elif choice==11:
        print("Thank you for using the system!")
        break
    else:
        print("Invalid Choice! Please Try Again")

conobj.close()