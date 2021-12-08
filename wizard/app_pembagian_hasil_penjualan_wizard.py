from odoo import fields, models, _

class AppPembagianHasilPenjualanWizard(models.TransientModel):
    _name = "app.pembagian.hasil.penjualan.wizard"

    user_id = fields.Many2many('res.users', string='Sales Person')
    # project_id = fields.Many2one('account.analytic.account', string='Project')
    state = fields.Selection([('approved','Approved'), ('reward', 'Reward'), ('cancelled', 'Cancelled'), ('permission', 'Perizinan'), ('pinjaman_pemilik_lahan', 'Pinjaman Pemilik Lahan'), ('omset', 'Omset')], string='State', required=True, copy=False, tracking=True,default='-')
    uom_id = fields.Many2one('product.uom', string='uom')
    


    def print_pembagian_hasil_xlsx(self):
        template_report = ''
        if self.state == 'approved':
            template_report = 'app_custom.action_pembagian_hasil_penjualan_xlsx'
        elif self.state == 'reward':
            template_report = 'app_custom.action_pembagian_hasil_reward_promotion_xlsx'
        elif self.state == 'cancelled':
            template_report = 'app_custom.action_pembagian_hasil_pembatalan_xlsx'
        elif self.state == 'permission':
            template_report = 'app_custom.action_pembagian_hasil_perizinan_xlsx'
        elif self.state == 'pinjaman_pemilik_lahan':
            template_report = 'app_custom.action_pembagian_hasil_pinjaman_lahan_xlsx'
        elif self.state == 'omset':
            template_report = 'app_custom.action_pembagian_hasil_laporan_omset_xlsx'
        else:
            template_report = 'Unknown'

        return self.env.ref(template_report).report_action(self)