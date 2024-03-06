my_List=[4,5,0,-7,5,]
def smallest_numbers(numbers):
    smallest=numbers[0]
    
    for num in my_List:
        if(num<smallest ):
            smallest=num
            
    return smallest
print(smallest_numbers(my_List))

