import re
#import datetime
from random import randrange
import time


class testHelperSM:

    def __init__(self, app):
        self.app = app


#    def find_region(self):
#        wd = self.app.wd
#        wd.find_element_by_xpath("//div[@id='mCSB_2_container']/ul/li[2]/label")
#        wd.find_element_by_xpath("//form[@id='frmSearch']//button[.='Поиск']")

#    def find_region2(self, reg_name):
#        wd = self.app.wd
#        self.app.wait_smBlock(600)
#        wd.find_element_by_xpath("//div[@id='aggregatesPlaceholder']/table/tbody/tr/td[2]/div/div/div[1]/span[2]").click()
#        wd.find_element_by_xpath("//div[@id='mCSB_6_container']/div/ul/li[20]/label").click()
#        wd.find_element_by_id("aggSearchText").click()
#        wd.find_element_by_id("aggSearchText").clear()
#        wd.find_element_by_id("aggSearchText").send_keys("%s" % reg_name)
#        wd.find_element_by_id("aggSearch").click()
#        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[6]/label").click()
#        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[6]/span[3]").click()
#        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[6]/label").click()
#        wd.find_element_by_xpath("//div[@id='mCSB_7_container']/div/ul/li[7]/label").click()
#        wd.find_element_by_xpath("//div[@id='mainAggDlgContent']//button[.='Применить фильтр']").click()
#        self.app.wait_smBlock(600)
#        self.press_search_button()


#    def find_region3(self):
#        wd = self.app.wd
#        self.app.wait_smBlock(600)
#        i = randrange(24)
#        wd.find_element_by_xpath("//div[@id='aggregatesPlaceholder']/table/tbody/tr[2]/td[1]/div/div/div[1]/span[2]").click()
#        self.app.wait_sm_artefact_Block(10)
#        if i > 0:
            #element = wd.find_element_by_xpath("//div[@id='mCSB_11_container']/div/ul/li[%s]/label" % i)
            #ActionChains(wd).move_to_element(element).perform()
#            wd.find_element_by_xpath("//div[@id='mCSB_11_container']/div/ul/li[%s]/label" % i).click()
#        else:
#            i = 2
#            wd.find_element_by_xpath("//div[@id='mCSB_11_container']/div/ul/li[%s]/label" % i).click()
#        wd.find_element_by_xpath("//div[@id='mainAggDlgContent']//button[.='Применить фильтр']").click()
#        self.app.wait_smBlock(20)
#        self.press_search_button()

#    def find_in_container_number(self, range_container_numbers, container_number):
#        wd = self.app.wd
#        self.app.wait_smBlock(600)
#        spicok = []
#        i = randrange(1, 4, 1)
#        if container_number == 0:
#            ct = randrange(1, range_container_numbers, 1)
#        else:
#            ct = container_number
#        if not self.is_sm_advSearch_is_displayed():
#            if len(wd.find_elements_by_xpath("//div[@class='block-label']//a[.='Показать/скрыть']")) < 2:
#                wd.find_element_by_xpath("//div[@class='block-label']//a[.='Показать/скрыть']").click()
#            else:
#                wd.find_element_by_xpath("//div[@id='advSearch']/div[2]/a").click()
#        if i > 0 and ct > 0:
#            if ct == 1:
#                if i < 3:
#                    wd.find_element_by_xpath("//div[@id='mCSB_1_container']/ul/li[%s]/label" % str(i)).click()
#                if i == 3:
#                    i = 2
#                    wd.find_element_by_xpath("//div[@id='mCSB_1_container']/ul/li[%s]/label" % str(i)).click()
#            elif ct == 2:
#                try:
#                    wd.find_element_by_xpath("//div[@id='mCSB_2_container']/ul/li[%s]/label" % str(i)).click()
#                except:
#                    wd.find_element_by_xpath("//div[@id='mCSB_1_container']/ul/li[%s]/label" % str(i)).click()
#            elif ct == 3:
#                wd.find_element_by_xpath("//div[@id='mCSB_3_container']/ul/li[%s]/label" % str(i)).click()
#            elif ct == 4:
#                wd.find_element_by_xpath("//div[@id='mCSB_4_container']/ul/li[%s]/label" % str(i)).click()
#            elif ct == 5:
#                wd.find_element_by_xpath("//div[@id='mCSB_5_container']/ul/li[%s]/label" % str(i)).click()
#            elif ct == 6:
#                wd.find_element_by_xpath("//div[@id='mCSB_6_container']/ul/li[%s]/label" % str(i)).click()
#            elif ct == 7:
#                    wd.find_element_by_xpath("//div[@id='mCSB_7_container']/ul/li[%s]/label" % str(i)).click()
#            elif ct == 8:
#                    wd.find_element_by_xpath("//div[@id='mCSB_8_container']/ul/li[%s]/label" % str(i)).click()
#            elif ct == 9:
#                    wd.find_element_by_xpath("//div[@id='mCSB_9_container']/ul/li[%s]/label" % str(i)).click()
#            elif ct == 10:
#                    wd.find_element_by_xpath("//div[@id='mCSB_10_container']/ul/li[%s]/label" % str(i)).click()
#        else:
#            i = 2
#            wd.find_element_by_xpath("//div[@id='mCSB_2_container']/ul/li[%s]/label" % str(i)).click()
#        self.press_search_button()
#        return i, ct

    def press_search_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@id='frmSearch']//button[.='Поиск']").click()

