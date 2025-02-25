# 빼기 함수
def subtract(a, b):
    return a - b


# 곱하기 함수
def multiply(a, b):
    return a * b


# 나누기 함수
def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

def power(a, b):
    return a ** b

def mod(a, b):
    return a % b

# 함수 사용 예시
if __name__ == "__main__":
    print("빼기:", subtract(10, 5))
    print("곱하기:", multiply(10, 5))
    print("나누기:", divide(10, 5))
