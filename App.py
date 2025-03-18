import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S" )
print(now)

while True:
    user_action = input("Type add, display, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        task = user_action[4:]

        tasks = functions.get_tasks()


        tasks.append(task.capitalize() + '\n')

        functions.write_tasks(tasks)

    elif user_action.startswith("display"):
        tasks = functions.get_tasks()

        for index, item in enumerate(tasks):
            item = item.strip('\n')
            result = f"{index+1}.{item}"
            print(result)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            tasks = functions.get_tasks()

            new_task= input("Type new task: ")
            tasks[number] = new_task.capitalize() + '\n'


            functions.write_tasks(tasks)
        except ValueError :
            print("Command in not valid (Must include numbers)")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index= number - 1

            tasks = functions.get_tasks()

            todo_to_remove = tasks[index].strip('\n')

            tasks.pop(index)

            functions.write_tasks(tasks)

            notification = f"{todo_to_remove} has been removed !"
            print(notification)
        except IndexError:
            print("command is not valid (Todo not found)")
        except ValueError:
            print("command is not valid (enter a number)")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("Goodbye!".upper())






