# File: /content/odoo_doc17.0/fr/content/applications/productivity/calendar.md

show-content

:   

Calendar
========

Odoo **Calendar** is a scheduling app that allows users to integrate a
company\'s business flow into a single management platform. By
integrating with the other apps in Odoo\'s ecosystem, **Calendar**
allows users to schedule and organize meetings, schedule events, plan
employee appraisals, coordinate projects, and more -- all from the same
platform.

Upon opening the `Calendar app`{.interpreted-text role="menuselection"},
users have an overview of their current meetings. The selected view
option appears as a `Day`{.interpreted-text role="guilabel"},
`Week`{.interpreted-text role="guilabel"}, `Month`{.interpreted-text
role="guilabel"}, or `Year`{.interpreted-text role="guilabel"} drop-down
menu. Under the view options drop-down menu, users can also enable or
disable `Show weekends`{.interpreted-text role="guilabel"}.



::: {.tip}
::: {.title}
Tip
:::

Depending on the selected view option, users can click the
`oi-arrow-left`{.interpreted-text role="icon"}
`oi-arrow-right`{.interpreted-text role="icon"}
`(left or right arrow)`{.interpreted-text role="guilabel"} buttons to
switch between days, weeks, etc., and switch back to the current day
with the `Today`{.interpreted-text role="guilabel"} button.
:::

Sync third-party calendars
--------------------------

