from odoo import api, fields, models
class Agenda(models.Model):
    _name = 'agenda'
    nombre = fields.Char('nombre', required=True)
    apellidos = fields.Char('apellidos', required=False)
    telefono = fields.Char('telefono', required=True)
    email = fields.Char('email', required=True)