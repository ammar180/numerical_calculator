# keypad.py

import tkinter as tk


def create_keypad(root, input_var, output_var, from_var, on_equal):
    """
    Create the keypad
    root      : main program window
    input_var : input StringVar
    output_var: output StringVar (used in AC)
    from_var  : current number system type (for future extensions)
    on_equal  : callback function called when = button is pressed
    Returns:
        keypad_frame, buttons_refs
    """

    keypad_frame = tk.Frame(root, bg="white")
    keypad_frame.pack(pady=15)

    buttons_refs = {}  # store digit and letter buttons

    def press_key(val):
        # add digit/letter to input field
        input_var.set(input_var.get() + val)

    def backspace():
        # delete last character
        input_var.set(input_var.get()[:-1])

    def clear():
        # clear input and output
        input_var.set("")
        output_var.set("")

    # button layout
    buttons_layout = [
        ["AC", "⌫", "F", "E"],
        ["D", "C", "B", "A"],
        ["7", "8", "9", "="],
        ["4", "5", "6", ""],
        ["1", "2", "3", ""],
        ["0"]
    ]

    for r, row_vals in enumerate(buttons_layout):
        for c, val in enumerate(row_vals):
            if val == "":
                continue

            # assign command for each button
            if val == "AC":
                cmd = clear
            elif val == "⌫":
                cmd = backspace
            elif val == "=":
                cmd = on_equal
            else:
                cmd = lambda v=val: press_key(v)

            btn = tk.Button(
                keypad_frame,
                text=val,
                font=("Arial", 16),
                width=5,
                height=2,
                command=cmd,
                bg="white"
            )
            btn.grid(row=r, column=c, padx=5, pady=5)

            # store input buttons (digits and letters only)
            if val not in ["AC", "⌫", "="]:
                buttons_refs[val] = btn

    return keypad_frame, buttons_refs
