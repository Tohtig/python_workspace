# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="some_group", header="some_header", footer="some_footer"))
    app.group.modify_first_group(Group(name="modify_group", header="modify_header", footer="modify_footer"))

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="some_group", header="some_header", footer="some_footer"))
    app.group.modify_first_group(Group(name="modify_group"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="some_group", header="some_header", footer="some_footer"))
    app.group.modify_first_group(Group(header="modify_header"))