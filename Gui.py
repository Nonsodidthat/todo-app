import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip= "enter to-do", key= "task")
new_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_tasks(), key= "tasks",
                      enable_events= True, size=(25,15))
new_button2 = sg.Button("Edit")
new_button3 = sg.Button("Complete")
new_button4 = sg.Button("Exit")

window = sg.Window("My to-do app",
                   layout=[[label], [input_box], [new_button],
                           [list_box,new_button2, new_button3], [new_button4]],
                   font= ('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            tasks = functions.get_tasks()
            new_task = values["task"] + '\n'
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window['tasks'].update(values= tasks)
            window['task'].update(value="")
        case 'Edit':
            task_to_edit = values["tasks"][0]
            new_task_in = values["task"]
            tasks = functions.get_tasks()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task_in + '\n'
            functions.write_tasks(tasks)
            window['tasks'].update(values= tasks)
            window['task'].update(value="")
        case 'Complete':
            tasks = functions.get_tasks()
            task_to_remove = values["tasks"][0]
            index = tasks.index(task_to_remove)
            tasks.pop(index)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)
            window['task'].update(value="")
        case 'tasks':
            window['task'].update(value= values["tasks"][0])
        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break


window.close()