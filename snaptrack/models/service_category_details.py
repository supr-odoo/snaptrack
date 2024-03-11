from odoo import fields, models


class ServiceCategory(models.Model):
    _name = "snaptrack.service.category"

    product_name = fields.Many2one("product.product", string="Product Category")
    price = fields.Float(string="Price")
