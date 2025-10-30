Manage sales teams
==================

The *Sales Teams* feature within Odoo\'s *CRM* app allows for the
creation and management of multiple sales teams, each with their own
assignment rules, invoicing targets, and roster of salespeople.

Create a sales team
-------------------

To create a new sales team, go to
`CRM app --> Configuration --> Sales Teams`{.interpreted-text
role="menuselection"}, then click `New`{.interpreted-text
role="guilabel"}.

On the blank sales team form, enter a name in the
`Sales Team`{.interpreted-text role="guilabel"} field.

Next, select a `Team Leader`{.interpreted-text role="guilabel"} from the
drop-down list.

Set an `Email Alias`{.interpreted-text role="guilabel"} to automatically
generate a lead/opportunity for this sales team whenever a message is
sent to that unique email address. Choose whether to accept emails from
`Everyone`{.interpreted-text role="guilabel"},
`Authenticated Partners`{.interpreted-text role="guilabel"},
`Followers Only`{.interpreted-text role="guilabel"}, or
`Authenticated Employees`{.interpreted-text role="guilabel"}.

Select a `Company`{.interpreted-text role="guilabel"} from the drop-down
menu to assign this team to.

::: {.note}
::: {.title}
Note
:::

The `Company`{.interpreted-text role="guilabel"} field is only visible
in multi-company databases, and is not required.
:::

{.align-center}

::: {.note}
::: {.title}
Note
:::

If the *Sales* app is installed on the database, an
`Invoicing Target`{.interpreted-text role="guilabel"} field appears on
the sales team form. This is the revenue target for the current month.
The amount entered in this field is used to populate the invoicing
progress bar on the `sales team dashboard
<crm/sales-team-dashboard>`{.interpreted-text role="ref"}.
:::

### Add sales team members

To add team members, click `Add`{.interpreted-text role="guilabel"}
under the `Members`{.interpreted-text role="guilabel"} tab when editing
the sales team\'s configuration page. This opens a
`Create Sales Team Members`{.interpreted-text role="guilabel"} pop-up
window.

::: {.note}
::: {.title}
Note
:::

If the `Rule-Based Assignment`{.interpreted-text role="guilabel"}
feature has **not** been enabled on the *CRM* app\'s *Settings* page,
clicking `Add`{.interpreted-text role="guilabel"} under the
`Members`{.interpreted-text role="guilabel"} tab opens an
`Add: Salespersons`{.interpreted-text role="guilabel"} pop-up window.
Tick the checkbox to the far-left of the salesperson to be added to the
team, then click `Select`{.interpreted-text role="guilabel"}.

{.align-center}
:::

Select a user from the `Salesperson`{.interpreted-text role="guilabel"}
drop-down list to add them to the team. To prevent this salesperson from
being automatically assigned leads, tick the
`Skip auto assignment`{.interpreted-text role="guilabel"} checkbox. If
this feature is activated, the salesperson can still be assigned leads
manually.

{.align-center}

The `Leads (30 days)`{.interpreted-text role="guilabel"} field tracks
how many leads the salesperson has been assigned in the past thirty days
for this team, and the maximum number of leads they should be assigned.
To edit the maximum number of leads this salesperson can be assigned,
enter that amount in the `Leads
(30 days)`{.interpreted-text role="guilabel"} field.

::: {.tip}
::: {.title}
Tip
:::

`Assignment rules <../track_leads/lead_scoring>`{.interpreted-text
role="doc"} can be configured for individual salespeople using the
`Domain`{.interpreted-text role="guilabel"} section.
:::

Click `Save & Close`{.interpreted-text role="guilabel"} when finished,
or `Save & New`{.interpreted-text role="guilabel"} to add additional
members.

Enable multi teams
------------------

To allow salespeople to be assigned to more than one sales team, the
*Multi Teams* setting needs to be enabled. First, navigate to
`CRM app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Under the `CRM`{.interpreted-text
role="guilabel"} section, tick the checkbox labeled
`Multi Teams`{.interpreted-text role="guilabel"}. Then, click
`Save`{.interpreted-text role="guilabel"} at the top-left of the page.

{.align-center}

Sales team dashboard {#crm/sales-team-dashboard}
--------------------

To view the sales team dashboard, go to
`CRM app --> Sales --> Teams`{.interpreted-text role="menuselection"}.
Any team the user is a member of appears in the dashboard.

{.align-center}

Each Kanban card gives an overview of the sales team\'s open
opportunities, quotations, sales orders, and expected revenue, as well
as a bar graph of new opportunities per week, and an invoicing progress
bar.

Click the `Pipeline`{.interpreted-text role="guilabel"} button to go
directly to that team\'s *CRM* pipeline.

Click on the `fa-ellipsis-v`{.interpreted-text role="icon"}
`(vertical ellipsis)`{.interpreted-text role="guilabel"} icon in the
top-right corner of the Kanban card to open a drop-down menu. Then, to
view or edit the team\'s settings, click
`Configuration`{.interpreted-text role="guilabel"}.

::: {.seealso}
\- `../optimize/utilize_activities`{.interpreted-text role="doc"} -
`../track_leads/lead_scoring`{.interpreted-text role="doc"}
:::
