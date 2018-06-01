# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0).

from openerp import api, fields, models

class PurchaseRequest(models.Model):
    _inherit = 'purchase.request'

    state = fields.Selection( default='approved')
    
    @api.multi
    @api.onchange('id','state')
    def _set_status(self):
        for line in self:
            line.state = 'approved'

class PurchaseRequestLine(models.Model):
    
    _inherit = 'purchase.request.line'
    
    group_id = fields.Many2one('procurement.group', string="Procurement Group", copy=False)