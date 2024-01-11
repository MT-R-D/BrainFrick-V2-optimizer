import re

# globals
values = {}


def load_code(file_path):
    f = open(file_path, 'r')
    code_buffer = f.readlines()
    for i, op in enumerate(code_buffer):
        code_buffer[i] = op.strip()
    return code_buffer


def save_code(file_path, code):
    if code is None:
        return
    f = open(file_path, 'w')
    f.write(code)


def parse_operation(operation):
    pattern = r"\[(\d+)\]\s+([^\s]+)\s+(.+)"
    match = re.match(pattern, operation)
    if match:
        return match.groups()
    else:
        raise ValueError(f"Invalid string format: {operation}")


def run_operation(index: int, operator: str, value: int):
    if operator == '+':
        values[index] = values.get(index, 0) + value
    elif operator == '-':
        values[index] = values.get(index, 0) - value
    elif operator == '*':
        values[index] = values.get(index, 0) * value
    elif operator == '/':
        values[index] = values.get(index, 0) // value
    elif operator == '=':
        values[index] = value


def consider_operation(index: str, operator: str, value: str):
    index = int(index)
    value = int(value)

    run_operation(index, operator, value)


def generate_optimized_code():
    code = ''
    for index, value in values.items():
        code += f"[{index}] = {value}\n"
    return code


def main():
    code = load_code('code.txt')
    for op in code:
        index, operator, value = parse_operation(op)
        consider_operation(index, operator, value)
    optimized_code = generate_optimized_code()
    save_code('optimized.txt', optimized_code)


if __name__ == '__main__':
    main()
