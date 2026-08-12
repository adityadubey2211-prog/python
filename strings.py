# concatination
str1 = "Aditya"
str2 = "Dubey"
finalstr = str1 + str2
print(finalstr) #output -> AdityaDubey
print(len(finalstr))#output -> 11
print(finalstr[0])#output -> A
print(finalstr[1])#output -> d
print(finalstr[1:4])#output -> dit
print(finalstr[-5:-1])#output -> Dube
str3 = "I love dubai"
print(str3.endswith("i"))#true because str3 ends with "i"
print(str3.capitalize())# output -> I love dubai (it dose not change orignal string)
print(str3.replace("I",  "WE"))# output -> WE love dubai
print(str3.find("dubai"))# output -> 7
print(str3.count("e"))# output -> 1