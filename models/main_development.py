from odoo import fields, models, _

class MainDevelopment(models.Model):
    _name = "main.development"

    main_id = fields.Many2one('order.model', string='order')
    name_reward = fields.Char('Nama Hadiah')
    price = fields.Float('Harga')
    qty = fields.Float('Quantity', default=0.0)
    weight = fields.Float('Satuan', default=0.0)
    amount_total = fields.Float(string='Total', compute='_compute_total')
    delivery_date = fields.Datetime(string='Tanggal Penyerahan Hadiah', required=True, index=True)
    status = fields.Selection([('OK', 'ok'), ('Belum', 'belum')])
    note = fields.Char('Catatan', required=True)
    