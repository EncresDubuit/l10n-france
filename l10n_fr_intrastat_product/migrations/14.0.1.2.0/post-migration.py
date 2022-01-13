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
        SET year = {integer_year} || ''
        """.format(integer_year=openupgrade.get_legacy_name("year"))
    )


def map_l10n_fr_intrastat_product_declaration_month(env):
    openupgrade.map_values(
        env.cr,
        openupgrade.get_legacy_name("month"),
        "month",
        _months,
        table="l10n_fr_intrastat_product_declaration",
    )


@openupgrade.migrate()
def migrate(env, version):
    update_l10n_fr_intrastat_product_declaration_year(env)
    map_l10n_fr_intrastat_product_declaration_month(env)
    