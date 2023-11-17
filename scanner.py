import PySimpleGUI as sg

sg.theme("Dark Blue 3")

text_elem = sg.Text(size=(18, 1), key='-GTIN-', enable_events=True)

layout =    [[sg.Text("Scan your EAN/GTIN Code")],
            [sg.Text("EAN/GTIN:"), [text_elem] ],
            [sg.Button("Close", size=(15,1))]]

# Create the window
window = sg.Window("Handscanner", layout, size=(400,200), return_keyboard_events=True, use_default_focus=False)

# Create an event loop
while True:

    event, values = window.read()
    ## Close Event
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    elif event == sg.WIN_CLOSED:
        break


    text_elem.update(event)

window.close()


# key = input()
# print(key)