#    def is_sm_advSearch_is_displayed(self):
#        try:
#            text = self.app.wd.find_element_by_id("advSearchContent").value_of_css_property("display")
#            if text == 'block':
#             return True
#        except:
#            return False

#    def find_zakazchik_for_purchases_list(self):
#        wd = self.app.wd
#        self.app.wait_smBlock(600)
#        i = randrange(24)
#        wd.find_element_by_xpath(
#            "//div[@id='aggregatesPlaceholder']/table/tbody/tr[1]/td[3]/div[2]/div/div[1]/span[2]").click()
#        self.app.wait_sm_artefact_Block(10)
#        wd.find_element_by_id("aggSearchText").click()
#        wd.find_element_by_id("aggSearchText").clear()
#        wd.find_element_by_id("aggSearchText").send_keys("администрация")
#        wd.find_element_by_id("aggSearch").click()
#        self.app.wait_sm_artefact_Block(10)
#        if i > 0:
#            wd.find_element_by_xpath("//div[@id='mCSB_12_container']/div/ul/li[%s]/label" % i).click()
#        else:
#            i = 2
#            wd.find_element_by_xpath("//div[@id='mCSB_12_container']/div/ul/li[%s]/label" % i).click()
#        wd.find_element_by_xpath("//div[@id='mainAggDlgContent']//button[.='Применить фильтр']").click()
#        self.app.wait_smBlock(600)
#        self.press_search_button()


# ! not work
#    def search_in_opened_container(self):
#        wd = self.app.wd
#        self.app.wait_smBlock(600)
#        if not self.is_sm_advSearch_is_displayed():
#            if len(wd.find_elements_by_xpath("//div[@class='block-label']//a[.='Показать/скрыть']")) < 2:
#                wd.find_element_by_xpath("//div[@class='block-label']//a[.='Показать/скрыть']").click()
#            else:
#                wd.find_element_by_xpath("//div[@id='advSearch']/div[2]/a").click()
#        i = randrange(1, 24, 1)
#        c = len(wd.find_elements_by_css_selector("span.agg-widget_btn"))
#        ct = randrange(c)
#        wd.find_elements_by_css_selector("span.agg-widget_btn")[ct].click()
#        self.app.wait_sm_artefact_Block(10)
#        #найти как кликнуть на элементе

#        wd.find_element_by_xpath("//div[@id='mainAggDlgContent']//button[.='Применить фильтр']").click()
#        self.app.wait_smBlock(600)
#        self.press_search_button()




