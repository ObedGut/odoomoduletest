# -*- coding: utf-8 -*-
# from odoo import http


# class Agendaprueba(http.Controller):
#     @http.route('/agendaprueba/agendaprueba', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agendaprueba/agendaprueba/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('agendaprueba.listing', {
#             'root': '/agendaprueba/agendaprueba',
#             'objects': http.request.env['agendaprueba.agendaprueba'].search([]),
#         })

#     @http.route('/agendaprueba/agendaprueba/objects/<model("agendaprueba.agendaprueba"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agendaprueba.object', {
#             'object': obj
#         })
