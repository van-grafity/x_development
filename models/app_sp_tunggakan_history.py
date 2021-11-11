from odoo import api, fields, models
from odoo.tools.translate import _

class AppSpTunggakanHistory(models.Model):
    _name = "app.sp.tunggakan.history"

    order_id = fields.Many2one('order.model', string='order')
    document_type = fields.Selection([('sp1','SP 1'), ('sp2', 'SP 2'), ('sp3', 'SP 3'), ('cancel', 'Pembatalan')], string='Document Type')
    document_no = fields.Char('Document No.')
    document_date = fields.Date('Document Type')