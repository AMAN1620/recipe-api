from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(5, 5)

        self.assertEqual(res, 11)


# class CalcTestsSub(SimpleTestCase):

#     def test_subtract_numbers(self):
#         res = calc.sub(5, 6)

#         self.assertEqual(res, 1)
