# FOR Loop

for i in range (5):
    print(i)
print(" ")

for number in range(1 , 11 , 2):
    print(number)
print(" ")    
#  output starts from 1 and goes up to 10 with a step of 2 
# (when we use step, it will skip the numbers in between)
# (when we use stop, it will stop at the number before the stop number  )

"""  ******** break Statement ********  """

for count in range(5):
    if count == 3:
        break
    print(count)
print("loop ended")
print(" ")


for num in range(5):
    print(num)
    if num == 3:
        break
print("loop ended")
print(" ")


"""  ******** continue Statement ********  """

for n in range(5):
    if n == 3:
        continue
    print(n)
print("loop ended")
print(" ")


for j in range(5):
    print(j)
    if j == 3:
        continue
print("loop ended")
print(" ")



