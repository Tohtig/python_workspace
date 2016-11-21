# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ёжик", middlename="Ежов", lastname="Грибанов", nickname="Мачо",
                                   home_phone="zadarma.com", address="Лес", mobile="нет розетки",
                                   work_phone="в лесу телефона нет", fax="пришлите с Печкиным", byear="1988"))
    app.contact.delete_first_contact()
