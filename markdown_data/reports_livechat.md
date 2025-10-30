# File: /content/odoo_doc17.0/fr/content/applications/websites/livechat/reports.md

Reports
=======

Odoo *Live Chat* includes several reports that allow for the monitoring
of operator performance and the identification of trends in customer
conversations.

Available reports
-----------------

The following reports are included in the *Live Chat* app:

-   `Sessions History <livechat/sessions-history>`{.interpreted-text
    role="ref"}
-   `Session Statistics <livechat/session-statistics>`{.interpreted-text
    role="ref"}
-   `Operator Analysis <livechat/operator-analysis>`{.interpreted-text
    role="ref"}

::: {.note}
::: {.title}
Note
:::

The *Live Chat Ratings Report* can also be accessed through the
`Report`{.interpreted-text role="guilabel"} menu. For more information
on this report, and on the *Live Chat* rating process, see
`Live Chat Ratings
<../livechat/ratings>`{.interpreted-text role="doc"}.
:::

To access a drop-down menu of all the available reports, navigate to
`Live Chat app
--> Report`{.interpreted-text role="menuselection"}.

### Sessions History {#livechat/sessions-history}

The *Sessions History* report displays an overview of live chat
sessions, including session dates, participant name and country, session
duration, the number of messages, and the rating. It also provides
access to the complete transcripts of live chat sessions.

To access this report, navigate to
`Live Chat app --> Report --> Sessions History`{.interpreted-text
role="menuselection"}.

{.align-center}

The information in this report can be exported, or inserted into a
spreadsheet.

Click the `⚙️ (gear)`{.interpreted-text role="guilabel"} icon to the
right of the `History`{.interpreted-text role="guilabel"} page title, in
the top-left corner. Doing so reveals a drop-down menu.

From the drop-down menu, click `Export All`{.interpreted-text
role="guilabel"} to export all sessions to a spreadsheet, or
`Insert list in spreadsheet`{.interpreted-text role="guilabel"} to
insert the information in a new, or existing, spreadsheet.

To only export select sessions, first select the desired sessions to be
exported from the list, by clicking the checkbox to the left of each
individual session. With the sessions selected, click the
`⚙️ (gear) Actions`{.interpreted-text role="guilabel"} icon in the
top-center of the page, and click `Export`{.interpreted-text
role="guilabel"} or `Insert list in spreadsheet`{.interpreted-text
role="guilabel"}.

To view the transcript of an individual conversation, click anywhere on
the entry line. This opens the *Discuss* thread for the conversation.

In the *Discuss* thread, the conversation view displays the entire
transcript of the conversation. At the top of the conversation, there is
a list of the web pages the visitor browsed before beginning their chat
session, along with corresponding time stamps. If the visitor left a
rating, it is included at the end of the transcript.

{.align-center}

### Session Statistics {#livechat/session-statistics}

The *Session Statistics* report provides a statistical overview of live
chat sessions. The default view for this report displays sessions
grouped by the date of creation.

To access this report, navigate to
`Live Chat app --> Reports --> Session
Statistics`{.interpreted-text role="menuselection"}.

![The stacked bar graph view of the *Session Statistics* report, with
results grouped by Creation Date (hour), then by
rating.](reports/sessions-statistics.png){.align-center}

To view a different measure, click the `Measures`{.interpreted-text
role="guilabel"} drop-down menu at the top-left of the report. The
measures available for this report include:

-   `# of speakers`{.interpreted-text role="guilabel"}: number of
    participants in the conversation.
-   `Days of activity`{.interpreted-text role="guilabel"}: number of
    days since the operator\'s first session.
-   `Duration of Session (min)`{.interpreted-text role="guilabel"}: the
    duration of a conversation, in minutes.
-   `Is visitor anonymous`{.interpreted-text role="guilabel"}: denotes
    whether the conversation participant is anonymous.
-   `Messages per session`{.interpreted-text role="guilabel"}: the total
    number of messages sent in a conversation. This measure is included
    in the default view.
-   `Rating`{.interpreted-text role="guilabel"}: the rating received by
    an operator at the end of a session, if one was provided.
-   `Session not rated`{.interpreted-text role="guilabel"}: denotes if a
    session did **not** receive a rating at the end of the conversation.
-   `Time to answer (sec)`{.interpreted-text role="guilabel"}: the
    average time, in seconds, before an operator responds to a chat
    request.
-   `Visitor is Happy`{.interpreted-text role="guilabel"}: denotes
    whether a positive rating was provided. If the visitor gave either a
    negative or neutral rating, they are considered *unhappy*.
