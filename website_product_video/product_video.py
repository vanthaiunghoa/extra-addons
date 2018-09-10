# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductVideo(models.Model):
    _inherit = 'product.template'

    name_video = fields.Char('Name Video')
    description_video = fields.Text('Description')
    iframe_video = fields.Text('SRC iframe video')


