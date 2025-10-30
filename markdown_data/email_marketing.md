# File: /content/odoo_doc17.0/fr/content/applications/marketing/email_marketing.md

show-content

:   

Email Marketing
===============

The Odoo *Email Marketing* app provides drag-and-drop design tools,
pre-built templates, and other interactive features to create engaging
email campaigns. The *Email Marketing* app also provides\| detailed
reporting metrics to track the campaigns\' overall effectiveness.

::: {.seealso}
[Odoo Tutorial: Email
Marketing](https://www.odoo.com/slides/slide/email-marketing-essentials-989?fullscreen=1)
:::

::: {.cards}
::: {.card target="email_marketing/mailing_lists"}
Mailing lists

Silo contacts into specific mailing lists.
:::

::: {.card target="email_marketing/unsubscriptions"}
Manage unsubscriptions (Blacklist)

Allow recipients to unsubscribe and blacklist from future mailings.
:::

::: {.card target="email_marketing/lost_leads_email"}
Lost leads reactivation email

Target lost leads with Email Marketing.
:::

::: {.card target="email_marketing/analyze_metrics"}
Analyze Metrics

Analyzing campaign metrics.
:::
:::

Email marketing dashboard
-------------------------

After installing the application, click the
`Email Marketing`{.interpreted-text role="menuselection"} app icon from
the main Odoo dashboard. Doing so reveals the main
`Mailings`{.interpreted-text role="guilabel"} dashboard in the default
list view.

{.align-center}

In the search bar, the default filter of `My Mailings`{.interpreted-text
role="guilabel"} is present to show all the mailings related to the
current user. To remove that filter, click the
`✖️ (remove)`{.interpreted-text role="guilabel"} icon next to the filter
in the search bar. Doing so reveals all the mailings in the database.

The information on the `Mailings`{.interpreted-text role="guilabel"}
dashboard has four different view options, located in the upper-right
corner as individual icons.

The view options, from left-to-right, are:

-   `List <email_marketing/list-view>`{.interpreted-text role="ref"}
    (default view)
-   `Kanban <email_marketing/kanban-view>`{.interpreted-text role="ref"}
-   `Calendar <email_marketing/calendar-view>`{.interpreted-text
    role="ref"}
-   `Graph <email_marketing/graph-view>`{.interpreted-text role="ref"}

### List view {#email_marketing/list-view}

The list view, represented by the
`☰ (horizontal lines)`{.interpreted-text role="guilabel"} icon in the
upper-right corner, is the default view of the
`Mailings`{.interpreted-text role="guilabel"} dashboard in the
`Email Marketing`{.interpreted-text role="guilabel"} app.

While in list view, there are columns dedicated to different aspects of
information related to the listed emails. Those columns are as follows:

-   `Date`{.interpreted-text role="guilabel"}: the date the email was
    sent.
-   `Subject`{.interpreted-text role="guilabel"}: the subject of the
    email.
-   `Responsible`{.interpreted-text role="guilabel"}: the user who
    created the email, or the user who has been assigned to the email.
-   `Sent`{.interpreted-text role="guilabel"}: how many times the email
    has been sent.
-   `Delivered (%)`{.interpreted-text role="guilabel"}: percentage of
    sent emails that have been successfully delivered.
-   `Opened (%)`{.interpreted-text role="guilabel"}: percentage of sent
    emails that have been opened by the recipients.
-   `Clicked (%)`{.interpreted-text role="guilabel"}: percentage of sent
    emails that have been clicked by the recipients.
-   `Replied (%)`{.interpreted-text role="guilabel"}: percentage of sent
    emails that have been replied to by the recipients.
-   `Status`{.interpreted-text role="guilabel"}: the status of the email
    (`Draft`{.interpreted-text role="guilabel"},
    `In Queue`{.interpreted-text role="guilabel"}, or
    `Sent`{.interpreted-text role="guilabel"}).

To add or remove columns, click the
`Additional Options (two horizontal lines with dots)`{.interpreted-text
role="guilabel"} icon, located to the far-right of the column titles in
list view. Doing so reveals a drop-down menu of additional column
options.

### Kanban view {#email_marketing/kanban-view}

The Kanban view, represented by the
`(inverted bar graph)`{.interpreted-text role="guilabel"} icon, can be
accessed in the upper-right corner of the `Mailings`{.interpreted-text
role="guilabel"} dashboard in the `Email Marketing`{.interpreted-text
role="guilabel"} app.

{.align-center}

While in Kanban view, the email information is displayed in the various
stages.

The stages are: `Draft`{.interpreted-text role="guilabel"},
`In Queue`{.interpreted-text role="guilabel"},
`Sending`{.interpreted-text role="guilabel"}, and
`Sent`{.interpreted-text role="guilabel"}.

-   `Draft`{.interpreted-text role="guilabel"}: the email is still being
    written/created.
-   `In Queue`{.interpreted-text role="guilabel"}: the email is
    scheduled to be sent at a later date.
-   `Sending`{.interpreted-text role="guilabel"}: the email is currently
    being sent to its recipients.
-   `Sent`{.interpreted-text role="guilabel"}: the email has already
    been sent to its recipients.

In each stage, there are drag-and-drop cards representing the emails
that have been created/sent, and the stage they are in represents the
current status of that mailing.

Each card on the `Mailings`{.interpreted-text role="guilabel"} dashboard
provides key information related to that specific email.

When the cursor hovers over the upper-right corner of an email campaign
card, a `⋮ (three
vertical dots)`{.interpreted-text role="guilabel"} icon appears. When
clicked, a mini drop-down menu reveals the option to color-code the
email, `Delete`{.interpreted-text role="guilabel"} the email, or
`Archive`{.interpreted-text role="guilabel"} the message for potential
future use.

{.align-center}

### Calendar view {#email_marketing/calendar-view}

The calendar view, represented by a `📆 (calendar)`{.interpreted-text
role="guilabel"} icon, can be accessed in the upper-right corner of the
`Mailings`{.interpreted-text role="guilabel"} dashboard in the
`Email Marketing`{.interpreted-text role="guilabel"} app.

While in calendar view, a monthly calendar (by default), shows when the
mailings have been sent or are scheduled to be sent.

{.align-center}

The current date is represented by a `🔴 (red circle)`{.interpreted-text
role="guilabel"} icon over the date on the calendar.

To the right of the calendar, the options to filter the results by
`Responsible`{.interpreted-text role="guilabel"} and/or
`Status`{.interpreted-text role="guilabel"} are available, via
checkboxes.

::: {.tip}
::: {.title}
Tip
:::

To hide the right sidebar, click the `(panel-right)`{.interpreted-text
role="guilabel"} icon, located above the sidebar.
:::

In the top-left corner, above the calendar, the option to change the
time period being displayed is available via a drop-down menu, which
shows `Month`{.interpreted-text role="guilabel"}, by default. When
clicked, the drop-down menu that appears reveals the options:
`Day`{.interpreted-text role="guilabel"}, `Week`{.interpreted-text
role="guilabel"}, `Month`{.interpreted-text role="guilabel"} (default),
`Year`{.interpreted-text role="guilabel"}, and
`Show weekends`{.interpreted-text role="guilabel"} (selected by
default).

Clicking any of those options changes the calendar display to reflect
that desired amount of time.

Clicking either `⬅️ (left arrow)`{.interpreted-text role="guilabel"}
icon or `➡️ (right arrow)`{.interpreted-text role="guilabel"} icon
changes the calendar to a previous or future time, depending on what is
clicked, based on the chosen amount of time being represented.

To jump back to the current date, click the `Today`{.interpreted-text
role="guilabel"} button.

### Graph view {#email_marketing/graph-view}

The graph view, represented by a `(line graph)`{.interpreted-text
role="guilabel"} icon, can be accessed in the upper-right corner of the
`Mailings`{.interpreted-text role="guilabel"} dashboard in the
`Email Marketing`{.interpreted-text role="guilabel"} app.

While in graph view, the status of the emails on the
`Mailings`{.interpreted-text role="guilabel"} page is represented in a
bar graph, but other graph view options can be implemented, if needed.

{.align-center}

In the upper-left corner, above the graph, there is a
`Measures`{.interpreted-text role="guilabel"} drop-down menu. When
clicked, different filter options become available to further customize
the graph views.

Those `Measures`{.interpreted-text role="guilabel"} options are:
`A/B Testing percentage`{.interpreted-text role="guilabel"} and
`Count`{.interpreted-text role="guilabel"} (default).

To the right of the `Measures`{.interpreted-text role="guilabel"}
drop-down menu is an `Insert in Spreadsheet`{.interpreted-text
role="guilabel"} button, if the *Documents* application is installed.
When clicked, a pop-up window appears, in which the ability to add the
graph to a spreadsheet or dashboard becomes available.

Beside the `Measures`{.interpreted-text role="guilabel"} drop-down menu
and `Insert in Spreadsheet`{.interpreted-text role="guilabel"} button
are different graph view options. From left-to-right, those graph view
options are: `(bar
chart)`{.interpreted-text role="guilabel"} (default),
`(line chart)`{.interpreted-text role="guilabel"}, and
`(pie chart)`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Each graph view option provides its own series of additional view
options, which appear to the right of the selected graph view option.
:::

### Search options

Regardless of the view chosen for the `Mailings`{.interpreted-text
role="guilabel"} dashboard in the `Email
Marketing`{.interpreted-text role="guilabel"} app, the
`Filters`{.interpreted-text role="guilabel"},
`Group by`{.interpreted-text role="guilabel"}, and
`Favorites`{.interpreted-text role="guilabel"} options are always
available to further customize the information being displayed.

To access those options, click the `(downward arrow)`{.interpreted-text
role="guilabel"} icon, located to the right of the search bar. Doing so
reveals a drop-down mega menu featuring those filtering and grouping
options.

{.align-center}

These options provide various ways to specify and organize the
information seen on the `Mailings`{.interpreted-text role="guilabel"}
dashboard.

::: {.tabs}
::: {.tab}
Filters

This section of the drop-down mega menu provides different ways to
filter email results being shown on the `Mailings`{.interpreted-text
role="guilabel"} dashboard in the `Email Marketing`{.interpreted-text
role="guilabel"} app.

{.align-center}

The options are: `My Mailings`{.interpreted-text role="guilabel"},
`Sent Date`{.interpreted-text role="guilabel"},
`A/B Tests`{.interpreted-text role="guilabel"},
`A/B Tests to review`{.interpreted-text role="guilabel"},
`Archived`{.interpreted-text role="guilabel"}, and
`Add Custom Filter`{.interpreted-text role="guilabel"}.

If `Add Custom Filter`{.interpreted-text role="guilabel"} is selected,
Odoo reveals a pop-up window, with three customizable fields to fill in,
in order to create custom filter rules for Odoo to use to retrieve
results that fit more specific criteria.

{.align-center}
:::

::: {.tab}
Group By

This section of the drop-down mega menu provides different ways to group
email results being shown on the `Mailings`{.interpreted-text
role="guilabel"} dashboard in the `Email Marketing`{.interpreted-text
role="guilabel"} app.

{.align-center}

Using this section, the data can be grouped by the messages\'
`Status`{.interpreted-text role="guilabel"}, or who it was
`Sent By`{.interpreted-text role="guilabel"}.

There is also the option to group the data by
`Sent Period`{.interpreted-text role="guilabel"}, which has its own
sub-menu of options to choose from. The `Sent Period`{.interpreted-text
role="guilabel"} options are `Year`{.interpreted-text role="guilabel"},
`Quarter`{.interpreted-text role="guilabel"}, `Month`{.interpreted-text
role="guilabel"}, `Week`{.interpreted-text role="guilabel"}, and
`Day`{.interpreted-text role="guilabel"}.

If none of the above `Group By`{.interpreted-text role="guilabel"}
options deliver the desired results, click
`Add Custom Group`{.interpreted-text role="guilabel"} at the bottom of
the `Group By`{.interpreted-text role="guilabel"} section. Doing so
reveals a drop-down menu, wherein custom criteria can be selected and
applied, thus delivering any grouping of data that may be desired.
:::

::: {.tab}
Favorites

This section provides the opportunity to save custom filters and/or
groupings for future use. To utilize this section, click the
`Save current search`{.interpreted-text role="guilabel"} field, which
reveals additional fields.

{.align-center}

Give the favorited filter/grouping a title on the blank line above the
checkboxes for `Default filter`{.interpreted-text role="guilabel"} and
`Shared`{.interpreted-text role="guilabel"}.

Ticking the box for `Default filter`{.interpreted-text role="guilabel"}
makes this favorited filter/grouping the default option. Ticking the box
for `Shared`{.interpreted-text role="guilabel"} allows other users to
see and use this favorited filter/grouping.

When all desired options are configured, click `Save`{.interpreted-text
role="guilabel"} to save the filter/grouping in the
`Favorites`{.interpreted-text role="guilabel"} section of the mega
drop-down menu.
:::
:::

Settings
--------

To view and modify the *Email Marketing* settings, navigate to
`Email Marketing app
--> Configuration --> Settings`{.interpreted-text role="menuselection"}.

{.align-center}

On the `Settings`{.interpreted-text role="guilabel"} page, there are
four features available.

{.align-center}

The features are:

-   `Mailing Campaigns`{.interpreted-text role="guilabel"}: enables the
    option to manage mass mailing campaigns.
-   `Blacklist Option when Unsubscribing`{.interpreted-text
    role="guilabel"}: allows recipients to blacklist themselves from
    future mailings during the unsubscribing process.
-   `Dedicated Server`{.interpreted-text role="guilabel"}: provides the
    option to utilize a separate, dedicated server for mailings. When
    enabled, Odoo reveals a new field (and link), in which the specific
    server configurations must be entered, in order for it to connect
    properly to Odoo.
-   `24H Stat Mailing Reports`{.interpreted-text role="guilabel"}:
    allows users to check how well mailings have performed a day after
    it has been sent.

Create an email {#email_marketing/create_email}
---------------

To create an email, open the `Email Marketing`{.interpreted-text
role="menuselection"} application, and click the `New`{.interpreted-text
role="guilabel"} button in the upper-left corner of the
`Mailings`{.interpreted-text role="guilabel"} dashboard page.

Clicking `New`{.interpreted-text role="guilabel"} reveals a blank email
form.

{.align-center}

On the email form, there are fields for the
`Subject <email_marketing/subject>`{.interpreted-text role="ref"} and
`Recipients <email_marketing/recipients>`{.interpreted-text role="ref"}
of the email.

Beneath that, there are three tabs:
`Mail Body <email_marketing/mail_body>`{.interpreted-text role="ref"},
`A/B Tests
<email_marketing/ab_tests>`{.interpreted-text role="ref"}, and
`Settings <email_marketing/settings_tab>`{.interpreted-text role="ref"}.

### Subject {#email_marketing/subject}

First, enter a `Subject`{.interpreted-text role="guilabel"} to the
email. The `Subject`{.interpreted-text role="guilabel"} is visible in
the recipients\' inbox, allowing them to quickly see what the message is
about.

::: {.note}
::: {.title}
Note
:::

The `Subject`{.interpreted-text role="guilabel"} field is mandatory. An
email can **not** be sent without a `Subject`{.interpreted-text
role="guilabel"}.
:::

The `(smiley face with a plus sign)`{.interpreted-text role="guilabel"}
icon at the end of the `Subject`{.interpreted-text role="guilabel"}
field represents emojis that can be added to the
`Subject`{.interpreted-text role="guilabel"} field. Clicking that icon
reveals a pop-up menu of emojis that can be used.

Beside the `(smiley face with a plus sign)`{.interpreted-text
role="guilabel"} icon at the end of the `Subject`{.interpreted-text
role="guilabel"} field is an empty `(star)`{.interpreted-text
role="guilabel"} icon. When clicked, the `(star)`{.interpreted-text
role="guilabel"} icon turns gold, and the email is saved as a template
in the `Mail Body`{.interpreted-text role="guilabel"} tab, which can be
used again in the future.

### Recipients {#email_marketing/recipients}

Beneath the `Subject`{.interpreted-text role="guilabel"} field on the
email form is the `Recipients`{.interpreted-text role="guilabel"} field.
In this field, select the recipients of the email. By default, the
`Mailing List`{.interpreted-text role="guilabel"} option is selected,
but clicking the field reveals a drop-down menu of other recipient
options.

With the default `Mailing List`{.interpreted-text role="guilabel"}
option selected, a specific mailing list **must** be chosen from the
adjacent `Select mailing lists`{.interpreted-text role="guilabel"} field
drop-down menu.

::: {.tip}
::: {.title}
Tip
:::

More than one mailing list can be chosen from the
`Select mailing lists`{.interpreted-text role="guilabel"} field.
:::

Odoo then sends the email to contacts on that specific mailing list(s).

::: {.seealso}
`email_marketing/mailing_lists`{.interpreted-text role="doc"}
:::

When the `Recipients`{.interpreted-text role="guilabel"} field is
clicked, a drop-down menu of other options is revealed. Each option
provides different ways Odoo can create a target audience for the email.

{.align-center}

Those options (excluding the default `Mailing List`{.interpreted-text
role="guilabel"}) provide the option to create a more specified
recipient filter, in an equation-like format, which appears beneath the
`Recipients`{.interpreted-text role="guilabel"} field.

The `Recipients`{.interpreted-text role="guilabel"} field options, other
than the default `Mailing List`{.interpreted-text role="guilabel"}
option, are as follows:

-   `Contact`{.interpreted-text role="guilabel"}: ties specifically to
    the *Contacts* app, and includes all the contacts entered in the
    database.
-   `Event Registration`{.interpreted-text role="guilabel"}: ties
    specifically to the *Events* app, and provides opportunities to
    interact with event registrants, in order to communicate important
    information about the event(s), or nurture other valuable actions,
    such as post-event surveys, purchases, etc.
-   `Lead/Opportunity`{.interpreted-text role="guilabel"}: ties
    specifically to records in the *CRM* application, which opens up a
    number of opportunities to influence sales or purchase decisions.
-   `Mailing Contact`{.interpreted-text role="guilabel"}: ties
    specifically to the *Email Marketing* app, and focuses on specific
    mailing contacts that have been entered in that specific
    application, and are related to a specific mailing list. These
    contacts are also unique because they do *not* have their own
    contact card in the *Contacts* application. This list can be
    accessed by navigating to
    `Email Marketing app --> Mailing Lists --> Mailing List Contacts`{.interpreted-text
    role="menuselection"}.
-   `Sales Order`{.interpreted-text role="guilabel"}: ties specifically
    to the *Sales* app, and focuses on a specific sales orders in the
    database.

#### Add recipient filter

To add a more specific recipient filter to any
`Recipient`{.interpreted-text role="guilabel"} option, select any
recipient option (other than `Mailing List`{.interpreted-text
role="guilabel"}), and click the `Modify filter (right-facing
arrow)`{.interpreted-text role="guilabel"} icon beneath the
`Recipient`{.interpreted-text role="guilabel"} field to reveal three
subsequent filter rule fields, formatted like an equation.

It is highly recommended that users implement detailed targeting
criteria for the `Recipients`{.interpreted-text role="guilabel"} field.
Typically, a single line of targeting logic is not sufficient enough for
an email campaign.

While the `Mailing List`{.interpreted-text role="guilabel"} option is
adequate for the `Recipients`{.interpreted-text role="guilabel"} field,
the `Lead/Opportunity`{.interpreted-text role="guilabel"} and
`Event Registration`{.interpreted-text role="guilabel"} options provide
far more detailed targeting criteria, which can be added on top of those
seed sources.

::: {.example}
For example, with the `Lead/Opportunity`{.interpreted-text
role="guilabel"} option chosen in the `Recipients`{.interpreted-text
role="guilabel"} field, users can add various custom criteria related to
`Created on`{.interpreted-text role="guilabel"} dates,
`Stages`{.interpreted-text role="guilabel"}, `Tags`{.interpreted-text
role="guilabel"}, `Lost Reasons`{.interpreted-text role="guilabel"},
`Sales Teams`{.interpreted-text role="guilabel"},
`Active`{.interpreted-text role="guilabel"} statuses,
`Country`{.interpreted-text role="guilabel"}, and so much more.

{.align-center}
:::

To reveal the sub-menu options within the filter rule fields, click each
field, and make the desired selections, until the preferred
configuration has been achieved.

The number of `records`{.interpreted-text role="guilabel"} in the
database that match the configured rule(s) are indicated beneath the
configured filter rule(s), in green.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Some sub-menu options in the first rule field allow for a second choice
to provide even more specificity.
:::

To the right of each rule, there are three additional options,
represented by `➕ (plus
sign)`{.interpreted-text role="guilabel"}, `(sitemap)`{.interpreted-text
role="guilabel"}, and `🗑️ (trash)`{.interpreted-text role="guilabel"}
icons.

-   The `➕ (plus sign)`{.interpreted-text role="guilabel"} icon adds a
    new node (line) to the overall targeting logic.
-   The `(sitemap)`{.interpreted-text role="guilabel"} icon adds a
    branch to the node. A branch contains two additional, indented
    sub-nodes that are related to that specific rule, providing even
    more specificity to the parent line above it.
-   The `🗑️ (trash)`{.interpreted-text role="guilabel"} icon deletes a
    specific node (line) in the array of logic.

### Mail Body tab {#email_marketing/mail_body}

In the `Mail Body`{.interpreted-text role="guilabel"} tab, there are a
number of pre-configured message templates to choose from.

{.align-center}

Select the desired template, and proceed to modify every element of its
design details with Odoo\'s drag-and-drop building blocks, which appear
on the right sidebar when a template is chosen.

{.align-center}

The features on the sidebar used to create and customize emails are
separated into three sections: `Blocks`{.interpreted-text
role="guilabel"}, `Customize`{.interpreted-text role="guilabel"}, and
`Design`{.interpreted-text role="guilabel"}.

Each building block provides unique features and professional design
elements. To use a building block, drag-and-drop the desired block
element onto the body of the email being built. Once dropped, various
aspects of the building block can be customized.

::: {.tip}
::: {.title}
Tip
:::

To build an email from the ground up, without any building block
elements, select the `Plain Text`{.interpreted-text role="guilabel"}
template. When selected, Odoo provides a completely blank email canvas,
which can be customized in a number of way using the front-end rich text
editor that accepts forward slash [/]{.title-ref} commands.

When [/]{.title-ref} is typed into the blank body of the email, while
using a `Plain Text`{.interpreted-text role="guilabel"} template, a
drop-down menu of various design elements appears, which can be used to
create the desired email design.

{.align-center}
:::

### A/B Tests tab {#email_marketing/ab_tests}

Initially, when the `A/B Tests`{.interpreted-text role="guilabel"} tab
is opened on an email form, the only option available is
`Allow A/B Testing`{.interpreted-text role="guilabel"}. This is **not**
a required option.

If this option is enabled, recipients are only mailed *once* for the
entirety of the campaign.

This allows the user to send different versions of the same mailing to
randomly selected recipients to gauge the effectiveness of various
designs, formats, layouts, content, and so on \-- without any duplicate
messages being sent.

When the checkbox beside `Allow A/B Testing`{.interpreted-text
role="guilabel"} is ticked, an `on (%)`{.interpreted-text
role="guilabel"} field appears, in which the user determines the
percentage of the pre-configured recipients that are going to be sent
this current version of the mailing as part of the test.

::: {.note}
::: {.title}
Note
:::

The default figure in the `on (%)`{.interpreted-text role="guilabel"}
field is [10]{.title-ref}, but that figure can be changed at any time.
:::

Beneath that, two additional fields appear:

The `Winner Selection`{.interpreted-text role="guilabel"} field provides
a drop-down menu of options, wherein the user decides what criteria
should be used to determine the \"winning\" version of the email tests
that are sent.

The options in the `Winner Selection`{.interpreted-text role="guilabel"}
field are as follows:

-   `Manual`{.interpreted-text role="guilabel"}: allows the user to
    determine the \"winning\" version of the mailing. This option
    removes the `Send Final On`{.interpreted-text role="guilabel"}
    field.
-   `Highest Open Rate`{.interpreted-text role="guilabel"} (default):
    the mailing with the highest open rate is determined to be the
    \"winning\" version.
-   `Highest Click Rate`{.interpreted-text role="guilabel"}: the mailing
    with the highest click rate is determined to be the \"winning\"
    version.
-   `Highest Reply Rate`{.interpreted-text role="guilabel"}: the mailing
    with the highest reply rate is determined to be the \"winning\"
    version.
-   `Leads`{.interpreted-text role="guilabel"}: the mailing with the
    most leads generated is determined to be the \"winning\" version.
-   `Quotations`{.interpreted-text role="guilabel"}: the mailing with
    the most quotations generated is determined to be the \"winning\"
    version.
-   `Revenues`{.interpreted-text role="guilabel"}: the mailing with the
    most revenue generated is determined to be the \"winning\" version.

The `Send Final On`{.interpreted-text role="guilabel"} field allows
users to choose a date that is used to know *when* Odoo should determine
the \"winning\" email, and subsequently, send that version of the email
to the remaining recipients.

{.align-center}

To the right of those fields is a
`Create an Alternative Version`{.interpreted-text role="guilabel"}
button. When clicked, Odoo presents a new `Mail Body`{.interpreted-text
role="guilabel"} tab for the user to create an alternate version of the
email to test.

### Settings tab {#email_marketing/settings_tab}

The options present in the `Settings`{.interpreted-text role="guilabel"}
tab of the mail form are divided into two sections:
`Email Content`{.interpreted-text role="guilabel"} and
`Tracking`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The options available in the `Settings`{.interpreted-text
role="guilabel"} tab vary depending on if the *Mailing Campaigns*
feature is activated in `Email Marketing --> Configuration -->
Settings`{.interpreted-text role="menuselection"}. See
`email_marketing/mailing-campaigns`{.interpreted-text role="ref"} for
more information.
:::

Without the *Mailing Campaigns* feature activated, the
`Settings`{.interpreted-text role="guilabel"} tab on the email form only
contains the `Preview Text`{.interpreted-text role="guilabel"},
`Send From`{.interpreted-text role="guilabel"},
`Reply To`{.interpreted-text role="guilabel"},
`Attachments`{.interpreted-text role="guilabel"}, and
`Responsible`{.interpreted-text role="guilabel"} fields.

{.align-center}

#### Email content

-   `Preview Text`{.interpreted-text role="guilabel"}: allows the user
    to enter a preview sentence to encourage recipients to open the
    email. In most inboxes, this is displayed next to the subject. If
    left empty, the first characters of the email content appear,
    instead. The ability to add an emoji in this field is available, as
    well, via the `(smiley face with a plus sign)`{.interpreted-text
    role="guilabel"} icon.
-   `Send From`{.interpreted-text role="guilabel"}: designate an email
    alias that displays as the sender of this particular email.
-   `Reply To`{.interpreted-text role="guilabel"}: designate an email
    alias to whom all the replies of this particular email are sent.
-   `Attach a file`{.interpreted-text role="guilabel"}: if any specific
    files are required (or helpful) for this email, click the
    `Attachments`{.interpreted-text role="guilabel"} button, and upload
    the desired file(s) to the email.

#### Tracking

-   `Responsible`{.interpreted-text role="guilabel"}: designate a user
    in the database to be responsible for this particular email.

::: {.note}
::: {.title}
Note
:::

If the *Mailing Campaign* feature *is* activated, an additional
`Campaign`{.interpreted-text role="guilabel"} field appears in the
`Tracking`{.interpreted-text role="guilabel"} section of the
`Settings`{.interpreted-text role="guilabel"} tab.

{.align-center}

The additional `Campaign`{.interpreted-text role="guilabel"} field
allows users to attach this particular email to a mailing campaign, if
desired.

If the desired campaign is not available in the initial drop-down menu,
select `Search
More`{.interpreted-text role="guilabel"} to reveal a complete list of
all mailing campaigns in the database.

Or, type the name of the desired mailing campaign in the
`Campaign`{.interpreted-text role="guilabel"} field, until Odoo reveals
the desired campaign in the drop-down menu. Then, select the desired
campaign.
:::

Send, schedule, test
--------------------

Once the mailing is finalized, the following options can be utilized,
via buttons located in the upper-left corner of the email form:
`Send <email_marketing/send>`{.interpreted-text role="ref"}, `Schedule
<email_marketing/schedule>`{.interpreted-text role="ref"}, and
`Test <email_marketing/test>`{.interpreted-text role="ref"}.

### Send {#email_marketing/send}

The `Send`{.interpreted-text role="guilabel"} button reveals a
`Ready to unleash emails?`{.interpreted-text role="guilabel"} pop-up
window.

{.align-center}

When the `Send to all`{.interpreted-text role="guilabel"} button is
clicked, Odoo sends the email to the desired recipients. Once Odoo has
sent the mailing, the status changes to `Sent`{.interpreted-text
role="guilabel"}.

### Schedule {#email_marketing/schedule}

The `Schedule`{.interpreted-text role="guilabel"} button reveals a
`When do you want to send your mailing?`{.interpreted-text
role="guilabel"} pop-up window.

{.align-center}

In this pop-up window, click the `Send on`{.interpreted-text
role="guilabel"} field to reveal a calendar pop-up window.

{.align-center}

From the calendar pop-up window, select the future date and time for
Odoo to send this email. Then, click `✔️ Apply`{.interpreted-text
role="guilabel"}. When a date and time are chosen, click the
`Schedule`{.interpreted-text role="guilabel"} button, and the status of
the mailing changes to `In Queue`{.interpreted-text role="guilabel"}.

### Test {#email_marketing/test}

The `Test`{.interpreted-text role="guilabel"} button reveals a
`Test Mailing`{.interpreted-text role="guilabel"} pop-up window.

{.align-center}

From this pop-up window, enter the email addresses of the contacts to
whom Odoo should send this test email in the
`Recipients`{.interpreted-text role="guilabel"} field. Multiple contacts
can be added in this field, if desired.

Once all the desired email addresses have been entered in the
`Recipients`{.interpreted-text role="guilabel"} field, click the
`Send Test`{.interpreted-text role="guilabel"} button.

::: {.warning}
::: {.title}
Warning
:::

By default, there\'s a daily limit applied for **all emails** sent
throughout **all applications**. So, if there are remaining emails to be
sent after a limit has been reached, those mailings are **not** sent
automatically the next day. The sending needs to be forced, by opening
the email and clicking `Retry`{.interpreted-text role="guilabel"}.
:::

Mailing campaigns {#email_marketing/mailing-campaigns}
-----------------

The *Email Marketing* application provides users with the ability to
build mailing campaigns.

In order to create and customize mailing campaigns, the *Mailing
Campaigns* feature **must** be activated in the *Settings* page of the
*Email Marketing* application. To do that, navigate to
`Email Marketing app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, tick the box beside
`Mailing Campaigns`{.interpreted-text role="guilabel"}, and click the
`Save`{.interpreted-text role="guilabel"} button.

{.align-center}

Once the `Mailing Campaigns`{.interpreted-text role="guilabel"} feature
is activated, a new `Campaigns`{.interpreted-text role="guilabel"} menu
option appears in the header.

When that is clicked, Odoo reveals a separate
`Campaigns`{.interpreted-text role="guilabel"} page, displaying all the
mailing campaigns in the database, and the current stage they are in,
showcased in a default Kanban view.

{.align-center}

::: {.note}
::: {.title}
Note
:::

This information can also be viewed in a list, by clicking the
`☰ (horizontal lines)`{.interpreted-text role="guilabel"} icon in the
upper-right corner.
:::

Clicking any campaign from the `Campaigns`{.interpreted-text
role="guilabel"} page reveals that campaign\'s form.

There are two different ways to create and customize campaigns in the
*Email Marketing* application, either directly from the
`Campaigns page <email_marketing/campaign-page>`{.interpreted-text
role="ref"} or through the
`Settings tab <email_marketing/campaign-settings>`{.interpreted-text
role="ref"} on an email form.

### Create mailing campaign (from campaigns page) {#email_marketing/campaign-page}

When the *Mailing Campaigns* feature is activated, a new *Campaigns*
option appears in the header of the *Email Marketing* application.
Campaigns can be created directly on the *Campaigns* page in the *Email
Marketing* app.

To do that, navigate to
`Email Marketing app --> Campaigns --> New`{.interpreted-text
role="menuselection"}.

#### Kanban view

When the `New`{.interpreted-text role="guilabel"} button is clicked in
the default Kanban view on the `Campaigns`{.interpreted-text
role="guilabel"} page, a Kanban card appears in the
`New`{.interpreted-text role="guilabel"} stage.

{.align-center}

New campaign cards can also be made by clicking the
`➕ (plus sign)`{.interpreted-text role="guilabel"} at the top of any
Kanban stage on the `Campaigns`{.interpreted-text role="guilabel"} page.

When the new campaign Kanban card appears, the options to enter a
`Campaign Name`{.interpreted-text role="guilabel"}, a
`Responsible`{.interpreted-text role="guilabel"}, and
`Tags`{.interpreted-text role="guilabel"} become readily available.

To add the campaign to the Kanban stage, click the
`Add`{.interpreted-text role="guilabel"} button.

To delete the campaign, click the `🗑️ (trash can)`{.interpreted-text
role="guilabel"} icon.

To further customize the campaign, click the `Edit`{.interpreted-text
role="guilabel"} button, which reveals the campaign form for additional
modifications.

::: {.note}
::: {.title}
Note
:::

A `Campaign Name`{.interpreted-text role="guilabel"} **must** be entered
in the Kanban card, in order for the `Edit`{.interpreted-text
role="guilabel"} button to reveal the campaign form for further
modifications.
:::

#### List view

To enter the list view on the `Campaigns`{.interpreted-text
role="guilabel"} page, click the
`☰ (horizontal lines)`{.interpreted-text role="guilabel"} icon in the
upper-right corner. Doing so reveals all campaign information in a list
format.

{.align-center}

To create a campaign from the `Campaigns`{.interpreted-text
role="guilabel"} page while in list view, click the
`New`{.interpreted-text role="guilabel"} button. Doing so reveals a
blank campaign form.

{.align-center}

From this campaign form, a `Campaign Name`{.interpreted-text
role="guilabel"}, a `Responsible`{.interpreted-text role="guilabel"},
and `Tags`{.interpreted-text role="guilabel"} can be added.

At the top of the form, various metric-related smart buttons can be seen
that showcase specific analytics related to the campaign. Those smart
buttons are: `Revenues`{.interpreted-text role="guilabel"},
`Quotations`{.interpreted-text role="guilabel"},
`Opportunities`{.interpreted-text role="guilabel"}, and
`Clicks`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Once a `Campaign Name`{.interpreted-text role="guilabel"} is entered and
saved, additional buttons appear at the top of the campaign form.

Those additional buttons are: `Send Mailing`{.interpreted-text
role="guilabel"} and `Send SMS`{.interpreted-text role="guilabel"}.
:::

### Campaign form

On the campaign form (after clicking `Edit`{.interpreted-text
role="guilabel"} from the Kanban card, or selecting an existing campaign
from the `Campaigns`{.interpreted-text role="guilabel"} page) there are
additional options and metrics available.

{.align-center}

At the top of the form, various smart buttons can be seen that showcase
specific analytics related to the campaign. Those smart buttons are:
`Revenues`{.interpreted-text role="guilabel"},
`Quotations`{.interpreted-text role="guilabel"},
`Opportunities`{.interpreted-text role="guilabel"}, and
`Clicks`{.interpreted-text role="guilabel"}.

There are also buttons to `Send Mailing`{.interpreted-text
role="guilabel"}, `Send SMS`{.interpreted-text role="guilabel"},
`Add Post`{.interpreted-text role="guilabel"}, and
`Add Push`{.interpreted-text role="guilabel"} (push notification).

::: {.note}
::: {.title}
Note
:::

If the `Send Mailing`{.interpreted-text role="guilabel"} and
`Send SMS`{.interpreted-text role="guilabel"} buttons are not readily
available, enter a `Campaign Name`{.interpreted-text role="guilabel"},
then save (either manually or automatically). Doing so reveals those
buttons.
:::

The status of the campaign can be viewed in the upper-right corner of
the campaign form, as well.

### Create mailing campaign (from settings tab) {#email_marketing/campaign-settings}

To create a new campaign from the `Settings`{.interpreted-text
role="guilabel"} tab of a mailing form, click the
`Campaign`{.interpreted-text role="guilabel"} field, and start typing
the name of the new campaign. Then, select either
`Create "[Campaign Name]"`{.interpreted-text role="guilabel"} or
`Create and edit...`{.interpreted-text role="guilabel"} from the
drop-down menu that appears.

{.align-center}

Select `Create`{.interpreted-text role="guilabel"} to add this new
mailing campaign to the database, and modify its settings in the future.

Select `Create and Edit...`{.interpreted-text role="guilabel"} to add
this new mailing campaign to the database, and reveal a
`Create Campaign`{.interpreted-text role="guilabel"} pop-up window.

{.align-center}

Here, the new mailing campaign can be further customized. Users can
adjust the `Campaign
Name`{.interpreted-text role="guilabel"}, assign a
`Responsible`{.interpreted-text role="guilabel"}, and add
`Tags`{.interpreted-text role="guilabel"}.

Buttons to `Add Post`{.interpreted-text role="guilabel"} or
`Send Push`{.interpreted-text role="guilabel"} (push notifications) are
also available.

There is also a status located in the upper-right corner of the
`Create Campaign`{.interpreted-text role="guilabel"} pop-up window.

When all modifications are ready to be finalized, click
`Save & Close`{.interpreted-text role="guilabel"}. To delete the entire
campaign, click `Discard`{.interpreted-text role="guilabel"}.

::: {.seealso}
\- `email_marketing/mailing_lists`{.interpreted-text role="doc"} -
`email_marketing/unsubscriptions`{.interpreted-text role="doc"} -
`email_marketing/lost_leads_email`{.interpreted-text role="doc"} -
`email_marketing/analyze_metrics`{.interpreted-text role="doc"}
:::

::: {.toctree titlesonly=""}
email\_marketing/mailing\_lists email\_marketing/unsubscriptions
email\_marketing/lost\_leads\_email email\_marketing/analyze\_metrics
:::
