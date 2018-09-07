from selenium import webdriver
from fixture.session import SessionHelper
from fixture.testhelpermarker import testHelperMarker
from fixture.testhelpersm import testHelperSM


class Application:

    def __init__(self, browser, config, environment, baseUrlMarker, baseUrlSM, username, password, dashboard,
                 newtenders, participation, watch, market_potential, planned_purchases, company_list, solutions,
                 reports, smParticipants, smParticipantsCustomers, smParticipantsSuppliers, smPurchases, smPrices,
                 smCertificates, smLicences, smKontrol, smreports, smMonitorinds, smcompany_list, smPurchases_list,
                 smNmckList, smUser_History, smlogout):
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
