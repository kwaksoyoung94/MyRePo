# 오류 메시지 상수
DIVIDE_BY_ZERO_ERROR = "Cannot divide by zero."


# Arithmetic operations functions
def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError(DIVIDE_BY_ZERO_ERROR)
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b


# Example usage
if __name__ == "__main__":
    operations = {
        "Subtraction": subtract,
        "Multiplication": multiply,
        "Division": divide,
    }

    a, b = 10, 5
    for operation_name, operation_func in operations.items():
        print(f"{operation_name}: {operation_func(a, b)}")
