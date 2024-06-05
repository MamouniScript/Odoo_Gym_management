from odoo import fields, models, api

class Payment(models.Model):
    _name = 'mana_gym.payment'
    _description = 'Gym Payment'

    member_id = fields.Many2one('mana_gym.member', string='Member')
    membership_id = fields.Many2one('mana_gym.membership', string='Membership', compute='_compute_membership', store=True)
    amount = fields.Float(string='Amount')
    payment_date = fields.Date(string='Payment Date', default=fields.Date.context_today)
    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('crypto', 'Crypto')
    ], string='Payment Method', required=True)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue')
    ], string='Status', default='pending')

    @api.depends('member_id')
    def _compute_membership(self):
        for payment in self:
            if payment.member_id:
                payment.membership_id = payment.member_id.membership_type_id

    @api.onchange('membership_id')
    def _onchange_membership_id(self):
        if self.membership_id:
            self.amount = self.membership_id.price
