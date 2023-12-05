import unittest

from test_cases.Added_Player import TestAddedPlayer
from test_cases.Add_New_Player import TestAddNewPlayer
from test_cases.Change_language import TestChangeLanguage
from test_cases.Language_button import TestLanguageButton
from test_cases.login_to_the_system import TestLoginPage
from test_cases.Sign_out import TestSignOut


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAddedPlayer))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAddNewPlayer))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestChangeLanguage))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLanguageButton))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLoginPage))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSignOut))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
