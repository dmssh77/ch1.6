# 다양한 file 입출력 함수

f = open("text.txt", "r", encoding="utf-8")
text= f.read()
print(text)
#f.close()

# position은 바이트 단위
pos = f.tell()
print(pos)

# position은 이동시키고 다시 읽기
f.seek(0)

text = f.read()
print("----" + text + "----")
f.close()

# 라인 단위로 읽기
line_num = 0
f2 = open("fileio2.py", "rt", encoding="utf-8")
while True:
    line = f2.readline()
    if line == "":
        f2.close()
        break

    line_num += 1
    print("{0}: {1}".format(line_num, line))

    print(line)


f3 = open("fileio2.py", "rt", encoding="utf-8")

for line in enumerate(f3.readlines()):
    print(line)

f3.close()

print("-------------------------")

with open("fileio2.py", "rt", encoding="utf-8") as f4:
    for line in enumerate(f4.readlines()):
        print("{0}: {1}".format(line_num, line))

print(f4.closed)

