num=input("16진수 한글자 입력 :")

if (num>="0" and num<="9") or (num>="A" and num<"G") or (num>="a" and num<"g"):
  print("10진수 ==>",int(num,16))
else:
  print("16진수가 아닙니다")