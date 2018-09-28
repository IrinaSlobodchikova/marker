import re

#import datetime
#from random import randrange




class testHelperSM:

    def __init__(self, app):
        self.app = app


    def find_region(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='mCSB_2_container']/ul/li[2]/label")
        wd.find_element_by_xpath("//form[@id='frmSearch']//button[.='Поиск']")

    def find_region2(self):
        wd = self.app.wd
        self.app.wait_smBlock(120)
        wd.find_element_by_xpath("//div[@id='aggregatesPlaceholder']/table/tbody/tr/td[2]/div/div/div[1]/span[2]").click()
        wd.find_element_by_xpath("//div[@id='mCSB_6_container']/div/ul/li[20]/label").click()
        wd.find_element_by_id("aggSearchText").click()
        wd.find_element_by_id("aggSearchText").clear()
        wd.find_element_by_id("aggSearchText").send_keys("ростов")
        wd.find_element_by_id("aggSearch").click()
        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[6]/label").click()
        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[6]/span[3]").click()
        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[6]/label").click()
        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[7]/label").click()
        wd.find_element_by_xpath("//div[@id='mainAggDlgContent']//button[.='Применить фильтр']").click()
        self.app.wait_smBlock(20)
        wd.find_element_by_xpath("//form[@id='frmSearch']//button[.='Поиск']").click()


    def is_smresult_not_0(self):
        try:
            text = self.get_total_results()
            if text != '0':
             return True
        except:
            return False

    def check_results(self):
        self.app.wait_smBlock(120)
        if self.is_smresult_not_0():
            result = self.get_total_results()
            return result
        else:
            return '0'


    def get_total_results(self):
        wd = self.app.wd
        results = wd.find_element_by_xpath("//div[@class='panel_header']/h2").get_attribute("textContent")
        #clear_result = wd.find_element_by_xpath("//div[@class='panel_header']/h2").get_attribute("textContent")[13:len(results)]
        clear_result = results[13:len(results)]
        return self.clear_result(clear_result)
        #убрать пробелы перевести в инт

    def create_contact_report_all_in_dif_row_tel_mail(self):
        wd = self.app.wd
        wd.maximize_window()
        self.app.wait_smBlock(60)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Контакты']").click()
        self.app.wait_sm_artefact_Block(10)
        wd.find_element_by_xpath("//label[@for='cb-3']").click()
        if not wd.find_element_by_id("cb-3").is_selected():
            wd.find_element_by_id("cb-3").click()
        wd.find_element_by_xpath("//div[@id='divReportContactsSettings']//button[.='Сформировать']").click()

    def create_contact_report_allinone_tel_mail(self):
        wd = self.app.wd
        self.app.wait_smBlock(60)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Контакты']").click()
        self.app.wait_sm_artefact_Block(10)
        wd.find_element_by_xpath("//label[@for='cb-3']").click()
        if not wd.find_element_by_id("cb-3").is_selected():
            wd.find_element_by_id("cb-3").click()
        #Найти как кликнуть rb-1
        wd.find_element_by_xpath("//label[@for='rb-1']").click()
        wd.find_element_by_xpath("//div[@id='divReportContactsSettings']//button[.='Сформировать']").click()

    def create_contact_report_result(self):
        wd = self.app.wd
        self.app.wait_smBlock(20)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Результаты']").click()
        self.app.wait_sm_artefact_Block(10)
        wd.find_element_by_xpath("//div[@id='divReportSearchResultsSettings']//button[.='Сформировать']").click()

    def create_contact_report_statictic(self):
        wd = self.app.wd
        #добавить выбор чекбоксов
        self.app.wait_smBlock(20)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Статистика']").click()
        self.app.wait_sm_artefact_Block(10)
        wd.find_element_by_xpath("//div[@id='divReportStatisticsSettings']//button[.='Сформировать']").click()

    def create_contact_list_10000(self, cd2):
        wd = self.app.wd
        self.app.wait_smBlock(20)
        wd.find_element_by_xpath("//li[@id='UpdateList']//p[.='Добавить']").click()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").click()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").clear()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").send_keys("список компаний %s" % cd2)
        wd.find_element_by_xpath("//div[@id='addOrUpdateEntitiesListSearchDlg']//button[.='Сохранить']").click()

    def create_contact_list_50(self, cd2):
        wd = self.app.wd
        self.app.wait_smBlock(120)
        #выбор 50
        self.select_all_50()
        #создание первых списка по первым 50 компаниям
        wd.find_element_by_xpath("//li[@id='UpdateList']//p[.='Добавить']").click()
        wd.find_element_by_css_selector("td.w250").click()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").click()
        wd.find_element_by_xpath("//div[@id='autoCompleteRequestsContainer0']/a/span").click()
        wd.find_element_by_id("ui-id-2").click()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").click()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").clear()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").send_keys("список компаний %s" % cd2)
        wd.find_element_by_xpath("//div[@id='addOrUpdateEntitiesListSearchDlg']//button[.='Сохранить']").click()

    def select_all_50(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//label[@for='allItemsCb']").click()
        if not wd.find_element_by_id("allItemsCb").is_selected():
            wd.find_element_by_id("allItemsCb").click()

    def contact_from_contact_rep_is_present(self):
        wd = self.app.wd
        pass

    def clear_result(self, s):
        x = re.sub(" ", "", str(s))
        return x

    def clear_spase_result(self, s):
        x = re.sub(" ", "", str(s))
        return x

    report_cache = None

    def report_is_present_short(self, reestr_ex, report_type_ex, state_ex):
        wd = self.app.wd
        reestr = wd.find_element_by_xpath("//div[@id='reports']/div[3]/table/tbody/tr[1]/td[3]").text
        report_type = wd.find_element_by_xpath("//div[@id='reports']/div[3]/table/tbody/tr[1]/td[4]").text
        state = wd.find_element_by_xpath("//div[@id='reports']/div[3]/table/tbody/tr[1]/td[5]").text
        #if text == "Формируется":
        if state == "Создан" or state == state_ex:
            if report_type == report_type_ex:
                if reestr == reestr_ex:
                    return True
        return False
        #return reestr, report_type, state

    def get_old_contact_list(self):
        pass

    def contact_list_is_present(self):
        wd = self.app.wd
        #проверить время
        #проверить название
        #открыть (нужен метод принимающий название)
        #проверить заголовок

    def ensure_link_work(self):
        wd = self.app.wd
        header = wd.find_element_by_css_selector("h1.clip").text
        return header.rstrip()

    def ensure_link_type2_work(self):
        wd = self.app.wd
        header = wd.find_element_by_css_selector("h2").text
        return header[0:8]

    def delete_report(self):
        pass

    def delete_first_contact_list(self):
        wd = self.app.wd
        self.app.wait_smBlock(20)
        #придумать как найти чекбокс внизу чушь
        list = []
        #for row in wd.find_element_by_xpath("//input[@class='row-cb']"):
        #    cells = row.find_elements_by_tag_name("td")
        #    id = cells[0].find_element_by_tag_name("input").get_attribute("data-id")
        wd.find_element_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[1]/td[1]").click()
        if not wd.find_elements_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[1]/td[1]").is_selected():
            wd.find_element_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[1]/td[1]").click()

        wd.find_element_by_id("btnDel").click()
        wd.find_element_by_xpath("//div[@id='dlgYesNo']//button[.='Да']").click()


    def get_report_list(self):
        if self.report_cache is None:
            wd = self.app.wd
            self.report_cache = []
            for row in wd.find_elements_by_tag_name("tr"):
                cells = row.find_elements_by_tag_name("td")
                #id = cells[0].find_element_by_tag_name("input").get_attribute("data-id")
                #date = cells[1].text
                #reestr = cells[2].text
                #report_type = cells[3].text
                #state = cells[4].text
                #paramert = cells[5].text
        return self.report_cache[cells]


