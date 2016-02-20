# _*_ coding: utf-8 _*_
from openerp import models, fields, api


class JournalGroup(models.Model):
    _name = "account.journal.group"

    name = fields.Char()


class Journal(models.Model):
    _inherit = "account.journal"

    journal_group_id = fields.Many2one("account.journal.group", string="Journal Group")
