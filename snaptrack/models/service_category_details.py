from odoo import fields, models


class ServiceCategoryDetails(models.Model):
    _name = "service.category.details"

    name = fields.Char(string="Name")
    price = fields.Float(string="Price")

    service_id = fields.Many2one("snap.track")
