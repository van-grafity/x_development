from odoo import api, fields, models
from odoo import fields, models, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError

import time
from dateutil.parser import parse
import math

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

        historyObj_doc_type = self.env['app.sp.tunggakan.history']
        domain_type = [('document_type' ,'=' , search_keyword), ('order_id' ,'=' , self.order_id.id)]

        history_search_all = historyObj_doc_type.search(domain_type, order="create_uid desc")
        history_search_limit_doc_type = historyObj_doc_type.search(domain_type, order="create_uid desc", limit=1)
        print('xId 1 ', self.order_id.id)
        print('xId 2 ', history_search_limit_doc_type.order_id.id)
        self.histories_ids = history_search_all
        self.document_last_date = history_search_limit_doc_type.document_date

    def action_continue(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids')

        sphistoryObj = self.env['app.sp.tunggakan.history']
        bookingObj = self.env['order.model']        
        historyObj = self.env['app.sp.tunggakan.history']
        booking_search = bookingObj.search([('id', '=', active_ids)])

        last_sp = 0
        if self.document_type == 'sp1':
            last_sp = 1
        elif self.document_type == 'sp2':
            last_sp = 2
        elif self.document_type == 'sp3':
            last_sp = 3
        else:
            print('none')

        if self.document_type == 'cancel':
            self.document_no = str(self.env['ir.sequence'].next_by_code('app.btl')) + ' / APP-BTL / '+ ' /ABC '
        else:
            self.document_no = str(self.env['ir.sequence'].next_by_code('app.sp')) + ' / APP-SP / '+ ' /DEF '
        
        if self.document_type in ['sp2', 'sp3']:
            document = ''
            if self.document_type == 'sp2':
                document = 'sp1'

            domain = [('order_id', '=', active_ids), ('document_type', '=', document)]
            
            history_search_limit = historyObj.search(domain, order="create_uid desc", limit=1)

            if not history_search_limit:
                raise UserError(_('Maaf, Belum sampai ke Urutan SP sekarang. Silahkan Print SP sebelumnya'))
            else:
                sphistoryObj.create({
                    'order_id': booking_search.id,
                    'document_type': self.document_type,
                    'document_no' : self.document_no,
                    'document_date' : self.document_date,
                    })

                booking_search.write({
                    # 'last_sp_printed': last_sp,
                    'last_sp_doc_no': self.document_no,
                    # 'last_sp_doc_date': self.document_date
                    })

        elif self.document_type == 'sp1':
            sphistoryObj.create({
                'order_id': booking_search.id,
                'document_type': self.document_type,
                'document_no' : self.document_no,
                'document_date' : self.document_date,
                })
        elif self.document_type == 'cancel':
            domain_from = [('order_id', '=', active_ids), ('document_type', '=', 'sp1')]
            domain_to = [('order_id', '=', active_ids), ('document_type', '=', 'sp3')]

            
            history_search_from = historyObj.search(domain_from, order="create_uid desc", limit=1)
            history_search_to = historyObj.search(domain_to, order="create_uid desc", limit=1)   

            if not history_search_from and not history_search_to:
                raise UserError(_('Maaf, Belum sampai ke Urutan SP sekarang. Silahkan Print SP sebelumnya'))
            else:
                sphistoryObj.create({
                    'order_id': booking_search.id,
                    'document_type': self.document_type,
                    'document_no' : self.document_no,
                    'document_date' : self.document_date,
                    })