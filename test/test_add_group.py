# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="some_group", header="some_header", footer="some_footer"))
    # app.session.logout() # для проверки на падение/восстановление скрипта при ошибке в тесте и потери сессии

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))