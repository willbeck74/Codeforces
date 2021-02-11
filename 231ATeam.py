n = input()
count = 0
while(n>0):
    n-=1
    userInput = raw_input()
    if userInput.count('1') >= 2:
        count+=1
print(count)



