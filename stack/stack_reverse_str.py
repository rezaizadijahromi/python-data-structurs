from stack import Stack


def reverse_string(stack, input_str):

    for i in range(len(input_str)):
        stack.push(input_str[i])
    
    reverse = ""

    while not stack.is_empty():
        reverse += stack.pop()

    return reverse


stack = Stack()
input_str = "RezaIzadiJahromi"
print(reverse_string(stack, input_str))