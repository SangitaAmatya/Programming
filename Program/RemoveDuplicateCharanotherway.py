s = input("enter a string")
#
output = ''#empty string
for ch in s:
    if ch not in output:
        output=output+ch
print(output)
#2 nd way
duplicate="sssssssssdfeee"
duplicate_char=[]
for ch  in  duplicate:
            if ch not in duplicate_char:
                #
                duplicate_char.append(ch)
                Duplicate_char= ''.join(duplicate_char)
                #join all character present inside the list with out any separate
                print(duplicate_char)

                #3red way using set
dupli= "saaaanngiya"
duplicate_set=set(dupli)
output=''.join(duplicate_set)
print("duplicate : ",output)


