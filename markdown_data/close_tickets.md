# File: /content/odoo_doc17.0/fr/content/applications/services/helpdesk/advanced/close_tickets.md

Close tickets
=============

Once work has been completed on a *Helpdesk* ticket in Odoo, there are
several ways it can be closed.

In addition to manually closing solved tickets, automatically closing
inactive tickets keeps the pipeline up-to-date. At the same time,
allowing customers to close their own tickets minimizes confusion around
whether an issue is considered solved or not. This results in increased
operational capacity for support teams, and higher customer
satisfaction.

Manually close solved tickets
-----------------------------

As work on a ticket progresses, it is moved along to the next stage in
the pipeline. Once the issue is solved, the ticket is moved to a
*folded* stage. This marks the ticket as *closed*.

To fold a stage, navigate to the `Helpdesk`{.interpreted-text
role="menuselection"} app dashboard, and click on a team to open the to
reveal that team\'s pipeline on a separate page.

From the pipeline page, hover over a stage\'s heading, and click the
`⚙️ (gear)`{.interpreted-text role="guilabel"} icon that appears in the
top-right corner of that stage\'s Kanban column.

{.align-center}

From the menu that appears, select `Edit`{.interpreted-text
role="guilabel"}. This opens the stage\'s settings in a pop-up window.

In the pop-up window, check the box labeled,
`Folded in Kanban`{.interpreted-text role="guilabel"}, towards the top
of the window. Then, click `Save & Close`{.interpreted-text
role="guilabel"} to confirm the changes.

Tickets that reach this stage are now considered: *closed*.

{.align-center}

::: {.warning}
::: {.title}
Warning
:::

Clicking the `⚙️ (gear)`{.interpreted-text role="guilabel"} icon also
displays the option to `Fold`{.interpreted-text role="guilabel"} the
stage. This setting folds the stage *temporarily* to simplify the Kanban
view. This does **not** close the tickets in this stage. It also does
**not** permanently fold the stage. If a stage needs to be folded, so
the tickets can be marked as *closed*, the
`Folded in Kanban`{.interpreted-text role="guilabel"} checkbox **must**
be checked on the stage\'s settings.
:::

Automatically close inactive tickets
------------------------------------

Tickets that are inactive for a set period of time can be automatically
closed. At that point, they are moved to a folded stage.

To have Odoo automatically close inactive tickets, go to the desired
team\'s settings page, by navigating to
`Helpdesk app --> Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"}, and selecting the desired team to configure.
Under the `Self-Service`{.interpreted-text role="guilabel"} section,
enable `Automatic
Closing`{.interpreted-text role="guilabel"}.

After ticking the box for `Automatic Closing`{.interpreted-text
role="guilabel"}, three new fields appear beneath:

-   `Move to Stage`{.interpreted-text role="guilabel"}
-   `After (#) days of inactivity`{.interpreted-text role="guilabel"}
-   `In Stages`{.interpreted-text role="guilabel"}

If one of the team\'s stages is set to be folded in the Kanban view, the
folded stage is the default selection in the
`Move to Stage`{.interpreted-text role="guilabel"} field. If the team
has more than one folded stage, the folded stage that occurs first in
the pipeline is the default. If no stage is folded, the default
selection is the last stage in the pipeline.

The `After (#) days of inactivity`{.interpreted-text role="guilabel"}
field defaults to [7]{.title-ref}, but can be adjusted if necessary.

::: {.warning}
::: {.title}
Warning
:::

The `After (#) days of inactivity`{.interpreted-text role="guilabel"}
field does **not** take the working calendar into account when tracking
the amount of time a ticket has been inactive.
:::

If only certain stages should be used to track days of inactivity, they
can be added to the `In Stages`{.interpreted-text role="guilabel"}
field.

::: {.example}
A team\'s pipeline is created with the following stages:

-   [New]{.title-ref}
-   [In Progress]{.title-ref}
-   [Customer Feedback]{.title-ref}
-   [Closed]{.title-ref}

Tickets may linger in the `Customer Feedback`{.interpreted-text
role="guilabel"} stage, because once an issue is solved, customers may
not respond immediately. At that point, the tickets can be closed
automatically.

Tickets in the `New`{.interpreted-text role="guilabel"} and
`In Progress`{.interpreted-text role="guilabel"} stages could remain
inactive due to assignment or workload issues. The support team may be
looking into the issue even if they are not updating the ticket
directly. Closing these tickets automatically would result in issues
going unsolved.

Therefore, the `Automatic Closing`{.interpreted-text role="guilabel"}
settings for this team would be configured as below:

-   `Automatic Closing`{.interpreted-text role="guilabel"}: *checked*
-   `Move to Stage`{.interpreted-text role="guilabel"}:
    [Solved]{.title-ref}
-   `After`{.interpreted-text role="guilabel"} [7]{.title-ref}
    `days of inactivity`{.interpreted-text role="guilabel"}
-   `In Stages`{.interpreted-text role="guilabel"}: [Customer
    Feedback]{.title-ref}

{.align-center}
:::

Allow customers to close their own tickets
------------------------------------------

Enabling the `Closure by Customers`{.interpreted-text role="guilabel"}
setting allows customers to close their own tickets when they determine
that their issue has been resolved.

To allow customers to close their own tickets, start by navigating to
`Helpdesk app
--> Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"}, and click on a team to open the team\'s settings
page. Next, scroll to the `Self-Service`{.interpreted-text
role="guilabel"} section, and check the box for `Closure by
Customers`{.interpreted-text role="guilabel"}.

{.align-center}

Once the ticket closing settings are enabled, a
`Close Ticket`{.interpreted-text role="guilabel"} button is available
for customers when they view their ticket through the customer portal.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Customers are able to view their tickets by clicking the
`View the ticket`{.interpreted-text role="guilabel"} link they receive
by email. The link is included in the
`Helpdesk: Ticket Received`{.interpreted-text role="guilabel"} template,
which is added to the first stage of a team by default. This link does
**not** require a customer to have access to the portal to view or
respond to their ticket.

Customers with access to the portal can view their tickets under
`My Account -->
Tickets`{.interpreted-text role="menuselection"}.
:::
