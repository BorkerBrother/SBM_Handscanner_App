import PySimpleGUI as sg

sg.theme("Dark Blue 3")

character_array = []
text_elem = sg.Text(size=(50, 1), key='-GTIN-', enable_events=True, text_color="white", font=20)

layout =    [[sg.Text("Scan your EAN/GTIN Code")],
            [sg.Text("EAN/GTIN:", font=20), (text_elem)],
            [sg.Button("Close", size=(15,1)), sg.Button("New", size=(15,1)) ]]

# Create the window
window = sg.Window("Handscanner", layout, size=(300,100), return_keyboard_events=True, use_default_focus=False)

# Create an event loop
while True:

    event, values = window.read()
    ## Close Event
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    elif event == sg.WIN_CLOSED:
        break

    if event == "New" or event == "BackSpace:8":
        # Clear the character array
        character_array = []
        text_elem.update("")

    if event != "New":
        # Update the text element and append the character to the array
        character = event
        text_elem.update(''.join(character_array + [character]))
        character_array.append(character)

    print(event)
window.close()


# key = input()
# print(key)

