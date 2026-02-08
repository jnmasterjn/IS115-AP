def push(my_stack:list, ele):
    return my_stack.append(ele)

def pop(my_stack:list):
    return my_stack.pop()


my_stack = [5, 4, 3, 2, 1]
print(my_stack)
push(my_stack, 9)
print(my_stack)
print(pop(my_stack))
print(my_stack)
