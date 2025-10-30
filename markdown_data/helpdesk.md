# File: /content/odoo_doc17.0/fr/content/applications/services/helpdesk.md

show-content

:   

show-toc

:   

Helpdesk
========

Odoo *Helpdesk* is a ticketing-based customer support application.
Multiple teams can be configured and managed in one dashboard, each with
their own pipeline for tickets submitted by customers. Pipelines are
organized in customizable stages that enable teams to track, prioritize,
and solve customer issues quickly and efficiently.

Create a Helpdesk team
----------------------

To view or modify *Helpdesk* teams, go to
`Helpdesk app --> Configuration -->
Helpdesk Teams`{.interpreted-text role="menuselection"}. To create a new
team, click the `New`{.interpreted-text role="guilabel"} button in the
top-left of the dashboard.

{.align-center}

On the blank Helpdesk team form, enter a `Name`{.interpreted-text
role="guilabel"} for the new team. Then, enter a description of the team
in the field below the team name, if desired. To change the company this
team is assigned to, select it from the `Company`{.interpreted-text
role="guilabel"} drop-down menu.

::: {.important}
::: {.title}
Important
:::

The team description is published on the public facing `website form
<helpdesk/overview/receiving_tickets>`{.interpreted-text role="doc"},
where customers and portal users submit tickets. The description
included in this field should **not** include any information that is
for internal use only.

{.align-center}
:::

### Visibility & Assignment

The *Visibility* settings alter which internal users and portal users
have access to this team and its tickets. The *Assignment* settings
alter how users are assigned to handle each ticket.

#### Determine team visibility

Under the `Visibility`{.interpreted-text role="guilabel"} section,
select one of the following options to determine who can view this team
and its tickets:

-   `Invited internal users (private)`{.interpreted-text
    role="guilabel"}: internal users can access the team and the tickets
    they are following. This access can be modified on each ticket
    individually by adding or removing the user as a follower. Internal
    users are considered *invited* once they are added as followers to
    an individual ticket, or
    `to the team itself <helpdesk/follow>`{.interpreted-text
    role="ref"}.
-   `All internal users (company)`{.interpreted-text role="guilabel"}:
    all internal users can access the team and all of its tickets.
-   `Invited portal users and all internal users (public)`{.interpreted-text
    role="guilabel"}: all internal users can access the team and all of
    its tickets. Portal users can only access the tickets they are
    following.

::: {.example}
A [Customer Support]{.title-ref} team, meant to handle general shipping
and product issues, would have the visibility set on
`Invited portal users and all internal users`{.interpreted-text
role="guilabel"}.

At the same time, a [Financial Services]{.title-ref} team handling
tickets related to accounting or tax information would only need to be
visible to `Invited internal users`{.interpreted-text role="guilabel"}.
:::

::: {.warning}
::: {.title}
Warning
:::

A team\'s visibility can be altered after the initial configuration.
However, if the team changes from public access to either private or
company-only access, portal users are removed as followers from both the
team, and from individual tickets.
:::

#### Follow all team\'s tickets {#helpdesk/follow}

If a user should be notified about any updates regarding tickets for
this team, select their name from the `Followers`{.interpreted-text
role="guilabel"} drop-down menu, located in the
`Follow All Team's Tickets`{.interpreted-text role="guilabel"} field.
Multiple users can be selected to follow a single team.

::: {.important}
::: {.title}
Important
:::

External contacts can be selected in the `Followers`{.interpreted-text
role="guilabel"} field. If the team\'s visibility is set to
`Invited internal users (private)`{.interpreted-text role="guilabel"},
followers are notified about updates to the team\'s tickets, but are
**not** able to view them in the portal.
:::

#### Automatically assign new tickets

When tickets are received, they need to be assigned to a member of the
team. This is done either manually on each ticket individually, or
through `Automatic Assignment`{.interpreted-text role="guilabel"}. Check
the `Automatic Assignment`{.interpreted-text role="guilabel"} checkbox
to enable this feature for the team.

