# File: /content/odoo_doc17.0/fr/content/applications/marketing/marketing_automation.md

show-content

:   

Marketing Automation
====================

Use the Odoo **Marketing Automation** application to create dynamic
campaigns with actions that automatically occur within a defined
duration, such as sending a series of timed mass emails or engaging with
leads based on their interactions with marketing campaigns.

While the application is designed to be user-friendly for creating,
launching, and reviewing marketing campaigns, it also provides advanced
features to automate repetitive tasks throughout the database.

Get started by creating a
`new campaign from scratch <marketing_automation/campaigns>`{.interpreted-text
role="ref"} or start with a
`campaign template <marketing_automation/campaign-templates>`{.interpreted-text
role="ref"}.

::: {.seealso}

:::

::: {.cards}
::: {.card target="marketing_automation/target_audience"}
Audience targeting

Configure the target audience for a campaign.
:::

::: {.card target="marketing_automation/workflow_activities"}
Workflow activities

Define the activities that occur within a campaign.
:::

::: {.card target="marketing_automation/testing_running"}
Testing/running campaigns

Launch a test or run a campaign.
:::

::: {.card target="marketing_automation/understanding_metrics"}
Campaign metrics

Review the metrics of a campaign.
:::
:::

Configuration
-------------

To begin, make sure the **Marketing Automation** application is
`installed <general/install>`{.interpreted-text role="ref"}.

::: {.important}
::: {.title}
Important
:::

Installing the **Marketing Automation** application also installs the
`Email Marketing
<email_marketing>`{.interpreted-text role="doc"} app, as most features
of Odoo **Marketing Automation** are dependent on that specific
application.

Additionally, install the `CRM <../sales/crm>`{.interpreted-text
role="doc"} and `SMS Marketing <sms_marketing>`{.interpreted-text
role="doc"} applications to access *all* of the features available in
**Marketing Automation**.

The following documentation assumes that all three of these dependent
applications are installed on the database.
:::

Campaigns {#marketing_automation/campaigns}
---------

A *campaign* refers to a workflow of activities that are automatically
executed to a target audience, based on predefined filters, triggers,
and durations of activities.

A new campaign can be created from scratch or from a `template
<marketing_automation/campaign-templates>`{.interpreted-text
role="ref"}.

To create a campaign, navigate to the
`Marketing Automation`{.interpreted-text role="menuselection"}
application and click the `New`{.interpreted-text role="guilabel"}
button to reveal a new campaign form.

### Campaign templates {#marketing_automation/campaign-templates}

Odoo provides six campaign templates to help users get started. The
campaign template cards **only** display when there are no existing
campaigns in the database. Once a campaign has been created, the
template cards on the *Campaigns* dashboard are replaced with a Kanban
view of the existing campaigns.

To get started with a template, navigate to the
`Marketing Automation`{.interpreted-text role="menuselection"}
application, from the main Odoo dashboard, to open the
`Campaigns`{.interpreted-text role="guilabel"} dashboard, which displays
six
`campaign template <marketing_automation/campaign_templates>`{.interpreted-text
role="doc"} cards:

-   | `fa-tag`{.interpreted-text role="icon"}
      `Tag Hot Contacts`{.interpreted-text role="guilabel"}
    | `Send a welcome email to contacts and tag them if they click it.`{.interpreted-text
      role="guilabel"}

-   | `fa-hand-peace-o`{.interpreted-text role="icon"}
      `Welcome Flow`{.interpreted-text role="guilabel"}
    | `Send a welcome email to new subscribers, remove the address that bounced.`{.interpreted-text
      role="guilabel"}

-   | `fa-check-square`{.interpreted-text role="icon"}
      `Double Opt-in  <marketing_automation/campaign_templates/double_optin>`{.interpreted-text
      role="doc"}
    | `Send an email to new recipients to confirm their consent.`{.interpreted-text
      role="guilabel"}

-   | `fa-search`{.interpreted-text role="icon"}
      `Commercial prospection`{.interpreted-text role="guilabel"}
    | `Send a free catalog and follow-up according to reactions.`{.interpreted-text
      role="guilabel"}

-   | `fa-phone`{.interpreted-text role="icon"}
      `Schedule Calls`{.interpreted-text role="guilabel"}
    | `If a lead is created for existing contact, schedule a call with their salesperson.`{.interpreted-text
      role="guilabel"}

-   | `fa-star`{.interpreted-text role="icon"}
      `Prioritize Hot leads`{.interpreted-text role="guilabel"}
    | `Send an email to new leads and assign them a high priority if they open it.`{.interpreted-text
      role="guilabel"}



These templates are designed to be used as starting points for creating
new campaigns. Click one of the template cards to open the campaign
form.

::: {.tip}
::: {.title}
Tip
:::

To display the campaign template cards again after a campaign has been
created, type the name of a campaign that does **not** exist in the
database into the search bar, then press `Enter`{.interpreted-text
role="kbd"}.

For example, searching for [empty]{.title-ref} displays the campaign
template cards again, as long as there is not a campaign with the name
\"empty\" in the database.
:::

Targets and filters
-------------------

On the campaign form, the `Target`{.interpreted-text role="guilabel"}
and `Filter`{.interpreted-text role="guilabel"} section, also referred
to as the domain, contains the fields used to define the target audience
for the campaign\'s reach (i.e., the unique contact records in the
database).

