# -*- coding: utf-8 -*-

from odoo import models, fields, api


class agendaprueba(models.Model):
    _name = 'agendaprueba.agendaprueba'
    _description = 'agendaprueba.agendaprueba'

    nombre = fields.Char()
    telefono = fields.Char()
