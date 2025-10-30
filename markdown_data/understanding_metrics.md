# File: /content/odoo_doc17.0/fr/content/applications/marketing/marketing_automation/understanding_metrics.md

Campaign metrics
================

*Campaign metrics* are detailed statistics and analytics within a
marketing campaign, measuring its success and effectiveness. Triggered
marketing activities populate relevant activity blocks with real-time
metrics, in the campaign detail form.

Activity analytics
------------------

In the `Workflow`{.interpreted-text role="guilabel"} section of a
campaign detail form in the *Marketing Automation* app, where the
various campaign activities are located, a collection of useful data can
be found on every individual activity block, like number of
communications `Sent`{.interpreted-text role="guilabel"}, percentage of
messages that have been `Clicked`{.interpreted-text role="guilabel"},
and more.

{.align-center}

To the left of the activity block, the configured
`trigger time <workflow_activities>`{.interpreted-text role="doc"} is
displayed as a duration (either `Hours`{.interpreted-text
role="guilabel"}, `Days`{.interpreted-text role="guilabel"},
`Weeks`{.interpreted-text role="guilabel"}, or
`Months`{.interpreted-text role="guilabel"}) if it corresponds to period
after the workflow begins.

::: {.note}
::: {.title}
Note
:::

If the trigger time is dependent on another activity or triggering
action (e.g. `Mail:
Replied`{.interpreted-text role="guilabel"}, etc.) the time is
displayed, along with the necessary action for that activity to be
activated (e.g. [Replied after 2 Hours]{.title-ref}).

{.align-center}
:::

In the activity block, an icon represents each activity type. An
`✉️ (envelope)`{.interpreted-text role="guilabel"} icon means the
activity is an email. Three tiny, interlocking
`⚙️ (gear)`{.interpreted-text role="guilabel"} icons means the activity
is an internal action. And, a small, basic
`📱 (mobile)`{.interpreted-text role="guilabel"} icon means the activity
is an SMS.

::: {.tip}
::: {.title}
Tip
:::

The activity type name is also displayed in smaller font below the
activity title.
:::

Beside the activity icon, at the top of the activity block, is the title
of the activity. To the right of the activity title, there are
`Edit`{.interpreted-text role="guilabel"} and `Delete`{.interpreted-text
role="guilabel"} buttons.

Click `Edit`{.interpreted-text role="guilabel"} to open the
`Open: Activities`{.interpreted-text role="guilabel"} pop-up form for
that specific activity, in which that activity can be modified. Click
the `Delete`{.interpreted-text role="guilabel"} button to completely
delete that specific activity from the workflow.

::: {.seealso}
`workflow_activities`{.interpreted-text role="doc"}
:::

### Activity graph tab

In every activity block, the `Graph (pie chart icon)`{.interpreted-text
role="guilabel"} tab is open by default, displaying related metrics as a
simple line graph. The success metrics are represented in
[green]{.title-ref} and the rejected metrics are represented in
[red]{.title-ref}.

Numerical representations of both `Success`{.interpreted-text
role="guilabel"} and `Rejected`{.interpreted-text role="guilabel"}
activities are shown to the right of the line graph.

::: {.tip}
::: {.title}
Tip
:::

Hovering over any point in the line graph of the activity block reveals
a notated breakdown of data for that specific date.

{.align-center}
:::

Beneath the graph in the activity block, for *Email* or *SMS* activity
types, a line of accessible data figures provide a bird\'s eye view of
the campaign activity, including: `Sent`{.interpreted-text
role="guilabel"} (numerical), `Clicked`{.interpreted-text
role="guilabel"} (percentage), `Replied`{.interpreted-text
role="guilabel"} (percentage), and `Bounced`{.interpreted-text
role="guilabel"} (percentage).

::: {.tip}
::: {.title}
Tip
:::

Clicking any of those stats on the `DETAILS`{.interpreted-text
role="guilabel"} line, beneath the line graph, reveals a separate page
containing every specific record for that particular data point.
:::

### Activity filter tab

Next to the `Graph`{.interpreted-text role="guilabel"} tab on the
activity block, there\'s the option to open a `Filter`{.interpreted-text
role="guilabel"} tab (represented by a `filter/funnel`{.interpreted-text
role="guilabel"} icon).

{.align-center}

Clicking the `Filter`{.interpreted-text role="guilabel"} tab on an
activity block, reveals what the specific filters are for that
particular campaign activity, and how many records in the database match
that specific criteria.

::: {.tip}
::: {.title}
Tip
:::

Clicking the `records`{.interpreted-text role="guilabel"} link beneath
the displayed filter reveals a separate pop-up window containing a list
of all the records that match that specific campaign activity rule(s).
:::

Link tracker
------------

Odoo tracks all URLs used in marketing campaigns. To access and analyze
those URLs, navigate to
`Marketing Automation app --> Reporting --> Link Tracker`{.interpreted-text
role="menuselection"}. Doing so reveals a
`Link Statistics`{.interpreted-text role="guilabel"} page, wherein all
campaign-related URLs can be analyzed.

{.align-center}

