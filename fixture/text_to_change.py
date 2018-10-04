from selenium.webdriver.support.expected_conditions import _find_element


class text_to_change():
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    def __call__(self, wd):
        actual_text = _find_element(wd, self.locator).text
        return actual_text != self.text

