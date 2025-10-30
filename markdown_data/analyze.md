# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/purchase/advanced/analyze.md

Purchase Analysis report
========================

The *Purchase Analysis* report provides statistics about products
purchased using Odoo\'s **Purchase** app. This data is useful for
gaining a deeper understanding of key metrics related to purchase orders
(POs), including the quantity of products ordered and received, the
amount of time it takes to receive purchased products, and more.

To open the Purchase Analysis report, navigate to
`Purchase app --> Reporting -->
Purchase`{.interpreted-text role="menuselection"}.

::: {.important}
::: {.title}
Important
:::

The `Purchase Analysis`{.interpreted-text role="guilabel"} report is one
of many reports available across the Odoo app suite. This documentation
only covers the measures specific to the
`Purchase Analysis`{.interpreted-text role="guilabel"} report, along
with a few use case examples.

For a full overview of the basic features available in most Odoo
reports, see the documentation on
`reporting essentials <../../../essentials/reporting>`{.interpreted-text
role="doc"}.
:::

Measures
--------

*Measures* refer to the various datasets that can be displayed on the
`Purchase Analysis`{.interpreted-text role="guilabel"} report, with each
dataset representing a key statistic about
`POs (purchase orders)`{.interpreted-text role="abbr"} or products. To
choose a measure, click the `Measures`{.interpreted-text
role="guilabel"} `fa-caret-down`{.interpreted-text role="icon"} button,
and select one of the options from the drop-down menu:

-   `# of Lines`{.interpreted-text role="guilabel"}: The number of
    `PO (purchase order)`{.interpreted-text role="abbr"} order lines,
    across all `POs (purchase orders)`{.interpreted-text role="abbr"}.
-   `Average Cost`{.interpreted-text role="guilabel"}: The average cost
    of `POs (purchase orders)`{.interpreted-text role="abbr"}.
-   `Days to Confirm`{.interpreted-text role="guilabel"}: The number of
    days it takes to confirm a `PO (purchase order)`{.interpreted-text
    role="abbr"}.
-   `Days to Receive`{.interpreted-text role="guilabel"}: The number of
    days it takes to receive the products in a
    `PO (purchase order)`{.interpreted-text role="abbr"}.
-   `Gross Weight`{.interpreted-text role="guilabel"}: The total weight
    of purchased products.
-   `Qty Billed`{.interpreted-text role="guilabel"}: The quantity of a
    product (or products) for which the vendor has already been billed.
-   `Qty Ordered`{.interpreted-text role="guilabel"}: The quantity of a
    product (or products) ordered.
-   `Qty Received`{.interpreted-text role="guilabel"}: The quantity of
    an ordered product (or products) received.
-   `Qty to be Billed`{.interpreted-text role="guilabel"}: The quantity
    of an ordered product (or products) for which the vendor has yet to
    be billed.
-   `Total`{.interpreted-text role="guilabel"}: The total amount spent,
    including tax.
-   `Untaxed Total`{.interpreted-text role="guilabel"}: The total amount
    spent, excluding tax. This measure is selected by default.
-   `Volume`{.interpreted-text role="guilabel"}: The total volume of
    ordered products, for products which are measured by volume.
-   `Count`{.interpreted-text role="guilabel"}: The total count of
    `POs (purchase orders)`{.interpreted-text role="abbr"}.

::: {.tip}
::: {.title}
Tip
:::

Only one measure can be selected at a time when one of the
`fa-area-chart`{.interpreted-text role="icon"}
`(graph view)`{.interpreted-text role="guilabel"} options is enabled.
However, multiple measures, and varying group-by criteria (on the x and
y axes), can be selected when using the
`oi-view-pivot`{.interpreted-text role="icon"}
`(pivot table)`{.interpreted-text role="guilabel"}.
:::

