# -*- coding: utf-8 -*-



from odoo import fields, models


class add_blog(models.Model):
    _inherit = "blog.post"

    description = fields.Text('Description')
