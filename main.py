"""
put operators between numbers to make 100
"""


def process(numbers, operators):
    """
    builds a string then calls eval on it
    """
    out_str = ""
    for num, opr in zip(numbers, operators):
        out_str += str(num)+opr.strip()
    out_str += str(numbers[-1])
    return_value = eval(out_str)

    return return_value, out_str


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

        accumulator, out_str = process(numbers, operators)
        if accumulator == 100:
            print(out_str)


if __name__ == "__main__":
    main()
