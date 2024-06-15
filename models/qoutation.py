from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    # product_added = fields.Boolean(related="order_line.product_added",default=False)

    
    @api.constrains('order_line')
    @api.onchange('order_line')
    def _onchange_check_products(self):
        
        if len(self.order_line) > 1:

            raise ValidationError("Only one product per line is allowed")
    

# class SaleOrderLine(models.Model):
#     _inherit = 'sale.order.line'

#     product_added = fields.Boolean(string='Product', default=False)

#     @api.onchange('product_id')
#     @api.depends('product_id')
#     def check_unique_product(self):
#         for line in self:
