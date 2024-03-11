from odoo import models


class BookingRequest(models.Model):
    _inherit = "snaptrack.booking.request"

    def generate_quotation(self):
        Task = self.env["project.task"]
        project = (
            self.env["project.project"].sudo().create({"name": self.customer_id.name})
        )
        photographer = self.assigned_photographer_id  # Get the assigned photographer
        task_vals = {
            "name": self.customer_id.name,
            "project_id": project.id,
            "user_ids": [(4, photographer.id)],  # Assign the task to the photographer
            "description": self.request_details,  # Display booking request details in task description
            "date_deadline": self.preferred_date,  # Set deadline as preferred date
        }
        Task.sudo().create(task_vals)
        self.status = "assigned"
        return super().generate_quotation()
