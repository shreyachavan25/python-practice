""" A list of items """

color = ["red", "green", "blue", "yellow", "orange", "purple"]
scores = [10, 20, 30, 40, 50]
print(color)
print(scores)
print(" ")




"""" ACCESSING ITEMS IN A LIST """

colors = ["red", "green", "blue", "yellow", "orange", "purple"]
print("Accessing items in a list using positive indexing")
print(colors[0])  # red
print(colors[1])  # green
print(colors[5])  # purple
print(colors[4])  # orange
print(" ")
print("Accessing items in a list using negative indexing")
print(colors[-1])  # purple
print(colors[-2])  # orange
print(colors[-5])  # green
print(colors[-6])  # red
print(" ")




""" COMMON LIST OPERATIONS """

color1 = ["red", "green", "blue"]
print(color1) # ['red', 'green', 'blue']
print(len(color1)) # 3

color1.append("yellow") # add an item to the end of the list
print(color1) # ['red', 'green', 'blue', 'yellow'] 

color1.remove("green") # remove an item from the list
print(color1) # ['red', 'blue', 'yellow']   

color1[0] = "purple"
print(colors)