#    def get_artef_parametrs(self, ct):
#        wd = self.app.wd
#        self.app.wait_smBlock(600)
#        for row in wd.find_elements_by_xpath("//div[@id='mCSB_%s_container']/ul/li[1]" % ct):

#            cells = row.find_elements_by_tag_name("span")
#            results = cells[0].find_element_by_tag_name("em").text
#            try:
#                parametr = cells[3].text
#            except:
#                parametr = cells[2].text
#            return parametr


#    def get_artef_param(self, ct):
#        wd = self.app.wd
#        param = self.get_artef_parametrs(ct)
#        return param

#    def is_smresult_not_0(self):
#        try:
#            text = self.get_total_results()
#            if text != '0':
#             return True
#        except:
#            return False

#    def check_results(self):
#        self.app.wait_smBlock(900)
#        if self.is_smresult_not_0():
#            result = self.get_total_results()
#            return result
#        else:
#            return '0'


#    def get_total_results(self):
#        wd = self.app.wd
#        results = wd.find_element_by_xpath("//div[@class='panel_header']/h2").get_attribute("textContent")
#        #clear_result = wd.find_element_by_xpath("//div[@class='panel_header']/h2").get_attribute("textContent")[13:len(results)]
#        clear_result = results[13:len(results)]
#        return self.clear_result(clear_result)


    def create_contact_report_all_in_dif_row_tel_mail(self):
        wd = self.app.wd
        wd.maximize_window()
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Контакты']").click()
        self.app.wait_sm_artefact_Block(10)
        wd.find_element_by_xpath("//label[@for='cb-3']").click()
        if not wd.find_element_by_id("cb-3").is_selected():
            wd.find_element_by_id("cb-3").click()
        wd.find_element_by_xpath("//label[@for='rb-0']").click()
        if not wd.find_element_by_id("rb-0").is_selected():
            wd.find_element_by_id("rb-0").click()
        wd.find_element_by_xpath("//div[@id='divReportContactsSettings']//button[.='Сформировать']").click()

    def create_contact_report_all_in_dif_row_tel_mail_zakazchiki(self):
        wd = self.app.wd
        wd.maximize_window()
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Контакты']").click()
        self.app.wait_sm_artefact_Block(10)
        wd.find_element_by_xpath("//label[@for='cb-3']").click()
        if not wd.find_element_by_id("cb-3").is_selected():
            wd.find_element_by_id("cb-3").click()
        wd.find_element_by_xpath("//label[@for='cb-8']").click()
        if not wd.find_element_by_id("cb-8").is_selected():
            wd.find_element_by_id("cb-8").click()
        wd.find_element_by_xpath("//label[@for='cb-9']").click()
        if wd.find_element_by_id("cb-9").is_selected():
            wd.find_element_by_id("cb-9").click()
        wd.find_element_by_xpath("//label[@for='rb-0']").click()
        if not wd.find_element_by_id("rb-0").is_selected():
            wd.find_element_by_id("rb-0").click()
        wd.find_element_by_xpath("//div[@id='divReportContactsSettings']//button[.='Сформировать']").click()

    def create_contact_report_allinone_tel_mail(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Контакты']").click()
        self.app.wait_sm_artefact_Block(10)
        wd.find_element_by_xpath("//label[@for='cb-3']").click()
        if not wd.find_element_by_id("cb-3").is_selected():
            wd.find_element_by_id("cb-3").click()
        wd.find_element_by_xpath("//label[@for='rb-1']").click()
        if not wd.find_element_by_id("rb-1").is_selected():
            wd.find_element_by_id("rb-1").click()
        wd.find_element_by_xpath("//div[@id='divReportContactsSettings']//button[.='Сформировать']").click()

    def create_contact_report_allinone_tel_mail_zakazchiki(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Контакты']").click()
        self.app.wait_sm_artefact_Block(10)
        wd.find_element_by_xpath("//label[@for='cb-3']").click()
        if not wd.find_element_by_id("cb-3").is_selected():
            wd.find_element_by_id("cb-3").click()
        wd.find_element_by_xpath("//label[@for='cb-8']").click()
        if not wd.find_element_by_id("cb-8").is_selected():
            wd.find_element_by_id("cb-8").click()
        wd.find_element_by_xpath("//label[@for='cb-9']").click()
        if wd.find_element_by_id("cb-9").is_selected():
            wd.find_element_by_id("cb-9").click()
        wd.find_element_by_xpath("//label[@for='rb-1']").click()
        if not wd.find_element_by_id("rb-1").is_selected():
            wd.find_element_by_id("rb-1").click()
        wd.find_element_by_xpath("//div[@id='divReportContactsSettings']//button[.='Сформировать']").click()

    def create_contact_report_result(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Результаты']").click()
        self.app.wait_sm_artefact_Block(10)
        wd.find_element_by_xpath("//div[@id='divReportSearchResultsSettings']//button[.='Сформировать']").click()

    def create_contact_report_statictic(self):
        wd = self.app.wd
        #добавить выбор чекбоксов
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Статистика']").click()
        self.app.wait_sm_artefact_Block(10)
        wd.find_element_by_xpath("//div[@id='divReportStatisticsSettings']//button[.='Сформировать']").click()

    def create_contact_list_10000(self, cd2, text):
        wd = self.app.wd
        self.app.wait_smBlock(900)
        wd.find_element_by_xpath("//li[@id='UpdateList']//p[.='Добавить']").click()
        wd.find_element_by_xpath("//label[@for='sallResults']").click()
        if not wd.find_element_by_id("sallResults").is_selected():
            wd.find_element_by_id("sallResults").click()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").click()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").clear()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").send_keys(text % cd2)
        time.sleep(2)
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").click()
        wd.find_element_by_xpath("//div[@id='addOrUpdateEntitiesListSearchDlg']//button[.='Сохранить']").click()


    def create_purchases_company_list_50(self, cd2, text):
        wd = self.app.wd
        self.app.wait_smBlock(900)
        #выбор 50
        self.select_all_50()
        #создание первых списка по первым 50 компаниям
        wd.find_element_by_xpath("//li[@id='UpdateList']//p[.='Добавить']").click()
        wd.find_element_by_xpath("//label[@for='scheckedResults']").click()
        if not wd.find_element_by_id("scheckedResults").is_selected():
            wd.find_element_by_id("scheckedResults").click()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").click()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").clear()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").click()
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").send_keys(text % cd2)
        time.sleep(2)
        wd.find_element_by_xpath("//input[@class='ui-autocomplete-input']").click()
        wd.find_element_by_xpath("//div[@id='addOrUpdateEntitiesListSearchDlg']//button[.='Сохранить']").click()

    def select_all_50(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//label[@for='allItemsCb']").click()
        if not wd.find_element_by_id("allItemsCb").is_selected():
            wd.find_element_by_id("allItemsCb").click()

#    def clear_result(self, s):
#        x = re.sub(" ", "", str(s))
#        return x

#    def clear_spase_result(self, s):
#        x = re.sub(" ", "", str(s))
#        return x



    def report_is_present_short(self, reestr_ex, report_type_ex, state_ex):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        reestr = wd.find_element_by_xpath("//div[@id='reports']/div[3]/table/tbody/tr[1]/td[3]").text.rstrip()
        report_type = wd.find_element_by_xpath("//div[@id='reports']/div[3]/table/tbody/tr[1]/td[4]").text.rstrip()
        state = wd.find_element_by_xpath("//div[@id='reports']/div[3]/table/tbody/tr[1]/td[5]").text.rstrip()
        if state == "Создан" or state == state_ex:
            if report_type == report_type_ex:
                if reestr == reestr_ex:
                    return True
        return False


    def report_is_present_date(self, cd2):
        wd = self.app.wd
        date = wd.find_element_by_xpath("//div[@id='reports']/div[3]/table/tbody/tr[1]/td[2]").text.rstrip()
        exp_date = "Сегодня " + cd2
        cd2_hour = cd2[0:2]
        cd2_minute = cd2[3:5]
        exp_date2 = "Сегодня " + cd2_hour + ":" + str(int(cd2_minute) + 1)
        if date == exp_date or date == exp_date2:
            return True
        return False

    def monitoring_is_present(self, cd2, cd3, text, reestr_ex):
        wd = self.app.wd
        wd.refresh()
        self.app.wait_smBlock(600)
        date = wd.find_element_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[1]/td[2]").text.rstrip()
        exp_date = "Сегодня " + cd3
        cd2_hour = cd3[0:2]
        cd2_minute = cd3[3:5]
        exp_name = text[0:-3] + " " + cd2
        exp_date2 = "Сегодня " + cd2_hour + ":" + str(int(cd2_minute) + 1)
        exp_date3 = "Сегодня " + cd2_hour + ":" + "0" + str(int(cd2_minute) + 1)
        reestr = wd.find_element_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[1]/td[3]").text.rstrip()
        name = wd.find_element_by_xpath("//div[@class='panel_layer']//a[.='%s']" % exp_name).text.rstrip()
        #name = wd.find_element_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[1]/td[4]").text.rstrip()
        if date == exp_date or date == exp_date2 or date == exp_date3:
            if reestr == reestr_ex:
                if name == exp_name:
                    return True
        return False

    def click_on_monitoring_link(self, cd2, text):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        exp_name = text[0:-3] + " " + cd2
        wd.find_element_by_xpath("//div[@class='panel_layer']//a[.='%s']" % exp_name).click()


    def contact_or_purchases_list_is_present(self, cd2, text):
        wd = self.app.wd
        #проверить время
        self.app.wait_smBlock(600)
        cd_contact_list = wd.find_element_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[1]/td[2]").text.rstrip()
        current_name = wd.find_element_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[1]/td[3]").text.rstrip()
        created_name = text[0:-3] + " " + cd2
        cd_contact_list_date = cd_contact_list[0:2]
        cd2_date = cd2[0:2]
        cd_contact_list_month = cd_contact_list[3:5]
        cd2_month = cd2[3:5]
        cd_contact_list_year = cd_contact_list[6:10]
        cd2_year = cd2[6:10]
        if len(cd_contact_list) == 18:
            cd_contact_list_hour = cd_contact_list[11:12]
            cd_contact_list_minute = cd_contact_list[13:15]
        else:
            cd_contact_list_hour = cd_contact_list[11:13]
            cd_contact_list_minute = cd_contact_list[14:16]
        cd2_hour = cd2[11:13]
        cd2_minute = cd2[14:16]
        if cd_contact_list_date == cd2_date:
            if cd_contact_list_month == cd2_month:
                if cd_contact_list_year == cd2_year:
                    if cd_contact_list_hour == cd2_hour or cd_contact_list_hour == cd2_hour[1:2]:
                        if cd_contact_list_minute == cd2_minute or cd_contact_list_minute == str(int(cd2_minute) + 1):
                            if current_name.startswith(created_name):
                                return True
        else:
            return False

    def ensure_link_work(self):
        wd = self.app.wd
        header = wd.find_element_by_css_selector("h1.clip").text
        return header.rstrip()

    def ensure_link_type2_work(self):
        wd = self.app.wd
        header = wd.find_element_by_css_selector("h2").text
        return header[0:8]

    def open_first_contact_list(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[1]/td[3]/div/div[1]/a").click()

    def create_report_covladeltsy(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Совладельцы']").click()
        wd.find_element_by_xpath("//div[@id='divReportCoownersSettings']//button[.='Сформировать']").click()
        wd.find_element_by_css_selector("div.toast-title").click()

    def create_report_affelir(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Аффилированность']").click()
        wd.find_element_by_xpath("//div[@id='divReportAffilationSettings']//button[.='Сформировать']").click()

    def create_report_prices_zakazchik(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Цены']").click()
        wd.find_element_by_xpath("//label[@for='rb-0']").click()
        if not wd.find_element_by_id("rb-0").is_selected():
            wd.find_element_by_id("rb-0").click()
        #wd.find_element_by_xpath("//label[@for='cb-2']").click()
        #if not wd.find_element_by_id("cb-2").is_selected():
        #    wd.find_element_by_id("cb-2").click()
        #wd.find_element_by_xpath("//label[@for='cb-3']").click()
        #if not wd.find_element_by_id("cb-3").is_selected():
        #    wd.find_element_by_id("cb-3").click()
        #wd.find_element_by_xpath("//label[@for='cb-4']").click()
        #if not wd.find_element_by_id("cb-4").is_selected():
        #    wd.find_element_by_id("cb-4").click()
        wd.find_element_by_xpath("//div[@id='divReportPricesSettings']//button[.='Сформировать']").click()

    def create_report_prices_postavschik(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Цены']").click()
        wd.find_element_by_xpath("//label[@for='rb-1']").click()
        if not wd.find_element_by_id("rb-1").is_selected():
            wd.find_element_by_id("rb-1").click()
        #wd.find_element_by_xpath("//label[@for='cb-5']").click()
        #if not wd.find_element_by_xpath("//label[@for='cb-5']").is_selected():
        #    wd.find_element_by_xpath("//label[@for='cb-5']").click()
        #wd.find_element_by_xpath("//label[@for='cb-6']").click()
        #if not wd.find_element_by_xpath("//label[@for='cb-6']").is_selected():
        #    wd.find_element_by_xpath("//label[@for='cb-6']").click()
        wd.find_element_by_xpath("//div[@id='divReportPricesSettings']//button[.='Сформировать']").click()

    def create_report_rnpSuppliers(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Поставщик в РНП']").click()
        wd.find_element_by_xpath("//div[@id='divRnpSuppliersSettings']//button[.='Сформировать']").click()

    def create_report_RnpParticipantsSettings(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='Участник в РНП']").click()
        wd.find_element_by_xpath("//div[@id='divRnpParticipantsSettings']//button[.='Сформировать']").click()

    def create_report_FasComplaintsSettings(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        wd.find_element_by_xpath("//div[@class='panel_header']//p[.='ФАС']").click()
        wd.find_element_by_xpath("//div[@id='divFasComplaintsSettings']//button[.='Сформировать']").click()

    def save_requesr(self, cd2, text):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        try:
            wd.find_element_by_link_text("Сохранить запрос").click()
        except:
            try:
                wd.find_element_by_link_text("Сохранить запрос/Мониторинг").click()
            except:
                try:
                    wd.find_element_by_link_text("Сохранить запрос ").click()
                except:
                    wd.find_element_by_link_text("Сохранить запрос/Мониторинг ").click()
        wd.find_element_by_id("requestName").click()
        wd.find_element_by_id("requestName").clear()
        wd.find_element_by_id("requestName").send_keys(text % cd2)
        time.sleep(2)
        wd.find_element_by_id("requestName").click()
        wd.find_element_by_xpath("//div[@id='divSaveRequest']//button[.='Сохранить']").click()

    def refresh_page(self):
        wd = self.app.wd
        wd.refresh()
        self.app.wait_smBlock(600)



    def contact_from_contact_rep_is_present(self):
        wd = self.app.wd
        pass

    def get_old_contact_list(self):
        pass

    def delete_report(self):
        pass

    def delete_first_contact_list(self):
        wd = self.app.wd
        self.app.wait_smBlock(600)
        #придумать как найти чекбокс, внизу чушь
        list = []
        #for row in wd.find_element_by_xpath("//input[@class='row-cb']"):
        #    cells = row.find_elements_by_tag_name("td")
        #    id = cells[0].find_element_by_tag_name("input").get_attribute("data-id")
        wd.find_element_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[1]/td[1]").click()
        if not wd.find_elements_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[1]/td[1]").is_selected():
            wd.find_element_by_xpath("//div[@class='panel_layer']/div[2]/table/tbody/tr[1]/td[1]").click()

        wd.find_element_by_id("btnDel").click()
        wd.find_element_by_xpath("//div[@id='dlgYesNo']//button[.='Да']").click()


