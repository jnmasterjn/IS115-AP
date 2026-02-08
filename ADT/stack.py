#this function checks if the braces in text are balanced
#ex) j{ani}ce is balance; j{{janci}rijfe is not balance


def push(my_stack:list, x):
    return my_stack.insert(0, x)

def check_braces(text):

    my_stack = []
    for letter in text:
        if letter == "{":
            push(my_stack, letter)
        elif letter == "}":
            if len(my_stack) > 0:
                my_stack.pop()
            else:
                return False
    return len(my_stack) == 0


print(check_braces("j{ani}ce"))
print(check_braces("j{{janci}rijfe"))