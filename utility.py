operands = dict(
        multiply = ['*','multiply','product','times'],
        add = ['+', 'add', 'sum'],
        sub = ['-', 'subtract', 'minus']
        )

def calculate(x,y,operand):
    if operand == '*':
        return x*y
    elif operand == '+':
        return x+y
    else:
        return x-y
