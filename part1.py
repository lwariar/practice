#Write a function that takes in a list and prints each item in the list.
def print_each_item(myList):
    for item in myList:
        print(item)

#Write a function that takes in a list of words. For each word, the function should print a tuple of (first_letter_of_word, word).
def print_tuple(myList):
    for word in myList:
        print((word[0], word))

#Write a function that takes in a list of numbers. It should print every other number, starting with the number at index 0.
def print_every_other(myList):
    print(myList[::2])

#Write a function that takes in a list and an item. It should return True if the list contains the item. Otherwise, return False.
def find_item(myList, item):
    for each_item in myList:
        if each_item == item:
            return True
    return False

#Write a function that takes in a string and returns the length of that string. You cannot use the len function.
def find_length(str):
    length = 0
    for char in str:
        length += 1
    return length

#Write a function that takes in a sentence as a string. The function should print the length of each word in the sentence.
#Your sentence will not contain any punctuation.
def print_len_word(str):
    for word in str.split():
        print(word, len(word))

#Write a function that takes in a list of numbers and returns the largest number in the list. You cannot use the max function.
def largest_number(myList):
    largest = myList[0]
    for num in myList:
        if num > largest:
            largest = num
    return largest