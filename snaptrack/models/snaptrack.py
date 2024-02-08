from odoo import models, fields


class User(models.Model):
    _name = "snap.track"
    _description = "this is description"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    services = fields.Selection(
        [("wedding", "Wedding"), ("casual", "Casual"), ("product", "product")]
    )
    services = fields.Selection([("ph1", "Ankit"), ("ph2", "Aman"), ("ph3", "Ayan")])
    prefered_date = fields.Date("Prefered Date")