![View of a Helpdesk team settings page emphasizing the automatic assignment features in Odoo
Helpdesk.](helpdesk/helpdesk-visibility-assignment.png){.align-center}

As soon as `Automatic Assignment`{.interpreted-text role="guilabel"} has
been enabled, additional fields appear.

Select one of the following assignment methods, based on how the
workload should be allocated across the team:

-   `Each user is assigned an equal number of tickets`{.interpreted-text
    role="guilabel"}: tickets are assigned to team members based on
    total ticket count, regardless of the number of open or closed
    tickets they are currently assigned.
-   `Each user has an equal number of open tickets`{.interpreted-text
    role="guilabel"}: tickets are assigned to team members based on how
    many open tickets they are currently assigned.

::: {.note}
::: {.title}
Note
:::

When
`Each user is assigned an equal number of tickets`{.interpreted-text
role="guilabel"} is selected, the overall number of tickets assigned to
team members is the same, but it does **not** consider the current
workload.

When `Each user has an equal number of open tickets`{.interpreted-text
role="guilabel"} is selected, it ensures a balanced workload among team
members, as it takes the current number of active tickets into account.
:::

Finally, add the `Team Members`{.interpreted-text role="guilabel"} who
are to be assigned tickets for this team. Leave the field empty to
include all employees who have the proper assignments and access rights
configured in their user account settings.

::: {.important}
::: {.title}
Important
:::

If an employee has time off scheduled in the *Time Off* application,
they are **not** assigned tickets during that time. If no employees are
available, the system looks ahead until there is a match.
:::

::: {.seealso}
\- `Manage users <users/add-individual>`{.interpreted-text role="ref"} -
`Access rights <../general/users/access_rights>`{.interpreted-text
role="doc"}
:::

Create or modify stages
-----------------------

*Stages* are used to organize the *Helpdesk* pipeline and track the
progress of tickets. Stages are customizable, and can be renamed to fit
the needs of each team.

::: {.important}
::: {.title}
Important
:::

`Developer mode <developer-mode>`{.interpreted-text role="ref"} **must**
be activated to access the stages menu. To activate developer mode, go
to `Settings app --> General Settings --> Developer
Tools`{.interpreted-text role="menuselection"}, and click
`Activate the developer mode`{.interpreted-text role="guilabel"}.
:::

To view or modify *Helpdesk* stages, go to
`Helpdesk app --> Configuration -->
Stages`{.interpreted-text role="menuselection"}.

The default list view on the `Stages`{.interpreted-text role="guilabel"}
page displays the stages currently available in *Helpdesk*. They are
listed in the order they appear in the pipeline.

To change the order of the stages, click the
`oi-draggable`{.interpreted-text role="icon"} `(drag)`{.interpreted-text
role="guilabel"} icon, to the left of the stage name, and drag it to the
desired place on the list.

![View of the stage list page emphasizing the buttons used to change the order the stages
appear in the list.](helpdesk/stages-list-buttons.png){.align-center}

::: {.tip}
::: {.title}
Tip
:::

Change the stage order on the Kanban view of a *Helpdesk* team\'s
pipeline by dragging and dropping individual columns.
:::

To create a new stage, click the `New`{.interpreted-text
role="guilabel"} button at the top-left of the stage list. Doing so
reveals a blank stage form.

Choose a `Name`{.interpreted-text role="guilabel"} for the new stage,
and add a description, if desired. Then, proceed to fill out the
remaining fields following the steps below.

{.align-center}

### Add email and SMS templates to stages

When an `Email Template`{.interpreted-text role="guilabel"} is added to
a stage, an email is automatically sent to the customer when a ticket
reaches that specific stage in the pipeline. Likewise, adding an
`SMS Template`{.interpreted-text role="guilabel"} triggers an SMS text
message to send to the customer.

::: {.important}
::: {.title}
Important
:::

