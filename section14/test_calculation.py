import unittest

import lesson_unittest

release_name = 'lesson2'

class CalTest(unittest.TestCase):
    def setUp(self):
        print('setup')
        self.cal = lesson_unittest.Cal()

    def tearDown(self):
        print('clean up')
        del self.cal

    # @unittest.skip('skip!')
    @unittest.skipIf(release_name=='lesson', 'skip!!')
    def test_add_num_and_double(self):
        # cal = lesson_unittest.Cal()
        self.assertEqual(self.cal.add_num_and_double(1, 1,), 4)

    def test_add_num_and_double_raise(self):
        # cal = lesson_unittest.Cal()
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')

if __name__ == '__main__':
    unittest.main()