Users can sync Odoo with existing
`Outlook <calendar/outlook>`{.interpreted-text role="doc"} and/or
`Google <calendar/google>`{.interpreted-text role="doc"} calendars, by
heading to
`Calendar app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. From here, enter `Client ID`{.interpreted-text
role="guilabel"} and `Client Secret`{.interpreted-text role="guilabel"}.
There is also an option to pause synchronization by ticking the
checkbox, or automating synchronization by keeping it blank.

Once the desired configurations are complete, be sure to click
`Save`{.interpreted-text role="guilabel"} before moving on.

Events created in synced calendars automatically appear across the
integrated platforms.

::: {.seealso}
\-
`Synchronize Outlook calendar with Odoo <calendar/outlook>`{.interpreted-text
role="doc"} -
`Synchronize Google calendar with Odoo <calendar/google>`{.interpreted-text
role="doc"}
:::

Create activities from chatter
------------------------------

Instantly create new meetings anywhere in Odoo through an individual
record\'s chatter, like in a **CRM** opportunity card or task in the
**Projects** app.

From the chatter, click on the `Activities`{.interpreted-text
role="guilabel"} button. In the `Schedule Activity`{.interpreted-text
role="guilabel"} pop-up window, select the desired
`Activity Type`{.interpreted-text role="guilabel"}, which populates a
set of buttons, depending on the activity.

Activities that involve other schedules, like
`Meeting`{.interpreted-text role="guilabel"} or
`Call for Demo`{.interpreted-text role="guilabel"}, link to the
**Calendar** app. Select one of these activities to link to the
**Calendar** app, then hit `Open Calendar`{.interpreted-text
role="guilabel"} to navigate back to the app. Alternatively, it is also
possible to `Schedule & Mark as Done`{.interpreted-text role="guilabel"}
to close out the activity, or select `Done & Schedule
Next`{.interpreted-text role="guilabel"} to keep the
`Schedule Activity`{.interpreted-text role="guilabel"} window open to
create another.

::: {.seealso}
`Schedule activities in Odoo <../essentials/activities>`{.interpreted-text
role="doc"}
:::

Plan an event
-------------

To put an event on the calendar, open the
`Calendar app`{.interpreted-text role="menuselection"}, and click into
the target date. On the `New Event`{.interpreted-text role="guilabel"}
pop-up window that appears, start by adding the event title.



The target date auto-populates in the `Start`{.interpreted-text
role="guilabel"} field. This can be changed by clicking into the date
section, and selecting a date from the calendar. For multi-day events,
select the end date in the second field, then click
`Apply`{.interpreted-text role="guilabel"}.

Tick the `All Day`{.interpreted-text role="guilabel"} checkbox if there
is no specific start or end time.

For events with specific start and stop times, ensure the
`All Day`{.interpreted-text role="guilabel"} checkbox is unticked to
enable time selection. With the `All Day`{.interpreted-text
role="guilabel"} checkbox unticked, time selections appear in the
`Start`{.interpreted-text role="guilabel"} field.

The signed-in user auto-populates as the first attendee. Additional
`Attendees`{.interpreted-text role="guilabel"} can be added or created
from here, as well.

For virtual meetings, copy and paste the URL into the space provided in
the `Videocall URL`{.interpreted-text role="guilabel"} field. Or, click
`fa-plus`{.interpreted-text role="icon"}
`Odoo meeting`{.interpreted-text role="guilabel"} to create a link.

Next, either create the event by clicking
`Save & Close`{.interpreted-text role="guilabel"}, or select `More
Options`{.interpreted-text role="guilabel"} to further configure the
event.

::: {.tip}
::: {.title}
Tip
:::

Once the event is created, users can click into the virtual meeting
directly from the calendar event to access more configuration options.
:::



The `Description`{.interpreted-text role="guilabel"} field allows users
to add additional information and details about the meeting.

Click `More Options`{.interpreted-text role="guilabel"} to navigate to
the meeting form, which provides additional configurations for the
event:

-   `Duration`{.interpreted-text role="guilabel"}: Define the length of
    the meeting in `hours`{.interpreted-text role="guilabel"}, or toggle
    the `All Day`{.interpreted-text role="guilabel"} switch.
-   `Recurrent`{.interpreted-text role="guilabel"}: Tick the checkbox to
    create a recurring meeting. Once selected, this opens new fields:
    -   `Timezone`{.interpreted-text role="guilabel"}: Select the
        timezone for which this meeting time is specified.
    -   `Repeat`{.interpreted-text role="guilabel"}: Select the
        recurring period of this meeting. Depending on what type of
        recurrence has been selected, a subsequent field appears, in
        which users can indicate when the meeting should recur. For
        example, if `Monthly`{.interpreted-text role="guilabel"} is
        selected as the `Repeat`{.interpreted-text role="guilabel"}
        option, a new field appears, in which the user decides on what
        `Day of Month`{.interpreted-text role="guilabel"} the meeting
        should recur.
    -   `Until`{.interpreted-text role="guilabel"}: Select the limited
        `Number of repetitions`{.interpreted-text role="guilabel"} this
        meeting should recur, the `End date`{.interpreted-text
        role="guilabel"} of when the recurrences should stop, or if the
        meetings should recur `Forever`{.interpreted-text
        role="guilabel"}.
-   `Tags`{.interpreted-text role="guilabel"}: Add tags to the event,
    like [Customer Meeting]{.title-ref} or [Internal
    Meeting]{.title-ref}. These can be searched and filtered in the
    **Calendar** app when organizing multiple events.
-   `Appointment`{.interpreted-text role="guilabel"}: Link existing or
    new appointments. These can be configured through the
    `Share Availabilities <calendar/share-availabilities>`{.interpreted-text
    role="ref"} button from the main **Calendar** dashboard.
-   `Privacy`{.interpreted-text role="guilabel"}: Toggle between
    visibility options to control who can view the event.
-   `Organizer`{.interpreted-text role="guilabel"}: This is defaulted to
    the current Odoo user. Select a new one from existing users, or
    create and edit a new user.
-   `Description`{.interpreted-text role="guilabel"}: Add additional
    information or details about the meeting.
-   `Reminders`{.interpreted-text role="guilabel"}: Select notification
    options to send to attendees. Choose a default notification, or
    configure new reminders.

Coordinate with teams\' availability
------------------------------------

When scheduling an event for multiple users, on the **Calendar** app
dashboard, tick the checkbox next to `Attendees`{.interpreted-text
role="guilabel"} to view team members\' availability. Tick (or untick)
the checkbox next to listed users to show (or hide) individual
calendars.



Share Availabilities {#calendar/share-availabilities}
--------------------

On the **Calendar** app main dashboard, click the
`Share Availabilities`{.interpreted-text role="guilabel"} button at the
top of the page. Next, click and drag to select the available times and
dates on the calendar to add them as options in the invitation.

::: {.tip}
::: {.title}
Tip
:::

To remove a selected time range, hover over the availability to click
the `fa-trash`{.interpreted-text role="icon"}
`(trash)`{.interpreted-text role="guilabel"} icon.
:::

::: {.note}
::: {.title}
Note
:::

Within the `Share Availabilities`{.interpreted-text role="guilabel"}
feature, selecting times is only possible on the *Day* calendar views.
:::

Once availability has been selected, click the
`fa-external-link`{.interpreted-text role="icon"}
`Open`{.interpreted-text role="guilabel"} button to navigate to the
associated appointment.



Several configuration options are available on the appointment form:

In the `Scheduling`{.interpreted-text role="guilabel"} field, set a
minimum hour window to ensure appointments are confirmed a specified
amount of time in advance. For example, set [01:00]{.title-ref} to
require attendees to confirm at least one hour before their appointment
time.

In the `Allow Cancelling`{.interpreted-text role="guilabel"} field, set
a maximum hour window before the appointment that attendees are able to
cancel.

The `Availability on`{.interpreted-text role="guilabel"} field enables
attendees to book `Users`{.interpreted-text role="guilabel"} or
`Resources`{.interpreted-text role="guilabel"}, such as meeting rooms or
tables. After selecting `Users`{.interpreted-text role="guilabel"} or
`Resources`{.interpreted-text role="guilabel"}, type in the desired user
or resource in the space below.

The `Front-End Display`{.interpreted-text role="guilabel"} field is used
to choose `No Picture`{.interpreted-text role="guilabel"} or
`Show Pictures`{.interpreted-text role="guilabel"} related to the
selected user or resource on the appointment page.

If `Resources`{.interpreted-text role="guilabel"} has been selected in
the `Availability on`{.interpreted-text role="guilabel"} field, users
have an option to `Manage Capacities`{.interpreted-text
role="guilabel"}.

Tick the checkbox to limit the maximum amount of people that can use the
resource at the same time.

The `Assignment Method`{.interpreted-text role="guilabel"} field enables
the order in which attendees book their time and user/resource:

-   `Pick User/Resource then Time`{.interpreted-text role="guilabel"}
-   `Select Time then User/Resource`{.interpreted-text role="guilabel"}

If `Resources`{.interpreted-text role="guilabel"} has been selected in
the `Availability On`{.interpreted-text role="guilabel"} field, a third
option is available, `Select Time then auto-assign`{.interpreted-text
role="guilabel"}.

Optionally, configure the following tabs:

-   `calendar/appointment-schedule`{.interpreted-text role="ref"}
-   `calendar/appointment-options`{.interpreted-text role="ref"}
-   `calendar/appointment-questions`{.interpreted-text role="ref"}
-   `calendar/appointment-messages`{.interpreted-text role="ref"}

Click the `Preview`{.interpreted-text role="guilabel"} button to see how
the appointment link looks for attendees.

Once the configurations are finished, click the
`Share`{.interpreted-text role="guilabel"} button to generate a link to
send directly, or click `Publish`{.interpreted-text role="guilabel"} to
publish the appointment selection on the connected Odoo website.

### Schedule tab {#calendar/appointment-schedule}

In the `Schedule`{.interpreted-text role="guilabel"} tab of the
appointment form, time slots can be managed. The target date and time
populate as the first time slots.

To add a new time slot, hit `Add a line`{.interpreted-text
role="guilabel"}. Click into the new blank space under the
`From`{.interpreted-text role="guilabel"} field, then select and enter
the new target start date and time, respectively. Repeat under the new
blank space under `To`{.interpreted-text role="guilabel"} to select and
enter the new target end date and time.

### Options tab {#calendar/appointment-options}

The `Options`{.interpreted-text role="guilabel"} tab provides additional
configurations:

-   `Website`{.interpreted-text role="guilabel"}: Specify which website
    this meeting invitation will be published on.
-   `Timezone`{.interpreted-text role="guilabel"}: This defaults to the
    company\'s timezone selected in the **Settings** app. To change the
    timezone, select the desired option from the drop-down menu.
-   `Location`{.interpreted-text role="guilabel"}: Select or create new
    locations from the drop-down menu. If this field is left empty, the
    meeting is considered to be taking place online.
-   `Videoconference Link`{.interpreted-text role="guilabel"}: Select
    from `Odoo Discuss`{.interpreted-text role="guilabel"} or
    `Google Meet`{.interpreted-text role="guilabel"} to include a video
    conference link in the meeting invitation, or leave it blank to
    prevent generating a meeting URL.
-   `Manual Confirmation`{.interpreted-text role="guilabel"}: Only shown
    if `Resources`{.interpreted-text role="guilabel"} has been selected
    in the `Availability On`{.interpreted-text role="guilabel"} field.
    Tick the checkbox and enter a maximum percentage of the selected
    resource(s)\' total capacity to create a manual confirmation
    requirement to finalize the meeting.
-   `Up-front Payment`{.interpreted-text role="guilabel"}: Tick the
    checkbox to require users to pay before confirming their booking.
    Once this is ticked, a link appears to
    `oi-arrow-right`{.interpreted-text role="icon"} `Configure
    Payment Providers`{.interpreted-text role="guilabel"}, which enables
    online payments.
-   `Limit to Work Hours`{.interpreted-text role="guilabel"}: If
    `Users`{.interpreted-text role="guilabel"} has been selected in the
    `Availability On`{.interpreted-text role="guilabel"} field, tick the
    checkbox to limit meeting time slots to the selected
    `users' working hours <../hr/employees/new_employee>`{.interpreted-text
    role="doc"}.
