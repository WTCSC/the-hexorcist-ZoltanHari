import sys
import time

def type_out(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_decimal(number_string, original_base):
    total_value = 0
    power = 0
    for char in number_string[::-1]:
        digit_value = digits.index(char.upper())
        total_value += digit_value * (original_base ** power)
        power += 1  
    return total_value

def from_decimal(total_value, new_base):
    if new_base < 2 or new_base > 36:
        raise ValueError("Base must be between 2 and 36")
    if total_value == 0:
        return "0"
    result_string = ""
    while total_value > 0:
        remainder = total_value % new_base
        total_value //= new_base
        result_string = digits[remainder] + result_string
    return result_string

def validate_number_string(number_string):
    invalid_chars = [c for c in number_string if c not in digits]
    return invalid_chars

def validate_base(base):
    if not isinstance(base, int):
        raise ValueError("Base must be an integer.")
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")
    return True

def validate_different_bases(original_base, new_base):
    if original_base == new_base:
        raise ValueError("New base must be different from original base")
    return True


if __name__ == "__main__":
    while True:
        type_out("Please tell me the number string that needs exorcising:")
        number_string = input().strip().upper()
        invalid_chars = validate_number_string(number_string)
        if invalid_chars:
            type_out(f"The number string '{' '.join(invalid_chars)}' doesn't need to be exorcised, please tell me the one that actually needs exorcising.")
        else:
            break

    while True:
        type_out("Tell me the base that has possessed the number string (2–36):")
        try:
            original_base = int(input())
            validate_base(original_base)
        except ValueError:
            type_out("That not a demon base that can possess a number string. Tell me which demon possessed the number string")
            continue

        invalid_digits_for_base = [char for char in number_string if digits.index(char.upper()) >= original_base]
        if invalid_digits_for_base:
            type_out(f"Error: Digit(s) '{' '.join(invalid_digits_for_base)}' not valid for base {original_base}.")
            continue
        else:
            break

    while True:
        type_out("Tell me which base you need to have after the exorcism (2–36):")
        try:
            new_base = int(input())
            validate_base(new_base)
            validate_different_bases(original_base, new_base)
        except ValueError:
            type_out("That not one of the demon bases I get from the exorcism. Tell me which demon I need to extract the number string")
            continue
        else:
            break


    decimal_value = to_decimal(number_string, original_base)
    result_string = from_decimal(decimal_value, new_base)
    type_out(f"{number_string} in base {original_base} is {result_string} in base {new_base}")
