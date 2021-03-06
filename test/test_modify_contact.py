# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ёжик", middlename="Ежов", lastname="Грибанов", nickname="Мачо",
                                   home_phone="zadarma.com", address="Лес", mobile="нет розетки",
                                   work_phone="в лесу телефона нет", fax="пришлите с Печкиным", byear="1988"))
    app.contact.modify_first_contact(Contact(firstname="Modify_name", middlename="Modify_Ежов", lastname="Modify_Грибанов", nickname="Modify_Мачо",
                               home_phone="Modify_zadarma.com", address="Modify_Лес", mobile="Modify_нет розетки",
                               work_phone ="Modify_в лесу телефона нет", fax="Modify_пришлите с Печкиным", byear="1999"))