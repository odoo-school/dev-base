from odoo import api, fields, models


class SocialSubscriber(models.Model):
    _name = 'social.subscriber'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'social.subscriber']

    promo_count = fields.Integer(compute='_compute_promo_count')
    filename = fields.Char(string='File Name', help="Technical field for the file name", readonly=True)

    @api.depends('promo_ids')
    def _compute_promo_count(self):
        for rec in self:
            rec.promo_count = len(rec.promo_ids)
