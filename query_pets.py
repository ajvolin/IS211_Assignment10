#!/usr/bin/python
# -*- coding: utf-8 -*-

"""query_pets.py: IS 211 Assignment 10."""

__author__ = 'Adam Volin'
__email__ = 'Adam.Volin56@spsmail.cuny.edu'

import sys
import load_pets


def display_person(id, pets_db):
    """Function to display a person's information and pets."""
    
    # Select the person with the provided ID number
    person = (pets_db.cursor.execute('''
                SELECT  first_name,
                        last_name,
                        age
                FROM person
                WHERE id = (? )
            ''', (id, ))).fetchall()
    
    # Check to see if a record could be found for the ID number
    if len(person) > 0:
        print("\n{} {}, {} years old.".format(person[0][0], 
                                    person[0][1], person[0][2]))

        # Select pets that belong to the person
        pets = (pets_db.cursor.execute('''
                SELECT  name,
                        breed,
                        age,
                        dead
                FROM pet
                INNER JOIN person_pet
                on person_pet.pet_id = pet.id
                WHERE person_pet.person_id = (? )
            ''', (id, ))).fetchall()

        # Check to see if pets could be found for the ID number
        if len(pets) > 0:
            for pet in pets:
                print("{} {} {} {}, a {}, that {} {} years old." \
                    .format(
                            person[0][0], 
                            person[0][1],
                            "owns" if pet[3] == 0 else "owned",
                            pet[0],
                            pet[1],
                            "is" if pet[3] == 0 else "was",
                            pet[2]
                        )
                    )

        # Otherwise print a messsage that the person has no pets
        else:
            print("{} {} owned no pets.".format(person[0][0], 
                                    person[0][1]))

        # Print new line for readability
        print("\n")
    
    # Otherwise print a message that the person could not be found.
    else:
        print("Unable to locate a person with that ID number, please try again.")


def get_id():
    """
    Function to request a person's ID #
    
    Returns:
        (int): An ID number for a person
    """
    try:
        id = int(input('Enter a person ID # or -1 to exit: '))
        return id

    except ValueError:
        print('Please enter a valid numerical person ID')
        get_id()


def main():
    """The function that runs when the program is executed."""

    # Use the PetsDB class to connect to the pets.db sqlite database
    pets_db = load_pets.PetsDB()

    # Track if the user wishes to exit
    exit_signal = False

    while not exit_signal:
        id = get_id()

        if id == -1:
            print('Received entry of -1. Exiting program.')
            exit_signal = True
            
        else:
            display_person(id, pets_db)

    sys.exit()


if __name__ == '__main__':
    main()
