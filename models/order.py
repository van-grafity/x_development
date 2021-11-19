# from odoo import fields, models, _
from odoo.tools.populate import compute
from odoo import api, fields, models, SUPERUSER_ID, _

from dateutil.relativedelta import relativedelta
from time import gmtime, strftime
from datetime import datetime, timezone, timedelta
from datetime import date

class Order (models.Model):
    _name = "order.model"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    # transaction_id = fields.Char('Transaction Id')
    transaction_id = fields.Integer(string='Transaction id', compute='_get_increment')
    state = fields.Selection([('draft', 'Draft'), ('submit', 'Submit'), ('approved', 'Approved')])
    name = fields.Many2one('customer.model', 'name')
    car_id = fields.Char('Car Id')
    line_ids = fields.One2many('order.model.line', 'order_id', 'Line')
    start_rental_date = fields.Date("Start Rental Date", track_visibility='onchange')
    end_rental_date = fields.Datetime("End Rental Date", track_visibility='onchange')
    expected_date = fields.Date("Expected Date", track_visibility='onchange')
    total_price = fields.Char("Total", compute='_get_amount_total')
    payment_status = fields.Boolean('Status', default=False)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    reward_ids = fields.One2many('app.pembagian.hasil.reward.promotion', 'order_id', string='Reward')
    sp_history_ids = fields.One2many('app.sp.tunggakan.history', 'order_id', string='Rekening Bank')

    last_sp_printed = fields.Integer('Last printed SP')
    last_sp_doc_no = fields.Char('Last printed SP No.')
    last_sp_doc_date = fields.Date('Last printed SP Date.')
    last_cancel_printed_no = fields.Char('Last SP cancelled No.')

    received_date = fields.Date()
    experiment_date = fields.Date(string="Fill in by 1 weeks")
    is_one_weeks = fields.Boolean(compute="compute_schedule_experiment_date_by_weeks")
    late_one_weeks = fields.Char(style="color: red;")
    result_trial_date = fields.Text()
    is_one_month = fields.Boolean(compute="compute_trial_result_by_month")
    late_one_month = fields.Char(style="color: red;")
    result_date = fields.Date(string="Fill result date 1 month")

    def _compute_who_user_has_groups(self):
        print("xIs user ?")
        # if self.env.user.has_group('sales_team.group_sale_salesman'):
        #     print("The User belongs to an Salesman Group")
        # else:
        #     print("Whoops! User does not belong to this Group")

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

    def button_draft(self):
        print('xQm current state ->', self.state)
        self.write({'state': 'draft'}) 
        return {}

    def button_confirm(self):
        print('xQm current state ->', self.state)
        for models in self:
            if models.state == 'draft':
                self.action_submit()
            elif models.state == 'submit':
                self.action_approve()

    def action_submit(self):
        self.ensure_one()
        self.state = 'submit'
    
    def action_approve(self):
        self.ensure_one()
        self.state = 'approved'

    def show_tunggakan_wizard(self):
        context = {
            'default_name' : self.car_id
        }

        action = {
            'name': _('Detail Order'),
            'res_model': 'app.sp.tunggakan.wizard',
            'view_mode': 'form',
            'type': 'ir.actions.act_window',
            'target':'new',
            'context': context,
        }

        return action

    def action_crm_lead_view(self):
            self.ensure_one()
            action = {
                'name': _('CRM'),
                'type': 'ir.actions.act_window',
                'view_mode': 'tree',
                'res_model': 'order.model',
                'res_id': self.car_id,            
            }
            return action

    # FOR TEST is_one_month set to is_one_weeks on ui and base on values == date_days
    # if one week before customer received date
    def compute_schedule_experiment_date_by_weeks(self):
        for item in self:
            if(item.received_date):
                date_days= (item.received_date + relativedelta(days =+7)).strftime('%Y-%m-%d')
                todays = strftime("%Y-%m-%d", gmtime())
                print('xToday ', todays)

                if  "2021-11-18" >= date_days and item.experiment_date == False:
                    item.is_one_weeks = False
                    item.late_one_weeks = 'Cannot empty is schedule experiment date'
                else:
                    item.is_one_weeks = True
                    item.late_one_weeks = ''
            else:
                item.is_one_weeks = False
        print('xisEmpty by weeks ',item.is_one_weeks)
        self.env.cr.execute(
                """
                select start_rental_date from order_model
                """
            )
        product_query = self.env.cr.fetchall()
        if product_query:
            for x in product_query:
                x_id = x[0]
                print('xQueryOrderModel ', x_id)

    # if one month before customer received date
    def compute_trial_result_by_month(self):
        for item in self:
            if(item.received_date):
                date_month= (item.received_date + relativedelta(months=+1)).strftime('%Y-%m')
                todays = strftime("%Y-%m-%d", gmtime())

                if "2021-11-18" >= date_month and item.result_trial_date == False:
                    item.is_one_month = False
                    item.late_one_month = 'Cannot empty is trial results and analysis'
                else:
                    item.is_one_month = True
                    item.late_one_month = ''
            else:
                item.is_one_month = False
        print('xisEmpty by month ',item.is_one_month)

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
