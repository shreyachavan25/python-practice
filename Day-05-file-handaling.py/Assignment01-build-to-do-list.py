file_name = "tasks.txt"

while True:
	print("\n=== Personal To-Do List ===")
	print("1. View tasks")
	print("2. Add a task")
	print("3. Exit")

	choice = input("Choose an option (1-3): ")

	if choice == "1":
		print("\n--- Current Tasks ---")

		try:
			with open(file_name, "r") as file:
				tasks = file.readlines()

			if len(tasks) == 0:
				print("No tasks yet.")
			else:
				for number, task in enumerate(tasks, start=1):
					print(number, task.strip())
		except FileNotFoundError:
			print("No tasks yet.")

	elif choice == "2":
		new_task = input("\nWhat do you need to do? ")

		with open(file_name, "a") as file:
			file.write(new_task + "\n")

		print("Task saved!")

	elif choice == "3":
		print("\nGoodbye! Stay productive.")
		break

	else:
		print("\nInvalid choice. Please choose 1, 2, or 3.")
