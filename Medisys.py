from file_aid import *
from colorama import Fore, Style
import pyfiglet

RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
END = Style.RESET_ALL
BACK = f"{RED}{'-' * 10}|{END} "
FRONT = f" {RED}|{'-' * 10}{END}"
doctor_txt = "Doctors.txt"
patient_txt = "Patients.txt"


def doctor_management():
    try:
        print(f"{BACK}Doctor Management{FRONT}", f"{GREEN}1. Add new doctor",
              "2. Remove doctor",
              "3. Edit doctor information",
              "4. Search a doctor", "5. Show all doctors",
              "6. Show doctors by specialty", f"0. Return{END}", sep="\n")
        user_input = input(f"{BLUE}Please select an option: {END}")
        match user_input:
            case "0":
                main_menu()
            case "1":
                add_doctor()
            case "2":
                remove_doctor()
            case "3":
                edit_doctor()
            case "4":
                search_a_doctor()
            case "5":
                all_doctors()
            case "6":
                doctors_by_specialty()
            case _:
                print_colored_message("Invalid input", RED)
                doctor_management()
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)
        doctor_management()


def add_doctor():
    try:
        print(f"{BACK}Add new doctor{FRONT}")
        while True:
            doctor_id = input(f"{BLUE}Doctor id: {END}")
            doctor_id_existence = False
            with open(doctor_txt, "a+", encoding='utf-8') as file:
                file.seek(0)
                for line in file:
                    if line.strip().split(",")[0] == doctor_id:
                        print_colored_message("The doctor id has already been registered", RED)
                        break
                else:
                    doctor_id_existence = True
            if doctor_id_existence:
                break
        name = input(f"{BLUE}Doctor name: {END}").capitalize()
        while True:
            mobile = input(f"{BLUE}Mobile number: {END}")
            if mobile_number_allowed_length(mobile):
                mobile_exists = False
                with open(doctor_txt, "r", encoding='utf-8') as file:
                    for line in file:
                        element = line.strip().split(",")
                        if element[2] == mobile and (element[0] != doctor_id or element[1] != name):
                            print_colored_message(f"This phone number is already registered", RED)
                            mobile_exists = True
                            break
                if not mobile_exists:
                    break
        while True:
            specialty = input(
                f"{BLUE}Specialty (Cardiology, Ophthalmology, Pediatrics, General): {END}").strip().capitalize()
            if specialty in ['Cardiology', 'Ophthalmology', 'Pediatrics', 'General']:
                break
            else:
                print_colored_message("Please enter a valid specialty (Cardiology,"
                                      " Ophthalmology, Pediatrics, General)", RED)
        write_files(doctor_txt, f"{doctor_id},{name},{mobile},{specialty}\n", 'a')
        print_colored_message("Doctor information successfully registered", YELLOW)
        doctor_management()
    except FileNotFoundError:
        print_colored_message(f"{doctor_txt} not found", RED)
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)
        add_doctor()


def remove_doctor():
    try:
        print(f"{BACK}Remove doctor{FRONT}")
        while True:
            doctor_id = input(f"{BLUE}Doctor id: {END}")
            doctor_found = False
            lines = read_files(doctor_txt)
            for line in lines:
                if line.split(",")[0] == doctor_id:
                    doctor_found = True
                    break
            if doctor_found:
                break
            else:
                print_colored_message("Doctor not found", RED)
        lines = read_files(doctor_txt)
        new_lines = [line for line in lines if line.split(",")[0] != doctor_id]
        write_files(doctor_txt, "".join(new_lines), 'w')
        print_colored_message("Doctor information successfully removed", YELLOW)
        doctor_management()
    except FileNotFoundError:
        print_colored_message(f"{doctor_txt} not found", RED)
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)


def edit_doctor():
    try:
        print(f"{BACK}Edit doctor information{FRONT}")
        while True:
            doctor_id = input(f"{BLUE}Doctor id: {END}")
            doctor_found = False
            lines = read_files(doctor_txt)
            for line in lines:
                if line.split(",")[0] == doctor_id:
                    doctor_found = True
                    break
            if doctor_found:
                break
            else:
                print_colored_message("Doctor not found", RED)
        name = input(f"{BLUE}Doctor name: {END}").capitalize()
        while True:
            mobile = input(f"{BLUE}Mobile number: {END}")
            if mobile_number_allowed_length(mobile):
                mobile_exists = False
                with open(doctor_txt, "r", encoding='utf-8') as file:
                    for line in file:
                        element = line.strip().split(",")
                        if element[2] == mobile and (element[0] != doctor_id or element[1] != name):
                            print_colored_message(f"This phone number is already registered", RED)
                            mobile_exists = True
                            break
                if not mobile_exists:
                    break
        while True:
            specialty = input(
                f"{BLUE}Specialty (Cardiology, Ophthalmology, Pediatrics, General): {END}").strip().capitalize()
            if specialty in ['Cardiology', 'Ophthalmology', 'Pediatrics', 'General']:
                break
            else:
                print_colored_message("Please enter a valid specialty (Cardiology,"
                                      " Ophthalmology, Pediatrics, General)", RED)
        new_lines = [f"{doctor_id},{name},{mobile},{specialty}\n" if line.split(",")[0] == doctor_id else line for
                     line in lines]
        write_files(doctor_txt, "".join(new_lines), 'w')
        print_colored_message("Doctor information successfully edited", YELLOW)
        doctor_management()
    except FileNotFoundError:
        print_colored_message(f"{doctor_txt} not found", RED)
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)


