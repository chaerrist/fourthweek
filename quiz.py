# 1번
def is_even(n):
    if n %2 == 0:
        print("짝수")
    else:
        print("홀수")
        
num = input("숫자를 입력하세요: ")
is_even(int(num))

# 2번
def reverse_str(msg):
    return msg[::-1]

in_msg = input("문자열: ")
print(reverse_str(in_msg))

# 3번
add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b

numb1 = input("숫자를 입력하시오")
numb2 = input("숫자를 입력하시오")

def pr_num(n1, n2):
    num1 = int(n1)
    num2 = int(n2)
    print(add(num1, num2))
    print(sub(num1, num2))
    print(mul(num1, num2))
    print(div(num1, num2))
    
pr_num(numb1, numb2)

#4번
num_list = []

for i in range(5):
    k = 0
    imp_num = input("숫자를 입력하시오: ")