The target audience specifies the type of records available for use in
the campaign, such as *Lead/Opportunity*, *Event Registration*,
*Contact*, and more.

### Records

The contacts in the system that fit the specified criteria for a
campaign are referred to as *records*.

The number of records that are displayed next to the campaign
`Filter`{.interpreted-text role="guilabel"} represent the total number
of records the campaign is targeting.

### Participants

The records that are engaged by the campaign are referred to as
*participants*.

The number of participants engaged in a test run are shown in the
*Tests* smart button, which displays on the top of the campaign form
after a test has been run.

The number of participants engaged in a running, or stopped, campaign
are shown in the *Participants* smart button at the top of the campaign
form.

::: {.seealso}
`Audience targeting <marketing_automation/target_audience>`{.interpreted-text
role="doc"}
:::

Workflow
--------

A *workflow* consists of an activity, many activities, or a sequence of
activities organized in a campaign. A campaign\'s workflow is defined in
the `Workflow`{.interpreted-text role="guilabel"} section of the
campaign form.

### Activities

*Activities* are the methods of communication or server actions,
organized in a workflow, that are executed within a campaign. Once
running, each activity displays the number of participants that are
engaged by the activity as *Success* and *Rejected* counts.

To create one of the following activities, click
`Add new activity`{.interpreted-text role="guilabel"} in the
`Workflow`{.interpreted-text role="guilabel"} section of the campaign
form:

-   `Email <marketing_automation/email-activity-type>`{.interpreted-text
    role="ref"}: an email that is sent to the target audience.
-   `Server action <marketing_automation/sa-activity-type>`{.interpreted-text
    role="ref"}: an internal action within the database that is
    executed.
-   `SMS <marketing_automation/sms-activity-type>`{.interpreted-text
    role="ref"}: a text message that is sent to the target audience.

::: {.seealso}
`marketing_automation/workflow_activities`{.interpreted-text role="doc"}
:::

Testing and running
-------------------

Once a campaign has been created, it can be tested to ensure the
workflow is functioning as expected, to check for errors, and correct
any mistakes before it reaches its target audience.

After testing, the campaign can be launched to start engaging the target
audience. The campaign can also be launched *without* testing, if the
user is confident in the workflow.

::: {.seealso}
`marketing_automation/testing_running`{.interpreted-text role="doc"}
:::

Reporting
---------

A range of reporting metrics are available to measure the success of
each campaign. Navigate to
`Marketing Automation app --> Reporting`{.interpreted-text
role="menuselection"} to access the following menu options:

-   `Link Tracker`{.interpreted-text role="guilabel"}: displays the
    metrics of links to track the number of clicks.
-   `Traces`{.interpreted-text role="guilabel"}: displays the results of
    all activities from all campaigns.
-   `Participants`{.interpreted-text role="guilabel"}: displays an
    overview of the participants of all campaigns.

Additionally, each activity within the workflow of a campaign displays
its engagement metrics.

::: {.seealso}
`marketing_automation/understanding_metrics`{.interpreted-text
role="doc"}
:::

::: {.toctree titlesonly=""}
marketing\_automation/target\_audience
marketing\_automation/workflow\_activities
marketing\_automation/testing\_running
marketing\_automation/understanding\_metrics
marketing\_automation/campaign\_templates
:::
