"""
En un episodio de CSI un capo de la mafia diseño un interesante método para evitar que en
sus mensajes descubrieran los números telefónicos, las direcciones y los valores reales de
sus transacciones. El método se llamaba Saltando al 5. 

Es una estrategia simple e ingeniosa, cada digito es cambiado por el opuesto del teclado 
telefónico saltando al número 5, como lo muestra la siguiente figura:

Como lo muestra la figura:
    • Del 1 se salta al 9 y del 9 al 1 (por encima del 5).
    • Del 2 se salta al 8 y del 8 al 2 (por encima del 5).
    • Del 3 se salta al 7 y del 7 al 3 (por encima del 5).
    • Del 4 se salta al 6 y del 6 al 4 (por encima del 5).
    • Del 5 se salta al 0 y del 0 al 5.

Así cuando se pasaba un mensaje primero se codificaban todos los números en él de acuerdo
con los saltos.

Por ejemplo, si el mensaje es: “Llamar despuésde las 9:54 al teléfono 3122345676”, 
el mensaje codificado sería: “Llamar después de la 1:06 al teléfono 7988760434”.

Lo que debes hacer es implementar una función que codifique y otra que decodifique mensajes
utilizando la estrategia Saltando al 5. Así que muestra un menú con las opciones.

"""

def menu():
    """Show diferent option for the user

    Returns:
    (str): 1 or 2 for encode or decode respectively
    """

    while True:

        print("""
        Select a option:
        1. encode
        2. decode
        3. exit
        """)

        option = input()

        if option == "1" or option == "2":
            return option 
        elif option == "3":
            print("Bye! ")
            exit()
        else:
            print("Select a correct option.")


def separate_numbers(message):
    """Separate numbers of a string in a different list

    Args:
        message (str): String with the numbers to separate

    Returns:
        (List): List with numbers 
    """
    list_message = list(message)
    numbers = []
    for item in list_message:
        """Compare ASCII values."""
        if (ord(item) >= 48) and (ord(item) <= 57):
            numbers.append(item)
    return numbers


def join_numbers(message, numbers):
    """Replace the numbers in a list with other numbers list

    Args:
        message (List): List where the numbers will be replaced
        numbers (List): List with numbers

    Returns:
        (str): String with new number incorporated
    """
    list_message = list(message)
    count = 0
    for index, char in enumerate(list_message):
        """Compare ASCII values."""
        if (ord(char) >= 48) and (ord(char) <= 57):
            list_message[index] = numbers[count]
            count += 1
        if count == len(numbers): break

    """convert list to str"""
    str_message = "".join(list_message)  
    return str_message


def encode_and_decode(message):
    """Encode or decode a message

    Args:
        message (str): String to encode or decode

    Returns:
        (str): Encode or decode message
    """
    numbers = separate_numbers(message)

    for index, num in enumerate(numbers):
        if num == "1": numbers[index] = "9"
        elif num == "2": numbers[index] = "8"
        elif num == "3": numbers[index] = "7"
        elif num == "4": numbers[index] = "6"
        elif num == "5": numbers[index] = "0"
        elif num == "6": numbers[index] = "4"
        elif num == "7": numbers[index] = "3"
        elif num == "8": numbers[index] = "2"
        elif num == "9": numbers[index] = "1"
        elif num == "0": numbers[index] = "5"

    encode_message = join_numbers(message, numbers)
    return encode_message


def main():
    """Principal system function."""
    option = menu()
    
    message = input("Enter the message: \n")

    new_message = encode_and_decode(message)

    if option == "1":
        print("The encode message is:")
        print(new_message)
    else: 
        print("The decode message is:")
        print(new_message)


if __name__ == "__main__":
    main() 

