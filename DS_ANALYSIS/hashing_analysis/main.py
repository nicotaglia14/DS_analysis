""""sites used:
 https://www.geeksforgeeks.org/introduction-to-hashing-data-structure-and-algorithm-tutorials/
 https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/
 https://medium.com/enjoy-algorithm/introduction-to-hashing-in-programming-617960aeccf2#:~:text=The%20division%20method%20or%20modular%20hashing&text=In%20the%20division%20method%20of,h(k)%20%3D%204.
"""

import math


txtFile = open("passwords.txt", "r")  # Open the txt file to read the data in it
reader = txtFile.read()
passwd_list = list(set(reader.split()))  # Get the data into a list of unique passwords

hash_table = {}


# function that assigns a value based on the addition of ascii values to each password
def create_keys(word):
    key = 0
    for letter in word:
        index = ord(letter)
        key += index
    return key


# function that creates the hash table and assigns the passwords to a key using addition method. It tracks the
# collisions
def addition_method(passwords):
    collisions = 0
    hash_table.clear()
    for word in passwords:
        key = create_keys(word)

        # If statement that determines if there is a value assigned to that key and detect collisions
        if hash_table.get(key) is None:
            hash_table[key] = word
        else:
            collisions += 1
    return collisions


# function that creates the hash table and assigns the password to a key usaing division method. It tracks the
# collisions
def division_method(passwords):
    collisions = 0
    hash_table.clear()
    for word in passwords:
        """ the numeric value of the word is divided by the length of the word in the
        attempt to reduce the amount of collisions by assigning different key values to words of different lengths but
        same ascii values"""
        key = create_keys(word) / len(word)

        # If statement that determines if there is a value assigned to that key and detect collisions
        if hash_table.get(key) is None:
            hash_table[key] = word
        else:
            collisions += 1
    return collisions


# function that creates the hash table and assigns the password to a key using multiplication method. It tracks the
# collisions
def mult_method(passwords):
    collisions = 0
    hash_table.clear()
    for word in passwords:
        key_value = create_keys(word)

        """The numeric value of the password is multiplied by the length of the hash table (biggest prime number bigger
        than the length of the passwords list. This method is based on the method shown in the link provided for the 
        assignment"""
        key = math.floor(10007 * (key_value * 0.357840 % len(word)))

        # If statement that determines if there is a value assigned to that key and detect collisions
        if hash_table.get(key) is None:
            hash_table[key] = word
        else:
            collisions += 1
    return collisions


check_add_method = addition_method(passwd_list)
print(f"Addition method: {check_add_method} collisions")
print(hash_table, "\n")

check_division_method = division_method(passwd_list)
print(f"Division method: {check_division_method} collisions")
print(hash_table, "\n")

check_multiplication_method = mult_method(passwd_list)
print(f"Multiplication method: {check_multiplication_method} collisions")
print(hash_table, "\n")
