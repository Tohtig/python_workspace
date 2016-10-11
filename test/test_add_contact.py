# -*- coding: utf-8 -*-
from model.contact import Contact


def test_test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Ёжик", middlename="Ежов", lastname="Грибанов", nickname="Мачо",
                               home_phone="zadarma.com", adress="Лес", mobile="нет розетки",
                               work_phone="в лесу телефона нет", fax="пришлите с Печкиным", byear="1988"))
    app.session.logout()
