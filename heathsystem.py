def getdate():
	import datetime
	return datetime.datetime.now()

def lock(k):
	if k==1:
		c =int(input("enter 1 for exercise 2 for food\n:>"))
		if c==1:
			v =input("enter your exercise:\n:>")
			with open("kanu-ex.txt", "a") as f:
				f.write(str([str(getdate())]) +" : " + v+"\n")
				print("added")
		if c==2:
			v =input("enter your food:\n:>")
			with open("kanu-food.txt", "a") as f:
				f.write(str([str(getdate())]) +" : " + v+"\n")
				print("added")
	elif k==2:
		c =int(input("enter 1 for food 2 for exercise:\n:>"))
		if c==1:
			v=str(input("enter your food:\n:>"))
			with open("golu-food.txt", "a") as f:
				f.write(str([str(getdate())]) +" : " + v+"\n")
				print("added")
		if c==2:
			v =input("enter your exercise:\n:>")
			with open("golu-ex.txt", "a") as f:
				f.write(str([str(getdate())]) +" : " + v+"\n")
				print("added")
	else:
		print("enter valid number")

def retreive(k):
	if k==1:
		c=int(input("enter 1 for exercise 2 for food\n:>"))
		if c==1:
			with open("kanu-ex.txt") as f:
				for i in f:
					print(i, end="")
		elif c==2:
			with open("kanu-food.txt") as f:
				for i in f:
					print(i,end="")
	if k==2:
		c=int(input("enter 1 for exercise 2 for food\n:>"))
		if c==1:
			with open("golu-ex.txt") as f:
				for i in f:
					print(i, end="")
		elif c==2:
			with open("golu-food.txt") as f:
				for i in f:
					print(i,end="")

print("\t====health management==== \n\t\tsystem")
a =int(input("\nPress the below\n1: for kanu \n2: for golu\n3: for exit \n:>"))
if a==1:	
	b=int(input("press 1 for lock 2 for retreive:\n:>"))
	if b==1:
		print(a)
		lock(a)
	elif b==2:
		print(a)
		retreive(a)
	else :
		print("enter valid number")
elif a==2:	
	b=int(input("enter 1 for lock 2 for retreive:\n:>"))
	if b==1:
		print(a)
		lock(a)
	elif b==2:
		print(a)
		retreive(a)
	else :
		print("enter valid number")
elif a==3:
	print("Thanks for visiting\nvisit again")
else:
	print("enter valid value")
			