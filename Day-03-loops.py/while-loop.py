# WHILE LOOP

health = 3

while health > 0:
    print(f"player is alive , health : {health}")
    health -= 1

print(" ")


"""  ******** break Statement ********  """

while True:
    user_input = input("type 'exit' to exit the loop : ")
    if user_input == "exit":
        break
    print(f" You typed : {user_input}")
print("loop ended")
print(" ")


"""  ******** continue Statement ********  """

current_slot = 0
while current_slot < 5 :
    current_slot += 1
    if current_slot == 3:
        print(f"current slot : {current_slot}")
        continue
    print(f"current slot : {current_slot}")
print("Inventor scan completed")