##1stway
string = "saangitta"
x = set()
result = ''
for i in string:
    if i not in x:
        x.add(i)
        result=result+str(string.count(i))+i
        print(result)

        ##Anotherway
        # If you have to write the Python program to count frequency of each character without
        # using any String method
        # then you can write it using an outer and inner for loop.
        # In the outer loop take the character at index 0 and in the inner loop check
        # if such character is found again in the string, if yes then increment count.
        #replace() method of the str class is used to remove all the occurrences of the character
        # for which count is done so that same character is not picked again.

        def count_char (text):
            for i in range (len (text)):
                if len (text) == 0:
                    break;
                ch = text [0]
                # don't count frequency of spaces
                if ch == ' ' or ch == '\t':
                    continue
                count = 1
                for j in range (1, len (text)):
                    if ch == text [j]:
                        count += 1
                # replace all other occurrences of the character
                # whose count is done, strip() is required for
                # scenario where first char is replaced and there is
                # space after that
                text = text.replace (ch, '').strip ()
                print (ch + " - ", count)

        count_char ('sanggita  ass')