-   `Create Opportunities`{.interpreted-text role="guilabel"}: When this
    is selected, each scheduled appointment creates a new **CRM**
    opportunity.
-   `Reminders`{.interpreted-text role="guilabel"}: Add or delete
    notification reminders in this field. Select the blank space for
    additional options.
-   `Confirmation Email`{.interpreted-text role="guilabel"}: Tick the
    checkbox to automatically send a confirmation email to attendees
    once the meeting is confirmed. Select from the email templates or
    click `Search More...`{.interpreted-text role="guilabel"}, then
    `New`{.interpreted-text role="guilabel"} to create a custom
    template.
-   `Cancelation Email`{.interpreted-text role="guilabel"}: Tick the
    checkbox to automatically send a cancelation email to attendees if
    the meeting is canceled. Select from the email templates or click
    `Search More...`{.interpreted-text role="guilabel"}, then
    `New`{.interpreted-text role="guilabel"} to create a custom
    template.
-   `CC to`{.interpreted-text role="guilabel"}: Add contacts to be
    notified of meeting updates in this field, regardless if they attend
    the meeting.
-   `Allow Guests`{.interpreted-text role="guilabel"}: Tick the checkbox
    to allow attendees to invite guests.

### Questions tab {#calendar/appointment-questions}

In the `Questions`{.interpreted-text role="guilabel"} tab, add questions
for the attendee to answer when confirming their meeting. Click
`Add a line`{.interpreted-text role="guilabel"} to configure a
`Question`{.interpreted-text role="guilabel"}. Then select a
`Question Type`{.interpreted-text role="guilabel"}, optionally add a
`Placeholder`{.interpreted-text role="guilabel"} answer, and choose
whether it is a `Required Answer`{.interpreted-text role="guilabel"}.

To learn how to create more comprehensive questionnaires, head to the
**Survey** app documentation on
`creating and configuring data-capturing questions
<../marketing/surveys/questions>`{.interpreted-text role="doc"}.

### Messages tab {#calendar/appointment-messages}

In the `Introduction Message`{.interpreted-text role="guilabel"} field
of the `Messages`{.interpreted-text role="guilabel"} tab, add additional
meeting information that appears on the invitation.

Information added to the
`Extra Message on Confirmation`{.interpreted-text role="guilabel"} field
appears once the meeting is confirmed.

::: {.toctree titlesonly=""}
calendar/outlook calendar/google
:::
