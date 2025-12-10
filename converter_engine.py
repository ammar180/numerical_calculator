# قاموس بيحدد قيمة الأساس لكل نوع عدد
types = {'BIN': 2, 'OCT': 8, 'DEC': 10, 'HEX': 16}

# قيم الحروف الخاصة بالأعداد الست عشرية
hex_nums = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def any_to_dec(num, num_type):
    """
    Convert a number from any system (BIN/OCT/DEC/HEX) to decimal (int)
    """
    result = 0
    base = types.get(num_type.upper(), 0)

    # نمشي على الرقم من اليمين للشمال
    for place, digit in enumerate(reversed(num)):
        # لو رقم
        if digit.isdigit():
            digit = int(digit)
        else:
            # لو حرف (A-F)
            digit = hex_nums.get(digit.upper(), 0)

        result += digit * (base ** place)

    return result


def dec_to_any(num, convert_type):
    """
    """
    base = types.get(convert_type.upper(), 0)
    num = int(num)

    if num == 0:
        return "0"

    result = ''

    while num > 0:
        remainder = num % base

        if remainder >= 10:
            for letter, value in hex_nums.items():
                if value == remainder:
                    remainder = letter
                    break

        result += str(remainder)
        num //= base

    return result[::-1]
