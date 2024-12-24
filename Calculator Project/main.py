from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
n1=int(input("What is the first number?"))
operator=input("Choose a mathematical operator:")
n2=int(input("What is the second number?"))
n3=0
n4=0
dictionary= {"+": add, "-": subtract, "*": multiply, "/": divide}

#print(dictionary["*"](8,4))

for key in dictionary:
    if operator == key:
        n3 = dictionary[operator](n1, n2)
        print(n3)
c=input("Would you like to continue working with the previous result?").lower()
if c=="yes":
    n1 = n3
    n2 = int(input("What is the second number?"))
    operator = input("Choose a mathematical operator:")
    for key in dictionary:
        if operator==key:
            n3 = dictionary[operator](n1, n2)
            print(n3)
else:
    print("\n" * 20)









