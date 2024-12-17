import math
def add(a,b):
    sum = a +b 
    return sum 

def sub(a,b):
    sub = a - b 
    return sub 

def mul(a,b):
    mul = a * b
    return mul 

def div(a,b):
    divide = round(a / b)
    return divide 

def modulus(a,b):
    modulus = a%b 
    return modulus 

def main():
    print("Welcome to Caluculator Gnerator")
    while True:
        print("\n 1.ADD \n 2.SUBTRACT \n 3.MULTIPLY \n 4.DIVISION \n 5.MODULUS \n 6.EXIT")
        choice = int(input("Enter the choice: ")) 
        if choice == 1:
           num_1 = int(input("Enter the number_1: "))
           num_2 = int(input("Enter the number_2: "))
           total = add(num_1,num_2)
           print("The Sum is:",total)
        elif choice == 2:
            num_1 = int(input("Enter the number_1: "))
            num_2 = int(input("Enter the number_2: "))
            total = sub(num_1,num_2)
            print("The Subtract is:",total)
        elif choice == 3:
           
            num_1 = int(input("Enter the number_1: "))
            num_2 = int(input("Enter the number_2: "))
            total = mul(num_1,num_2)
            print("The multiplication is:",total)
            
        elif choice == 4:
             num_1 = int(input("Enter the number_1: "))
             num_2 = int(input("Enter the number_2: "))
             total = div(num_1,num_2)
             print("The division is:",total)
             
        elif choice == 5:
             num_1 = int(input("Enter the number_1: "))
             num_2 = int(input("Enter the number_2: "))
             total = modulus(num_1,num_2)
             print("The modulus is:",total)
        elif choice == 6:
             print("Exiting")
             break
        else:
             print("invalid input")
             continue 
            
main()
          
        
   

    