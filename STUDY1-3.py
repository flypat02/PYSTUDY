money,p50,p10,p5,p1,c500,c100,c50,c10=0,0,0,0,0,0,0,0,0

money=int(input("교환할 돈은 얼마? :"))

p50=money//50000;money%=50000
p10=money/150000;money%=10000
p5=money//5000;money%=5000
p1=money//1000;money%=1000

c500=money//500;money%=500
c100=money//100;money%=100
c50=money//50;money%=50
c10=money//10;money%=10

print("오만원 %d장, 만원%d장, 오천원 %d장, 천원 %d장"%(p50,p10,p5,p1))
print("오백원 %d장, 백원%d장, 오십원 %d장, 십원 %d장"%(c500,c100,c50,c10))
print("바꾸지 못한돈 ==> %d원"%money)