# print() 연습
import sys

print(1)
print("Hello", "World")

x = 0.2
s = "Hello World"

# sep, end 키워드 파라미터 지정
print(x, s, sep=",")
print(str(x) + "," + s)

print(x, s, sep=",", end=" ")

# 기본적인 print() 호출은
print(sep=" ", end="\n")

# file 파라미터 지정 가능
print("Hello World", file=sys.stdout)
print("error", file=sys.stderr)

# file 출력
f = open("hello.txt", "w")
print("hello world", file=f)

# 참고
sys.stdout.write("wowwow")

