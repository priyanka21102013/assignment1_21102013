#01 Average of numbers
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
n3=int(input("Enter the third number"))
avg=(n1+n2+n3)/3
print("average of numbers",avg)

#02 income tax
gross_income=int(input("Enter gross income"))
dependent=int(input("number of dependent"))
tax_income=gross_income-10000-(dependent*3000)
tax=tax_income*0.2
print(tax)

#03 order
n1=int(input("Enter number of students"))
odr=["SID","Name","Gender","Course Name","CGPA"]
for j in range(n1):
    nodr=[]
    SID=int(input("Enter SID"))
    Name=input("Enter Name")
    Gender=input("Enter Gender:")#Gender should br F/M and U for unknown
    Course_Name=input("Enter the Course:")
    CGPA=float(input("Enter CGPA:"))
    nodr.append(SID)
    nodr.append(Name)
    nodr.append(Course_Name)
    nodr.append(CGPA)
    print(odr)
    print(nodr)

#04 Marks of students
s1=float(input("Enter marks of first student="))
s2=float(input("Enter marks of second student= "))
s3=float(input("Enter marks of a third student="))
s4=float(input("Enter marks of a four student="))
s5=float(input("Enter marks of a five student="))
slst=[s1,s2,s3,s4,s5]
slst.sort()
print(slst)

#5
   #(a)
color=["Red","Green","White","Black","Pink","Yellow"]
color.pop(3)
print(color)

    #(b)
color[3]="purple"
print(color)
