import unittest
from student import Student


class TestStudent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('~~~~setUpClass~~~~\n')

    @classmethod
    def tearDownClass(cls):
        print('~~~~tearDownClass~~~~\n')

    def setUp(self):
        self.obj_anna = Student('ana', 'kowalska', 4.6, None)
        self.obj_arek = Student('arkadiusz', 'nowak', 3.8, None)
        print(f'Tu metoda "setUP"')

    def test_email(self):
        self.assertEqual(self.obj_anna.email, 'ana.kowalska@university.com')
        self.assertEqual(self.obj_arek.email, 'arkadiusz.nowak@university.com')
        self.obj_anna.name = 'anna'
        self.assertEqual(self.obj_anna.email, 'anna.kowalska@university.com')
        print(f'Tu metoda "test_mail"')

    def test_fullname(self):
        self.assertEqual(self.obj_anna.fullname, 'Ana Kowalska')
        self.assertEqual(self.obj_arek.fullname, 'Arkadiusz Nowak')
        self.obj_anna.last = 'Zamezna'
        self.assertEqual(self.obj_anna.fullname, 'Ana Zamezna')
        print(f'Tu metoda "test_fullname"')

    def test_grand_scholarship_success(self):
        self.obj_anna.grant_scholarship()
        self.assertEqual(self.obj_anna.scholarship, True)
        self.obj_arek.grant_scholarship()
        self.assertEqual(self.obj_arek.scholarship, False)
        print(f'Tu metoda "test_grand..."')

    def tearDown(self):
        print(f'Tu metoda "tearDown"')


if __name__ == "__main__":
    unittest.main()
