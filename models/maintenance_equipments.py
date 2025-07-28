from odoo import models, fields, api, _

class SdMaintenanceEquipments(models.Model):
    _inherit = 'maintenance.equipment'

    asset_no = fields.Char()
