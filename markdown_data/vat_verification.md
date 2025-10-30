# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/taxes/vat_verification.md

VAT numbers verification (VIES)
===============================

[VAT Information Exchange
System](https://ec.europa.eu/taxation_customs/vies/#/vat-validation), or
**VIES**, is a tool provided by the European Commission that allows you
to check the validity of VAT numbers for companies registered in the
European Union.

Odoo\'s VAT Validation feature uses the VIES to verify your contacts\'
VAT numbers directly from Odoo\'s interface.

::: {.note}
::: {.title}
Note
:::

Regardless of whether or not the Verify VAT Numbers feature is enabled,
Odoo checks the format of a contact\'s VAT against the [expected format
of VAT numbers](https://en.wikipedia.org/wiki/VAT_identification_number)
from that country.
:::

VIES VAT number verification
----------------------------

To activate this feature, go to
`Accounting --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. In the `Taxes`{.interpreted-text role="guilabel"}
section, enable the `Verify VAT Numbers`{.interpreted-text
role="guilabel"} feature, and click on `Save`{.interpreted-text
role="guilabel"}.

Once the `Verify VAT Numbers`{.interpreted-text role="guilabel"} feature
is enabled, if the contact\'s `Tax ID`{.interpreted-text
role="guilabel"} field is populated *and* its country is different from
your company\'s country, Odoo displays an
`Intra-Community Valid`{.interpreted-text role="guilabel"} checkbox.
Odoo tests the VAT number through the VIES and automatically checks or
unchecks the `Intra-Community Valid`{.interpreted-text role="guilabel"}
checkbox depending on the validity of the VAT number.



::: {.important}
::: {.title}
Important
:::

It is possible to manually override the
`Intra-Community Valid`{.interpreted-text role="guilabel"} field on a
contact in case the automatic VIES check is incorrect (for example, if
the company was recently created and its VAT is not yet in the VIES).
This change is logged in the chatter for transparency.
:::

::: {.note}
::: {.title}
Note
:::

Odoo can
`automatically apply fiscal positions <fiscal_positions/automatic>`{.interpreted-text
role="ref"}. If the Verify VAT Numbers feature is enabled, any fiscal
positions with VAT required enabled will require Intra-Community valid
VAT numbers to apply automatically.
:::
