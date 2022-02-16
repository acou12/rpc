from math import *
import traceback


stack = []
variables = {}
debug = True

def main():
    while (True):
        go()

n = 0

def evaluate(tokens):
    tokens = [x for x in tokens if x != ""]
    global stack
    backup_stack = stack.copy() # in case there's an error
    making_expression = False
    for token in tokens:
        token = token.lower()
        try: 
            if token[0] == '}':
                making_expression = False
                stack.append(expression)
            elif making_expression:
                expression += token + " "
            elif token == '?':
                if not pop():
                    return 
            elif token in list(operators):
                stack.append(operators[token]())
            elif token in list(special_functions):
                special_functions[token]()
            elif token[0] == '\\':
                variables[token[1:]] = pop()
            elif token[0] == '/':
                if token[-1] == '!':
                    evaluate(variables[token[1:-1]].split(' '))
                else:
                    stack.append(variables[token[1:]])
            elif token[0] == '{':
                making_expression = True
                expression = ""
            elif token[0] == '!':
                evaluate(pop().split(' '))
            else:
                stack.append(float(token))
        except:
            print("an error ocurred on the following token: " + token)
            if (debug): 
                traceback.print_exc()
            stack = backup_stack
            return

def go():
    global stack
    inp = input("RPC >>> ")
    if inp == "":
        print(stack)
        return
    split = inp.strip().split(' ')
    evaluate(split)
    global n
    if len(stack) > 0:
        variables[str(n)] = stack[-1]
        print("/" + str(n) + " = " + str(stack[-1]))
        n += 1


def pop(n = -1):
    return stack.pop(n) if len(stack) > -(1 + n) else 0

def peek(n = -1):
    return stack[-n] if len(stack) > -(n) else 0

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
    'len': lambda: len(stack)
}

special_functions = {
    'swap': lambda: stack.append(pop(-2)),
    'roll': lambda: stack.append(pop(int(-pop()-1))),
    'drop': lambda: stack.pop(),
    'dup': lambda: stack.append(stack[-1]),
    'pick': lambda: stack.append(stack[int(-pop()-1)])
}

# example function (factorial)
evaluate(
    "{ dup 1 - ? dup 1 - /fact! * } \\fact".split(' ')
    # explaination:
    # {                  begin function
    # dup 1 -            push the top of the stack minus 1
    # ?                  if it's zero, exit
    # dup 1 - /fact! *   if not, push (n - 1)! * n
    # }                  end function
    # \fact             define the function as fact
)

main()