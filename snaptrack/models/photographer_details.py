from odoo import models, fields


class PhotographerDetails(models.Model):
    _name = "photographer.details"
    _description = "This is the description of photographer"

    name = fields.Char(string="Name")