def search_a_doctor():
    try:
        print(f"{BACK}Search a doctor{FRONT}")
        doctor_id = input(f"{BLUE}Doctor id: {END}")
        print(f"{RED}{'-' * 18}{END}")
        with open(doctor_txt, "r", encoding='utf-8') as file:
            doctor_id_exists = False
            for line in file:
                element = line.strip().split(",")
                if element[0] == doctor_id:
                    print(
                        f"{BLUE}Doctor id: {END}{element[0]}\n{BLUE}Name: {END}{element[1]}\n{BLUE}"
                        f"Mobile number: {END}{element[2]}{BLUE}\nSpecialty: {END}{element[3]}\n")
                    doctor_id_exists = True
            if not doctor_id_exists:
                print_colored_message("Doctor not found", RED)
        doctor_management()
    except FileNotFoundError:
        print_colored_message(f"{doctor_txt} not found", RED)
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)


def all_doctors():
    try:
        print(f"{BACK}Show doctor list{FRONT}")
        with open(doctor_txt, "r", encoding='utf-8') as file:
            lines = sorted(file.readlines(), key=lambda a: a.split(",")[1])
            for line in lines:
                element = line.strip().split(",")
                print(
                    f"{BLUE}Doctor id: {END}{element[0]}\n{BLUE}Name: {END}{element[1]}\n{BLUE}Specialty: {END}"
                    f"{element[2]}\n", end=f"{RED}{'-' * 18}{END}\n")
        doctor_management()
    except FileNotFoundError:
        print_colored_message(f"{doctor_txt} not found", RED)
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)


def doctors_by_specialty():
    try:
        print(f"{BACK}Show doctors by specialty{FRONT}")
        while True:
            specialty = input(
                f"{BLUE}Specialty (Cardiology, Ophthalmology, Pediatrics, General): {END}").strip().capitalize()
            if specialty in ['Cardiology', 'Ophthalmology', 'Pediatrics', 'General']:
                break
            else:
                print_colored_message("Please enter a valid specialty (Cardiology,"
                                      " Ophthalmology, Pediatrics, General)", RED)

        print(f"{RED}{'-' * 18}{END}")
        specialty_exists = False
        with open(doctor_txt, "r", encoding='utf-8') as file:
            for line in file:
                element = line.strip().split(",")
                if element[3] == specialty:
                    print(f"{BLUE}Doctor code: {END}{element[0]}\n{BLUE}Name: {END}{element[1]}\n"
                          f"{BLUE}Mobile number: {END}{element[2]}", end=f"\n{RED}{'-' * 18}{END}\n")
                    specialty_exists = True

        if not specialty_exists:
            print_colored_message("No doctor found with the requested specialty", RED)

        doctor_management()
    except FileNotFoundError:
        print_colored_message(f"{doctor_txt} not found", RED)
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)


def patient_management():
    try:
        print(f"{BACK}Patient Management{FRONT}", f"{GREEN}1. Add new patient",
              "2. Remove patient",
              "3. Edit patient information",
              "4. Show patients of a doctor",
              "5. Show all patients", f"0. Return{END}", sep="\n")
        user_input = input(f'{BLUE}Please select an option: {END}')
        match user_input:
            case "0":
                main_menu()
            case "1":
                add_patient()
            case "2":
                remove_patient()
            case "3":
                edit_patient()
            case "4":
                patients_of_a_doctor()
            case "5":
                all_patients()
            case _:
                print_colored_message("Invalid input", RED)
                patient_management()
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)
        patient_management()


def add_patient():
    try:
        print(f"{BACK}Add new patient{FRONT}")
        while True:
            with open(patient_txt, "a+", encoding='utf-8') as file:
                file.seek(0)
            while True:
                kode_melli = input(f"{BLUE}Patient national id: {END}")
                if national_id_allowed_length(kode_melli):
                    break
            while True:
                name = input(f"{BLUE}Patient name: {END}").capitalize()
                lines = read_files(patient_txt)
                for line in lines:
                    element = line.strip().split(",")
                    if element[0] == kode_melli and element[1] != name:
                        print_colored_message(f"This national id is already registered with the name {element[1]}", RED)
                        break
                else:
                    break
            while True:
                doctor_id = input(f"{BLUE}Doctor id: {END}")
                if doctor_exists(doctor_id):
                    write_files(patient_txt, f"{kode_melli},{name},{doctor_id}\n", 'a')
                    print_colored_message("Patient information successfully registered", YELLOW)
                    patient_management()
                    break
                else:
                    print_colored_message("Doctor with this code is not registered", RED)
    except FileNotFoundError:
        print_colored_message(f"{patient_txt} not found", RED)
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)
        add_patient()


