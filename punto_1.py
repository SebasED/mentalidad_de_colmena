"""
Ace quiere ser voluntario para viajar a K-Pax, para ello la Agencia Espacial Canadiense 
requiere que llene un formulario que ayude a obtener más información de él y su familia.
Tu debes ayudar a Ace creando un programa para completar la información solicitada sin 
sobrescribirel archivo. Ten presente quelos datos con * son los másimportantes, siuno de
esos campos no se llena, no podráser admitido, en caso de que el dato solicitado no sea
importante, el programa deberáponer “unknown”. Archivo: required_data.txt
"""


def start_menu():
    """Show two options (Yes or No) and return a boolean

    Returns:
    (bool): True or False
    
    """

    while True:

        print("""
        Do you want to fill the file for traveling to K-pax?
        - Yes
        - No
        """)

        option = input().lower()

        if not (option == "yes" or option == "no"):
             print("Enter a valid option")
             print() 
        elif option == "yes": return True
        elif option == "no": return False


def read_file():
    """Read the empty file.

    Returns:
        (List): List with the lines of the file
    """
    with open("required_data.txt", "r+") as f:
        return f.readlines()


def write_file(new_file):
    """Overwrite or create a new file

    Args:
        new_file (List): List with the lines for the new file
    """
    with open("required_data_full.txt", "w") as f:
        f.writelines(new_file)


def enter_data(file):
    """The user enters the requiered data 

    Args:
        file (List): List with the lines of the empty file

    Returns:
        (List): List with the user's data
    """
    new_file = []
    for line in file:

        if (" -" in line) or (line.startswith("|")) or (line == '\n') or (line.startswith("•")):
            new_file.append(line)
            print(line)
            continue

        """Print lina with the information that the user needs to enter."""
        print(line)
        if "*" in line:
            string = input()
            while not string:
                print("You need to enter a value in this field \n")
                string = input()
                if string:
                    new_file.append(concatenate_string(line, string))
                    break
            new_file.append(concatenate_string(line, string))
        else:
            string = input()
            new_file.append(concatenate_string(line, string))

    return new_file


def concatenate_string(line, string):
    """Concatenate two strings

    Args:
        line (str): Information from the empty file
        string (str): Information that the user enter

    Returns:
        str: Join between the require information and the user's information
    """
    if not line.endswith("\n"):
        return line + " " + string
    else:
        return line[:-1] + " " + string + "\n"


def main():
    """Principal system function."""
    if start_menu():
        file = read_file()
        file = enter_data(file)
        write_file(file)
    else:
        print("Bye! ")
        exit()


if __name__ == "__main__":
    main() 