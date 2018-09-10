# -*- coding: utf-8 -*-
import json
import logging
import requests
from odoo import models, fields, api
from odoo.exceptions import Warning


class website(models.Model):
    _inherit = 'website'

    recaptcha_site_key = fields.Char(string ='reCAPTCHA Site Key' ,default="6LfE2jMUAAAAAFiFKgnQwBfrZFLBgqpKV9iA9HyT")
    recaptcha_private_key = fields.Char(string='reCAPTCHA Private Key',default="6LfE2jMUAAAAAGsmAQpIkoGM3gOGwjNQEQ1QrWiC")

    """
    def is_captcha_valid(self, cr, uid, ids, response, context={}):
        for website in self.browse(cr, uid, ids, context=context):
            get_res = {'secret': website.recaptcha_private_key, 'response': response}
            try:
                response = requests.get('https://www.google.com/recaptcha/api/siteverify', params=get_res)
            except Exception, e:
                raise osv.except_osv(('Invalid Data!'), ("%s.") % (e))
            res_con = json.loads(response.content)
            if res_con.has_key('success') and res_con['success']:
                return True
        return False
    """


