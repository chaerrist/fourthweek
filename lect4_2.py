# 콜백 함수
# def prt_func(n):
#     print("hello", n)
    
# def callfunc(fx):
#     for i in range(5):
#         fx(i)
    
# callfunc(prt_func)

# def update_msg(name: str) -> list:
#     msg = []
#     msg.append("Hello," + name)
#     msg.append("Bye," + name)
#     return msg

# def greeting(in_name: str) -> list:
#     gt_msg = None
#     gt_msg = update_msg(in_name)
#     return gt_msg 

# res = greeting("python")

# for message in res:
#     print(message)

# import calc

# print(calc.add(8, 4))
# print(calc.sub(8, 4))
# print(calc.mul(8, 4))
# print(calc.div(8, 4))


import calc as cl

print(cl.add(8, 4))
print(cl.sub(8, 4))
print(cl.mul(8, 4))
print(cl.div(8, 4))



import mod.circle_mod as cm

print(cm.pi)
t = int(input("숫자를 입력하시오."))
print("%d 의 넓이는 %d 입니다.", t, cm.area(t))
print("%d 의 둘레는 %d 입니다.", t, cm.circum(t))

import mod.str_util as smod

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutstr(url, "/", 3)
print(res)

import math

# 입력받은 수 제곱근 계산 : sqrt
input_num = float(input("숫자를 입력하시오"))
sq_res = math.sqrt(input_num)
print(sq_res)
# 삼각함수 계산 sin * pi / 2
sin_res = math.sin(math.pi /2)
print(sin_res)
# 자연로그 x=y, x=e^y = log(e)
e_res = math.log(math.e)
print(e_res)
# 지수계산 ln(x) = y, x= e^y, x=exp(y) 즉, exp(x)
exp_res = math.exp(input_num)
print(exp_res)
# 파이계산 pi
pi_res = math.pi
print(pi_res)