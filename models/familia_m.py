# -*- coding: utf-8 -*-
from odoo import api, fields, models

class FamiliaM(models.Model):
    _inherit = 'familia.m'
    lead_user = fields.Boolean(string="Lead User",
                               compute="_compute_lead_user")
    not_lead_user = fields.Boolean(string="Not Lead User",
                                   compute="_compute_not_lead_user",
                                   store=True)
    my_db = fields.char(default=lambda self: self.env.cr.dbname, string="Data Base")

    @api.depends("main_user")
    def _compute_lead_user(self):
        for record in self:
            record.lead_user = record.main_user

    @api.depends("main_user")
    def _compute_not_lead_user(self):
        for record in self:
            record.not_lead_user = not record.main_user
