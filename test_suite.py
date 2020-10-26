import unittest
from test_partida import TestPartida
from test_ahorcado import TestAhorcado


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Test1))
    test_suite.addTest(unittest.makeSuite(Test2))
    return test_suite

if __name__ == "__main__":
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests) 