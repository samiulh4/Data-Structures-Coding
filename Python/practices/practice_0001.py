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


# Checking an empty stack
def check_empty(stack):
    if len(stack) <= 0:
        print('Your Current Stack Is Empty !')
        return False
    else:
        return True




if __name__ == '__main__':
    print('Starting Program...')
    stack = create_stack()
    # print(check_empty(stack))
    push_stack(stack, str(9))
    push_stack(stack, str(5))
    push_stack(stack, str(3))
    push_stack(stack, str(8))