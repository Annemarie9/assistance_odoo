# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/vendor_bills/sequence.md

Vendor bill sequence
====================

When confirming a vendor bill, Odoo generates a unique vendor bill
reference number. By default, it uses the sequence format
[BILL/year/month/incrementing-number]{.title-ref} (e.g.,
[BILL/2025/01/00001]{.title-ref}), which restarts from
[00001]{.title-ref} each year.

However, it is possible to
`change the sequence format <accounting/vendor_bills/resequencing>`{.interpreted-text
role="ref"} and its periodicity, and to `mass-resequence vendor bills
<accounting/vendor_bills/mass-resequencing>`{.interpreted-text
role="ref"}.

::: {.note}
::: {.title}
Note
:::

Changes made to reference numbers are logged in the chatter.
:::

Changing the default sequence {#accounting/vendor_bills/resequencing}
-----------------------------

To customize the default sequence, open the last confirmed vendor bill,
click `Reset to
Draft`{.interpreted-text role="guilabel"}, and edit the vendor bill\'s
reference number.



Odoo then explains how the detected format will be applied to all future
vendor bills. For example, if the current vendor bill\'s month is
withdrawn, the sequence\'s periodicity will change to every year instead
of every month.



::: {.tip}
::: {.title}
Tip
:::

The sequence format can be edited directly when creating the first
vendor bill of a given sequence period.
:::

Mass-resequencing vendor bills {#accounting/vendor_bills/mass-resequencing}
------------------------------

It can be helpful to resequence multiple vendor bill numbers. For
example, when importing vendor bills from another accounting system and
the reference originates from the previous software, continuity for the
current year must be maintained without restarting from the beginning.

::: {.note}
::: {.title}
Note
:::

This feature is only available to users with administrator or advisor
access.
:::

Follow these steps to resequence vendor bill numbers:

1.  Activate the `developer mode <developer-mode>`{.interpreted-text
    role="ref"}.
2.  In the vendor bills list view, select the vendor bills that need a
    new sequence.
3.  Click the `fa-cog`{.interpreted-text role="icon"}
    `Actions`{.interpreted-text role="guilabel"} menu and select
    `Resequence`{.interpreted-text role="guilabel"}.
4.  In the `Ordering`{.interpreted-text role="guilabel"} field, choose
    to
    -   `Keep current order`{.interpreted-text role="guilabel"}: The
        order of the numbers remains the same.
    -   `Reorder by accounting date`{.interpreted-text role="guilabel"}:
        The number is reordered by accounting date.
5.  Set the `First New Sequence`{.interpreted-text role="guilabel"}.
6.  `Preview Modifications`{.interpreted-text role="guilabel"} and click
    `Confirm`{.interpreted-text role="guilabel"}.



::: {.note}
::: {.title}
Note
:::

\- To indicate where the sequence change began, the first vendor bill in
the new sequence is highlighted in red in the
`Vendor Bills`{.interpreted-text role="guilabel"} list. This visual
marker is permanent and purely informational. - If there are any
irregularities in the new sequence, such as gaps, cancelled, or deleted
entries within the open period, a
`Gaps in the sequence`{.interpreted-text role="guilabel"} message
appears in the `Vendor Bills`{.interpreted-text role="guilabel"} journal
on the Accounting dashboard. To view more details about the related
vendor bill(s), click `Gaps in the sequence`{.interpreted-text
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
    `Bill Date`{.interpreted-text role="guilabel"} doesn\'t align with
    the date in the new sequence, such as using a 2024 sequence
    (BILL/2024/MM/XXXX) for an vendor bill dated in 2025.

In these cases, a `Validation Error`{.interpreted-text role="guilabel"}
message appears.
:::
