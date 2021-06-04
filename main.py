
import modules
import additions
import deductions


def main():
    # password model
    password = "Patatabc93@"
    password_length = len(password)

    if(password_length > 8):
        modules.counter_Additions['countSize'] += password_length
        addition = additions.Additions(
            password, password_length)  # returns % addition
        deduction = deductions.Deductions(password)  # returns % deductions

        # Send score
        print("Score: ", addition - deduction, "%")
        # return addition - deduction

    else:
        # alert
        print("Password must be larger or equeal than 8 characters")
