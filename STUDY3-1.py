#1번
def solution(flo):
  result=flo
  return result

flo=float(input("숫자 입력 :"))

result=solution(flo)

print("%.2f의 정수 부분은 %d입니다"%(flo,result))

#2번
def solution(my_string,target):
  if target in my_string:
    return 1
  else:
    return 0

my_string="banana"
target=input("입력하시오:")

gap=solution(my_string,target)
print("%d"%gap)

#3번
def solution (num_str):
    a=[]
    result=0
    for i in str(num_str):
      a.append(i)
    
    a=list(map(int,a)) #int형으로 형변환
    
    for k in range(0,len(a),1):
      result
      result+=a[k]
    return result
  
num_str=input("숫자를 입력하시오:")
hap=solution(num_str)
print("값은 :%d"%hap)

#4번
def solution (num_list):
  num_list.sort() #오름차순 정렬
  answer=num_list[:5] #5개까지 출력
  return answer

num_list=[12,4,15,46,38,1,14]
up=solution(num_list)
print(up)

#5번
def solution(my_string):
  return my_string.split() 

my_string=input("문자열을 입력하세요:")
na=solution(my_string)
print(na)