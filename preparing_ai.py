command=input("What do you want to do,here are some questions to do?"
   "1.To check if the number is odd or even"
   "2.To check if the student can passed in the exams or not"
   "3.To check greater number"
   "4.To check whether the alphabet is a vowel or not"
   "5.To write the mulitples of one number different integers value"
   "6.To add numbers in a list and and find a number of your choice in that list"
   "7.TO arrange numbers in ascending or descending order")
if command=="1":
    number=int(input("Enter a number to check if it is odd or even"))
    if number%2==0:
        print("The number is even")
    else:
        print("The number is odd")
elif command=="2":
    marks=int(input("Enter the marks of the student"))
    if marks>=40:
        print("The student is passed")
    else:
        print("The student is failed")
elif command=="3":
    number=int(input("Enter the number"))
    if number1 > number2:
        print("The number",number1,"is greater than",number2)
    else:
        print("The number",number2,"is greater than",number1)
elif command=="4":
    alphabet=input("Enter an alphabet")
    if alphabet in ["a","e","i","o","u"]:
        print("The given alphabet is a vowel")
    else:
        print("The given alphabet is not a vowel")
elif command =="5":
    number=int(input("Enter a number"))
    for i in range(1,11):
        print(number,"*",i,"=",number*i)
elif command==6:
    list1=[]
    n=int(input("Enter elements to add"))
    for i in range(n):
        list1.append(int(input("Enter the element")))
    search=int(input("Enter the element to search"))
    if search in list1:
        print("The element is in the list")
    else:
        print("The element is not in the list")
elif command=="7":
    l=[]
    n=int(input("Enter elements to add"))
    for i in range(n):
        l.append(int(input("Enter the element")))
    l.sort()
    print("The list in ascending order is",l)
    l.sort(reverse=True)
    print("The list in descending order is",l)    


