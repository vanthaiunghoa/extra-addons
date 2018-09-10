import ast

from odoo import models
from odoo.addons.base.ir.ir_qweb.assetsbundle import AssetsBundle


class QWeb(models.AbstractModel):
    """ QWeb object for rendering stuff in the website context """

    _inherit = 'ir.qweb'

    def _get_asset(self, xmlid, options, css=True, js=True, debug=False, async=False, values=None):
        debug = True
        items = super(QWeb, self)._get_asset(xmlid, options, css, js, debug, async, values)
        return items

    def _compile_directive_call_assets(self, el, options):
        """ This special 't-call' tag can be used in order to aggregate/minify javascript and css assets"""

        return super(QWeb, self)._compile_directive_call_assets(el, options)