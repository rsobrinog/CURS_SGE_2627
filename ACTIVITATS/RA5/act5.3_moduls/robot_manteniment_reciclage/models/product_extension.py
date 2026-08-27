from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    mantenimiento_ids = fields.One2many(
        'robot.mantenimiento',
        'product_id',
        string="Manteniment"
    )

    reciclaje_ids = fields.One2many(
        'robot.reciclaje',
        'product_id',
        string="Reciclatge"
    )
