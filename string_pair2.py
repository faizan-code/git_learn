text = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numVowels = [2, 2, 1, 2, 2, 2, 1, 2, 2, 2]
n = int(input())
number = list(map(int, input().strip().split()))
s = 0
for i in range(n):
    for num in str(number[i]):
        s = s + numVowels[int(num)]
        result = 0
for i in range(n-1):
    for j in range(i+1,n):
        if number[i] + number[j] == s:
            result = result+1
if result <= 100:
        print(text[result],end="")
else:
        print("greater 100",end="")