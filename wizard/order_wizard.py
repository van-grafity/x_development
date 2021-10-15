from odoo import fields, models, _

class OrderWizard(models.TransientModel):
    _name = "xdev.order.wizard"

    name=fields.Char('Name')

    # order_id = fields.Many2one('sale.order', string='Sale Order')
    # partner_id = fields.Many2one('res.partner', string='Customer', related='order_id.partner_id')
 
    # def approve_blacklisted_customer_order(self):
    #     # panggil method action_confirm pada sale order saat ini
    #     # sertakan context agar bisa mencegah infinite loop
    #     self.order_id.with_context({'approve_blacklisted_customer_order': 1}).action_confirm()
