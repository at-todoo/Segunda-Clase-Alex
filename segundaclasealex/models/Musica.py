# -*- coding: utf-8 -*-

from odoo import models, fields, api


class segundaclasealex(models.Model):
     _name = 'Musica.rockmetal'
     _description = 'esta clase almacena generos musicales'

     Nombre = fields.Char()
     Genero = fields.Integer()
     Album = fields.Float(compute="_value_pc", store=True)
     Canciones = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
