# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/reporting/intrastat.md

Intrastat
=========

Intrastat is the data collection and statistics production system for
goods traded among EU member states. It collects data on:

-   Commercial transactions of goods for use, consumption, investment,
    or resale with ownership transfer;
-   Goods movements without transfer of ownership (e.g., stock
    relocations or moves of goods before or after outsourced production
    or processing, and after maintenance or repair);
-   Returns of goods.

::: {.note}
::: {.title}
Note
:::

Although the Intrastat system continues to be used, the term Intrastat
is not used in the [latest
legislation](http://data.europa.eu/eli/reg/2019/2152/2022-01-01),
referring instead to *intra-Union trade in goods statistics*.
:::

::: {.seealso}
[Eurostat Statistics Explained - Glossary:
Intrastat](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Intrastat)
:::

General configuration {#intrastat/general-configuration}
---------------------

Enable the Intrastat report by going to
`Accounting --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Under the `Customer Invoices`{.interpreted-text
role="guilabel"} section, tick `Intrastat`{.interpreted-text
role="guilabel"} and then `Save`{.interpreted-text role="guilabel"}.

### Default transaction codes: invoice and refund {#intrastat/default-transaction-codes}

You can set a default
`transaction code <intrastat/transaction-code>`{.interpreted-text
role="ref"} for all newly created invoice and refund transactions. Under
`Accounting --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, select a
`Default invoice transaction code`{.interpreted-text role="guilabel"}
and/or a `Default refund transaction
code`{.interpreted-text role="guilabel"} and then
`Save`{.interpreted-text role="guilabel"}. The code will be set
automatically on all respective invoice lines.

### Region code {#intrastat/region-code}

The region code is **only used by Belgian companies**. Under
`Accounting -->
Configuration --> Settings`{.interpreted-text role="menuselection"},
select the `Company Intrastat Region`{.interpreted-text role="guilabel"}
where the company is located and then `Save`{.interpreted-text
role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

If your warehouses are located in more than one region, you can define
the region code at the level of each warehouse instead. To do so, go to
`Inventory --> Configuration -->
Warehouses`{.interpreted-text role="menuselection"}, select a warehouse,
set its `Intrastat region`{.interpreted-text role="guilabel"}, and then
`Save`{.interpreted-text role="guilabel"}.

{.align-center}
:::

Product configuration {#intrastat/product-configuration}
---------------------

All products must be properly configured to be included in the Intrastat
report.

### Commodity code {#intrastat/commodity-code}

Commodity codes are internationally recognized reference numbers used to
classify goods depending on their **nature**. Intrastat uses the
[Combined
Nomenclature](https://taxation-customs.ec.europa.eu/customs-4/calculation-customs-duties/customs-tariff/combined-nomenclature_en).

To add a commodity code, go to
`Accounting --> Customers --> Products`{.interpreted-text
role="menuselection"} and select a product. Under the
`Accounting`{.interpreted-text role="guilabel"} tab, set the product\'s
`Commodity Code`{.interpreted-text role="guilabel"}.

::: {.seealso}
[National Bank of Belgium - Intrastat commodity
codes](https://www.nbb.be/en/statistics/foreign-trade/nomenclature-and-codes)
:::

### Quantity: weight and supplementary unit {#intrastat/quantity}

Depending on the nature of the goods, it is necessary to specify either
the product\'s weight in kilos (without packaging) or the product\'s
supplementary unit, such as square meter ([m2]{.title-ref}), number of
items ([p/st]{.title-ref}), liter ([l]{.title-ref}), or gram
([g]{.title-ref}).

To add a product\'s weight or supplementary unit, go to
`Accounting --> Customers -->
Products`{.interpreted-text role="menuselection"} and select a product.
Under the `Accounting`{.interpreted-text role="guilabel"} tab, depending
on the commodity code set, either fill in the product
`Weight`{.interpreted-text role="guilabel"} or its
`Supplementary Units`{.interpreted-text role="guilabel"}.

### Country of origin {#intrastat/origin-country}

To add the product\'s country of origin, go to
`Accounting --> Customers --> Products`{.interpreted-text
role="menuselection"} and select a product. Under the
`Accounting`{.interpreted-text role="guilabel"} tab, set the
`Country of Origin`{.interpreted-text role="guilabel"}.

Invoices and bills configuration {#intrastat/invoice-bill-configuration}
--------------------------------

Once products are properly configured, several settings must be
configured on the invoices and bills you create.

### Transaction code {#intrastat/transaction-code}

Transaction codes are used to identify a transaction\'s nature.
`Default transaction codes
<intrastat/default-transaction-codes>`{.interpreted-text role="ref"} can
be set for invoice and refund transactions.

To set a transaction code on an invoice line, create an invoice or a
bill, click the columns selection button, tick
`Intrastat`{.interpreted-text role="guilabel"}, and use the newly-added
`Intrastat`{.interpreted-text role="guilabel"} column to select a
transaction code.

{.align-center}

::: {.seealso}
[National Bank of Belgium - Intrastat: Nature of transactions from
January
2022](https://www.nbb.be/doc/dd/onegate/data/new_natures_of_transaction_2022_en.pdf)
:::

### Partner country {#intrastat/partner-country}

The partner country represents the vendor\'s country for bills and the
customer\'s country for invoices. It is automatically filled in using
the country set in the contact\'s `Country`{.interpreted-text
role="guilabel"} field.

To edit the partner country manually, create an invoice or a bill, click
the `Other Info`{.interpreted-text role="guilabel"} tab, and select the
`Intrastat Country`{.interpreted-text role="guilabel"}.

### Transport code {#intrastat/transport-code}

The transport code identifies the presumed **mode of transport** used to
send the goods (arrival or dispatch).

To add the transport code, create an invoice or a bill, go to the
`Other info`{.interpreted-text role="guilabel"} tab, and select the
`Intrastat Transport Mode`{.interpreted-text role="guilabel"}.

### Value of the goods {#intrastat/value}

The value of a good is the untaxed `Subtotal`{.interpreted-text
role="guilabel"} (`Price`{.interpreted-text role="guilabel"} multiplied
by `Quantity`{.interpreted-text role="guilabel"}) of an invoice line.

Partner configuration {#intrastat/partner}
---------------------

Two fields from the partner\'s contact form are used with Intrastat:
`VAT`{.interpreted-text role="guilabel"} and `Country`{.interpreted-text
role="guilabel"}. The country can be
`manually set <intrastat/partner-country>`{.interpreted-text role="ref"}
on the invoice or bill.

Generate the Intrastat report
-----------------------------

Generate the report by going to
`Accounting --> Reporting --> Audit Reports:
Intrastat Report`{.interpreted-text role="menuselection"}. It is
automatically computed based on the `default configuration
<intrastat/general-configuration>`{.interpreted-text role="ref"} and the
information found on the `products
<intrastat/product-configuration>`{.interpreted-text role="ref"},
`invoices and bills
<intrastat/invoice-bill-configuration>`{.interpreted-text role="ref"},
and `partners <intrastat/partner>`{.interpreted-text role="ref"}.

Export the report as a PDF, XLSX, or XML file to post it to your legal
administration.

Each report line refers to a single invoice line and contains the
following information:

-   Invoice or bill reference number;
-   System, which is a code automatically generated depending on whether
    the document is an invoice (dispatch) or a bill (arrival);
-   `Country <intrastat/partner-country>`{.interpreted-text role="ref"},
    which is the vendor\'s country for arrivals and the customer\'s
    country for dispatches;
-   `Transaction Code <intrastat/transaction-code>`{.interpreted-text
    role="ref"};
-   (If your company is located in Belgium)
    `Region Code <intrastat/region-code>`{.interpreted-text role="ref"};
-   `Commodity Code <intrastat/commodity-code>`{.interpreted-text
    role="ref"};
-   `Origin Country <intrastat/origin-country>`{.interpreted-text
    role="ref"};
-   `Partner VAT <intrastat/partner>`{.interpreted-text role="ref"};
-   `Transport Code <intrastat/transport-code>`{.interpreted-text
    role="ref"};
-   `Incoterm Code <../customer_invoices/incoterms>`{.interpreted-text
    role="doc"};
-   `Weight <intrastat/quantity>`{.interpreted-text role="ref"};
-   `Supplementary Units <intrastat/quantity>`{.interpreted-text
    role="ref"}; and
-   `Value <intrastat/value>`{.interpreted-text role="ref"}, which is
    always expressed in euros even if the original invoice or bill used
    another currency.
