# File: /content/odoo_doc17.0/fr/content/applications/marketing/social_marketing/social_campaigns.md

Social marketing campaigns
==========================

Social marketing campaigns help companies connect directly with the
marketplace. These campaigns are helpful when introducing a new product
to customers, explaining the value of a product or service, or when
advertising an upcoming event or product release.

The most effective social marketing campaigns typically involve multiple
channels to maximize content distribution, and Odoo\'s *Social
Marketing* application acts as a singular control center to monitor,
plan, post, track, and analyze all of the various content and content
channels within a single dashboard.

Campaigns page
--------------

To access a complete overview of all social marketing campaigns, open
the `Social
Marketing`{.interpreted-text role="menuselection"} application, and
click `Campaigns`{.interpreted-text role="menuselection"} from the
header menu. Doing so reveals a separate page with every campaign in a
default kanban view.

{.align-center}

Each *stage* in the kanban view can be edited, by clicking the
`gear icon`{.interpreted-text role="guilabel"} to the left of the
`+ (plus sign)`{.interpreted-text role="guilabel"} - located to the
right of the stage title.

::: {.note}
::: {.title}
Note
:::

The **gear icon** *only* appears when the cursor hovers to the left of
the **+ (plus sign)**. When the gear icon is clicked, a drop-down menu
reveals the options: `Fold`{.interpreted-text role="guilabel"},
`Edit Stage`{.interpreted-text role="guilabel"}, and
`Delete`{.interpreted-text role="guilabel"}.
:::

{.align-center}

Clicking `Fold`{.interpreted-text role="guilabel"} minimizes that
specific stage\'s column. The stage column can be restored by clicking
the folded version of it on the main `Campaigns`{.interpreted-text
role="guilabel"} dashboard in the default kanban view.

Selecting `Edit Stage`{.interpreted-text role="guilabel"} reveals a
pop-up window, in which the name and the sequence of the stage can be
modified. If changes are made, be sure to click `Save`{.interpreted-text
role="guilabel"}.

Clicking `Delete`{.interpreted-text role="guilabel"} removes the stage
entirely.

::: {.note}
::: {.title}
Note
:::

To add a new stage to the pipeline, side-scroll to the right on the
`Campaigns`{.interpreted-text role="guilabel"} dashboard, click
`Add a Column`{.interpreted-text role="guilabel"}, enter in the desired
information, and click `Add`{.interpreted-text role="guilabel"}.
:::

::: {.tip}
::: {.title}
Tip
:::

The same social marketing campaign information on the
`Campaigns`{.interpreted-text role="guilabel"} dashboard can also be
viewed as a list, by selecting the `List`{.interpreted-text
role="guilabel"} option, located under the search bar, in the
upper-right corner.
:::

Create social marketing campaigns
---------------------------------

First, open the `Social Marketing`{.interpreted-text
role="menuselection"} application, and select
`Campaigns`{.interpreted-text role="guilabel"} from the header menu.

On the `Campaigns`{.interpreted-text role="guilabel"} dashboard, a new
campaign can be created by clicking the quick add
`+ (plus sign)`{.interpreted-text role="guilabel"} located in the
top-right corner of each stage in the pipeline, visible in the kanban
view. Campaigns can also be created by clicking
`Create`{.interpreted-text role="guilabel"} in the upper-left corner of
the `Campaigns`{.interpreted-text role="guilabel"} dashboard.

Both options reveal a new campaign detail window directly on the
`Campaigns`{.interpreted-text role="guilabel"} dashboard when clicked.

{.align-center}

Here, the `Campaign Name`{.interpreted-text role="guilabel"},
`Responsible`{.interpreted-text role="guilabel"}, and
`Tags`{.interpreted-text role="guilabel"} can be entered. When all
modifications are complete, click `Add`{.interpreted-text
role="guilabel"} to add the campaign to the database.

Edit social marketing campaigns
-------------------------------

