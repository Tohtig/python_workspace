# -*- coding: utf-8 -*-
from model.group import Group


def test_del_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="modify_group", header="modify_header", footer="modify_footer"))
    app.session.logout()