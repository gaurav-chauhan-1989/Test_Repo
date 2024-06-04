import softest

class Test2(softest.TestCase):
    def test_2(self):
        self.soft_assert(self.assertEqual, 2, 3)
        print("Assertion Continue")
        self.soft_assert(self.assertEqual, 2, 2)
        self.assert_all()


class Test3(softest.TestCase):
    def test_3(self):
        self.soft_assert(self.assertEqual, 1 ,2)
        self.soft_assert(self.assertEqual, 2,2)
        self.assert_all()