num1=0xFF00 & 0X00FF
num2=0xFF00 | 0X00FF
num3=0xFF00 ^ 0X00FF

print(hex(num1),hex(num2),hex(num3))

"""0XFF00의 2진수 표현 1111/1111/0000/0000
0X00FF의 2진수 표현 0000/0000/1111/1111 
논리 곱의 결과:0000/0000/0000/0000 ==>0X0
논리 합의 결과:1111/1111/1111/1111 ==>0XFFFF
배타적 논리합의 결과1111/1111/1111/1111 ==>0XFFFF
"""