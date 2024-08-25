# This function store the personal user's data in a file.
# The path of the file will be inside the project's directory.
import os


def Store_Data_Into_Volume(user):
    # This is the PATH inside the Project Directory (current directory)
    # -> Python_App_Using_Kubernetes/Store_Data/Store_data.py
    absolutepath = os.path.abspath(__file__)

    # Go up one level -> Python_App_Using_Kubernetes/Store_Data
    one_level_up = os.path.dirname(absolutepath)

    # Go up two levels -> Python_App_Using_Kubernetes
    two_level_up = os.path.dirname(one_level_up)

    # Check if the directory inside the project exist or not.
    # In case it doesn't exist, it is created.
    directory_storage = os.path.join(two_level_up, "Storage")

    # Name of the file will contain the user's data.
    file_name = "Data_Users.txt"

    file_path = os.path.join(directory_storage, file_name)

    if not os.path.exists(directory_storage):
        os.makedirs(directory_storage)
        print(f"Created directory: {directory_storage}")

    try:
        with open(file_path, 'a+') as storage_file:
            storage_file.write(f"Name: {user.get_name()}\n")
            storage_file.write(f"Surname: {user.get_surname()}\n")
            storage_file.write(f"Address: {user.get_address()}\n")
            storage_file.write(f"Phone Number: {user.get_phone_number()}\n\n")
    except FileNotFoundError:
        with open(file_path, 'w+') as storage_file:
            storage_file.write(f"Name: {user.get_name()}\n")
            storage_file.write(f"Surname: {user.get_surname()}\n")
            storage_file.write(f"Address: {user.get_address()}\n")
            storage_file.write(f"Phone Number: {user.get_phone_number()}\n\n")
    except PermissionError:
        print("You do not have permission to access this file.")
    except IOError:
        print("An I/O error occurred while writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
