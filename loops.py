# print table of three
n = 3
i = 1
while i <=10:
    print(n*i)
    i += 1
print("program is ended")

# print all numbers in string:
list = [1,2,3,4,5,6]
i = 0
s = len(list)
while i < s:
    print(list[i])
    i += 1

# search a number in tupel
tup = (1,2,3,4,5)
p = len(tup)
i = 0
tar = 2
while i < p:
    if(tup[i] == tar):
        print("target is found at :", i)
    i += 1
print("program ended")