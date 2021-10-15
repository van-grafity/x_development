# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _

class Car(models.Model):
    _name = "xdev.rental"
    
    name = fields.Char('Brand')
    customer_id = fields.Many2one('customer.model', string='Customer')
    brand = fields.Char('Brand')
    type = fields.Char('Type')
    cost = fields.Char('Cost')
    images= fields.Binary('Link Image')
    payment_status = fields.Boolean('Payment status', default=False)

    def action_update_status_payment(self):
        for model in self:
            model.write({'payment_status' : True})
        return True
        # return {
        #     'name':_("Products to Process"),
        #     'view_mode': 'tree',
        #     'view_id': False,
        #     'view_type': 'tree,form',
        #     'res_model': 'xdev.rental',
        #     'res_id': partial_id,
        #     'type': 'ir.actions.act_window',
        #     # 'nodestroy': True,
        #     'target': 'new',
        #     # 'domain': '[]',
        #     # 'context': context
        # }
        if self.payment_status == False:
            self.payment_status = True
