task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound (yes/no)? ")
match priority:
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: {task} is a high-priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a high-priority task.")
    case "medium":
        print(f"Reminder: {task} is a medium-priority task.")
    case "low":
        print(f"Reminder: {task} is a low-priority task.")
    case _:
        print("Invalid priority level.")
