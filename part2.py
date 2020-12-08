#Write a function that takes in a list of strings. Return the longest string in the list.
def longest_string(myList):
    longest = myList[0]
    for str in myList:
        if len(str) > len(longest):
            longest = str
    return longest

#Write a function that takes in an item and a list. Return the number of times the given item appears in the list.
def item_in_list(item, myList):
    count = 0
    for each_item in myList:
        if each_item == item:
            count += 1
    return count

#Write a function that takes in a list of numbers. It should find all even numbers and return a list of their indices. For example
#[2, 4, 1] => [0, 1]
#[] => []
#[1] => []
def find_indices(myList):
    indices = []
    for i in range(0, len(myList)):
        if myList[i] % 2 == 0:
            indices.append(i)
    return indices

#Write a function that takes in a string and returns a string with all vowels replaced with *
def change_vowels(str):
    new_str = ""
    for char in str:
        if char in ['a','e','i','o','u']:
            new_str += '*'
        else:
            new_str += char
    return new_str

#Write a function that takes in a string and returns all unique characters in the string
def unique_chars(str):
    results = set()
    for char in str:
        results.add(char)
    return results

#Write a function that takes in a string and returns a character count dictionary. For example,
#'catty' => {'c': 1, 'a': 1, 't': 2, 'y': 1}
def char_dict(str):
    my_dict = {}
    for char in str:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1

    return my_dict

#Write a function that takes in two strings and returns True if the strings are anagrams of one another. For example,
#'moon', 'noom' => True
#'bat', 'snack' => False
#'', '' => True
def is_anagram(str1, str2):
    dict1 = {}
    for char in str1:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1        
    dict2 = {}
    for char in str2:
        if char in dict2:
            dict2[char] += 1
        else:
            dict2[char] = 1 

    return dict1 == dict2