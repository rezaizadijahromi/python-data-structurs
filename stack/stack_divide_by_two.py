from stack import Stack

def div_by_two(num):
    s = Stack()

    while num != 0:
        remainder = num % 2
        s.push(remainder)
        num //= 2
    
    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num


f = div_by_two(242)
print(f)

 