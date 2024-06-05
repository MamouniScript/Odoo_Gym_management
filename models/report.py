from odoo import fields, models, api

class Report(models.Model):
    _name = 'mana.gym.report'
    _description = 'Mana Gym Report'
    _auto = False
    _rec_name = 'id'

    id = fields.Integer(string='ID')
    member_id = fields.Many2one('mana_gym.member', string='Member')
    membership_type_id = fields.Many2one('mana_gym.membership', string='Membership Type')
    joining_date = fields.Date(string='Joining Date')
    membership_status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Membership Status')
    total_revenues = fields.Float(string='Total Revenues', compute='_compute_total_revenues')
    active_members_count = fields.Integer(string='Active Members Count', compute='_compute_active_members_count')
    this_years_revenues = fields.Float(string="This Year's Revenues", compute='_compute_this_years_revenues')
    memberships_per_type = fields.Text(string='Memberships per Membership Type', compute='_compute_memberships_per_membership_type')
    trainer_per_active_member_ratio = fields.Float(string='Trainer per Active Member Ratio', compute='_compute_trainer_per_active_member_ratio')
    overdue_payments_count = fields.Integer(string='Overdue Payments Count', compute='_compute_overdue_payments_count')

    @api.depends('membership_status')
    def _compute_total_revenues(self):
        # Logic to calculate total revenues
        total_revenues = 0.0
        total_revenues = self.env['mana_gym.payment'].search([('status', '=', 'paid')]).mapped('amount')
        for record in self:
            record.total_revenues = total_revenues

    @api.model
    def _compute_active_members_count(self):
        active_members_count = self.env['mana_gym.member'].search_count([('membership_status', '=', 'active')])
        self.active_members_count = active_members_count

    @api.model
    def _compute_this_years_revenues(self):
        today = fields.Date.today()
        this_year = today.year
        memberships = self.env['mana_gym.payment'].search([('payment_date', '>=', f'{this_year}-01-01')])
        this_years_revenues = sum(membership.amount for membership in memberships)
        self.this_years_revenues = this_years_revenues

    @api.model
    def _compute_memberships_per_membership_type(self):
        memberships_per_type = {}
        membership_types = self.env['mana_gym.membership'].search([])
        for membership_type in membership_types:
            memberships_count = self.env['mana_gym.member'].search_count([('membership_type_id', '=', membership_type.id)])
            memberships_per_type[membership_type.name] = memberships_count
        self.memberships_per_type = memberships_per_type

    @api.model
    def _compute_trainer_per_active_member_ratio(self):
        active_members_count = self.env['mana_gym.member'].search_count([('membership_status', '=', 'active')])
        trainers_count = self.env['mana_gym.trainer'].search_count([])
        if trainers_count:
            ratio = active_members_count / trainers_count
        else:
            ratio = 0
        self.trainer_per_active_member_ratio = ratio

    @api.model
    def _compute_overdue_payments_count(self):
        overdue_payments_count = self.env['mana_gym.payment'].search_count([('status', '=', 'overdue')])
        self.overdue_payments_count = overdue_payments_count

    '''
    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'mana_gym_report')
        self._cr.execute("""
            CREATE OR REPLACE VIEW mana_gym_report AS (
                SELECT
                    row_number() OVER () AS id,
                    m.id AS member_id,
                    m.membership_type_id,
                    m.joining_date,
                    m.membership_status
                FROM
                    mana_gym_member m
            )
        """)
    '''