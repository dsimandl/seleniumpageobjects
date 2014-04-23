from pageobjects.seleniumwrapper import SeleniumWrapper

selenium_server_connection = SeleniumWrapper()

locators = {}
locators["login.username"] = "username"
locators["login.password"] = "password"
locators["login.submit"] = "login"

