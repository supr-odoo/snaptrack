from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    name = fields.Char(
        string="Request Number",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: ("New"),
    )
    description = fields.Text(string="Description")
    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    request_details = fields.Text(string="Request Details")
    status = fields.Selection(
        [
            ("new", "New"),
            ("assigned", "Assigned"),
            ("in_progress", "In Progress"),
            ("completed", "Completed"),
        ],
        string="Status",
        default="new",
    )
    assigned_photographer_id = fields.Many2one(
        "res.users", string="Assigned Photographer"
    )
    preferred_date = fields.Date("Preferred Date")
    quotation_id = fields.Many2one("sale.order", string="Quotation")
    # category_id = fields.Many2one("snaptrack.service.category", string="Category")
    category = fields.Many2one("product.product", string="Product Category")

    def generate_quotation(self):
        if not self.category:
            return
        quotation_values = {
            "partner_id": self.customer_id.id,
            "partner_invoice_id": self.customer_id.id,
            "partner_shipping_id": self.customer_id.id,
            "order_line": [
                (
                    0,
                    0,
                    {
                        "product_id": self.category.id,
                        "price_unit": self.category.list_price,
                        "product_uom_qty": 1,
                    },
                )
            ],
        }

        quotation = self.env["sale.order"].create(quotation_values)

        return {
            "type": "ir.actions.act_window",
            "name": "Quotation",
            "res_model": "sale.order",
            "res_id": quotation.id,
            "view_mode": "form",
            "target": "current",
        }
