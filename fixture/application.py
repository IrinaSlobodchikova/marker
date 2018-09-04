from selenium import webdriver
from fixture.session import SessionHelper



class Application:

    def __init__(self, browser, config, environment, baseUrlMarker, baseUrlSM, username, password):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.config = config
        self.environment = environment
        self.baseUrlMarker = baseUrlMarker
        self.baseUrlSM = baseUrlSM
        self.username = username
        self.password = password
        self.wd.implicitly_wait(5)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False



    def open_marker_home_page(self):
        wd = self.wd
        wd.get(self.baseUrlMarker)


    def open_sm_home_page(self):
        wd = self.wd
        wd.get(self.baseUrlSM)

    #def return_to_home_page(self):
    #    wd = self.wd
    #    if  not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
    #        wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()
