def max_number(first_number, second_number, third_number):

    largest_number = first_number

    if(second_number > largest_number):
        largest_number = second_number

    if (third_number >  largest_number):
        largest_number = third_number

        return largest_number


first_number = int(input("Enter the first number: "))

second_number = int(input("Enter the second nunber: "))

third_number = int(input("Enter the third number: "))


max = max_number(first_number, second_number, third_number) 
print("the largest number is ", max)







