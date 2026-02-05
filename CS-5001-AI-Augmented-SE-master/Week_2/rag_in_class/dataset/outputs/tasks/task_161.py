def remove_elements(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result

def insert_element(list1, element, position):
    if position < 0 or position > len(list1):
        return list1
    list1.insert(position, element)
    return list1

def find_element(list1, element):
    for i, x in enumerate(list1):
        if x == element:
            return i
    return -1

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

def count_vowels(s):
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count
