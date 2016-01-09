import unittest
from sasm3 import Lexer, Parser


def test(asmfile):
    print(asmfile)
    lexer = Lexer(asmfile)
    parser = Parser(lexer)
    parser.parse()
    return True


asmfile1 = ("""
end
""")

asmfile2 = ("""



end
""")

asmfile3 = ("""
;-- Comment 1
  ;-- Comment 2


  end
""")

asmfile4 = ("""
;-- Comentario 1
;-- Comentario 2

     org 0

     org 100

     org H'100

     org 512     ;-- Comentario 3

     end
""")

asmfile5 = ("""
    org hola


    org 0

    org H'00

    org H'CACA

    org inicio

     end
""")

asmfile6 = ("""
val1   DATA 10
val2   DATA h'FA
       DATA 1, 2, 3, 4, 5, 6
val3   DATA "a", 3, "b", "hola"
       DATA "sentence...."

     end
""")


class TestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(test(asmfile1), True)

    def test_2(self):
        self.assertEqual(test(asmfile2), True)

    def test_3(self):
        self.assertEqual(test(asmfile3), True)

    def test_4(self):
        self.assertEqual(test(asmfile4), True)

    def test_5(self):
        self.assertEqual(test(asmfile5), True)

    def test_6(self):
        self.assertEqual(test(asmfile6), True)


# -- Main program
if __name__ == '__main__':
    unittest.main()
