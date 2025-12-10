
# Numerical Converter

A small GUI application for converting numbers between binary (BIN), octal (OCT), decimal (DEC), and hexadecimal (HEX).

This project provides a simple keypad-driven interface (Tkinter) and conversion logic in Python.

## Features

- Convert numbers between BIN / OCT / DEC / HEX
- Read-only input field with keypad entry (AC, backspace, =)
- Automatic enabling/disabling of keypad keys based on selected base

## Requirements

- Python 3.7+ (Tkinter is required — typically included with standard Python installations)

## Install & Run

1. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Run the application:

```powershell
python main.py
```

The GUI window will open. Use the keypad to enter values and the comboboxes to select source/target bases.

## Usage

- Use the dropdown on the left to select the input base (`DEC` by default).
- Use the dropdown on the right to select the target base (`BIN` by default).
- Enter digits/letters using the on-screen keypad (manual typing is disabled).
- `AC` clears input and output; `⌫` (backspace) removes the last character; `=` computes the conversion.

Examples:

- Convert `A` from `HEX` to `DEC` → `10`
- Convert `1011` from `BIN` to `HEX` → `B`

## Project Structure

- `main.py` — application entrypoint; wires GUI and logic together
- `gui_io.py` — creates the main Tkinter window and I/O widgets
- `keypad.py` — keypad layout and button callbacks
- `keypad_manager.py` — enable/disable keypad buttons based on selected base
- `converter_engine.py` — conversion helpers: `any_to_dec` and `dec_to_any`
- `controller.py` — coordinates conversions between different bases

## Notes

- The app uses a read-only input field and relies on the on-screen keypad to prevent invalid manual input.
- The conversion is implemented by converting to decimal as an intermediate step when needed.
