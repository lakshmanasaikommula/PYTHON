def validate_atm_pin_code(pin):
    is_valid = True
    is_having_four_or_six_charecters = (len(pin) == 4) or (len(pin) == 6)

    if is_having_four_or_six_charecters:
        is_all_digits = pin.isdigit()
        if not is_all_digits:
            is_valid = False
    else:
        is_valid = False

    if is_valid:
        print("Valid PIN Code")
    else:
        print("Invalid PIN Code")
    # Complete this function


pin = input()
validate_atm_pin_code(pin)
# Call the validate_atm_pin_code function