The default view on the `Link Statistics`{.interpreted-text
role="guilabel"} page is the `Bar Chart`{.interpreted-text
role="guilabel"} view, but there are different view options available in
the upper-left corner. There is the option to view the statistics as a
`Line Chart`{.interpreted-text role="guilabel"} or
`Pie Chart`{.interpreted-text role="guilabel"}.

Beside that, there is also the option to view the statistics as
`Stacked`{.interpreted-text role="guilabel"}, and the data can be put
into `Descending`{.interpreted-text role="guilabel"} or
`Ascending`{.interpreted-text role="guilabel"} order.

To the far-left of the view options, there is the
`Measures`{.interpreted-text role="guilabel"} drop-down menu. When
clicked, the options to view the `Number of Clicks`{.interpreted-text
role="guilabel"} or total `Count`{.interpreted-text role="guilabel"} are
available. And, to the right of the `Measures`{.interpreted-text
role="guilabel"} drop-down menu, there\'s the ability to add any data to
a spreadsheet by clicking the `Insert in Spreadsheet`{.interpreted-text
role="guilabel"} button.

Also, in the upper-right corner of the
`Link Statistics`{.interpreted-text role="guilabel"} page, to the
far-right of the search bar, there are additional view options to choose
from: the default `Graph`{.interpreted-text role="guilabel"} view, the
`Pivot`{.interpreted-text role="guilabel"} table view, and the
`List`{.interpreted-text role="guilabel"} view.

Traces
------

Odoo tracks all activities used in every marketing campaign. The data
related to these activities can be accessed and analyzed in the
`Traces`{.interpreted-text role="guilabel"} page, which can be found by
navigating to
`Marketing Automation app --> Reporting --> Traces`{.interpreted-text
role="menuselection"}.

{.align-center}

The default view on the `Traces`{.interpreted-text role="guilabel"} page
is the `Bar Chart`{.interpreted-text role="guilabel"} view, but there
are different view options available in the upper-left corner. There is
the option to view the statistics as a `Line Chart`{.interpreted-text
role="guilabel"} or `Pie Chart`{.interpreted-text role="guilabel"}.

At the top of the graph, there\'s a color key, informing the user which
activities have been `Processed`{.interpreted-text role="guilabel"},
`Scheduled`{.interpreted-text role="guilabel"}, and
`Rejected`{.interpreted-text role="guilabel"}. There\'s also an outline
indicator to inform users of the `Sum`{.interpreted-text
role="guilabel"} of certain activities, as well.

Beside the various view option in the upper-left corner of the
`Traces`{.interpreted-text role="guilabel"} page, there is also the
option to view the statistics as `Stacked`{.interpreted-text
role="guilabel"}, and the data can be put into
`Descending`{.interpreted-text role="guilabel"} or
`Ascending`{.interpreted-text role="guilabel"} order.

To the far-left of the view options, there is the
`Measures`{.interpreted-text role="guilabel"} drop-down menu. When
clicked, the options to view the `Document ID`{.interpreted-text
role="guilabel"} or total `Count`{.interpreted-text role="guilabel"} are
available. And, to the right of the `Measures`{.interpreted-text
role="guilabel"} drop-down menu, there\'s the ability to add any data to
a spreadsheet by clicking the `Insert in Spreadsheet`{.interpreted-text
role="guilabel"} button.

Also, in the upper-right corner of the
`Link Statistics`{.interpreted-text role="guilabel"} page, to the
far-right of the search bar, there are additional view options to choose
from: the default `Graph`{.interpreted-text role="guilabel"} view, the
`Pivot`{.interpreted-text role="guilabel"} table view, and the
`List`{.interpreted-text role="guilabel"} view.

Participants
------------

Odoo tracks all participants related to every marketing campaign. The
data related to these participants can be accessed and analyzed in the
`Participants`{.interpreted-text role="guilabel"} page, which can be
found by navigating to
`Marketing Automation app --> Reporting --> Participants`{.interpreted-text
role="menuselection"}.

{.align-center}

The default view on the `Participants`{.interpreted-text
role="guilabel"} page is the `Pie Chart`{.interpreted-text
role="guilabel"} view, but there are different view options available in
the upper-left corner. There is the option to view the statistics as a
`Line Chart`{.interpreted-text role="guilabel"} or
`Bar Chart`{.interpreted-text role="guilabel"}.

At the top of the graph, there\'s a color key that describes the type of
participants found in the graph.

To the far-left of the view options, there is the
`Measures`{.interpreted-text role="guilabel"} drop-down menu. When
clicked, the options to view the `Record ID`{.interpreted-text
role="guilabel"} or total `Count`{.interpreted-text role="guilabel"} are
available. And, to the right of the `Measures`{.interpreted-text
role="guilabel"} drop-down menu, there\'s the ability to add any data to
a spreadsheet by clicking the `Insert in Spreadsheet`{.interpreted-text
role="guilabel"} button.

Also, in the upper-right corner of the
`Link Statistics`{.interpreted-text role="guilabel"} page, to the
far-right of the search bar, there are additional view options to choose
from: the default `Graph`{.interpreted-text role="guilabel"} view, the
`Pivot`{.interpreted-text role="guilabel"} table view, and the
`List`{.interpreted-text role="guilabel"} view.
