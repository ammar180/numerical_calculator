import tkinter as tk
from tkinter import ttk
from converter_engine import types


def create_main_window():
    """
    Create the main program window + input and output elements
    Returns:
        root, input_var, output_var, from_var, to_var, from_box, to_box
    """
    root = tk.Tk()
    root.title("Base Converter")
    root.geometry("350x620")
    root.config(bg="white")

    # متغيرات الإدخال والإخراج وأنواع الأنظمة
    input_var = tk.StringVar()
    output_var = tk.StringVar()
    from_var = tk.StringVar(value="DEC")
    to_var = tk.StringVar(value="BIN")

    # عنوان التطبيق
    tk.Label(
        root,
        text="Numerical Converter",
        font=("Arial", 18),
        bg="white"
    ).pack(pady=10)

    # ----- جزء الإدخال -----
    input_frame = tk.Frame(root, bg="white")
    input_frame.pack(pady=5)

    input_entry = tk.Entry(
        input_frame,
        textvariable=input_var,
        font=("Arial", 20),
        width=10,
        justify="center",
        state="readonly"   # يقرأ فقط – المستخدم يكتب من الأزرار
    )
    input_entry.grid(row=0, column=0, padx=10)

    # قائمة اختيار نوع الرقم الداخل
    from_box = ttk.Combobox(
        input_frame,
        textvariable=from_var,
        values=list(types.keys()),
        width=5,
        state="readonly"
    )
    from_box.grid(row=0, column=1)

    # ----- جزء الإخراج -----
    output_frame = tk.Frame(root, bg="white")
    output_frame.pack(pady=5)

    output_entry = tk.Entry(
        output_frame,
        textvariable=output_var,
        font=("Arial", 20),
        width=10,
        justify="center",
        state="readonly"
    )
    output_entry.grid(row=0, column=0, padx=10)

    # قائمة اختيار النوع المحول إليه
    to_box = ttk.Combobox(
        output_frame,
        textvariable=to_var,
        values=list(types.keys()),
        width=5,
        state="readonly"
    )
    to_box.grid(row=0, column=1)

    return root, input_var, output_var, from_var, to_var, from_box, to_box
