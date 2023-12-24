# -*- coding: utf-8 -*-
from odoo import api, fields, models

class FamiliaM(models.Model):
    _inherit = 'familia.m'
    my_nickname = fields.Char(string="My Nickname")
    my_age = fields.Integer(string="My Age")
    main_user = fields.Boolean(string="Is main user?")