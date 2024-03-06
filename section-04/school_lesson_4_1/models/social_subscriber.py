from odoo import _, fields, models
from odoo.exceptions import UserError


class SocialSubscriber(models.Model):
    _inherit = 'social.subscriber'

    profile_url = fields.Char(string="Profile URL")

    def action_open_profile(self):
        self.ensure_one()
        if not self.profile_url:
            raise UserError(_(
                "Profile URL is not specified for this subscriber. Please specify it firstly."
            ))
        return {
            'type': 'ir.actions.act_url',
            'url': self.profile_url,
            'target': 'new',  # available values: self | new ("new" is equal to target="_blank")
            'target_type': 'public',  # optional for external links (otherwise redirect to /web)
        }
