my_List=[0,-1,2,3,4,-6,-7]
#Create a function that gets a list of numbers, and returns the sum of all positive ones.
def postive_num(numbers):
    sum=0
    for i in numbers:
        if i > 0:
            sum =sum+i
    return sum
print(postive_num(my_List))


#Create a function that takes a boolean value and returns a "Yes" for true and "No" for false
def boolean_value(value):
    if (value):
        return "yes"
    else:
        return "no"

print(boolean_value(True))

#Create a function that when given a list of numbers returns the smallest number in the list.
def smallest_numbers(numbers):
    smallest=numbers[0]
    for num in my_List:
        if(num<smallest ):
            smallest=num
            
    return smallest
print(smallest_numbers(my_List))

#Create a function that calculates the average of the values in a list
def average(numbers):
    average=sum(numbers)/len(numbers)

    return average
print(average(my_List))

'''For every number from 1 to 20 do the following:
if the number is a multiple of 3, print "Fizz"
if the number is a multiple of 5, print "Buzz"
if the number is a multiple of both 3 and 5 print "FizzBuzz"
Otherwise, just print the number'''
for num in range(1,20):
    
        if(num%3==0 and num%5==0):
            print("fizzbuzz")
        elif num%3==0:
            print("fizz")
        elif num%5==0:
            print("buzz")
        else:
            print(num)


