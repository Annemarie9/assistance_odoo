# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/taxes/eu_distance_selling.md

EU intra-community distance selling
===================================

EU intra-community distance selling involves the cross-border trade of
goods and services from vendors registered for VAT purposes to
individuals (B2C) located in a European Union member state. The
transaction is conducted remotely, typically through online platforms,
mail orders, telephone, or other means of communication.

EU intra-community distance selling is subject to specific VAT rules and
regulations. The vendor must charge VAT per the VAT rate applicable in
the buyer\'s country.

::: {.note}
::: {.title}
Note
:::

This remains applicable even if the vendor is located outside of the
European Union.
:::

Configuration
-------------

The **EU Intra-community Distance Selling** feature helps you comply
with this regulation by creating and configuring new **fiscal
positions** and **taxes** based on your company\'s country. To enable
it, go to
`Accounting --> Configuration --> Settings --> Taxes`{.interpreted-text
role="menuselection"}, tick
`EU Intra-community Distance Selling`{.interpreted-text
role="guilabel"}, and `Save`{.interpreted-text role="guilabel"}.



::: {.tip}
::: {.title}
Tip
:::

Whenever you add or modify taxes, you can automatically update your
fiscal positions. To do so, go to
`Accounting/Invoicing --> Settings --> Taxes --> EU Intra-community Distance
Selling`{.interpreted-text role="menuselection"} and click on the
`Refresh tax mapping`{.interpreted-text role="guilabel"}.
:::

::: {.note}
::: {.title}
Note
:::

We highly recommend checking that the proposed mapping is suitable for
the products and services you sell before using it.
:::

::: {.seealso}
\- `../taxes`{.interpreted-text role="doc"} -
`../../fiscal_localizations`{.interpreted-text role="doc"} -
`fiscal_positions`{.interpreted-text role="doc"}
:::

One-Stop Shop (OSS)
-------------------

The `OSS (One-Stop Shop)`{.interpreted-text role="abbr"} system
introduced by the European Union simplifies VAT collection for
**cross-border** sales of goods and services. It primarily applies to
business-to-consumer **(B2C)** cases. With the OSS, businesses can
register for VAT in their home country and use a single online portal to
handle VAT obligations for their sales within the EU. There are **two
primary schemes**: the **Union OSS** scheme for cross-border services
and the **Import OSS** scheme for goods valued at or below €150.

### Reports

To generate **OSS sales** or **OSS imports** reports and submit them
onto the OSS portal, go to
`Accounting --> Reporting --> Tax Report`{.interpreted-text
role="menuselection"}, click `Report: Generic Tax
report`{.interpreted-text role="guilabel"}, and select either
`OSS Sales`{.interpreted-text role="guilabel"} or
`OSS Imports`{.interpreted-text role="guilabel"}. Once selected, click
on `PDF`{.interpreted-text role="guilabel"}, `XLSX`{.interpreted-text
role="guilabel"}, or `XML`{.interpreted-text role="guilabel"} in the
top-left corner. This generates the currently-opened report in the
selected format. Once generated, log into the platform of your competent
federal authority to submit it onto the OSS portal.



::: {.seealso}
\- [European Commission: OSS \| Taxation and Customs
Union](https://ec.europa.eu/taxation_customs/business/vat/oss_en)
:::
