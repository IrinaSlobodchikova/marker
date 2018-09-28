from selenium import webdriver
from fixture.session import SessionHelper
from fixture.testhelpermarker import testHelperMarker
from fixture.testhelpersm import testHelperSM
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime


class Application:

    def __init__(self, browser, config, environment, baseUrlMarker, baseUrlSM, username, password, dashboard,
                 newtenders, participation, watch, market_potential, planned_purchases, company_list, solutions,
                 reports, smParticipants, smParticipantsCustomers, smParticipantsSuppliers, smPurchases, smPrices,
                 smCertificates, smLicences, smKontrol, smreports, smMonitorinds, smcompany_list, smPurchases_list,
                 smNmckList, smUser_History, smlogout):
        if browser == "firefox":
            self.wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.testhelper = testHelperMarker(self)
        self.testhelpersm = testHelperSM(self)
        self.config = config
        self.environment = environment
        self.baseUrlMarker = baseUrlMarker
        self.baseUrlSM = baseUrlSM
        self.username = username
        self.password = password
        self.dashboard = dashboard
        self.newtenders = newtenders
        self.participation = participation
        self.watch = watch
        self.market_potential = market_potential
        self.planned_purchases = planned_purchases
        self.company_list = company_list
        self.solutions = solutions
        self.reports = reports
        self.smParticipants = smParticipants
        self.smParticipantsCustomers = smParticipantsCustomers
        self.smParticipantsSuppliers = smParticipantsSuppliers
        self.smPurchases = smPurchases
        self.smPrices = smPrices
        self.smCertificates = smCertificates
        self.smLicences = smLicences
        self.smKontrol = smKontrol
        self.smreports = smreports
        self.smMonitorinds = smMonitorinds
        self.smcompany_list = smcompany_list
        self.smPurchases_list = smPurchases_list
        self.smNmckList = smNmckList
        self.smUser_History = smUser_History
        self.smlogout = smlogout
        self.wd.implicitly_wait(10)

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
        #self.wait_smBlock(5)


    #def return_to_home_page(self):
    #    wd = self.wd
    #    if  not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
    #        wd.find_element_by_link_text("home").click()

    def wait_smBlock(self, timeout):
        wd = self.wd
        if self.session.is_sm_blocked():
            # text = self.app.wd.find_element_by_id("smBlock").value_of_css_property("display")
            wait = WebDriverWait(wd, timeout)  # seconds
            wait.until(EC.invisibility_of_element((By.ID, "smBlock")))

    def wait_sm_artefact_Block(self, timeout):
        wd = self.wd
        if self.session.is_sm_artef_blocked():
            # text = self.app.wd.find_element_by_id("smBlock").value_of_css_property("display")
            wait = WebDriverWait(wd, timeout)  # seconds
            wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.dlg-content_loader.dlg-content_loader--center")))

    def status_is_changed(self, state_ex, timeout):
        wd = self.wd
        state = wd.find_element_by_xpath("//div[@id='reports']/div[3]/table/tbody/tr[1]/td[5]").text
        if state == state_ex:
            wait = WebDriverWait(wd, timeout)  # seconds
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@id='reports']/div[3]/table/tbody/tr[1]/td[5]"), "Создан"))
        else:
            return state

    def banner_link_button(self, timeout, i):
        wd = self.wd
        wait = WebDriverWait(wd, timeout)  # seconds
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='toast-message']//a[.='%s']" % i)))
        wd.find_element_by_xpath("//div[@class='toast-message']//a[.='%s']" % i) .click()
        #try:
        #    text = self.app.wd.find_element_by_xpath(
        #        "//div[@class='toast-message']//a[.='Открыть отчеты']").value_of_css_property("display")
        #    if text == 'block':
        #        return True
        #except:
        #    return False

    def current_date_time(self):
        i = datetime.datetime.now()
        current_date = ("%s" % i.day + "." + "%s" % i.month + "." + "%s" % i.year)
        current_time = ("%s" % i.hour + ":" + "%s" % i.minute)

        return i

    def destroy(self):
        self.wd.quit()



