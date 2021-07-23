string = input("Enter a string : ")
output = ""
for ch in string :
    if ch not in output:
        output=output+ch
        list1 = []
        for ch in string:
            if ch not in list1:
                list1.append(ch)
                print(list1)
                output2=''.join(list1)

                print("Original string :", string)
                print ("After the removing the  string: ", output)
