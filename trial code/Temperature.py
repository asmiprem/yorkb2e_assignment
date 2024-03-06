
temperatures = [20,16,19,21,15,22,20]
#sum of all numbers
sum=sum(temperatures)
print (sum)

#average of all numbers
average = (sum)/len(temperatures)
print (average)
#print all numbers divisible by 3
for i in range(15,100,3):
    print(i)
#print all numbers
print(temperatures[:-4])

iS_cold="false";
is_hot="false";
is_warm="true";
temperature= iS_cold and (is_hot or is_warm)
print(temperature)
temperature= iS_cold  and is_hot or  is_warm
print (temperature)
