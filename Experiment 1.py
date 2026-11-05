name=input("Enter Student Name")
n=int(input("Enter Number of Subject:"))
total=0

for i in range(1,n+1):
    mark=float(input(f"Enter mark for Subject{i}:"))
    total+=mark
    percentage=total/n

if percentage>=90:
    Grade="A+"
    Performance="Outstanding"
elif percentage>=80:
    Grade="A"
    Performance="Excelent"
elif percentage>=70:
    Grade="B"
    Performance="Very Good"
elif percentage>=60:
    Grade="C"
    Performance="Good"
elif percentage>=50:
    Grade="D"
    Performance="Average"
else:
    Grade="F"
    Performance="Need Improvement"

print("\n---Acadamic Performance---")
print("Student Name:",name)
print("Total Marks:",total)
print("Percentage:",round(percentage,2),"%")
print("Grade:",Grade)
print("Performance:",Performance)




