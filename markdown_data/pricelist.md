# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/purchase/products/pricelist.md

Import vendor pricelist
=======================

Set vendor prices to auto-populate requests for quotations (RFQs) or
purchase orders (POs) with the unit price, once the product is added,
which reduces errors and saves time.

In Odoo, vendor pricelists can be
`added individually <purchase/products/pricelist>`{.interpreted-text
role="ref"} on the product form, or
`imported in bulk <purchase/products/import-pricelist>`{.interpreted-text
role="ref"}, via an XLSX or CSV file.

::: {.important}
::: {.title}
Important
:::

Please review this
`import guide <../../../essentials/export_import_data>`{.interpreted-text
role="doc"} before uploading vendor pricelists.
:::

On product form {#purchase/products/pricelist}
---------------

To manually add the vendor price on the product form, go to the
`Purchase app -->
Products --> Products`{.interpreted-text role="menuselection"}, and
click the desired product.

::: {.note}
::: {.title}
Note
:::

Product forms are accessible from multiple apps, such as **Sales**,
**Inventory**, and **Manufacturing**.
:::

In the `Purchase`{.interpreted-text role="guilabel"} tab of the product
form, input the vendor and their price, to have this information
auto-populate on a request for quotation each time the product is
listed.

::: {.seealso}
`Vendor pricelist on product form <purchase/manage_deals/vendor-pricelist>`{.interpreted-text
role="ref"}
:::



Import vendor pricelist {#purchase/products/import-pricelist}
-----------------------

To import vendor pricelists, ensure the XLSX or CSV file is accurately
completed. The best way to obtain a correctly formatted template,
including product names, references, and vendor details, is to first
`export a pricelist <purchase/products/export-price>`{.interpreted-text
role="ref"} from the database.

Modify the exported file, as needed, then import it back into the Odoo
database.

### Export pricelist {#purchase/products/export-price}

To export a pricelist, go to
`Purchase app --> Configuration --> Vendor Pricelists`{.interpreted-text
role="menuselection"}.

On the page, tick the checkbox(es) for the desired vendor pricelists.

Then, click the `fa-cog`{.interpreted-text role="icon"}
`Actions`{.interpreted-text role="guilabel"} button that appears, and
choose `fa-upload`{.interpreted-text role="icon"}
`Export`{.interpreted-text role="guilabel"} from the drop-down menu.



In the resulting pop-up window, fields listed under the
`Fields to export`{.interpreted-text role="guilabel"} section are
included in the exported file. To add more fields, find the desired
field in the `Available fields`{.interpreted-text role="guilabel"}
section, and click the `fa-plus`{.interpreted-text role="icon"}
`(plus)`{.interpreted-text role="guilabel"} icon to the right of the
field.

::: {.note}
::: {.title}
Note
:::

To update to existing records, tick the
`I want to update data (import-compatible
export)`{.interpreted-text role="guilabel"} checkbox, and refer to the
section on the `External ID
<purchase/products/external-id>`{.interpreted-text role="ref"} field.

For details on commonly-used fields for importing vendor pricelists, see
the `Common fields
<purchase/products/common-fields>`{.interpreted-text role="ref"}
section.
:::

Select the desired `Export Format`{.interpreted-text role="guilabel"}:
`XLSX`{.interpreted-text role="guilabel"} or `CSV`{.interpreted-text
role="guilabel"}.

To save the selected fields as a template, click the
`Template`{.interpreted-text role="guilabel"} field, and select
`New template`{.interpreted-text role="guilabel"} from the drop-down
menu. Type the name of the new template, and click the
`fa-floppy-o`{.interpreted-text role="icon"} `(save)`{.interpreted-text
role="guilabel"} icon. After that, the template is a selectable option
when clicking the `Template`{.interpreted-text role="guilabel"} field.

Finally, click `Export`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

With `developer mode <developer-mode>`{.interpreted-text role="ref"}
turned on, the column names of the exported file display the *field
name* with the *technical name* in parenthesis.
:::

::: {.example alt="Exporting vendor pricelist."}
.. figure:: pricelist/export-data.png

Export vendor pricelist in XLSX format. It includes
`Product Template`{.interpreted-text role="guilabel"} and other fields
in the `Fields to export`{.interpreted-text role="guilabel"} section.
:::

#### External ID {#purchase/products/external-id}

*External ID* is a unique identifier used to update existing vendor
pricelists. Without it, imported records create new entries, instead of
updating existing ones. Including this field in the XLSX or CSV,
indicates the line replaces an existing vendor pricelist in the Odoo
database.

::: {.example alt="Show 'Ready Mat' appear twice."}
.. figure:: pricelist/duplicate-values.png

[Ready Mat]{.title-ref} appears twice because the external ID was
omitted during the price update from [\$790]{.title-ref} to
[\$780]{.title-ref}.
:::

To look-up the `External ID`{.interpreted-text role="guilabel"} for a
vendor pricelist, tick the `I want to update
data (import-compatible export)`{.interpreted-text role="guilabel"}
checkbox at the top of the `Export Data`{.interpreted-text
role="guilabel"} pop-up window.

::: {.note}
::: {.title}
Note
:::

Selecting `External ID`{.interpreted-text role="guilabel"} from the
`Available fields`{.interpreted-text role="guilabel"} section with the
`I want to update data (import-compatible export)`{.interpreted-text
role="guilabel"} checkbox ticked results in an export file with two
columns containing the external ID.
:::

#### Common fields {#purchase/products/common-fields}

Below is a list of commonly-used fields when importing vendor
pricelists:

  Field name                                                                    Used for                                                                                                                                                                                                                                Field in Odoo database                                                                                                                                                                                                                                                                                 Technical name of field
  ----------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------
  Vendor                                                                        The only required field for creating a vendor pricelist record. This field specifies the vendor associated with the product.                                                                                                            `Vendor`{.interpreted-text role="guilabel"} field in the `vendor pricelist of the product form                                                                                                                                                                                                         [partner\_id]{.title-ref}
                                                                                                                                                                                                                                                                                                                        <purchase/products/pricelist>`{.interpreted-text role="ref"}.                                                                                                                                                                                                                                          
  Product Template                                                              The Odoo product the vendor pricelist entry is related to.                                                                                                                                                                              `Product`{.interpreted-text role="guilabel"} field in the vendor pricelist.                                                                                                                                                                                                                            [product\_tmpl\_id]{.title-ref}
  Quantity                                                                      The minimum quantity required to receive the product at the specified price.                                                                                                                                                            `Quantity`{.interpreted-text role="guilabel"} field in the vendor pricelist. (If not visible, enable it by clicking the `oi-settings-adjust`{.interpreted-text role="icon"} `(adjust)`{.interpreted-text role="guilabel"} icon, and tick the `Quantity`{.interpreted-text role="guilabel"} checkbox)   [min\_qty]{.title-ref}
  Unit Price                                                                    The purchase price for the product from the vendor.                                                                                                                                                                                     `Price`{.interpreted-text role="guilabel"} field in the vendor pricelist.                                                                                                                                                                                                                              [price]{.title-ref}
  Delivery Lead Time                                                            `Number of days <inventory/warehouses_storage/purchase-lt>`{.interpreted-text role="ref"} before receiving the product after confirming a purchase order.                                                                               `Delivery Lead Time`{.interpreted-text role="guilabel"} field on the vendor pricelist.                                                                                                                                                                                                                 [delay]{.title-ref}
  Sequence                                                                      Defines the order of vendors in the pricelist when multiple vendors are available. For example, if [Azure Interior]{.title-ref} is listed first and Wood Corner second, their sequences would be [1]{.title-ref} and [2]{.title-ref}.   N/A                                                                                                                                                                                                                                                                                                    [sequence]{.title-ref}
  Company                                                                       Name of company the product belongs to.                                                                                                                                                                                                 `Company`{.interpreted-text role="guilabel"} field in the vendor pricelist.                                                                                                                                                                                                                            [company\_id]{.title-ref}
  `External ID <purchase/products/external-id>`{.interpreted-text role="ref"}   Unique ID of a record used to update existing vendor pricelists.                                                                                                                                                                        N/A                                                                                                                                                                                                                                                                                                    [id]{.title-ref}

  : Field name definitions

### Import records

With a template downloaded, fill out the XLSX or CSV file with the
necessary information. After inputting everything, import the file back
into the Odoo database, by going to
`Purchase app --> Configuration --> Vendor Pricelists`{.interpreted-text
role="menuselection"}.

On the page, click the `fa-cog`{.interpreted-text role="icon"}
`(gear)`{.interpreted-text role="guilabel"} icon in the top-left corner.
In the drop-down menu that appears, click
`Import records`{.interpreted-text role="guilabel"}.

Then, click `Upload File`{.interpreted-text role="guilabel"} in the
upper-left corner, and after selecting the XLSX or CSV file, confirm the
correct fields, and click `Import`{.interpreted-text role="guilabel"}.

::: {.seealso}
\- `../../../essentials/export_import_data`{.interpreted-text
role="doc"} -
`Common fields <purchase/products/common-fields>`{.interpreted-text
role="ref"}
:::



#### Formatting import file

To understand how to format import files for vendor pricelists, consider
the following example.

-   [Storage Box]{.title-ref} (`Reference`{.interpreted-text
    role="guilabel"}: [E-COM08]{.title-ref}) is sold by [Wood
    Corner]{.title-ref} for [\$10]{.title-ref}.
-   [Large Desk]{.title-ref} (`Reference`{.interpreted-text
    role="guilabel"}: [E-COM09]{.title-ref}) has no records in the
    vendor pricelist.

An import file is created to do the following:

-   Update the price for [Wood Corner]{.title-ref} from
    [\$10]{.title-ref} to [\$13]{.title-ref}.
-   Add pricelist for \`Storage Box\`: the vendor, [Ready
    Mat]{.title-ref} intends to sell the product for [\$14]{.title-ref}.
-   Add pricelist for \`Large Desk\`: vendor is [Wood
    Corner]{.title-ref}, price is [\$1299]{.title-ref}.
-   Add pricelist for \`Large Desk\`: vendor is [Azure
    Interior]{.title-ref}, price is [\$1399]{.title-ref}.

  id                                 company\_id                  delay   price     product\_tmpl\_id         sequence   partner\_id
  ---------------------------------- ---------------------------- ------- --------- ------------------------- ---------- ----------------
  product.product\_supplierinfo\_3   My Company (San Francisco)   3       13.00     \[E-COM08\] Storage Box   4          Wood Corner
                                     My Company (San Francisco)   3       14.00     \[E-COM08\] Storage Box   5          Ready Mat
                                     My Company (San Francisco)   2       1299.00   \[E-COM09\] Large Desk    6          Wood Corner
                                     My Company (San Francisco)   4       1399.00   \[E-COM09\] Large Desk    7          Azure Interior

  : Vendor pricelist data

::: {.note}
::: {.title}
Note
:::

The *technical field name* was used to create this information.
:::

::: {.note}
::: {.title}
Note
:::

Download the sample files for reference:

-   `Sample XLSX import file <pricelist/pricelist-example.xlsx>`{.interpreted-text
    role="download"}
-   `Sample CSV import file <pricelist/pricelist-example.csv>`{.interpreted-text
    role="download"}
:::
