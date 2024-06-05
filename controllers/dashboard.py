from odoo import http
from odoo.http import request

class ManaGymDashboard(http.Controller):

    @http.route('/mana_gym/dashboard', type='http', auth='user', website=True)
    def mana_gym_dashboard(self, **kw):
        members_count = request.env['mana_gym.member'].search_count([])
        active_memberships = request.env['mana_gym.member'].search_count([('membership_status', '=', 'active')])
        total_revenue = sum(request.env['mana_gym.payment'].search([]).mapped('amount'))

        values = {
            'members_count': members_count,
            'active_memberships': active_memberships,
            'total_revenue': total_revenue,
        }
        return request.render('mana_gym.mana_gym_dashboard_template', values)
