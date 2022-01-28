# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# Copyright 2021 ForgeFlow <http://www.forgeflow.com>

from openupgradelib import openupgrade  # pylint: disable=W7936

_months = [
    (1, "01"),
    (2, "02"),
    (3, "03"),
    (4, "04"),
    (5, "05"),
    (6, "06"),
    (7, "07"),
    (8, "08"),
    (9, "09"),
    (10, "10"),
    (11, "11"),
    (12, "12"),
]


def update_l10n_fr_intrastat_product_declaration_year(env):
    openupgrade.logged_query(
        env.cr, """
        UPDATE l10n_fr_intrastat_product_declaration
        SET year = TO_CHAR(year_moved0, '0000')
        """
    )


def map_l10n_fr_intrastat_product_declaration_month(env):
    openupgrade.logged_query(
        env.cr, """
        UPDATE l10n_fr_intrastat_product_declaration
        SET month = TO_CHAR(month_moved0, '00')
        """
    )


@openupgrade.migrate()
def migrate(env, version):
    update_l10n_fr_intrastat_product_declaration_year(env)
    map_l10n_fr_intrastat_product_declaration_month(env)
    