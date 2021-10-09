import unittest
from Phone import phone_methods

class Test_task2(unittest.TestCase):
    def context_search(self):
        number_contact = "+380994415656"
        self.assertEqual(phone_methods.search(number_contact), {"first_name": "Daniil", "last_name": "Roscha", "full_name": "Danil Roscha", "city": "Kyyv"})



if __name__ == '__main__':
    unittest.main()
