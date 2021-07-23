from Program.ReverseA_String import reverse

string = "This is my car"


def RevesrseA_String (string):
    string = "This is my car"
word_list = string.split ()
reversed_list = word_list [:: -1]
reversed_sentence = " ".join (reversed_list)
print ("Reverse a string is :" + reversed_sentence)
reversed = string [::-1]
print ("Reverse the word is  : " + reversed)
rev_letters = ' '.join (word [::-1] for word in string.split (" "))
print (rev_letters)
