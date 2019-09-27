"""
put operators between numbers to make 100
"""


def process(numbers, operators):
    """
    builds interprets the value
    """
    accum = 0
    activ = '+'
    hold = 0

    for num, opr in zip(numbers, operators):
        hold *= 10
        hold += num
        if opr == ' ':
            continue
        if activ == '+':
            accum += hold
        elif activ == '-':
            accum -= hold
        hold = 0
        activ = opr
    hold *= 10
    hold += numbers[-1]
    if activ == '+':
        accum += hold
    elif activ == '-':
        accum -= hold

    return accum


def stringify(numbers, operators):
    """
    builds a string
    """
    out_str = ""
    for num, opr in zip(numbers, operators):
        out_str += str(num)+opr.strip()
    out_str += str(numbers[-1])

    return out_str


def main():
    """
    main driver
    rotates the operators spedometer style
    """
    operators = ['+', '+', '+', '+', '+', '+', '+', '+']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while len(operators) != operators.count(' '):
        roll_over = True
        for idx, value in enumerate(operators):
            if roll_over:
                roll_over = False
                if value == '+':
                    operators[idx] = '-'
                elif value == '-':
                    operators[idx] = ' '
                elif value == ' ':
                    operators[idx] = '+'
                    roll_over = True

        accumulator = process(numbers, operators)

        if accumulator == 100:
            out_str = stringify(numbers, operators)
            print(out_str)


if __name__ == "__main__":
    main()
