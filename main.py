from controller import convert_value
from gui_io import create_main_window
from keypad import create_keypad
import keypad_manager


def main():
    # create the window and all I/O elements
    root, input_var, output_var, from_var, to_var, from_box, to_box = create_main_window()

    # callback function executed when user presses =
    def on_equal():
        num = input_var.get()
        from_type = from_var.get()
        to_type = to_var.get()

        result = convert_value(num, from_type, to_type)
        output_var.set(result)

    # create the keypad
    keypad_frame, buttons_refs = create_keypad(
        root=root,
        input_var=input_var,
        output_var=output_var,
        from_var=from_var,
        on_equal=on_equal
    )

    # bind number system type change to update buttons
    def on_from_changed(event=None):
        keypad_manager.update_buttons(buttons_refs, from_var.get())

    from_box.bind("<<ComboboxSelected>>", on_from_changed)

    # initial button update on program startup
    keypad_manager.update_buttons(buttons_refs, from_var.get())

    # run the program
    root.mainloop()


if __name__ == "__main__":
    main()
