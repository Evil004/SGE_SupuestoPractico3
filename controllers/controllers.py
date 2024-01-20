# -*- coding: utf-8 -*-
# from odoo import http


# class FctIes(http.Controller):
#     @http.route('/fct_ies/fct_ies', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fct_ies/fct_ies/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fct_ies.listing', {
#             'root': '/fct_ies/fct_ies',
#             'objects': http.request.env['fct_ies.fct_ies'].search([]),
#         })

#     @http.route('/fct_ies/fct_ies/objects/<model("fct_ies.fct_ies"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fct_ies.object', {
#             'object': obj
#         })
