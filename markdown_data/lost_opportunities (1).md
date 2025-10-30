Manage lost opportunities
=========================

Not every opportunity results in a successful sale. To keep the pipeline
up-to-date, *lost* opportunities need to be identified. Specifying why
an opportunity was lost provides additional insight that can prove
useful for future opportunities.

Mark an opportunity as lost
---------------------------

To mark an opportunity as lost, first open the
`CRM app`{.interpreted-text role="menuselection"}, and select an
opportunity from the pipeline, by clicking on its corresponding Kanban
card. Doing so reveals that opportunity\'s detail form.

Then, click `Lost`{.interpreted-text role="guilabel"}, located at the
top of the opportunity\'s detail form.

{.align-center}

This opens the `Mark Lost`{.interpreted-text role="guilabel"} pop-up
window. From the `Lost Reason`{.interpreted-text role="guilabel"}
drop-down menu, choose an existing lost reason. If no applicable reason
is available, create a new one by entering it into the
`Lost Reason`{.interpreted-text role="guilabel"} field, and clicking
`Create`{.interpreted-text role="guilabel"}.

Additional notes and comments can be added below the lost reason in the
designated `Closing Note`{.interpreted-text role="guilabel"} field.

::: {.tip}
::: {.title}
Tip
:::

Neither the `Lost Reason`{.interpreted-text role="guilabel"} field, nor
the `Closing Note`{.interpreted-text role="guilabel"} field, on the
`Mark Lost`{.interpreted-text role="guilabel"} pop-up window are
required. However, it is recommended to include this information for the
sake of traceability, accountability, and reporting purposes.
:::

When all the desired information has been entered in the
`Mark Lost`{.interpreted-text role="guilabel"} pop-up window, click
`Mark as Lost`{.interpreted-text role="guilabel"}.

{.align-center}

After clicking `Mark as Lost`{.interpreted-text role="guilabel"}, a red
`Lost`{.interpreted-text role="guilabel"} banner is added to the
upper-right corner of the opportunity.

{.align-center}

::: {.note}
::: {.title}
Note
:::

To mark an *inactive* (archived) opportunity as lost, set the
`Probability`{.interpreted-text role="guilabel"} field to
[0]{.title-ref} percent.
:::

