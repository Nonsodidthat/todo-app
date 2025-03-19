import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip= "enter to-do", key= "tasks")
new_button = sg.Button("Add")

window = sg.Window("My to-do app",
                   layout=[[label], [input_box], [new_button]],
                   font= ('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            tasks = functions.get_tasks()
            new_task = values["tasks"] + '\n'
            tasks.append(new_task)
            functions.write_tasks(tasks)
        case sg.WIN_CLOSED:
            break


window.close()