# Copyright 2020 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openupgradelib import openupgrade

_column_renames = {
    "l10n_fr_intrastat_product_declaration": [("year", None),("month", None),("type", "declaration_type")]
}


@openupgrade.migrate()
def migrate(cr, version):
    if not version:
        return

    openupgrade.rename_columns(env.cr, _column_renames)

