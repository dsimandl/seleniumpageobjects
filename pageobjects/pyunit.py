import sys, unittest, re, time, os.path, logging

from .logon.logonpagebuilder import LoginPageObject
from pageobjects import selenium_server_connection

class PageObjectExample(unittest.TestCase):

    def setUp(self):
        self.log = logging.getLogger("pragmatic.pageobjectexaple")
        self.verificationerrors = []
        self.selenium = selenium_server_connection.connect("localhost", 4444, "*chrome", "http://some.test.site")
        self.selenium.start()

    def testLogin(self):
        lpo = LoginPageObject(self.selenium)
        lpo.username = "adam@element34.ca"
        lpo.password = "password"
        lpo.submit()

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationerrors)


if __name__ == "__main__":
    unittest.main()