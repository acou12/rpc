from math import *

stack = []

def main():
    while (True):
        evaluate()

def evaluate():
    global stack
    backup_stack = stack.copy() # in case there's an error
    inp = input("RPC >>> ")
    if inp == "":
        print(stack)
        return
    split = inp.strip().split(' ')
    for token in split:
        token = token.lower()
        try: 
            if (token in list(operations)):
                stack.append(operations[token]())
            else:
                stack.append(float(token))
        except:
            print("an error ocurred on the following token: " + token)
            stack = backup_stack
            return
    print(stack[-1])


def pop(n = -1):
    return stack.pop(n) if len(stack) > 0 else 0
    
operations = {
    '+': lambda: pop() + pop(),
    '-': lambda: pop(-2) - pop(),
    '--': lambda: - pop(),
    '*': lambda: pop() * pop(),
    '/': lambda: pop(-2) / pop(),
    '^': lambda: pop(-2) ** pop(),
    '**': lambda: pop(-2) ** pop(),
    'log': lambda: log(pop()),
    'log10': lambda: log10(pop()),
    'ln': lambda: log(pop()),
    'l': lambda: log10(pop()),
    'sqrt': lambda: sqrt(pop()),
    'q': lambda: sqrt(pop()),
    'e': lambda: pop(-2) * (10 ** pop()),
    'ee': lambda: pop(-2) * (10 ** pop())
}

main()