-   `Count`{.interpreted-text role="guilabel"}: the total number of
    sessions.

### Operator Analysis {#livechat/operator-analysis}

The *Operator Analysis* report is used to monitor the performance of
individual live chat operators.

To access the report, navigate to
`Live Chat app --> Reports --> Operator Analysis`{.interpreted-text
role="menuselection"}.

The default view for this report is a bar chart, which only displays
conversations from the current month, as indicated by the
`This Month`{.interpreted-text role="guilabel"} default search filter.
Conversations are grouped by operator.

To view a different measure, click the `Measures`{.interpreted-text
role="guilabel"} drop-down menu at the top-left of the report. The
measures available for this report include:

-   `# of Sessions`{.interpreted-text role="guilabel"}: the number of
    sessions an operator participated in. This measure is included by
    default.
-   `Average duration`{.interpreted-text role="guilabel"}: the average
    duration of a conversation, in seconds.
-   `Average rating`{.interpreted-text role="guilabel"}: the average
    rating received by the operator.
-   `Time to answer`{.interpreted-text role="guilabel"}: the average
    amount of time before the operator responds to a chat request, in
    seconds.
-   `Count`{.interpreted-text role="guilabel"}: the total number of
    sessions.

{.align-center}

View and filter options
-----------------------

On any Odoo report, the view and filter options vary, depending on what
data is being analyzed, measured, and grouped. See below for additional
information on the available views for the *Live Chat* reports.

::: {.note}
::: {.title}
Note
:::

The `Sessions History <livechat/sessions-history>`{.interpreted-text
role="ref"} report is **only** available in list view.
:::

### Pivot view

The *pivot* view presents data in an interactive manner. The
`Session Statistics
<livechat/session-statistics>`{.interpreted-text role="ref"} and
`Operator Analysis <livechat/operator-analysis>`{.interpreted-text
role="ref"} reports are available in pivot view.

The pivot view can be accessed on a report by selecting the
`grid icon`{.interpreted-text role="guilabel"} at the top-right of the
screen.

To add a group to a row or column, click the
`➕ (plus sign)`{.interpreted-text role="guilabel"} icon next to
`Total`{.interpreted-text role="guilabel"}, and then select one of the
groups from the drop-down menu that appears. To remove one, click the
`➖ (minus sign)`{.interpreted-text role="guilabel"} icon, and de-select
the appropriate option.

### Graph view

The *graph* view presents data in either a *bar*, *line*, or *pie*
chart. The `Session
Statistics <livechat/session-statistics>`{.interpreted-text role="ref"}
and `Operator Analysis <livechat/operator-analysis>`{.interpreted-text
role="ref"} reports are available in graph view.

Switch to the graph view by selecting the `line chart`{.interpreted-text
role="guilabel"} icon at the top-right of the screen. To switch between
the different charts, select the desired view\'s corresponding icon at
the top-left of the chart, while in graph view.

::: {.tip}
::: {.title}
Tip
:::

Both the bar chart and line chart can utilize the *stacked* view option.
This presents two or more groups of data on top of each other, instead
of next to each other, making it easier to compare data.
:::

### Save and share a favorite search

The *Favorites* feature found on reports allows users to save their most
commonly used filters, without having to reconstruct them every time
they are needed.

To create and save a filter to the *Favorites* section on the search bar
drop-down menu, follow the steps below:

1.  Set the necessary parameters using the `Filters`{.interpreted-text
    role="guilabel"} and `Group By`{.interpreted-text role="guilabel"}
    options available in the `Search...`{.interpreted-text
    role="guilabel"} bar drop-down menu and the
    `Measures`{.interpreted-text role="guilabel"} drop-down menu at the
    top-left of the report.
2.  Click the `🔻(triangle pointed down)`{.interpreted-text
    role="guilabel"} icon next to the `Search...`{.interpreted-text
    role="guilabel"} bar to open the drop-down menu.
3.  Under the `Favorites`{.interpreted-text role="guilabel"} heading,
    click `Save current search`{.interpreted-text role="guilabel"}.
4.  Rename the search.
5.  Select `Default filter`{.interpreted-text role="guilabel"} to have
    these filter settings automatically displayed when the report is
    opened. Otherwise, leave it blank.
6.  Select `Shared`{.interpreted-text role="guilabel"} to make this
    filter available to all other database users. If this box is not
    checked, the filter is only available to the user who creates it.
7.  Click `Save`{.interpreted-text role="guilabel"} to preserve the
    configuration for future use.
