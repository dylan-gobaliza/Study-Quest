tasks = []
xp = 0

# CREATE ALL FUNCTIONS #

def add_task():
    subject = input("\nEnter subject: ")
    topic = input("Enter topic: ")
    difficulty = int(input("Enter difficulty (1 - easy, 2 - medium, 3 - hard): "))

    print(f"\nTask added!")

    task = {
        "subject": subject,
        "topic": topic,
        "difficulty": difficulty
    }
    tasks.append(task)

def view_tasks():
    if len(tasks) == 0:
        print("\n -- NO TASKS AVAILABLE -- ")
        return

    print("\n -- OUTSTANDING TASKS --\n")
    for i in range(len(tasks)):
        task = tasks[i]
        print(f"\n{i + 1}. -- Subject: {task['subject']} -- Topic: {task['topic']} -- Difficulty: {task['difficulty']}\n")


def complete(xp):
    if len(tasks) == 0:
        print("\n -- NO TASKS AVAILABLE -- ")
        return xp

    print("\n -- OUTSTANDING TOPICS --\n")

    for i in range(len(tasks)):
        task = tasks[i]
        print(f"\n{i + 1}. {task['topic']}\n")
    task_number = int(input("\nEnter the number of the topic you want to submit: "))

    if 1 <= task_number <= len(tasks):
        print(f"\n✓ {tasks[task_number - 1]['topic']} completed!\n \n+{tasks[task_number - 1]['difficulty']*100} XP!")
        xp += tasks[task_number - 1]['difficulty'] * 100
        if xp >= goal:
            print("🎉 SESSION GOAL COMPLETE!")
        else:
            print(f"Goal progress: {xp} / {goal} XP")
        tasks.pop(task_number - 1)
    else:
        print("Invalid task number.")

    return xp

def show_progress():
    print(f"\n -- PROGRESS --\n")
    print(f"Total XP: {xp}")

## main game loop ##

print("\n -- WELCOME TO STUDY QUEST! --\n")

goal = int(input("How much XP do you want to earn? \n> "))

if goal <= 0:
    print("\nNumber must be positive.")
else:
    print(f"\nGoal: 0/{goal} XP")

while True:
    choice = input("\n1. Add task "
                   "\n2. View tasks"
                   "\n3. Submit task"
                   "\n4. Check status"
                   "\n5. Exit \n"
                   "\n> ")

    if choice == "1":
        add_task() 
    elif choice == "2":
        view_tasks()
    elif choice == "3": 
        xp = complete(xp)
    elif choice == "4":
        show_progress()
    elif choice == "5":
        print("Exiting program...")
        break
