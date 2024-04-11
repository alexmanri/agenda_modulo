from odoo import api, fields, models
class InformacionContacto(models.Model):
    _name = 'informacion.contacto'
    nombre = fields.Char('nombre', required=True)
    apellidos = fields.Char('apellidos', required=False)
    telefono = fields.Char('telefono', required=True)
    email = fields.Char('email', required=True)