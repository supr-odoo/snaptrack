from odoo import models, fields


class User(models.Model):
    _name = "snap.track"
    _description = "this is description"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone no")
    services = fields.Selection(
        string="Services",
        selection=[
            ("wedding", "Wedding Photography"),
            ("casual", "Casual Photography"),
            ("product", "Product Photography"),
        ],
    )
    photographers = fields.Many2one("photographer.details")
    prefered_date = fields.Date("Prefered Date")
    active = fields.Boolean(string="Active", default=True)
    last_seen = fields.Datetime(string="Last Seen", default=fields.Datetime.now)
    service_category_id = fields.One2many("service.category.details", "service_id")
