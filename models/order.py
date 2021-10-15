# from odoo import fields, models, _
from odoo.tools.populate import compute
from odoo import api, fields, models, SUPERUSER_ID, _

class Order (models.Model):
    _name = "order.model"

    # transaction_id = fields.Char('Transaction Id')
    transaction_id = fields.Integer(string='Transaction id', compute='_get_increment')
    name = fields.Many2one('customer.model', 'name')
    car_id = fields.Char('Car Id')
    line_ids = fields.One2many('order.model.line', 'order_id', 'Line')
    start_rental_date = fields.Datetime("Start Rental Date")
    end_rental_date = fields.Datetime("End Rental Date")
    expected_date = fields.Datetime("Expected Date")
    total_price = fields.Char("Total", compute='_get_amount_total')
    payment_status = fields.Boolean('Status', default=False)

    # atribut compute call function
    def _get_increment(self):
        self.transaction_id = 1 + 100

    @api.depends('line_ids.subtotal')
    def _get_amount_total(self):
        for order in self:
            amount_total = 0
            for line in order.line_ids:
                amount_total += line.subtotal
            order.write({'total_price': amount_total})

    def show_order_wizard(self):
        context = {
            'default_name' : self.car_id
        }

        action = {
            'name': _('Detail Order'),
            'res_model': 'xdev.order.wizard',
            'view_mode': 'form',
            'type': 'ir.actions.act_window',
            'target':'new',
            'context': context,
        }

        return action

class OrderLine (models.Model):
    _name = "order.model.line"

    car_name = fields.Many2one('xdev.rental', string='Car Name')
    amount = fields.Float("Price")
    total_days = fields.Float("Total Days Rental")
    subtotal = fields.Float("Subtotal", compute='_compute_total', readonly=True)
    code = fields.Char('Code', size=32, required=True, readonly=True,
                       default=lambda self: _('New'), track_visibility='onchange')

    # by field car_name to get cost
    @api.onchange('car_name')
    def _onchange_commitment_date(self):
        for order in self:
            order.amount = order.car_name.cost

    order_id = fields.Many2one('order.model', string='Order')

    @api.depends('total_days', 'amount')
    def _compute_total(self):
        for order in self:
            order.subtotal = order.total_days * order.amount
