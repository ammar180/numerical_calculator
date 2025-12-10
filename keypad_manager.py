# keypad_manager.py

from converter_engine import types

def update_buttons(buttons_refs, from_type):
    """
    Enable/disable number and letter buttons based on the selected number system type
    from_type   : "BIN" / "OCT" / "DEC" / "HEX"
    """
    base = types[from_type]

    for label, btn in buttons_refs.items():
        # HEX: all buttons are enabled
        if base == 16:
            btn.config(state="normal")

        # DEC: only 0-9
        elif base == 10:
            if label.isdigit() and int(label) < 10:
                btn.config(state="normal")
            else:
                btn.config(state="disabled")

        # OCT: only 0-7
        elif base == 8:
            if label.isdigit() and int(label) < 8:
                btn.config(state="normal")
            else:
                btn.config(state="disabled")

        # BIN: only 0 and 1
        elif base == 2:
            if label in ["0", "1"]:
                btn.config(state="normal")
            else:
                btn.config(state="disabled")
