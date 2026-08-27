# -*- coding: utf-8 -*-
from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    airiv_waybill_number = fields.Char(string="Indonesian Waybill / Resi", copy=False)
    airiv_shipping_label_url = fields.Char(string="Thermal Label URL", copy=False)
