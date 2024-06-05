# -*- coding: utf-8 -*-
# from odoo import http


# class ManaGym(http.Controller):
#     @http.route('/mana_gym/mana_gym', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mana_gym/mana_gym/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mana_gym.listing', {
#             'root': '/mana_gym/mana_gym',
#             'objects': http.request.env['mana_gym.mana_gym'].search([]),
#         })

#     @http.route('/mana_gym/mana_gym/objects/<model("mana_gym.mana_gym"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mana_gym.object', {
#             'object': obj
#         })
