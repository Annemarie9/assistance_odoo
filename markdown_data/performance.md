# File: /content/odoo_doc17.0/fr/content/applications/websites/ecommerce/performance.md

Performance management
======================

Odoo integrates a variety of tools to analyze and improve the
performance of your eCommerce website.

Data monitoring
---------------

**Website** allows monitoring and analysis of the sales performance of
your eCommerce. To access the **reporting view**, go to
`Website --> Reporting --> eCommerce`{.interpreted-text
role="menuselection"}. This dashboard helps you monitor everything
related to sales, such as sales performance per product, category, day,
etc.

{.align-center}

By clicking `Measures`{.interpreted-text role="guilabel"}, you can
select the type of measurement used, such as:

-   `Margin`{.interpreted-text role="guilabel"};
-   `Qty Invoiced`{.interpreted-text role="guilabel"};
-   `Untaxed Total`{.interpreted-text role="guilabel"};
-   `Volume`{.interpreted-text role="guilabel"};
-   \...

Other options include **multiple views (Pivot, etc.), comparison** by
periods or years, and directly `insert in spreadsheet`{.interpreted-text
role="guilabel"}, etc.

Analytics
---------

It is possible to link your Odoo website with
`analytics/plausible`{.interpreted-text role="ref"} and
`analytics/google-analytics`{.interpreted-text role="ref"}.

Email queue optimization {#ecommerce/performance/email_queue}
------------------------

For websites handling flash sales (e.g., event ticket sales) or
experiencing high traffic spikes, order confirmation emails can become a
performance bottleneck, potentially slowing down the checkout process
for other customers.

To improve performance, these emails can be queued and processed
separately from the order confirmation flow. This is managed by the
`Sales: Send pending emails`{.interpreted-text role="guilabel"}
scheduled action, which sends queued emails as soon as possible.

To enable asynchronous email sending:

1.  Enable the
    `developer mode </applications/general/developer_mode>`{.interpreted-text
    role="doc"}.
2.  Go to `Apps`{.interpreted-text role="menuselection"}, remove the
    `Apps`{.interpreted-text role="guilabel"} filter, and install the
    `Sales
    - Async Emails`{.interpreted-text role="guilabel"} module.
3.  Go to
    `Settings --> Technical --> System Parameters`{.interpreted-text
    role="menuselection"} and set the
    `sale.async_emails`{.interpreted-text role="guilabel"} system
    parameter to [True]{.title-ref}.
4.  Go to
    `Settings --> Technical --> Scheduled Actions`{.interpreted-text
    role="menuselection"} and ensure that the
    `Sales: Send pending emails`{.interpreted-text role="guilabel"}
    scheduled action is enabled.

::: {.caution}
::: {.title}
Caution
:::

Enabling this feature may delay order confirmation and invoice emails by
a few minutes. It is recommended only for high-traffic websites, as it
can introduce unnecessary delays for e-commerce websites with moderate
traffic.
:::
