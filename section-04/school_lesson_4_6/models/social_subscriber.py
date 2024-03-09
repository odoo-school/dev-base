from datetime import timedelta

from odoo import api, fields, models


class SocialSubscriber(models.Model):
    _inherit = 'social.subscriber'
    _date_name = 'start_date'  # Field to use for default calendar view

    @api.model
    def get_unusual_days(self, date_from, date_to=None):
        """ Specify days as unusual that will be marked in the different color in the calendar view. """
        return {
            fields.Date.to_string(fields.Date.today()): True,
            fields.Date.to_string(fields.Date.today() + timedelta(days=7)): True,
            fields.Date.to_string(fields.Date.today() + timedelta(days=14)): True,
            fields.Date.to_string(fields.Date.today() + timedelta(days=21)): True,
        }
