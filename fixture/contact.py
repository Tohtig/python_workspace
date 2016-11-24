class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("address", contact.address)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("byear", contact.byear)
        # wd.find_element_by_xpath("//input[@name='submit']").click()
        wd.find_element_by_name("submit").click()
        self.app.open_home_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title = 'Edit']").click()
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("address", contact.address)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("byear", contact.byear)
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.app.open_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        # init contact delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))