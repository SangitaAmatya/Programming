string = "sangggttsssita"
s = []
for i in string:
    # find the occurence is grater then one
    if string.count(i)>1:
        if i not in s:
         s.append((i))
         print (s)
