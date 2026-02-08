#use stack and queue to check if a word is palindrome


#functions for stack
def push(my_stack:list, ele):
    return my_stack.insert(0, ele)

def pop(my_stack:list):
    return my_stack.pop()

#functions for queue
def enqueue(my_queue:list, ele):
    return my_queue.append(ele)

def dequeue(my_queue:list):
    return my_queue.pop(-1)

def is_palindrome(text):
    my_stack = []
    my_queue = []
    for letter in text:
        push(my_stack, letter)
        enqueue(my_queue, letter)


    return my_stack == my_queue


print(is_palindrome("madam"))
print(is_palindrome("maierjfweijfdam"))
print(is_palindrome("racecar"))