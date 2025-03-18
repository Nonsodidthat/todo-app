import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip= "enter to-do")
new_button = sg.Button("add")

window = sg.Window("My to-do app", layout=[[label], [input_box], [new_button]])
window.read()
print("hello")
window.close()