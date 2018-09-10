# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MegaMenu(models.Model):
    _inherit = "website.menu"

    mega_menu = fields.Boolean('Mega Menu')
