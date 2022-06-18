import sys
import math


def main():
    rotors = []
    rotored_message = ""
    input_message   = ""
    output_message  = ""

    # Capturing inputs
    operation = input("Operation type (ENCODE|DECODE): ")
    pseudo_random_number = int(input("Caesar shift: "))
    for i in range(3):
        rotors.append(input(f"Rotor {i+1}: "))
    input_message = input(f"Message to {operation}: ")

    if operation == "ENCODE":
        # right-shift each character in the string by N
        for index, character in enumerate(input_message):
            # Beware about the overflow
            i = (ord(character) - ord("A") + pseudo_random_number + index) % (ord("Z") - ord("A") + 1)
            output_message += chr(i + ord("A"))
            
        # Now caesar shift has been created, send each character into consecutive rotors
        for rotor in rotors:
            for letter in output_message:
                index = ord(letter) - ord("A")
                rotored_message += rotor[index]
            output_message = rotored_message
            rotored_message = ""

    elif operation == "DECODE":
        for rotor in reversed(rotors):
            for letter in input_message:
                index = rotor.index(letter)
                rotored_message += chr(index + ord("A"))
            input_message = rotored_message
            rotored_message = ""
        
        # Left-shift each character in the string by N
        for index, character in enumerate(input_message):
            # Beware about the overflow
            i = (ord(character) - ord("A") - pseudo_random_number - index) % (ord("Z") - ord("A") + 1)
            output_message += chr(i + ord("A"))

    print(f"{output_message}")

if __name__ == "__EnigmaMachine__":
    main()