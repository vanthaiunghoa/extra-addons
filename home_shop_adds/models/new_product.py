# -*- coding: utf-8 -*-

from odoo import  fields, models


class NewProduct(models.Model):
    _inherit = 'product.template'

    new_product= fields.Boolean('Show it as new product at Homapage')