In order to edit a campaign in greater detail, and create/send various
forms of communications related to it, the template page for that
campaign must be accessed and modified, accordingly. There are multiple
ways to access a template page for a campaign.

-   After entering the pertinent information in the
    `Quick Add`{.interpreted-text role="guilabel"} campaign drop-down,
    click `Edit`{.interpreted-text role="guilabel"}.
-   Simply select the desired campaign from the
    `Campaigns`{.interpreted-text role="guilabel"} dashboard in list or
    kanban view.
-   On the `Campaigns`{.interpreted-text role="guilabel"} dashboard in
    the kanban view, select the `⋮ (three dots)`{.interpreted-text
    role="guilabel"} drop-down menu on the desired campaign, and select
    `Edit`{.interpreted-text role="guilabel"}.

Any of the above routes will reveal the *Campaign Template* page for
that specific campaign.

Social marketing campaign templates
-----------------------------------

On a *Campaign Template* page, numerous elements can be
customized/modified, and various forms of communications can be created,
modified, and sent or scheduled. Below is a sample of a completed
campaign template.

{.align-center}

::: {.important}
::: {.title}
Important
:::

In order for the `Send New Mailing`{.interpreted-text role="guilabel"}
option to appear on campaign templates, make sure the *Mailing
Campaigns* feature is enabled in the *Email Marketing* app. To do that,
navigate to
`Email Marketing --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, activate `Mailing
Campaigns`{.interpreted-text role="guilabel"}, and click
`Save`{.interpreted-text role="guilabel"}.
:::

::: {.note}
::: {.title}
Note
:::

In order for the `Send SMS`{.interpreted-text role="guilabel"} option to
appear, the Odoo *SMS Marketing* application must be installed on the
database.
:::

Add content and communications to campaigns
-------------------------------------------

If the proper settings and applications are installed (as instructed
above), there are four forms of communication/content options that can
be added to campaigns. Each of these options are displayed as buttons in
the upper-left corner of the campaign template page.

-   `Send New Mailing`{.interpreted-text role="guilabel"}: reveals a
    blank email template on a separate page, in which the message can be
    fully customized in a variety of ways.
-   `Send SMS`{.interpreted-text role="guilabel"}: reveals a blank SMS
    template on a separate page, in which a SMS communication can be
    created and configured.
-   `Send Social Post`{.interpreted-text role="guilabel"}: reveals a
    blank social post template on a separate page, in which a post can
    be created, and applied to social media accounts that are already
    connected to the database.
-   `Push Notification`{.interpreted-text role="guilabel"}: reveals a
    similar blank social post template on a separate page, however, the
    `Push Notification`{.interpreted-text role="guilabel"} options are
    already pre-selected in the `Post
    on`{.interpreted-text role="guilabel"} field.

Whichever form of communication is created, once it\'s completed, Odoo
returns to the `Campaign Template`{.interpreted-text role="guilabel"}
page, showcasing that new content in its corresponding tab (e.g.
`Mailings`{.interpreted-text role="guilabel"}, `SMS`{.interpreted-text
role="guilabel"}, `Social Media`{.interpreted-text role="guilabel"},
and/or `Push
Notifications`{.interpreted-text role="guilabel"}).

As content and communications are added to a campaign, tabs for those
specific mediums appear, along with a variety of analytical smart
buttons (e.g. `Revenues`{.interpreted-text role="guilabel"},
`Quotations`{.interpreted-text role="guilabel"},
`Leads`{.interpreted-text role="guilabel"}, etc.).

These smart buttons, located at the top of the template, display
different metrics related to the campaign, and its various
communications and content. Clicking any smart button reveals a separate
page dedicated to that particular element of the campaign, allowing for
quicker, more organized analysis.

::: {.note}
::: {.title}
Note
:::

The Odoo *Social Marketing* app is integrated with other Odoo
applications, such as *Sales*, *Invoicing*, *CRM*, and *Website*.
:::
