from math import *
import traceback


stack = []
debug = True

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
            if (token in list(operators)):
                stack.append(operators[token]())
            elif (token in list(special_functions)):
                special_functions[token]()
            else:
                stack.append(float(token))
        except:
            print("an error ocurred on the following token: " + token)
            if (debug): 
                traceback.print_exc()
            stack = backup_stack
            return
    print(stack[-1])


def pop(n = -1):
    return stack.pop(n) if len(stack) > -(1 + n) else 0



operators = {
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
    'ee': lambda: pop(-2) * (10 ** pop()),
}

special_functions = {
    'swap': lambda: stack.append(pop(-2)),
    'roll': lambda: stack.append(pop(int(-pop()-1))),
    'drop': lambda: stack.pop(),
    'dup': lambda: stack.append(stack[-1]),
    'pick': lambda: stack.append(stack[int(-pop()-1)])
}

main()