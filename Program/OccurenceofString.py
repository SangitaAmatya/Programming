import unittest


def count_char (text):
    resl = []
    for i in range (len (text)):
        if len (text) == 0:
            break;
        ch = text [0]
        if ch == ' ' or ch == '\t':
            continue
        count = 1
        for j in range (1, len (text)):
            if ch == text [j]:
                count += 1

        text = text.replace (ch, '').strip ()
        #print (ch + " - ", count)
        res =[ch,count]
        resl.append(res)

    print (resl)
    return resl

count_char ('My strin gggg')


class occurenceof_Stringf (unittest.TestCase):
    def testcase1 (self):
        expected=[['M', 1], ['y', 1], ['s', 1], ['t', 1], ['r', 1], ['i', 1], ['n', 1], ['g', 4]]
        self.assertEqual (expected,count_char ('My strin gggg'), True)
        expected=[['M', 1], ['y', 1], ['s', 1], ['t', 1], ['r', 1], ['i', 1], ['n', 1], ['g', 4]]

