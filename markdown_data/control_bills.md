# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/purchase/manage_deals/control_bills.md

Bill control policies
=====================

::: {#purchase/manage_deals/control-bills}
In Odoo\'s *Purchase* app, the *bill control* policy determines the
quantities billed by vendors on every purchase order (PO), for either
ordered or received quantities.
:::

The policy selected in the *Purchase* app settings acts as the default
value, and is applied to any new product created.

Configuration
-------------

To configure the *bill control* policy, navigate to
`Purchase app --> Configuration
--> Settings`{.interpreted-text role="menuselection"}, and scroll down
to the `Invoicing`{.interpreted-text role="guilabel"} section. Under
`Bill Control`{.interpreted-text role="guilabel"}, select either
`Ordered quantities`{.interpreted-text role="guilabel"} or
`Received quantities`{.interpreted-text role="guilabel"}. Then, click
`Save`{.interpreted-text role="guilabel"}.

{.align-center}

-   `Ordered quantities`{.interpreted-text role="guilabel"}: creates a
    vendor bill as soon as a `PO (Purchase Order)`{.interpreted-text
    role="abbr"} is confirmed. The products and quantities in the
    `PO (Purchase Order)`{.interpreted-text role="abbr"} are used to
    generate a draft bill.

-   `Received quantities`{.interpreted-text role="guilabel"}: a bill is
    created only *after* part of the total order has been received. The
    products and quantities received are used to generate a draft bill.
    An error message appears if creation of a vendor bill is attempted
    without receiving anything.

    {.align-center}

::: {.note}
::: {.title}
Note
:::

If a specific product should use a different control policy than
selected in the *Purchase* app settings, the
`Bill Control`{.interpreted-text role="guilabel"} policy for that
product can be changed from its product form.

To do that, navigate to
`Purchase app --> Products --> Products`{.interpreted-text
role="menuselection"}, and select a product. From the product form,
click the `Purchase`{.interpreted-text role="guilabel"} tab. Under the
`Vendor
Bills`{.interpreted-text role="guilabel"} section, modify the selection
in the `Control Policy`{.interpreted-text role="guilabel"} field.
:::

3-way matching
--------------

The *3-way matching* feature ensures vendor bills are only paid once
some (or all) of the products included in the
`PO (Purchase Order)`{.interpreted-text role="abbr"} have been received.

To activate *3-way matching*, navigate to
`Purchase app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, and scroll down to
the `Invoicing`{.interpreted-text role="guilabel"} section. Then, tick
the checkbox for `3-way matching`{.interpreted-text role="guilabel"} to
enable the feature, and click `Save`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.important}
::: {.title}
Important
:::

The `3-way matching`{.interpreted-text role="guilabel"} feature **only**
works with the `Bill Control`{.interpreted-text role="guilabel"} policy
set to `Received quantities`{.interpreted-text role="guilabel"}.
:::

### Pay vendor bills with 3-way matching

When *3-way matching* is enabled, vendor bills display a
`Should Be Paid`{.interpreted-text role="guilabel"} field under the
`Other Info`{.interpreted-text role="guilabel"} tab. When a new vendor
bill is created, the field is set to `Yes`{.interpreted-text
role="guilabel"}, since a bill **cannot** be created until at least some
of the products included in a `PO (Purchase Order)`{.interpreted-text
role="abbr"} have been received.

To create a vendor bill from a `PO (Purchase Order)`{.interpreted-text
role="abbr"}, navigate to `Purchase app --> Orders -->
Purchase Orders`{.interpreted-text role="menuselection"}. From the
`Purchase Orders`{.interpreted-text role="guilabel"} page, select the
desired `PO (Purchase Order)`{.interpreted-text role="abbr"} from the
list. Then, click `Create Bill`{.interpreted-text role="guilabel"}.
Doing so opens a new draft `Vendor Bill`{.interpreted-text
role="guilabel"} form, in the `Draft`{.interpreted-text role="guilabel"}
stage. Click the `Other Info`{.interpreted-text role="guilabel"} tab,
and locate the `Should Be
Paid`{.interpreted-text role="guilabel"} field.

::: {.important}
::: {.title}
Important
:::

The `PO (Purchase Order)`{.interpreted-text role="abbr"} selected from
the list **must not** be billed yet, or an
`Invalid Operation`{.interpreted-text role="guilabel"} pop-up window
appears. This occurs for `POs (Purchase Orders)`{.interpreted-text
role="abbr"} with a `Received quantities`{.interpreted-text
role="guilabel"} policy, and a `Fully Billed`{.interpreted-text
role="guilabel"} `Billing Status`{.interpreted-text role="guilabel"}.

{.align-center}
:::

Click the drop-down menu next to `Should Be Paid`{.interpreted-text
role="guilabel"} to view the available options: `Yes`{.interpreted-text
role="guilabel"}, `No`{.interpreted-text role="guilabel"}, and
`Exception`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If the total quantity of products from a
`PO (Purchase Order)`{.interpreted-text role="abbr"} has not been
received, Odoo only includes the products that *have* been received in
the draft vendor bill.
:::

Draft vendor bills can be edited to increase the billed quantity, change
the price of the products in the bill, and add additional products to
the bill.

If the draft bill\'s information is changed, the
`Should Be Paid`{.interpreted-text role="guilabel"} field status is set
to `Exception`{.interpreted-text role="guilabel"}. This means that Odoo
notices the discrepancy, but does not block the changes or display an
error message, since there might be a valid reason for making changes to
the draft bill.

To process the vendor bill, select a date in the
`Bill Date`{.interpreted-text role="guilabel"} field, and click
`Confirm`{.interpreted-text role="guilabel"}, followed by
`Register Payment`{.interpreted-text role="guilabel"}.

This opens a `Register Payment`{.interpreted-text role="guilabel"}
pop-up window. From this window, accounting information is pre-populated
based on the database\'s accounting settings. Click
`Create Payment`{.interpreted-text role="guilabel"} to process the
vendor bill.

Once payment has been registered for a vendor bill, and the bill
displays the green `Paid`{.interpreted-text role="guilabel"} banner, the
`Should Be Paid`{.interpreted-text role="guilabel"} field status is set
to `No`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

The `Should Be Paid`{.interpreted-text role="guilabel"} status on bills
is automatically set by Odoo. However, the status can be manually
changed by clicking the field\'s drop-down menu inside the
`Other Info`{.interpreted-text role="guilabel"} tab.
:::

View a purchase order\'s billing status
---------------------------------------

Once a `PO (Purchase Order)`{.interpreted-text role="abbr"} is
confirmed, its `Billing Status`{.interpreted-text role="guilabel"} can
be viewed under the `Other
Information`{.interpreted-text role="guilabel"} tab on the
`PO (Purchase Order)`{.interpreted-text role="abbr"} form.

To view the `Billing Status`{.interpreted-text role="guilabel"} of a
`PO (Purchase Order)`{.interpreted-text role="abbr"}, navigate to
`Purchase app -->
Orders --> Purchase Orders`{.interpreted-text role="menuselection"}, and
select a `PO (Purchase Order)`{.interpreted-text role="abbr"} to view.

Click the `Other Information`{.interpreted-text role="guilabel"} tab,
and locate the `Billing Status`{.interpreted-text role="guilabel"}
field.

{.align-center}

The table below details the different values the
`Billing Status`{.interpreted-text role="guilabel"} field could read,
and when they are displayed, depending on the *Bill Control* policy
used.

  Billing Status    On received quantities                           On ordered quantities
  ----------------- ------------------------------------------------ -----------------------
  Nothing to Bill   PO confirmed; no products received               *Not applicable*
  Waiting Bills     All/some products received; bill not created     PO confirmed
  Fully Billed      All/some products received; draft bill created   Draft bill created

::: {.seealso}
`manage`{.interpreted-text role="doc"}
:::
