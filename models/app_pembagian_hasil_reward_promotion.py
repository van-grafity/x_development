from odoo import api, fields, models

class AppPembagianHasilRewardPromotion(models.Model):
    _name = "app.pembagian.hasil.reward.promotion"

    order_id = fields.Many2one('order.model', string='order')
    name_reward = fields.Char('Nama Hadiah')
    price = fields.Float('Harga')
    qty = fields.Float('Quantity', default=0.0)
    weight = fields.Float('Satuan', default=0.0)
    amount_total = fields.Float(string='Total', compute='_compute_total')
    delivery_date = fields.Datetime(string='Tanggal Penyerahan Hadiah', required=True, index=True)
    status = fields.Selection([('OK', 'ok'), ('Belum', 'belum')])
    note = fields.Char('Catatan', required=True)

    def print_test(self):
        for order in self:
            print('get_booking_id', order.order_id)

    @api.depends('qty', 'price')
    def _compute_total(self):
        for reward in self:
            reward.amount_total = reward.qty * reward.price
            reward.print_test()