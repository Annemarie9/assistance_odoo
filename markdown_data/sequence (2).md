# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/customer_invoices/sequence.md

Invoice sequence
================

When confirming an invoice, Odoo generates a unique invoice reference
number. By default, it uses the sequence format
[INV/year/incrementing-number]{.title-ref} (e.g.,
[INV/2025/00001]{.title-ref}), which restarts from [00001]{.title-ref}
each year.

However, it is possible to
`change the sequence format <accounting/invoice/resequencing>`{.interpreted-text
role="ref"} and its periodicity, and to
`mass-resequence invoices <accounting/invoice/mass-resequencing>`{.interpreted-text
role="ref"}.

::: {.note}
::: {.title}
Note
:::

Changes made to reference numbers are logged in the chatter.
:::

Changing the default sequence {#accounting/invoice/resequencing}
-----------------------------

To customize the default sequence, open the last confirmed invoice,
click `Reset to
Draft`{.interpreted-text role="guilabel"}, and edit the invoice\'s
reference number.



Odoo then explains how the detected format will be applied to all future
invoices. For example, if the current invoice\'s month is added, the
sequence\'s periodicity will change to every month instead of every
year.



::: {.tip}
::: {.title}
Tip
:::

The sequence format can be edited directly when creating the first
invoice of a given sequence period.
:::

Mass-resequencing invoices {#accounting/invoice/mass-resequencing}
--------------------------

It can be helpful to resequence multiple invoice numbers. For example,
when importing invoices from another invoicing or accounting system and
the reference originates from the previous software, continuity for the
current year must be maintained without restarting from the beginning.

::: {.note}
::: {.title}
Note
:::

This feature is only available to users with administrator or advisor
access.
:::

Follow these steps to resequence invoice numbers:

1.  Activate the `developer mode <developer-mode>`{.interpreted-text
    role="ref"}.
2.  From the `Accounting Dashboard`{.interpreted-text role="guilabel"},
    open the `Customer Invoices`{.interpreted-text role="guilabel"}
    journal.
3.  Select the invoices that need a new sequence.
4.  Click the `fa-cog`{.interpreted-text role="icon"}
    `Actions`{.interpreted-text role="guilabel"} menu and select
    `Resequence`{.interpreted-text role="guilabel"}.
5.  In the `Ordering`{.interpreted-text role="guilabel"} field, choose
    to
    -   `Keep current order`{.interpreted-text role="guilabel"}: The
        order of the numbers remains the same.
    -   `Reorder by accounting date`{.interpreted-text role="guilabel"}:
        The number is reordered by accounting date.
6.  Set the `First New Sequence`{.interpreted-text role="guilabel"}.
7.  `Preview Modifications`{.interpreted-text role="guilabel"} and click
    `Confirm`{.interpreted-text role="guilabel"}.



::: {.note}
::: {.title}
Note
:::

\- To indicate where the sequence change began, the first invoice in the
new sequence is highlighted in red in the
`Customer Invoices`{.interpreted-text role="guilabel"} list. This visual
marker is permanent and purely informational. - If there are any
irregularities in the new sequence, such as gaps, cancelled, or deleted
entries within the open period, a
`Gaps in the sequence`{.interpreted-text role="guilabel"} message
appears in the `Customer Invoices`{.interpreted-text role="guilabel"}
journal on the Accounting dashboard. To view more details about the
related invoice(s), click `Gaps in the sequence`{.interpreted-text
role="guilabel"}. This visual marker is temporary and will disappear
once the entry\'s accounting date is on or after the lock date.
:::

::: {.tip}
::: {.title}
Tip
:::

Resequencing is not possible:

-   When entries are before a lock date.
-   When the sequence leads to a duplicate.
-   When the range is invalid. For example, if the
    `Invoice Date`{.interpreted-text role="guilabel"} doesn\'t align
    with the date in the new sequence, such as using a 2024 sequence
    (INV/2024/XXXXX) for an invoice dated in 2025.

In these cases, a `Validation Error`{.interpreted-text role="guilabel"}
message appears.
:::