def remove_patient():
    try:
        print(f"{BACK}Remove patient{FRONT}")
        while True:
            while True:
                kode_melli = input(f"{BLUE}Patient national id: {END}")
                if national_id_allowed_length(kode_melli):
                    break
            patient_found = False
            lines = read_files(patient_txt)
            for line in lines:
                if line.split(",")[0] == kode_melli:
                    patient_found = True
                    break
            if not patient_found:
                print_colored_message("national id not found", RED)
                continue
            lines = read_files(patient_txt)
            new_lines = [line for line in lines if line.split(",")[0] != kode_melli]
            write_files(patient_txt, "".join(new_lines), 'w')
            print_colored_message("Patient information successfully removed", YELLOW)
            patient_management()
    except FileNotFoundError:
        print_colored_message(f"{patient_txt} not found", RED)
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)


def edit_patient():
    try:
        print(f"{BACK}Edit patient information{FRONT}")
        while True:
            while True:
                kode_melli = input(f"{BLUE}Patient national id: {END}")
                if national_id_allowed_length(kode_melli):
                    break
            patient_found = False
            lines = read_files(patient_txt)
            for line in lines:
                if line.split(",")[0] == kode_melli:
                    patient_found = True
                    break
            if not patient_found:
                print_colored_message("national id not found", RED)
                continue
            name = input(f"{BLUE}Patient name: {END}").capitalize()
            while True:
                doctor_id = input(f"{BLUE}Doctor id: {END}")
                if doctor_exists(doctor_id):
                    new_lines = [f"{kode_melli},{name},{doctor_id}\n" if line.split(",")[0] == kode_melli else line
                                 for line in lines]
                    write_files(patient_txt, "".join(new_lines), 'w')
                    print_colored_message("Patient information successfully edited", YELLOW)
                    patient_management()
                    break
                else:
                    print_colored_message("Doctor with this code is not registered", RED)
    except FileNotFoundError:
        print_colored_message(f"{patient_txt} not found", RED)
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)


def patients_of_a_doctor():
    try:
        print(f"{BACK}Show patients of a doctor{FRONT}")
        while True:
            doctor_id = input(f"{BLUE}Doctor id: {END}")
            doctor_existence = doctor_exists(doctor_id)
            if doctor_existence:
                print(f"{RED}{'-' * 18}{END}")
                doctor_id_exists = False
                with open(patient_txt, "r", encoding='utf-8') as file:
                    for line in file:
                        element = line.strip().split(",")
                        if element[2] == doctor_id:
                            print(f"{BLUE}National code: {END}{element[0]}\n{BLUE}Name: {END}{element[1]}\n",
                                  end=f"{RED}{'-' * 18}{END}\n")
                            doctor_id_exists = True
                if not doctor_id_exists:
                    print_colored_message("No patient found with the requested doctor id", RED)

                patient_management()
                break
            else:
                print_colored_message("Doctor with this id is not registered", RED)
    except FileNotFoundError:
        print_colored_message(f"{patient_txt} not found", RED)
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)


def all_patients():
    try:
        print(f"{BACK}Show all patients{FRONT}")
        with open(patient_txt, "r", encoding='utf-8') as file:
            lines = sorted(file.readlines(), key=lambda a: a.split(",")[1])
            for line in lines:
                element = line.strip().split(",")
                print(
                    f"{BLUE}national id: {END}{element[0]}\n{BLUE}Name: {END}{element[1]}\n{BLUE}"
                    f"Doctor id: {END}{element[2]}\n", end=f"{RED}{'-' * 18}{END}\n")
        patient_management()
    except FileNotFoundError:
        print_colored_message(f"{patient_txt} not found", RED)
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)


def main_menu():
    try:
        result = pyfiglet.figlet_format("Medisys", font="slant")
        print(f"{GREEN}{result}{END}")
        print(f"{BACK}Main Menu{FRONT}", f"{GREEN}1. Doctor Management",
              "2. Patient Management",
              f"0. Exit{END}", sep="\n")
        user_input = input(f"{BLUE}Please select an option: {END}")
        match user_input:
            case "0":
                print_colored_message("Exiting...\nThank you for using this program", YELLOW)
                exit()
            case "1":
                doctor_management()
            case "2":
                patient_management()
            case _:
                print_colored_message("Invalid input", RED)
                main_menu()
    except Exception as e:
        print_colored_message(f"An error occurred: {e}", RED)
        main_menu()


if __name__ == '__main__':
    main_menu()