Use case: determine days to receive products from each vendor {#purchase/purchase-analysis-example}
-------------------------------------------------------------

One possible use case for the `Purchase Analysis`{.interpreted-text
role="guilabel"} report is determining how long each vendor takes to
deliver purchased items. This allows companies to make better informed
decisions about which vendors they want to purchase from.

::: {.example}
A local bike shop, *Bike Haus*, sells high-quality unicycles, bicycles,
tricycles, and all the accessories needed to ride and maintain them.
They purchase their inventory from a few different vendors, and then
sell those products on to customers through their storefront.

Recently, Bike Haus has decided to have their purchasing manager, David,
look into how long it has taken each of their vendors to deliver the
items they\'ve purchased during the current year, 2024.

David starts by navigating to
`Purchase app --> Reporting --> Purchase`{.interpreted-text
role="menuselection"}, and selecting the
`fa-bar-chart`{.interpreted-text role="icon"} (bar chart) graph type at
the top of the report.

Next, he clicks the `fa-caret-down`{.interpreted-text role="icon"}
`(toggle)`{.interpreted-text role="guilabel"} button on the right of the
search bar to open its drop-down menu. In the
`Confirmation Date`{.interpreted-text role="guilabel"} filter section,
he makes sure that **only** the `2024`{.interpreted-text
role="guilabel"} filter is enabled. Then, he selects the
`Vendor`{.interpreted-text role="guilabel"} option in the
`Group By`{.interpreted-text role="guilabel"} section, before clicking
away from the drop-down menu to close it.

Finally, David clicks on the `Measures`{.interpreted-text
role="guilabel"} `fa-caret-down`{.interpreted-text role="icon"}
drop-down menu, and selects the `Days to Receive`{.interpreted-text
role="guilabel"} option.

With all of these options enabled, the
`Purchase Analysis`{.interpreted-text role="guilabel"} report shows a
bar chart, with one bar for each vendor, representing the average number
of days it takes to receive products purchased from the vendor.

Using this data, David can see that it takes Bike Friends over 4.5 days,
on average, to deliver purchased products. This is more than four times
the amount of time it takes any other vendor.

Based on these findings, David makes the decision to reduce the quantity
of products purchased from Bike Friends.

{.align-center}
:::

Use case: compare vendor POs for two time periods
-------------------------------------------------

Another use for the `Purchase Analysis`{.interpreted-text
role="guilabel"} report is to compare key statistics about
`POs (purchase orders)`{.interpreted-text role="abbr"} for two different
time periods, for a specific vendor. By doing so, it is easy to
understand how purchases from the vendor have increased or decreased.

::: {.example}
Following the
`previous example <purchase/purchase-analysis-example>`{.interpreted-text
role="ref"}, it has been one month since Bike Haus decided to reduce the
quantity of products purchased from Bike Friends, one of their
retailers. Bike Haus\' purchasing manager, David, wants to understand
the impact this decision has had on the amount of money they have spent
on Bike Friends products.

David starts by navigating to
`Purchase app --> Reporting --> Purchase`{.interpreted-text
role="menuselection"}. Then, he selects the
`oi-view-pivot`{.interpreted-text role="icon"}
`(pivot table)`{.interpreted-text role="guilabel"} option at the top of
the screen.

In the search bar, he types [Bike Friends]{.title-ref}, and clicks
`Enter`{.interpreted-text role="guilabel"}, so the report only shows
data for purchases from Bike Friends.

Then, David clicks the `fa-caret-down`{.interpreted-text role="icon"}
`(toggle)`{.interpreted-text role="guilabel"} button on the right of the
search bar to open its drop-down menu. In the
`Confirmation Date`{.interpreted-text role="guilabel"} field, he leaves
the `June`{.interpreted-text role="guilabel"} and
`2024`{.interpreted-text role="guilabel"} filters enabled. He also
selects `Confirmation
Date: Previous Period`{.interpreted-text role="guilabel"} in the
`Comparison`{.interpreted-text role="guilabel"} section, before clicking
away from the drop-down menu to close it.

Next, David clicks on the `Measures`{.interpreted-text role="guilabel"}
`fa-caret-down`{.interpreted-text role="icon"} drop-down menu. He leaves
the `Total`{.interpreted-text role="guilabel"} and
`Untaxed Total`{.interpreted-text role="guilabel"} datasets enabled, and
disables the `Order`{.interpreted-text role="guilabel"} and
`Count`{.interpreted-text role="guilabel"} datasets.

Finally, David clicks the `fa-minus-square-o`{.interpreted-text
role="icon"} `Total`{.interpreted-text role="guilabel"} button above the
rows on the pivot table, and selects the `Product`{.interpreted-text
role="guilabel"} option.

With all of these options configured, the
`Purchase Analysis`{.interpreted-text role="guilabel"} report shows a
pivot table comparing purchase data for the current month, June, with
the previous month, May.

The pivot table is broken down into two main columns: one for the
untaxed total spent, and one for the taxed total spent. These columns
are further broken down into three smaller columns: the amount spent in
May, the amount spent in June, and the variation between the two months,
represented as a percentage.

On the left side of the pivot table, one row is shown for each product
purchased from Bike Friends during June. Using this report, David is
able to see that Bike Haus has spent much less money on products
purchased from Bike Friends, compared to the previous month.

{.align-center}
:::
