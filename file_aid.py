from colorama import Fore, Style


def print_colored_message(message, color):
    print(f"{color}{message}{END}")


def mobile_number_allowed_length(number):
    try:
        if not number.isdigit():
            print_colored_message("Please enter a number", RED)
            return False
        if len(number) != 11:
            if len(number) > 11:
                print_colored_message("The number of digits is more than the allowed limit", RED)
            else:
                print_colored_message("The number of digits is less than the allowed limit", RED)
            return False
        elif not number.startswith("09"):
            print_colored_message("Invalid mobile number", RED)
            return False
        return True
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)
        return False


def national_id_allowed_length(number):
    try:
        if not number.isdigit():
            print_colored_message("Please enter a number", RED)
            return False
        if len(number) != 10:
            if len(number) > 10:
                print_colored_message("The number of digits is more than the allowed limit", RED)
            else:
                print_colored_message("The number of digits is less than the allowed limit", RED)
            return False
        return True
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)
        return False


def read_files(file_name):
    try:
        with open(file_name, "r", encoding='utf-8') as file:
            return file.readlines()
    except Exception as e:
        print_colored_message(f"An error occurred while reading the file: {e}", RED)


def write_files(file_name, data, mode='w'):
    try:
        with open(file_name, mode, encoding='utf-8') as file:
            file.write(data)
    except Exception as e:
        print_colored_message(f"An error occurred while writing to file: {e}", RED)


def entity_exists(file_name, identifier, index):
    try:
        with open(file_name, "r", encoding='utf-8') as file:
            for line in file:
                if line.strip().split(",")[index] == identifier:
                    return True
        return False
    except FileNotFoundError:
        print_colored_message(f"{file_name} not found", RED)
        return False
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)
        return False


def doctor_exists(doctor_id):
    return entity_exists(doctor_txt, doctor_id, 0)


def patient_exists(national_id):
    return entity_exists(patient_txt, national_id, 0)


def mobile_exists(file_name, mobile, current_id=None, current_name=None):
    try:
        with open(file_name, "r", encoding='utf-8') as file:
            for line in file:
                element = line.strip().split(",")
                if element[2] == mobile and (element[0] != current_id or element[1] != current_name):
                    return True
        return False
    except FileNotFoundError:
        print_colored_message(f"{file_name} not found", RED)
        return False
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)
        return False


RED = Fore.RED
END = Style.RESET_ALL
doctor_txt = "Doctors.txt"
patient_txt = "Patients.txt"
