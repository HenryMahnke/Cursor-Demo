# hear is a short demo about what cursor tab can do. 
# we are going to program a simple calculator

def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b

#now we want to ask the user what they want to do 
while True:
    print("1. Add")
    print("2. Multiply")
    print("3. Subtract")
    print("4. Divide")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        break
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if choice == 1:
        print(add(a,b))
    elif choice == 2:
        print(multiply(a,b))
    elif choice == 3:
        print(subtract(a,b))
    elif choice == 4:
        print(divide(a,b))
    else:
        print("Invalid choice try again")
        continue
    print("--------------------------------")



