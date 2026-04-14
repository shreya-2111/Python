fail=0 #count fail subject
fm=0 # count failing  marks 

print("\n---------User Input--------\n")

sub1=int(input("Enter the marks of first subject: "))
if sub1<40:
	fail=fail+1
	fm=fm+(40-sub1)
	
sub2=int(input("\nEnter the marks of second subject: "))
if sub2<40:
	fail=fail+1
	fm=fm+(40-sub2)
	
sub3=int(input("\nEnter the marks of third subject: "))
if sub3<40:
	fail=fail+1
	fm=fm+(40-sub3)
	
sub4=int(input("\nEnter the marks of fourth subject: "))
if sub4<40:
	fail=fail+1
	fm=fm+(40-sub4)
	
sub5=int(input("\nEnter the marks of fifth subject: "))
if sub5<40:
	fail=fail+1
	fm=fm+(40-sub5)

print("\n--------Results--------")
print("\nFail Subject: ",fail)
print("\nGracing Marks: ",fm)

if fail<=2:
	if fm<=7:
		total=sub1+sub2+sub3+sub4+sub5
		print(total)
		per=(total*100)/500
		print(per)
		
		if per>90:
		 	print("A")
		if per>=75 and per<=89:
			print("B")
		if per>60 and per<=74:
			print("C")
		if per>=40 and per<=59:
			print("D")
		if per<40:
			print("E")
		if fm>0:
			print(f"Pass with Grace of {fm} Marks")

	else:
		print("Fail")
		
else:
	print("Student failed in more than 2 subjects ")

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	