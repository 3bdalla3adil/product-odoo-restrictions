from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class AccountMove(models.Model):

    _inherit = 'account.move'

    product_added = fields.Boolean(default=False)

    @api.constrains('invoice_line_ids')
    @api.onchange('invoice_line_ids')
    def _onchange_check_products(self):
        
        if len(self.invoice_line_ids) > 1:
            raise ValidationError('Only one product can be added order please remove.')
           