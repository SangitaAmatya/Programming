import unittest


def get_unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique
numbers = [1,2,2,24,5,6,7]
print(get_unique_numbers(numbers))
class Unique_Test(unittest.TestCase):
    def test1(self):
        expected = [4,5,7,8]
        self.assertEqual(expected,get_unique_numbers ([4,5,4,5,7,8]),True)

    def test2(self):
        expected = [4,5,7,8,-1]
        self.assertEqual(expected,get_unique_numbers ([4,5,4,5,7,8]),False)
# another way

List=[1,2,2,4,5,6,6,7]
unique_list=[]
for i in List:
    if i not in unique_list:
        unique_list.append(i)
        print("Unique number in a list is :",unique_list)
