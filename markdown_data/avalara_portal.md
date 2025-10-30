# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/taxes/avatax/avalara_portal.md

Avalara (Avatax) portal {#avatax/portal}
=======================

Avalara\'s (*AvaTax*) management console offers account management
options including: viewing/editing the transactions sent from Odoo to
*AvaTax*, details on how the taxes are calculated, tax reporting, tax
exemption management, and tax return resources.

::: {.tip}
::: {.title}
Tip
:::

Avalara is the software developer of the tax software, *AvaTax*.
:::

To access the console, first, navigate to either Avalara\'s
 or
 environment. This will depend
on which type of account was set in the
`integration <../avatax>`{.interpreted-text role="doc"}. Log in to the
management console.

{.align-center}

::: {.seealso}
For more information see Avalara\'s documentation: [Activate your
Communications Customer Portal
account](https://community.avalara.com/support/s/document-item?language=en_US&bundleId=qvv1656594440497&topicId=Activate_your_Communications_Customer_Portal_account.html&_LANG=enus).
:::

Transactions {#avalara/portal-transactions}
------------

To access transactions, click in the `Transactions`{.interpreted-text
role="guilabel"} link on the main dashboard upon logging into the
`avatax/portal`{.interpreted-text role="ref"}. To manually access the
*Transactions* page, while logged into the Avalara console, navigate to
`Transactions --> Transactions`{.interpreted-text role="menuselection"}.

{.align-center}

### Edit transaction

Click into a transaction to reveal more details about the transaction.
These details include sections on `Invoice detail`{.interpreted-text
role="guilabel"}, `Additional info`{.interpreted-text role="guilabel"},
and `Customer info`{.interpreted-text role="guilabel"}. Click
`fa-pencil`{.interpreted-text role="icon"}
`Edit document details`{.interpreted-text role="guilabel"} to make
changes to the transaction.

A `Discount`{.interpreted-text role="guilabel"} can be added to adjust
the invoice. This is especially useful in cases where the transaction
has already synced with Avalara / *AvaTax*, and changes need to be made
afterward.

### Filter {#avalara/portal-filter}

Filter transactions on the `Transactions`{.interpreted-text
role="guilabel"} page, by setting the `From`{.interpreted-text
role="guilabel"} and `To`{.interpreted-text role="guilabel"} fields, and
configuring other fields to filter by, including:

-   `Document Status`{.interpreted-text role="guilabel"}: any of the
    following options, `All`{.interpreted-text role="guilabel"},
    `Voided`{.interpreted-text role="guilabel"},
    `Committed`{.interpreted-text role="guilabel"},
    `Uncommitted`{.interpreted-text role="guilabel"}, or
    `Locked`{.interpreted-text role="guilabel"}.
-   `Document Code`{.interpreted-text role="guilabel"}: any of the
    following options, `Exactly match`{.interpreted-text
    role="guilabel"}, `Starts with`{.interpreted-text role="guilabel"},
    or `Contains`{.interpreted-text role="guilabel"}.
-   `Customer/Vendor Code`{.interpreted-text role="guilabel"}: the
    customer/vendor code in Odoo (e.g. [Contact18]{.title-ref}).
-   `Country`{.interpreted-text role="guilabel"}: the country this tax
    was calculated in; this is a text field.
-   `Region`{.interpreted-text role="guilabel"}: the region of the
    country, which varies based on the `Country`{.interpreted-text
    role="guilabel"} selection.

Click `fa-plus`{.interpreted-text role="icon"}
`Filters`{.interpreted-text role="guilabel"} to access the following
filter conditions:

-   `Document Type`{.interpreted-text role="guilabel"}: any of the
    following selections, `All`{.interpreted-text role="guilabel"},
    `Sales
    Invoice`{.interpreted-text role="guilabel"},
    `Purchase Invoice`{.interpreted-text role="guilabel"},
    `Return Invoice`{.interpreted-text role="guilabel"},
    `Inventory Transfer
    Inbound Invoice`{.interpreted-text role="guilabel"},
    `Inventory Transfer Outbound Invoice`{.interpreted-text
    role="guilabel"}, or `Customs
    Invoice`{.interpreted-text role="guilabel"}.
-   `Import ID`{.interpreted-text role="guilabel"}: represents the
    import ID of the document.

### Sort by

On the `Transactions`{.interpreted-text role="guilabel"} page,
transactions will be listed below, according to the set
`avalara/portal-filter`{.interpreted-text role="ref"}, located in the
top half of the page. The following columns are available by default, to
sort by ascending or descending order:

-   `Doc Code`{.interpreted-text role="guilabel"}: either of the
    following options, `Exactly match`{.interpreted-text
    role="guilabel"}, `Starts with`{.interpreted-text role="guilabel"},
    or `Contains`{.interpreted-text role="guilabel"}.
-   `Doc Status`{.interpreted-text role="guilabel"}: either of the
    following options, `All`{.interpreted-text role="guilabel"},
    `Voided`{.interpreted-text role="guilabel"},
    `Committed`{.interpreted-text role="guilabel"},
    `Uncommitted`{.interpreted-text role="guilabel"}, or
    `Locked`{.interpreted-text role="guilabel"}.
-   `Cust/Vendor Code`{.interpreted-text role="guilabel"} : this is the
    customer/vendor code in Odoo (e.g. Contact18).
-   `Region`{.interpreted-text role="guilabel"}: this is the region of
    the country, this will vary based on the `Country`{.interpreted-text
    role="guilabel"} selection.
-   `Amount`{.interpreted-text role="guilabel"}: the numeric amount of
    the total amount on the Odoo document.
-   `Tax`{.interpreted-text role="guilabel"}: the numeric amount of the
    tax applied to the total.

{.align-center}

#### Customize columns

Additional columns can be added by clicking the
`fa-cog`{.interpreted-text role="icon"}
`Customize columns`{.interpreted-text role="guilabel"}. On the resulting
popover window, click the drop-down menu for the
`column`{.interpreted-text role="guilabel"} that should be changed.

The following columns can be added for additional transactional
information:

-   `AvaTax calculated`{.interpreted-text role="guilabel"}: the amount
    of tax calculated by *AvaTax*.
-   `Country`{.interpreted-text role="guilabel"}: the country this tax
    was calculated in; this is a text field.
-   `Cust/vendor code`{.interpreted-text role="guilabel"}: the
    customer/vendor code in Odoo (e.g. [Contact18]{.title-ref}).
-   `Currency`{.interpreted-text role="guilabel"}: the standardized
    abbreviation for the currency the amount total is in.
-   `Doc date`{.interpreted-text role="guilabel"}: the document\'s date
    of creation.
-   `Doc status`{.interpreted-text role="guilabel"}: any of the
    following options, `All`{.interpreted-text role="guilabel"},
    `Voided`{.interpreted-text role="guilabel"},
    `Committed`{.interpreted-text role="guilabel"},
    `Uncommitted`{.interpreted-text role="guilabel"}, or
    `Locked`{.interpreted-text role="guilabel"}.
-   `Doc type`{.interpreted-text role="guilabel"}: any of the following
    selections, `All`{.interpreted-text role="guilabel"}, `Sales
    Invoice`{.interpreted-text role="guilabel"},
    `Purchase Invoice`{.interpreted-text role="guilabel"},
    `Return Invoice`{.interpreted-text role="guilabel"},
    `Inventory Transfer
    Inbound Invoice`{.interpreted-text role="guilabel"},
    `Inventory Transfer Outbound Invoice`{.interpreted-text
    role="guilabel"}, or `Customs
    Invoice`{.interpreted-text role="guilabel"}.
-   `Import ID`{.interpreted-text role="guilabel"}: represents the
    import ID of the document.
-   `Last modified`{.interpreted-text role="guilabel"}: timestamp of the
    last time the document was modified.
-   `Location code`{.interpreted-text role="guilabel"}: the location
    code used to calculate the tax, based on the delivery address.
-   `PO number`{.interpreted-text role="guilabel"}: the purchase order
    number.
-   `Reference code`{.interpreted-text role="guilabel"}: the Odoo
    reference code (e.g. NV/2024/00003)
-   `Region`{.interpreted-text role="guilabel"}: the region of the
    country,which varies based on the `Country`{.interpreted-text
    role="guilabel"} selection.
-   `Salesperson code`{.interpreted-text role="guilabel"}: the numeric
    ID of the user assigned to the sales order in Odoo.
-   `Tax date`{.interpreted-text role="guilabel"}: the month/day/year of
    the tax calculation.
-   `Tax override type`{.interpreted-text role="guilabel"}: where an
    exemption would appear, should there be none, the field populates
    with `None`{.interpreted-text role="guilabel"}.

To add a new column click the `fa-plus`{.interpreted-text role="icon"}
`Column`{.interpreted-text role="guilabel"}.

::: {.seealso}
For more information on *AvaTax* transactions, refer to this Avalara
documentation:
.
:::

### Import-export

While on the `avalara/portal-transactions`{.interpreted-text
role="ref"}, click `fa-download`{.interpreted-text role="icon"} `Import
transactions`{.interpreted-text role="guilabel"} or
`fa-upload`{.interpreted-text role="icon"}
`Export transactions`{.interpreted-text role="guilabel"} to import or
export transactions.

### Reports

To access reporting, navigate to the `Reports`{.interpreted-text
role="menuselection"} link in the top menu of the Avalara management
console. Next, select from one of the available reporting tabs:
`Transactions
reports`{.interpreted-text role="guilabel"},
`Liability & tax return reports`{.interpreted-text role="guilabel"}, or
`Exemption reports`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Additionally, there is a `Favorites`{.interpreted-text role="guilabel"}
tab and `Downloads`{.interpreted-text role="guilabel"} tab. The
`Favorites`{.interpreted-text role="guilabel"} tab contains any
favorited report configurations for the Avalara user. The
`Downloads`{.interpreted-text role="guilabel"} tab contains a list view
where the user can download the high-volume transaction reports created
in the last 30 days.
:::

Make a selection for the `Report Category`{.interpreted-text
role="guilabel"}, and the `Report Name`{.interpreted-text
role="guilabel"}, under the `Select a report`{.interpreted-text
role="guilabel"} section.

Next, fill out the `Select report details`{.interpreted-text
role="guilabel"} section. These options will vary based on the tab
selected above.

Depending on the report size, the following two options are available in
the section labeled,
`Select the approximate number of transactions for your report`{.interpreted-text
role="guilabel"}: `Create and
download the report instantly`{.interpreted-text role="guilabel"} (for
small reports) and `Create and download the report in
the background`{.interpreted-text role="guilabel"} (for larger reports).
Select one or the other depending on the volume of transactions in this
report.

Finally, under the section labeled,
`Report preview and export`{.interpreted-text role="guilabel"} make a
selection of the file type to download. Either a
`.PDF`{.interpreted-text role="guilabel"} or `.XLS`{.interpreted-text
role="guilabel"} can be chosen. Alternatively, the file can be previewed
by selecting the `Preview`{.interpreted-text role="guilabel"} option.

After making all the configurations, click
`Create report`{.interpreted-text role="guilabel"} to download the
report. Click `fa-star-o`{.interpreted-text role="icon"}
`Make this report a favorite`{.interpreted-text role="guilabel"} to save
the report configuration to the user\'s favorites.

After the report is created, click `fa-download`{.interpreted-text
role="icon"} `Download`{.interpreted-text role="guilabel"} to download
the file to the device.

::: {.tip}
::: {.title}
Tip
:::

Select a pre-configured report from the
`Frequently used reports`{.interpreted-text role="guilabel"} section of
the reporting dashboard.

Access this list by clicking on the `Reports`{.interpreted-text
role="guilabel"} option in the top menu of the Avalara management
console, and scroll to the bottom of the page.
:::

::: {.seealso}
[See Avalara\'s documentation: Reports in
AvaTax](https://community.avalara.com/support/s/document-item?language=en_US&bundleId=rjq1671176624730&topicId=Reports_in_AvaTax.html&_LANG=enus).
:::

Add more jurisdictions
----------------------

Additional jurisdictions (tax locations) can be added in the Avalara
management console. Navigate to either Avalara\'s
 or
 environment. This will depend
on which type of account was set in the
`integration <../avatax>`{.interpreted-text role="doc"}.

Next, navigate to `Settings --> Where you collect tax`{.interpreted-text
role="menuselection"}. Choose between the three different tabs,
depending on the business need. The first tab is
`Sales and use tax`{.interpreted-text role="guilabel"}, where tax can be
collected for the United States. Click the `fa-plus`{.interpreted-text
role="icon"} `Add to where
you collect sales and use tax`{.interpreted-text role="guilabel"} to add
another location where the company collects sales and use tax.

The second option, is the `VAT/GST`{.interpreted-text role="guilabel"}
tab where the `fa-plus`{.interpreted-text role="icon"} `Add a country
or territory where you collect VAT/GST`{.interpreted-text
role="guilabel"} can be selected to add another country or territory
where the company collects VAT/GST.

Finally, on the far-right, is the `Customs duty`{.interpreted-text
role="guilabel"} tab, where a country can be added where the company
collects customs duty. Simply click on the `fa-plus`{.interpreted-text
role="icon"} `Add a country
where you calculate customs duty`{.interpreted-text role="guilabel"}
icon below the tab.

![AvaTax management console, on the Where you collect tax page, with the add button and
sales and use tax tab highlighted.](avalara_portal/where-you-collect-tax.png){.align-center}

::: {.seealso}
[See Avalara\'s documentation: Add local jurisdiction
taxes](https://community.avalara.com/support/s/document-item?language=en_US&bundleId=bla1700809896571_bla1700809896571&topicId=nbw1698727575499.html&_LANG=enus).
:::

Tax exemption certificate
-------------------------

Tax exemption certificates for customers can be added into the Avalara
management console, so that *AvaTax* is aware of which customers may be
exempt from paying certain taxes. To add an *exception certificate*
navigate to `Exemptions --> Customer certificates`{.interpreted-text
role="menuselection"}. From there, click on the
`fa-plus`{.interpreted-text role="icon"}
`Add a certificate`{.interpreted-text role="guilabel"} to configure an
exemption.

::: {.warning}
::: {.title}
Warning
:::

An Avalara subscription to Exemption Certificate Management (ECM) is
required in order to attach certificate images, and to be ready for an
audit. For more on subscribing to this add-on, visit
.
:::

End-of-year operations
----------------------

Avalara\'s services include tax return services, for when it is time to
file taxes at the end of the year. To access Avalara\'s tax services
log, into the . Then,
from the main dashboard, click `Returns`{.interpreted-text
role="guilabel"}. Avalara will prompt the Avalara user to log in for
security purposes, and redirect the user to the *Returns* portal.

{.align-center}

Click `Get started`{.interpreted-text role="guilabel"} to begin the tax
return process. For more information, refer to this Avalara
documentation: [About Managed
Returns](https://community.avalara.com/support/s/document-item?language=en_US&bundleId=hps1656397152776_hps1656397152776&topicId=Learn_about_Managed_Returns.html&_LANG=enus).

::: {.tip}
::: {.title}
Tip
:::

Alternatively, click on the `Returns`{.interpreted-text
role="menuselection"} button in the top menu of the Avalara management
console.
:::

::: {.seealso}
\- `../avatax`{.interpreted-text role="doc"} -
`avatax_use`{.interpreted-text role="doc"} - [US Tax Compliance: Avatax
elearning
video](https://www.odoo.com/slides/slide/us-tax-compliance-avatax-2858?fullscreen=1)
:::
