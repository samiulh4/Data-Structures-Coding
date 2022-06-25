# https://www.programiz.com/dsa/stack
# Stack implementation in python


# Creating an empty stack
def create_stack():
    stack = []
    return stack


# Adding items into the stack
def push_stack(stack, item):
    stack.append(item)
    print("pushed item: " + item)
    return len(stack) - 1


# Checking an empty stack
def check_empty(stack):
    if len(stack) <= 0:
        print('Your Current Stack Is Empty !')
        return False
    else:
        return True


def print_stack (stack):
    print('Printing Stack...')
    # start point, stop point, increment/decrement
    for i in range(len(stack)-1, -1, -1):     
        print(stack[i])     
# end -:- print_stack()           




if __name__ == '__main__':
    print('Starting Program...')
    top = -1
    stack = create_stack()
    # print(check_empty(stack))
    top = push_stack(stack, str(9))
    top = push_stack(stack, str(5))
    top = push_stack(stack, str(7))
    top = push_stack(stack, str(1))
    top = push_stack(stack, str(3))
    top = push_stack(stack, str(8))
    print(top)
    #print_stack(stack)
