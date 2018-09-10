# -*- coding: utf-8 -*-

from odoo import fields, models


class AddFieldsEvent(models.Model):
    _inherit = "event.event"

    short_description = fields.Char('Short Description')
    website = fields.Char('Website')
    info = fields.Char('Info')
    facebook = fields.Char('Facebook')
    twitter = fields.Char('Twitter')
    googleplus = fields.Char('Google Plus')
    image = fields.Binary('Image')



