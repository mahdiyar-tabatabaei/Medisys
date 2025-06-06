# Medisys
🩺 Doctor & Patient Management System (Medisys)
A Python CLI program for managing doctors and patients using text files. Designed for simplicity and portability with no database required.

📌 Features

- Add, remove, edit, and search doctors
- Add, remove, edit, and list patients
- Filter patients by assigned doctor
- Search doctors by specialty
- Input validation (e.g. mobile number, national code)
- Colored output using `colorama` for better UX
- Simple data persistence with `.txt` files

🚀 How to Run

	1. Make sure Python 3 is installed on your system.
	2. Install required dependencies:
		pip install colorama pyfiglet
	3.Run the main script:
		python Medisys.py
🗂️ File Structure

	Medisys.py          # Main CLI logic and user interaction
	file_aid.py         # Helper functions for file I/O and validation
	Doctors.txt         # Stores doctor records
	Patients.txt        # Stores patient records
	README.md           # Project documentation
⚠️ Notes
This script works on any OS where Python is supported.

Data is stored in plain text files – no external database needed.

File I/O is handled simply and may not scale for large datasets.

👤 Author
[Mahdiyar Tabatabaei](https://github.com/mahdiyar-tabatabaei)
