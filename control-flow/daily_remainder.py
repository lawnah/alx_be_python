task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time-bound (yes or no)? ")
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
