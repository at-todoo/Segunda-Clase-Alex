# -*- coding: utf-8 -*-
# from odoo import http


# class Segundaclasealex(http.Controller):
#     @http.route('/segundaclasealex/segundaclasealex/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/segundaclasealex/segundaclasealex/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('segundaclasealex.listing', {
#             'root': '/segundaclasealex/segundaclasealex',
#             'objects': http.request.env['segundaclasealex.segundaclasealex'].search([]),
#         })

#     @http.route('/segundaclasealex/segundaclasealex/objects/<model("segundaclasealex.segundaclasealex"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('segundaclasealex.object', {
#             'object': obj
#         })
