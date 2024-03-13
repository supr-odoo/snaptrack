from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class BookingRequest(models.Model):
    _name = "snaptrack.booking.request"
    _description = "Photography / Video Request"

    name = fields.Char(
        string="Request",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: ("New"),
    )
    # description = fields.Text(string="Description")
    customer_id = fields.Many2one(
        "res.users", string="Customer", default=lambda self: self.env.user
    )
    request_details = fields.Text(string="Request Details")
    address = fields.Text(string="Address")
    status = fields.Selection(
        [
            ("new", "New"),
            ("assigned", "Assigned"),
            ("in_progress", "In Progress"),
            ("completed", "Completed"),
        ],
        string="Status",
        default="new",
        copy=False,
    )
    assigned_photographer_id = fields.Many2one(
        "res.partner", string="Assigned Photographer"
    )
    preferred_date = fields.Date("Preferred Date")
    quotation_id = fields.Many2one("sale.order", string="Quotation")
    # category_id = fields.Many2one("snaptrack.service.category", string="Category")
    # category = fields.Many2one("product.product", string="Product Category")
    product_category_id = fields.Many2many("product.product", string="Product Category")

    @api.constrains("preferred_date")
    def _check_preferred_date(self):
        today = date.today()
        for request in self:
            if request.preferred_date < today:
                raise ValidationError("Preferred date cannot be in the past.")

    def generate_quotation(self):
        if not self.product_category_id:
            return

        order_lines = []
        for product_category in self.product_category_id:
            order_line = {
                "product_id": product_category.id,
                "name": self.product_category_id.name,
                "price_unit": product_category.list_price,
                "product_uom_qty": 1,
            }
            order_lines.append((0, 0, order_line))
            print("=============", self.customer_id.name)
            quotation_values = {
                "partner_id": self.customer_id.id,
                "partner_invoice_id": self.customer_id.id,
                "partner_shipping_id": self.customer_id.id,
                "order_line": order_lines,
            }

        quotation = self.env["sale.order"].create(quotation_values)
        self.status = "assigned"

        return {
            "type": "ir.actions.act_window",
            "name": "Quotation",
            "res_model": "sale.order",
            "res_id": quotation.id,
            "view_mode": "form",
            "target": "current",
        }
