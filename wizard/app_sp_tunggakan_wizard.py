from odoo import api, fields, models
from odoo import fields, models, _

class AppSpTunggakanWizard(models.TransientModel):
    _name = "app.sp.tunggakan.wizard"

    order_id = fields.Many2one('order.model', string='Booking ID')
    document_type = fields.Selection([('sp1','SP 1'), ('sp2', 'SP 2'), ('sp3', 'SP 3'), ('cancel', 'Pembatalan')], string='Document Type')
    document_date = fields.Date(string='Document Date', default=lambda self: fields.Date.today())
    document_no = fields.Char('Document No.')
    document_last_date = fields.Date("Before SP")
    histories_ids = fields.One2many('app.sp.tunggakan.history', 'order_id', string='History')

    @api.onchange('document_type')
    def _get_histories(self):
        search_keyword = ''
        
        if self.document_type == 'sp2':
            search_keyword = 'sp1'
        elif self.document_type == 'sp3':
            search_keyword = 'sp2'
        else:
            search_keyword = 'sp3'

        historyObj = self.env['app.sp.tunggakan.history']
        domain_type = [('document_type' ,'=' , search_keyword), ('order_id' ,'=' , self.order_id.id)]
        
        history_search_limit = historyObj.search(domain_type, order="create_uid desc", limit=1)
        history_search_all = historyObj.search(domain_type, order="create_uid desc")
        
        self.histories_ids = history_search_all
        self.document_last_date = history_search_limit.document_date

    def action_continue(self):
       print('xaction_continue')