SMS Text Messaging is an
`In-App Purchase (IAP) </applications/essentials/in_app_purchase/>`{.interpreted-text
role="doc"} service that requires prepaid credits to work. Refer to [SMS
Pricing FAQ](https://iap-services.odoo.com/iap/sms/pricing) for
additional information.
:::

To select an existing email template, select it from the
`Email Template`{.interpreted-text role="guilabel"} field. Click on the
`oi-arrow-right`{.interpreted-text role="icon"}
`(right arrow)`{.interpreted-text role="guilabel"} icon to the right of
the field to edit the chosen template.

To create a new template, click the field, and enter a title for the new
template. Then, select `Create and edit`{.interpreted-text
role="guilabel"} from the drop-down menu that appears, and complete the
form details.

Follow the same steps to select, edit, or create an
`SMS Template`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.seealso}
`/applications/general/companies/email_template`{.interpreted-text
role="doc"}
:::

### Assign stages to a team

Make a selection in the `Helpdesk Teams`{.interpreted-text
role="guilabel"} field on the `Stages`{.interpreted-text
role="guilabel"} form. More than one team may be selected, since the
same stage can be assigned to multiple teams.

### Fold a stage

By default, stages are unfolded in the Kanban view of either tickets
dashboard: `My
Tickets`{.interpreted-text role="guilabel"}
(`Helpdesk app --> Tickets --> My Tickets`{.interpreted-text
role="menuselection"}) or `All Tickets`{.interpreted-text
role="guilabel"}
(`Helpdesk app --> Tickets --> All Tickets`{.interpreted-text
role="menuselection"}).

Tickets in an unfolded stage are visible in the pipeline under the stage
name, and are considered *open*.

Stages can be configured to be folded in the Kanban view of a tickets
page (`My Tickets`{.interpreted-text role="guilabel"} or
`All Tickets`{.interpreted-text role="guilabel"}).

The name of the folded stages are still visible, though the tickets in
the stage are no longer immediately visible.

To fold a stage, check the `Folded in Kanban`{.interpreted-text
role="guilabel"} box on the `Stages`{.interpreted-text role="guilabel"}
form.

::: {.warning}
::: {.title}
Warning
:::

Tickets that reach a *folded* stage are considered *closed*. Closing a
ticket before the work is completed can result in reporting and
communication issues. This setting should **only** be enabled for stages
that are considered *closing* stages.
:::

Stages can be temporarily folded in the Kanban view of the tickets
pipeline, as well.

View a specific team\'s pipeline by navigating to
`Helpdesk app`{.interpreted-text role="menuselection"}, and clicking the
team\'s Kanban card.

Select a stage to fold temporarily, then click the
`fa-gear`{.interpreted-text role="icon"} `(gear)`{.interpreted-text
role="guilabel"} icon, and select `Fold`{.interpreted-text
role="guilabel"} from the drop-down menu.

{.align-center}

::: {.important}
::: {.title}
Important
:::

Manually folding a stage from the Kanban view is temporary and does
**not** close the tickets in the stage.
:::

Merge tickets
-------------

If duplicate tickets are found in *Helpdesk*, they can be combined into
a single ticket using the *merge* feature.

::: {.important}
::: {.title}
Important
:::

The *merge* feature is **only** accessible if the `Data Cleaning
<../productivity/data_cleaning>`{.interpreted-text role="doc"}
application is installed on the database.
:::

To merge two or more tickets, navigate to
`Helpdesk app --> Tickets --> All Tickets`{.interpreted-text
role="menuselection"}. Identify the tickets to be merged, and tick the
checkbox at the far-left of each ticket to select them. Then, click the
`fa-cog`{.interpreted-text role="icon"} `Actions`{.interpreted-text
role="guilabel"} icon, and select `Merge`{.interpreted-text
role="guilabel"} from the drop-down menu. Doing so opens a new page
where the selected tickets are listed with their
`Similarity`{.interpreted-text role="guilabel"} rating. From here, click
either `Merge <data_cleaning/merge-records>`{.interpreted-text
role="ref"} to combine the tickets, or `DISCARD`{.interpreted-text
role="guilabel"}.

::: {.seealso}
\- 
:::

::: {.toctree titlesonly=""}
helpdesk/overview helpdesk/advanced
:::
