# _*_ coding: utf-8 _*_
from openerp import models, fields, api


class Voucher(models.Model):
    _inherit = "account.voucher"

    journal_group_id = fields.Many2one("account.journal.group", string="Journal Group")

    @api.onchange("journal_group_id")
    @api.multi
    def _onchange_journal_group(self):
        self.ensure_one()
        value = dict()
        if self.journal_group_id:
            domain = [("journal_group_id", "=", self.journal_group_id.id)]
            journal = self.env['account.journal'].search(domain)
            if journal:
                self.journal_id = journal[0] if len(journal) > 1 else journal
            else:
                self.journal_id = None
            value["domain"] = dict()
            value["domain"]["journal_id"] = domain
        return value
