
from openerp import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class ProcurementOrder(models.Model):
    _inherit = 'procurement.order'

    @api.model
    def _prepare_purchase_request(self, procurement):

        _logger.info("TESTAGU-PROCUREMENT-Prepare procuremen header" )
        res = super(ProcurementOrder, self)._prepare_purchase_request(procurement)
        res.state = 'approved'
        _logger.info("TESTAGU-PROCUREMENT-Prepare procuremen header %s " % (res) )
        return res

    @api.model
    def _prepare_purchase_request_line(self, purchase_request, procurement):
        return {
            'product_id': procurement.product_id.id,
            'name': procurement.product_id.name,
            'date_required': procurement.date_planned,
            'product_uom_id': procurement.product_uom.id,
            'product_qty': procurement.product_qty,
            'request_id': purchase_request.id,
            'origin': procurement.origin,
            'group_id': procurement.group_id,
            'procurement_id': procurement.id
        }

    @api.model
    def _search_existing_purchase_request(self, procurement):
        """This method is to be implemented by other modules that can
        provide a criteria to select the appropriate purchase request to be
        extended.

        Aca podria agrupar por GROUP-ID del procurement para no tener que generar siempre un PR nuevo. 
        Sino que agrupo todas las lineas en un PR unico. 

        """
        return False

class PurchaseRequestLine(models.Model):
    
    _inherit = 'purchase.request.line'
    
    group_id = fields.Many2one('procurement.group', string="Procurement Group", copy=False)