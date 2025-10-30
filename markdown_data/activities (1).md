# File: /content/odoo_doc17.0/fr/content/applications/essentials/activities.md

Activities
==========

*Activities* are follow-up tasks tied to a record in an Odoo database.

::: {#activities/important}
The icon used to display activities varies, depending on the
`activity type
<activities/types>`{.interpreted-text role="ref"}:
:::

-   `fa-clock-o`{.interpreted-text role="icon"}
    `(clock)`{.interpreted-text role="guilabel"} icon: the default
    activities icon.
-   `fa-phone`{.interpreted-text role="icon"}
    `(phone)`{.interpreted-text role="guilabel"} icon: a phone call is
    scheduled.
-   `fa-envelope`{.interpreted-text role="icon"}
    `(envelope)`{.interpreted-text role="guilabel"} icon: an email is
    scheduled.
-   `fa-check`{.interpreted-text role="icon"}
    `(check)`{.interpreted-text role="guilabel"} icon: a \"to-do\" is
    scheduled.
-   `fa-users`{.interpreted-text role="icon"}
    `(people)`{.interpreted-text role="guilabel"} icon: a meeting is
    scheduled.
-   `fa-upload`{.interpreted-text role="icon"}
    `(upload)`{.interpreted-text role="guilabel"} icon: a document is
    scheduled to be uploaded.
-   `fa-pencil-square-o`{.interpreted-text role="icon"}
    `(request signature)`{.interpreted-text role="guilabel"} icon: a
    signature request is scheduled.

Schedule activities
-------------------

Activities can be scheduled on any page of the database that contains a
`chatter
<activities/chatter>`{.interpreted-text role="ref"} thread,
`Kanban view <activities/kanban>`{.interpreted-text role="ref"},
`list view
<activities/list>`{.interpreted-text role="ref"}, or
`activities view <activities/activity>`{.interpreted-text role="ref"} of
an application.

### Chatter {#activities/chatter}

Activities can be created from the chatter on any record.

To schedule a new activity, click the `Activities`{.interpreted-text
role="guilabel"} button, located at the top of the chatter. In the
`Schedule Activity`{.interpreted-text role="guilabel"} pop-up window
that appears, `fill out the
Schedule Activity form <activities/form>`{.interpreted-text role="ref"}.

{.align-center}

### Kanban view {#activities/kanban}

Activities can also be created from the
`oi-view-kanban`{.interpreted-text role="icon"}
`(Kanban)`{.interpreted-text role="guilabel"} view.

To do so, click on the `fa-clock-o`{.interpreted-text role="icon"}
`(clock)`{.interpreted-text role="guilabel"} icon located at the bottom
of an individual record.

Click `+ Schedule An Activity`{.interpreted-text role="guilabel"}, then
proceed to `fill out the Schedule Activity form
<activities/form>`{.interpreted-text role="ref"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If a record already has a scheduled activity, the
`fa-clock-o`{.interpreted-text role="icon"} `(clock)`{.interpreted-text
role="guilabel"} icon is replaced by the icon that represents the
existing scheduled activity. Click on the activity type\'s icon to
schedule another activity.
:::

### List view {#activities/list}

Activities can also be created from a `oi-view-list`{.interpreted-text
role="icon"} `(list)`{.interpreted-text role="guilabel"} view.

If the `Activities`{.interpreted-text role="guilabel"} column is hidden,
reveal it using the `oi-settings-adjust`{.interpreted-text role="icon"}
`(settings adjust)`{.interpreted-text role="guilabel"} icon in the
far-right of the top row.

Then, click on the `fa-clock-o`{.interpreted-text role="icon"}
`(clock)`{.interpreted-text role="guilabel"} icon for the record the
activity is being added to, and click `+
Schedule an activity`{.interpreted-text role="guilabel"}. Proceed to
`fill out the Schedule Activity form <activities/form>`{.interpreted-text
role="ref"} that appears.

::: {.note}
::: {.title}
Note
:::

If a record already has a scheduled activity, the
`fa-clock-o`{.interpreted-text role="icon"} `(clock)`{.interpreted-text
role="guilabel"} icon is replaced by the icon that represents the
existing scheduled activity. Click on the activity type\'s icon to
schedule another activity.
:::

{.align-center}

### Activity view {#activities/activity}

Most applications in Odoo have an *Activity* view available. If
available, a `fa-clock-o`{.interpreted-text role="icon"}
`(clock)`{.interpreted-text role="guilabel"} icon is visible in the
top-right corner of the main menu bar, amongst the other view option
icons.

To open the activity view, click the `fa-clock-o`{.interpreted-text
role="icon"} `(clock)`{.interpreted-text role="guilabel"} icon.

{.align-center}

In this view, all the available activities are listed in the columns,
while the horizontal entries represent all the individual records.

Activities that appear green have a due date in the future, activities
that appear orange are due today, while activities appearing red are
overdue.

Color bars in each column represent records for specific activity types,
and display a number indicating how many activities are scheduled for
that type.

If multiple activity types are scheduled for a record, a number appears
in the box, indicating the total number of scheduled activities.

::: {.note}
::: {.title}
Note
:::

Activity colors, and their relation to an activity\'s due date, are
consistent throughout Odoo, regardless of the activity type, or the
view.
:::

To schedule an activity for a record, hover over the corresponding
field. Click the `fa-plus`{.interpreted-text role="icon"}
`(plus)`{.interpreted-text role="guilabel"} icon that appears, and then
`fill out the Schedule Activity form
<activities/form>`{.interpreted-text role="ref"}.

{.align-center}

### Schedule Activity form {#activities/form}

Activities can be scheduled from many different places, such as from the
`chatter
<activities/chatter>`{.interpreted-text role="ref"} of a record, or from
one of multiple views in an application, when available: the
`Kanban view <activities/kanban>`{.interpreted-text role="ref"},
`list view <activities/list>`{.interpreted-text role="ref"}, or
`activity
view <activities/activity>`{.interpreted-text role="ref"}.

Enter the following information on the form:

-   `Activity Type`{.interpreted-text role="guilabel"}: select the type
    of activity from the drop-down menu. The default options are:
    `Email`{.interpreted-text role="guilabel"}, `Call`{.interpreted-text
    role="guilabel"}, `Meeting`{.interpreted-text role="guilabel"}, or
    `To-Do`{.interpreted-text role="guilabel"}. Depending on what other
    applications are installed, additional options may be available.
-   `Summary`{.interpreted-text role="guilabel"}: enter a short title
    for the activity, such as [Discuss Proposal]{.title-ref}.
-   `Due Date`{.interpreted-text role="guilabel"}: using the calendar
    popover, select the activity\'s deadline.
-   `Assigned to`{.interpreted-text role="guilabel"}: by default, the
    current user populates this field. To assign a different user to the
    activity, select them from the drop-down menu.
-   `Notes`{.interpreted-text role="guilabel"}: add any additional
    information for the activity in this field.

When the `Schedule Activity`{.interpreted-text role="guilabel"} pop-up
window is completed, click one of the following buttons:

-   `Open Calendar`{.interpreted-text role="guilabel"}: opens the
    user\'s calendar to add and schedule the activity.

    Click on the desired date and time for the activity, and a
    `New Event`{.interpreted-text role="guilabel"} pop-up window
    appears. The summary from the *Schedule Activity* pop-up window
    populates the `Title`{.interpreted-text role="guilabel"} field.

    Enter the information in the `New Event`{.interpreted-text
    role="guilabel"} pop-up window, then click `Save &
    Close`{.interpreted-text role="guilabel"} to schedule it. Once
    scheduled, the activity is added to the chatter under the
    `Planned Activities`{.interpreted-text role="guilabel"} section.

    ::: {.important}
    ::: {.title}
    Important
    :::

    The `Open Calendar`{.interpreted-text role="guilabel"} button
    **only** appears if the `Activity Type`{.interpreted-text
    role="guilabel"} is set to either `Call`{.interpreted-text
    role="guilabel"} or `Meeting`{.interpreted-text role="guilabel"}.
    :::

-   `Schedule`{.interpreted-text role="guilabel"}: schedules the
    activity, and adds the activity to the chatter under
    `Planned Activities`{.interpreted-text role="guilabel"}.

-   `Schedule & Mark as Done`{.interpreted-text role="guilabel"}: adds
    the details of the activity to the chatter under
    `Today`{.interpreted-text role="guilabel"}. The activity is not
    scheduled, and is automatically marked as done.

-   `Done & Schedule Next`{.interpreted-text role="guilabel"}: adds the
    details of the activity to the chatter under
    `Today`{.interpreted-text role="guilabel"}. The activity is not
    scheduled, is automatically marked as done, and a new
    `Schedule Activity`{.interpreted-text role="guilabel"} pop-up window
    appears.

-   `Cancel`{.interpreted-text role="guilabel"}: discards any changes
    made on the `Schedule Activity`{.interpreted-text role="guilabel"}
    pop-up window.

{.align-center}

All scheduled activities {#activities/all}
------------------------

To view a consolidated list of activities, organized by application,
click the `fa-clock-o`{.interpreted-text role="icon"}
`(clock)`{.interpreted-text role="guilabel"} icon in the header menu,
located in the top-right corner.

If any activities are scheduled, the number of activities appear in a
red bubble on the `fa-clock-o`{.interpreted-text role="icon"}
`(clock)`{.interpreted-text role="guilabel"} icon.

All activities for each application are further divided into
subsections, indicating where in the application the activity is to be
completed. Each sub-section lists the number of scheduled activities
that are `Late`{.interpreted-text role="guilabel"}, due
`Today`{.interpreted-text role="guilabel"}, and scheduled in the
`Future`{.interpreted-text role="guilabel"}.

::: {.example}
In the *Time Off* application, one activity is scheduled to be done in
the *All Time Off* requests dashboard, and six activities are scheduled
to be done in the *Allocations* dashboard.

These requests appear in two separate lists in the all activities
drop-down menu: one labeled [Time Off]{.title-ref} and one labeled [Time
Off Allocation]{.title-ref}.

![The list of activities that is accessed from the main menu bar. Two entries for the Time
Off application are highlighted.](activities/activities-menu.png){.align-center}
:::

### Request a document

The option to `Request a Document`{.interpreted-text role="guilabel"} is
available at the bottom of the list of `all
scheduled activities <activities/all>`{.interpreted-text role="ref"},
the option to `Request a Document`{.interpreted-text role="guilabel"}
appears. Click `Request a Document`{.interpreted-text role="guilabel"},
and a `Request a file`{.interpreted-text role="guilabel"} pop-up window
appears.

Enter the following information on the form:

-   `Document Name`{.interpreted-text role="guilabel"}: enter a name for
    the document being requested.
-   `Request To`{.interpreted-text role="guilabel"}: select the user the
    document is being requested from using the drop-down menu.
-   `Due Date In`{.interpreted-text role="guilabel"}: enter a numerical
    value indicating when the document is due. Next to this field, a
    `Days`{.interpreted-text role="guilabel"} field is visible. Click
    `Days`{.interpreted-text role="guilabel"}, the default option, to
    reveal a drop-down menu. Select the desired time-frame option from
    the list. The options are `Days`{.interpreted-text role="guilabel"},
    `Weeks`{.interpreted-text role="guilabel"}, or
    `Months`{.interpreted-text role="guilabel"}.
-   `Workspace`{.interpreted-text role="guilabel"}: using the drop-down
    menu, select the specific `Workspace
    <documents/workspaces>`{.interpreted-text role="ref"} the document
    is being uploaded to.
-   `Tags`{.interpreted-text role="guilabel"}: select any desired tags
    from the drop-down menu. The available tags displayed are based on
    the tags configured for the selected `Workspace`{.interpreted-text
    role="guilabel"}.
-   `Message`{.interpreted-text role="guilabel"}: enter a message to
    clarify the document request in this field.

When all the fields are completed, click `Request`{.interpreted-text
role="guilabel"} to send the document request.

{.align-center}

Activity types {#activities/types}
--------------

To view the currently configured types of activities in the database,
navigate to
`Settings app --> Discuss section --> Activities setting --> Activity Types`{.interpreted-text
role="menuselection"}.

{.align-center}

Doing so reveals the `Activity Types`{.interpreted-text role="guilabel"}
page, where the existing activity types are found.

::: {.tip}
::: {.title}
Tip
:::

Individual applications have a list of *Activity Types* dedicated to
that application. For example, to view and edit the activities available
for the *CRM* application, go to
`CRM app --> Configuration --> Activity Types`{.interpreted-text
role="menuselection"}.
:::

{.align-center}

### Edit activity types

To edit an existing `activity type <activities/types>`{.interpreted-text
role="ref"}, click on the activity type, and the activity type form
loads.

Make any desired changes to the activity type form. The form
automatically saves, but it can be saved manually at any time by
clicking the `Save Manually`{.interpreted-text role="guilabel"} option,
represented by a `fa-cloud-upload`{.interpreted-text role="icon"}
`(cloud upload)`{.interpreted-text role="guilabel"} icon, located in the
top-left corner of the page.

### Create new activity types

To create a new `activity type <activities/types>`{.interpreted-text
role="ref"}, click `New`{.interpreted-text role="guilabel"} from the
`Activity Types`{.interpreted-text role="guilabel"} page, and a blank
activity type form loads.

Enter a `Name`{.interpreted-text role="guilabel"} for the activity type
at the top of the form, then enter the following information on the
form.

#### Activity Settings section

-   `Action`{.interpreted-text role="guilabel"}: using the drop-down
    menu, select an action associated with this new activity type. Some
    actions trigger specific behaviors after an activity is scheduled,
    such as:

    -   `Upload Document`{.interpreted-text role="guilabel"}: if
        selected, a link to upload a document is automatically added to
        the planned activity in the chatter.
    -   `Call`{.interpreted-text role="guilabel"} or
        `Meeting`{.interpreted-text role="guilabel"}: if selected, users
        have the option to open their calendar to select a date and time
        for the activity.
    -   `Request Signature`{.interpreted-text role="guilabel"}: if
        selected, a link to open a signature request pop-up window is
        automatically added to the planned activity in the chatter. This
        requires the Odoo *Sign* application to be installed.

    ::: {.note}
    ::: {.title}
    Note
    :::

    Available activity types vary based on the installed applications in
    the database.
    :::

-   `Folder`{.interpreted-text role="guilabel"}: select a specific
    `workspace <documents/workspaces>`{.interpreted-text role="ref"}
    folder to save a document to. This field **only** appears if
    `Upload Document`{.interpreted-text role="guilabel"} is selected for
    the `Action`{.interpreted-text role="guilabel"}.

    Using the drop-down menu, select the `Folder`{.interpreted-text
    role="guilabel"} the document is saved to.

-   `Default User`{.interpreted-text role="guilabel"}: select a user
    from the drop-down menu to automatically assign this activity to the
    selected user when this activity type is scheduled. If this field is
    left blank, the activity is assigned to the user who creates the
    activity.

-   `Default Summary`{.interpreted-text role="guilabel"}: enter a note
    to include whenever this activity type is created.

    ::: {.note}
    ::: {.title}
    Note
    :::

    The information in the `Default User`{.interpreted-text
    role="guilabel"} and `Default Summary`{.interpreted-text
    role="guilabel"} fields are included when an activity is created.
    However, they can be altered before the activity is scheduled or
    saved.
    :::

-   `Keep Done`{.interpreted-text role="guilabel"}: tick this checkbox
    to keep activities that have been marked as [Done]{.title-ref}
    visible in the
    `activity view <activities/activity>`{.interpreted-text role="ref"}.

-   `Default Note`{.interpreted-text role="guilabel"}: enter any notes
    to appear with the activity.

#### Next Activity section

It is possible to have another activity either suggested or triggered.
To do so, configure the `Next Activity`{.interpreted-text
role="guilabel"} section.

-   `Chaining Type`{.interpreted-text role="guilabel"}: select either
    `Suggest Next Activity`{.interpreted-text role="guilabel"} or
    `Trigger
    Next Activity`{.interpreted-text role="guilabel"} from the drop-down
    menu. Depending on the selected option, either the
    `Suggest`{.interpreted-text role="guilabel"} or
    `Trigger`{.interpreted-text role="guilabel"} field is displayed.

    ::: {.note}
    ::: {.title}
    Note
    :::

    The `Chaining Type`{.interpreted-text role="guilabel"} field does
    **not** appear if `Upload Document`{.interpreted-text
    role="guilabel"} is selected for the `Action`{.interpreted-text
    role="guilabel"}.
    :::

-   `Suggest/Trigger`{.interpreted-text role="guilabel"}: depending on
    what is selected for the `Chaining Type`{.interpreted-text
    role="guilabel"}, this field either displays
    `Suggest`{.interpreted-text role="guilabel"} or
    `Trigger`{.interpreted-text role="guilabel"}. Using the drop-down
    menu, select the activity to recommend or schedule as a follow-up
    task to the activity type.

-   `Schedule`{.interpreted-text role="guilabel"}: configure when the
    next activity is suggested or triggered.

    First, enter a numerical value indicating when the activity is
    suggested or triggered.

    Next to this field, a `Days`{.interpreted-text role="guilabel"}
    field is visible. Click `Days`{.interpreted-text role="guilabel"},
    the default option, to reveal a drop-down menu. Select the desired
    time-frame option from the list. The options are
    `Days`{.interpreted-text role="guilabel"}, `Weeks`{.interpreted-text
    role="guilabel"}, or `Months`{.interpreted-text role="guilabel"}.

    Lastly, using the drop-down menu, select whether the activity is
    scheduled or triggered either
    `after previous activity deadline`{.interpreted-text
    role="guilabel"} or `after completion date`{.interpreted-text
    role="guilabel"}.

{.align-center}

::: {.seealso}
\- `../productivity/discuss`{.interpreted-text role="doc"} -
`../productivity/discuss/team_communication`{.interpreted-text
role="doc"} -
`../sales/crm/optimize/utilize_activities`{.interpreted-text role="doc"}
:::
