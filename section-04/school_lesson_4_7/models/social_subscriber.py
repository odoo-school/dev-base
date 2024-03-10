from odoo import _, api, models


class SocialSubscriber(models.Model):
    _inherit = 'social.subscriber'

    def action_show_promo_from_kanban(self):
        self.ensure_one()
        return {
            'name': _('Social Promotions'),
            'type': 'ir.actions.act_window',
            'res_model': 'social.promo',
            'view_mode': 'tree',
            'context': {'default_subscriber_id': self.id},
            'domain': [('id', 'in', self.promo_ids.ids)],
            'target': 'new',
            # Available values of the "target":
            # 'current' - 'Current Window'  # default value
            # 'new' - 'New Window'
            # 'inline' - 'Inline Edit'
            # 'fullscreen' - 'Full Screen'
            # 'main' - 'Main action of Current Window'
        }

    def add_50_bonus(self):
        for subscriber in self:
            subscriber.write({'client_bonus': subscriber.client_bonus + 50})

    @api.model
    def _task_increase_bonus_per_month(self):
        subscribers = self.env['social.subscriber'].search([
            ('state', '=', 'registered'),
        ])
        for subscriber in subscribers:
            subscriber.write({'client_bonus': subscriber.client_bonus + 10})
