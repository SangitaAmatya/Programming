def checktheparenthsis(parentheses):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    map = dict(zip(open_list,close_list))
    a = []
    for i in parentheses:
        if i in open_list:
            a.append(map[i])
        elif i in close_list:
            if not a or i != a.pop():
                return "unbalance"
            if not a:
                return "balance"
            else:"unblance"
string = "{[]{()}}"
print (string, "-", checktheparenthsis (string))

string = "((()"
print (string, "-", checktheparenthsis (string))
