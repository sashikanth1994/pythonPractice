import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet")
box1 = sg.InputText(tooltip="Enter feet")

label2 = sg.Text("Enter Inches")
box2 = sg.InputText(tooltip="Inches")
button = sg.Button("Convert")

window = sg.Window("Converter", layout=[[label1, box1],[label2, box2], [button]])
window.read()
print("hello")
window.close()