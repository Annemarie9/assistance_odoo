# File: /content/odoo_doc17.0/fr/content/applications/essentials/contacts/merge.md

Merge contacts
==============

Odoo\'s *Contacts* application allows user\'s to merge duplicate
contacts, without losing any information in the process. This keeps the
database organized, and prevents contacts from being contacted by more
than one salesperson.

Merge duplicate contacts {#contacts/merge-duplicate}
------------------------

::: {.danger}
::: {.title}
Danger
:::

Merging is an irreversible action. Do **not** merge contacts unless
absolutely certain they should be combined.
:::

Navigate to the `Contacts app`{.interpreted-text role="menuselection"},
and select the `oi-view-list`{.interpreted-text role="icon"}
`(list)`{.interpreted-text role="guilabel"} icon. Select two or more
duplicate contacts from the list, and tick the checkbox (on the
far-left) for the contacts that should be merged. Then, click the
`fa-cog`{.interpreted-text role="icon"} `Actions`{.interpreted-text
role="guilabel"} icon, and select `Merge`{.interpreted-text
role="guilabel"} from the resulting drop-down menu.

{.align-center}

This opens the `Merge`{.interpreted-text role="guilabel"} pop-up window.
From here, review the details of the contacts before confirming they
should be merged. If any contacts in the list should **not** be merged,
click the `fa-times`{.interpreted-text role="icon"}
`(delete)`{.interpreted-text role="guilabel"} icon at the far right of
the contact.

::: {.tip}
::: {.title}
Tip
:::

Click the individual contact to open the record for that contact, and
view additional information.
:::

{.align-center}

Click the `Destination Contact`{.interpreted-text role="guilabel"}
field, and select an option from the drop-down list. This field defaults
to the contact record that was created first in the system.

After confirming the information on the pop-up window, click
`Merge Contacts`{.interpreted-text role="guilabel"}.

Deduplicate contacts
--------------------

After the merge is finished, a pop-up window appears confirming it is
complete. This pop-up window also contains a
`Deduplicate the other Contacts`{.interpreted-text role="guilabel"}
button. This feature searches for duplicated records, based on selected
criteria, and merges them automatically, or after manual approval.

Click the `Deduplicate the other Contacts`{.interpreted-text
role="guilabel"} button to open the `Deduplicate
Contacts`{.interpreted-text role="guilabel"} pop-up window.

Select one or more fields to be used in the search for duplicated
records. Duplicated contacts can be searched, based on the following
criteria:

-   `Email`{.interpreted-text role="guilabel"}
-   `Name`{.interpreted-text role="guilabel"}
-   `Is Company`{.interpreted-text role="guilabel"}
-   `VAT`{.interpreted-text role="guilabel"}
-   `Parent Company`{.interpreted-text role="guilabel"}

::: {.note}
::: {.title}
Note
:::

If more than one field is selected, only records that have **all**
fields in common are suggested as duplicates.
:::

If necessary, select criteria to be used to exclude potential duplicates
from the search. Potential duplicates can be excluded from the search,
based on the following criteria:

-   `A user associated to the contact`{.interpreted-text
    role="guilabel"}
-   `Journal Items associated to the contact`{.interpreted-text
    role="guilabel"}

After confirming the search criteria, click either
`Merge with Manual Check`{.interpreted-text role="guilabel"},
`Merge Automatically`{.interpreted-text role="guilabel"}, or
`Merge Automatically all process`{.interpreted-text role="guilabel"}.

If `Merge with Manual Check`{.interpreted-text role="guilabel"} is
selected, complete the merge by following the `steps
above <contacts/merge-duplicate>`{.interpreted-text role="ref"}.
