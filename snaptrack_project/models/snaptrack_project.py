from odoo import models


class BookingRequest(models.Model):
    _inherit = "snaptrack.booking.request"

    def generate_quotation(self):
        Task = self.env["project.task"]
        project = (
            self.env["project.project"].sudo().create({"name": self.customer_id.name})
        )
        # photographer = self.assigned_photographer_id

        for product in self.product_category_id:
            product_name = product.name
            tag = self.env["project.tags"].search([("name", "=", product_name)])
            if not tag:
                tag = self.env["project.tags"].create({"name": product_name})

            task_vals = {
                "name": self.customer_id.name,
                "project_id": project.id,
                # "user_ids": [(4, photographer.id)],
                "date_deadline": self.preferred_date,
                "tag_ids": [(4, tag.id)],
            }

        Task.sudo().create(task_vals)
        self.status = "assigned"
        return super().generate_quotation()