Create/edit lost reasons {#crm/lost-reasons}
------------------------

To create a new lost reason, or edit an existing one, navigate to
`CRM app -->
Configuration --> Lost Reasons`{.interpreted-text role="menuselection"}.

To edit an existing lost reason:

1.  Click on the reason to be edited to highlight it.
2.  Change the selected lost reason by editing the
    `Description`{.interpreted-text role="guilabel"} field.
3.  When finished, click `Save`{.interpreted-text role="guilabel"} in
    the upper-left corner.

To create a new lost reason:

1.  Click `New`{.interpreted-text role="guilabel"} in the upper-left
    corner of the `Lost Reasons`{.interpreted-text role="guilabel"}
    page.
2.  In the new blank line, click in the `Description`{.interpreted-text
    role="guilabel"} field, then type the new lost reason.
3.  When finished, click `Save`{.interpreted-text role="guilabel"}.

View lost opportunities
-----------------------

To retrieve lost opportunities in Odoo *CRM*, open the
`CRM app`{.interpreted-text role="menuselection"}. On the main
`Pipeline`{.interpreted-text role="guilabel"} dashboard, click into the
`Search...`{.interpreted-text role="guilabel"} bar at the top of the
page, and remove all of the default filters.

{.align-center}

Open the `Filters`{.interpreted-text role="guilabel"} drop-down menu, by
clicking the `🔻(triangle pointed down)`{.interpreted-text
role="guilabel"} icon to the right of the `Search...`{.interpreted-text
role="guilabel"} bar to open the drop-down menu containing
`Filters`{.interpreted-text role="guilabel"},
`Group By`{.interpreted-text role="guilabel"}, and
`Favorites`{.interpreted-text role="guilabel"} options, designated into
respective columns.

Select the `Lost`{.interpreted-text role="guilabel"} option from the
`Filters`{.interpreted-text role="guilabel"} section. Upon selecting
`Lost`{.interpreted-text role="guilabel"}, only the opportunities marked
as [Lost]{.title-ref} appear on the `Pipeline`{.interpreted-text
role="guilabel"} page.

### Sort opportunities by lost reason

To filter opportunities by a specific lost reason, click the
`🔻(triangle pointed down)`{.interpreted-text role="guilabel"} icon to
the right of the `Search...`{.interpreted-text role="guilabel"} bar
again to open the drop-down menu. In addition to the
`Lost`{.interpreted-text role="guilabel"} filter, under the
`Filters`{.interpreted-text role="guilabel"} column, click `Add Custom
Filter`{.interpreted-text role="guilabel"}, which opens an
`Add Custom Filter`{.interpreted-text role="guilabel"} pop-up window.

On the `Add Custom Filter`{.interpreted-text role="guilabel"} pop-up
window, click in the first field, and type [Lost Reason]{.title-ref} in
the `Search...`{.interpreted-text role="guilabel"} bar, or scroll to
search through the list to locate it. Then, click into the next field,
and select `=`{.interpreted-text role="guilabel"} from the drop-down
menu. Click into the third field, and select a lost reason from the
drop-down menu. Finally, click `Add`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

To view results for more than one lost reason, select the operator
`is in`{.interpreted-text role="guilabel"} in the second field of the
custom filter in the `Add Custom Filter`{.interpreted-text
role="guilabel"} pop-up window. Choosing this operator makes it possible
to choose multiple lost reasons in the third field.

{.align-center}
:::

Restore lost opportunities
--------------------------

To restore a lost opportunity, open the `CRM app`{.interpreted-text
role="menuselection"} to reveal the `Pipeline`{.interpreted-text
role="guilabel"} dashboard. Or, navigate to
`CRM app --> Sales --> My Pipeline`{.interpreted-text
role="menuselection"}. From here, click the
`🔻(triangle pointed down)`{.interpreted-text role="guilabel"} icon to
the right of the `Search...`{.interpreted-text role="guilabel"} bar to
open the drop-down menu that contains `Filters`{.interpreted-text
role="guilabel"}, `Group By`{.interpreted-text role="guilabel"}, and
`Favorites`{.interpreted-text role="guilabel"} columns.

Under the `Filters`{.interpreted-text role="guilabel"} column, select
`Lost`{.interpreted-text role="guilabel"}. Doing so reveals all the lost
opportunities on the `Pipeline`{.interpreted-text role="guilabel"} page.

::: {.tip}
::: {.title}
Tip
:::

To see all opportunities in the database, remove the default
`My Pipeline`{.interpreted-text role="guilabel"} filter from the
`Search...`{.interpreted-text role="guilabel"} bar.
:::

Then, click on the Kanban card of the desired lost opportunity to
restore, which opens that opportunity\'s detail form.

From the lost opportunity\'s detail form, click
`Restore`{.interpreted-text role="guilabel"} in the upper-left corner.
Doing so removes the red `Lost`{.interpreted-text role="guilabel"}
banner from the opportunity form, signifying the opportunity has been
restored.

{.align-center}

### Restore multiple opportunities at once

To restore multiple opportunities at once, navigate to the main
`Pipeline`{.interpreted-text role="guilabel"} dashboard in the *CRM*
app, open the `Filters`{.interpreted-text role="guilabel"} drop-down
menu, and select the `Lost`{.interpreted-text role="guilabel"} option.

Next, select the list view option, represented by the
`≣ (list)`{.interpreted-text role="guilabel"} icon in the upper-right
corner. Doing so places all the opportunities from the
`Pipeline`{.interpreted-text role="guilabel"} page in a list view. With
the list view chosen, select the checkbox to the left of each
opportunity to be restored.

Once the desired opportunities have been selected, click the
`⚙️ Actions`{.interpreted-text role="guilabel"} drop-down menu at the
top of the `Pipeline`{.interpreted-text role="guilabel"} page. From the
`⚙️ Actions`{.interpreted-text role="guilabel"} drop-down menu, select
`Unarchive`{.interpreted-text role="guilabel"}.

Doing so removes those selected opportunities from the
`Pipeline`{.interpreted-text role="guilabel"} page because they no
longer fit the `Lost`{.interpreted-text role="guilabel"} filter
criteria. Delete the `Lost`{.interpreted-text role="guilabel"} filter
from the search bar to reveal these newly-restored opportunities.

{.align-center}

Manage lost leads
-----------------

If *Leads* are enabled on a database, they can be marked as *lost* in
the same manner as opportunities. Leads use the same
`lost reasons <crm/lost-reasons>`{.interpreted-text role="ref"} as
opportunities.

::: {.note}
::: {.title}
Note
:::

To enable leads, navigate to
`CRM app --> Configuration --> Settings`{.interpreted-text
role="menuselection"} and check the `Leads`{.interpreted-text
role="guilabel"} checkbox. Then, click `Save`{.interpreted-text
role="guilabel"}. This adds a new `Leads`{.interpreted-text
role="guilabel"} menu to the header menu bar at the top of the page.
:::

### Mark a lead as lost

To mark a lead as lost, navigate to
`CRM app --> Leads`{.interpreted-text role="menuselection"}, and select
a lead from the list. Doing so reveals that lead\'s detail form.

Then, click `Lost`{.interpreted-text role="guilabel"}, located at the
top of the lead\'s detail form.

This opens the `Mark Lost`{.interpreted-text role="guilabel"} pop-up
window. From the `Lost Reason`{.interpreted-text role="guilabel"}
drop-down menu, choose an existing lost reason. If no applicable reason
is available, create a new one by entering it into the
`Lost Reason`{.interpreted-text role="guilabel"} field, and clicking
`Create`{.interpreted-text role="guilabel"}.

Additional notes and comments can be added below the lost reason
designated in the `Closing Note`{.interpreted-text role="guilabel"}
field.

When all the desired information has been entered in the
`Mark Lost`{.interpreted-text role="guilabel"} pop-up window, click
`Mark as Lost`{.interpreted-text role="guilabel"}.

### Restore lost leads

To restore a lost lead, navigate to
`CRM app --> Leads`{.interpreted-text role="menuselection"}, then click
the `🔻
(triangle pointed down)`{.interpreted-text role="guilabel"} icon to the
right of the `Search...`{.interpreted-text role="guilabel"} bar to open
the drop-down menu that contains the `Filters`{.interpreted-text
role="guilabel"}, `Group By`{.interpreted-text role="guilabel"}, and
`Favorites`{.interpreted-text role="guilabel"} columns.

Under the `Filters`{.interpreted-text role="guilabel"} column, select
`Lost`{.interpreted-text role="guilabel"}. Doing so reveals all the lost
leads on the `Leads`{.interpreted-text role="guilabel"} page.

Then, click on the desired lost lead to restore, which opens that
lead\'s detail form.

From the lost lead\'s detail form, click `Restore`{.interpreted-text
role="guilabel"} in the upper-left corner. Doing so removes the red
`Lost`{.interpreted-text role="guilabel"} banner from the lead form,
signifying the lead has been restored.

### Restore multiple leads at once

To restore multiple leads at once, navigate to
`CRM app --> Leads`{.interpreted-text role="menuselection"}, open the
`Filters`{.interpreted-text role="guilabel"} drop-down menu, and select
the `Lost`{.interpreted-text role="guilabel"} option. Select the
checkbox to the left of each lead to be restored.

Once the desired leads have been selected, click the
`⚙️ Actions`{.interpreted-text role="guilabel"} drop-down menu at the
top of the `Leads`{.interpreted-text role="guilabel"} page. From the
`⚙️ Actions`{.interpreted-text role="guilabel"} drop-down menu, select
`Unarchive`{.interpreted-text role="guilabel"}.

Doing so removes those selected leads from the `Leads`{.interpreted-text
role="guilabel"} page because they no longer fit the
`Lost`{.interpreted-text role="guilabel"} filter criteria. Delete the
`Lost`{.interpreted-text role="guilabel"} filter from the
`Search...`{.interpreted-text role="guilabel"} bar to reveal these
newly-restored leads.

::: {.seealso}
`../performance/win_loss`{.interpreted-text role="doc"}
:::
