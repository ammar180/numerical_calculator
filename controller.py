# controller.py

from converter_engine import any_to_dec, dec_to_any

def convert_value(num_str, from_type, to_type):
    """
    """
    if not num_str:
        return ""

    if from_type == to_type:
        return num_str

    if from_type == "DEC":
        return dec_to_any(num_str, to_type)

    if to_type == "DEC":
        dec_value = any_to_dec(num_str, from_type)
        return str(dec_value)

    dec_value = any_to_dec(num_str, from_type)
    return dec_to_any(dec_value, to_type)
