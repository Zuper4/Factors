print("\nThis is a program that finds the factors of a number that you will enter.")

number = int(input("\nEnter your number :"))

def factor(number):
    print("The factors of " +str(number)+ " are :")
    
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

factor(number)

