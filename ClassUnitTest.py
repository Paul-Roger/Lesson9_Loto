import unittest
from ClassesDefinition import *

class TestLotoCard(unittest.TestCase):

    def setUp(self):
        self.lottocard = LotoCard('Ivanoff')

    def tearDown(self):
        del self.lottocard

    def test_numofnonzero(self):
        self.assertEqual(num_of_nonzero([0, 1, 2, 0, 4, 0, 6, 0, 8, 9]), 6)

    def test_init(self):
        self.assertEqual(self.lottocard.ownername, 'Ivanoff')
        self.assertEqual(len(self.lottocard.bingoballs), 0)
        self.assertEqual(len(self.lottocard.numbers), MaxRows)
        self.assertEqual(len(self.lottocard.numbers[0]), MaxCol)

    def test_fillcard(self):
        numcount = 0
        figures= []
        is_double = False
        currnum = 0
        for i in range(len(self.lottocard.numbers)):
            numcount += num_of_nonzero(self.lottocard.numbers[i])
            for j in range(len(self.lottocard.numbers[i])):
                currnum = self.lottocard.numbers[i][j]
                if currnum > 0:
                    if currnum in figures:
                        is_double = True
                    else:
                        figures.append(currnum)
            if is_double:
                break
        self.assertEqual(numcount, 15)
        self.assertFalse(is_double)

    def test_contain(self):
        self.assertFalse(100 in self.lottocard)

    def test_crossout(self):
        for i in range(90):
            self.assertEqual(self.lottocard.crossout(i), 0)
            if len(self.lottocard.bingoballs) >=14:
                break
        self.lottocard.lotocardprn()
        print(self.lottocard.bingoballs)
        #self.assertEqual(self.lottocard.crossout(i), 1)


#====================================================================================================================
#====================================================================================================================

class TestLotoBag(unittest.TestCase):

    def setUp(self):
        self.lottobag = LotoBag()

    def tearDown(self):
        del self.lottobag

    def test_init(self):
        self.assertEqual(len(self.lottobag.balls), 90)
        self.assertListEqual(self.lottobag.selected, [])

    def test_Len(self):
        self.assertEqual(len(self.lottobag), 90)

    def test_nextball(self):
        for i in range(90):
            self.assertGreater(self.lottobag.nextball(), 0)
            self.assertEqual(len(self.lottobag.balls), 89 - i)
            self.assertEqual(len(self.lottobag.selected), i + 1)
        self.assertEqual(self.lottobag.nextball(), 0)

    def test_sub(self):
        self.lottobag2 = LotoBag()
        self.lottobag2 -= 13
        self.assertFalse(13 in self.lottobag2.balls)
        self.assertTrue(12 in self.lottobag2.balls)


#====================================================================================================================
#====================================================================================================================

class TestLotoPlayer(unittest.TestCase):

    def setUp(self):
        self.lottoplayer = LotoPlayer("Ivanov", False)

    def tearDown(self):
        del self.lottoplayer

    def test_init(self):
        self.assertEqual(self.lottoplayer.name, 'Ivanov')
        self.assertEqual(len(self.lottoplayer.lotocard.numbers), MaxRows)
        self.assertEqual(len(self.lottoplayer.lotocard.numbers[0]), MaxCol)

    def test_checball(self):
        for i in range(10):
            self.assertEqual(self.lottoplayer.checkball(i), 0)

