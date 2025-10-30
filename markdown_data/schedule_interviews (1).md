# File: /content/odoo_doc17.0/fr/content/applications/hr/recruitment/schedule_interviews.md

Schedule interviews
===================

Schedule in-person, virtual, and phone interviews with Odoo through the
*Recruitment* app.

An interview can be scheduled in one of two ways: either by the
`recruitment team
<recruitment/schedule_interviews/recruitment-scheduled>`{.interpreted-text
role="ref"}, or by the `applicant
<recruitment/schedule_interviews/applicant-scheduled>`{.interpreted-text
role="ref"}.

Recruitment team scheduled interviews {#recruitment/schedule_interviews/recruitment-scheduled}
-------------------------------------

When an applicant reaches the interview stage, the recruitment team
should schedule the interview, by first coordinating a suitable date and
time with the applicant and interviewers.

To schedule the interview, navigate to the applicant\'s card, by first
going to the `Recruitment app`{.interpreted-text role="menuselection"},
and clicking the relevant job card. This opens the
`Applications`{.interpreted-text role="guilabel"} page for that job
position. Then, click the desired applicant\'s card to view their
detailed applicant form.

To schedule an phone, virtual, or in-person interview, click the
`No Meeting`{.interpreted-text role="guilabel"} smart button at the top
of the applicant\'s record.

::: {.note}
::: {.title}
Note
:::

The *Meetings* smart button displays `No Meeting`{.interpreted-text
role="guilabel"} if no meetings are currently scheduled. For applicants
who are new to the `First Interview`{.interpreted-text role="guilabel"}
stage, this is the default.

If there is one meeting already scheduled, the smart button displays *1
Meeting*, with the date of the upcoming meeting beneath it. If more than
one meeting is scheduled, the button displays *Next Meeting*, with the
date of the first upcoming meeting beneath it.
:::

Clicking the *Meetings* smart button loads a calendar, showing the
scheduled meetings and events for the currently signed-in user, as well
as the employees who are listed under the `Attendees`{.interpreted-text
role="guilabel"} section, located to the right of the calendar.

To change the currently loaded meetings and events being displayed,
uncheck an attendee whose calendar events are to be hidden. Only the
checked attendees are visible on the calendar.

{.align-center}

To add a meeting to the calendar when in the *Day* or *Week* view, click
on the start time of the meeting and drag down to the end time. Doing so
selects the date, time, and the length of the meeting.

A meeting can also be added in this view by clicking on the desired day
*and* time slot.

Both methods cause a
`New Event <recruitment/schedule_interviews/event-card>`{.interpreted-text
role="ref"} pop-up window to appear.

### New event pop-up window {#recruitment/schedule_interviews/event-card}

Clicking a grid, corresponding with the time and date, opens the
`New Event`{.interpreted-text role="guilabel"} pop-up window to schedule
a meeting.

Enter the information on the form. The only required fields to enter are
a title for the meeting, along with the `Start`{.interpreted-text
role="guilabel"} (and end date/time) fields.

Once the card details are entered, click
`Save & Close`{.interpreted-text role="guilabel"} to save the changes
and create the interview.

After entering in a required name for the meeting, the fields available
to modify on the `New Event`{.interpreted-text role="guilabel"} card are
as follows:

-   `Meeting Title`{.interpreted-text role="guilabel"}: enter the
    subject for the meeting. This should clearly indicate the purpose of
    the meeting. The default subject is the
    `Subject/Application Name`{.interpreted-text role="guilabel"} on the
    applicant\'s card.

-   `Start`{.interpreted-text role="guilabel"}: start and end date and
    times for the meeting. Clicking either of these fields opens a
    calendar pop-up window. Click `Apply`{.interpreted-text
    role="guilabel"} to close the window.

-   `All Day`{.interpreted-text role="guilabel"}: tick the box to
    schedule an all-day interview. If this box is ticked, the
    `Start`{.interpreted-text role="guilabel"} field changes to
    `Start Date`{.interpreted-text role="guilabel"}.

-   `Attendees`{.interpreted-text role="guilabel"}: select the people
    who should attend the meeting. The default employee listed is the
    person who created the meeting. Add as many other people as desired.

-   `Videocall URL`{.interpreted-text role="guilabel"}: if the meeting
    is virtual, or if there is a virtual option available, click
    `fa-plus`{.interpreted-text role="icon"}
    `Odoo meeting`{.interpreted-text role="guilabel"}, and a URL is
    automatically created for the meeting, which populates the field.

-   `Description`{.interpreted-text role="guilabel"}: enter a brief
    description in this field. There is an option to enter formatted
    text, such as numbered lists, headings, tables, links, photos, and
    more. Use the powerbox feature, by typing a [/]{.title-ref} to
    reveal a list of options.

    Scroll through the options and click on the desired item. The item
    appears in the field, and can be modified. Each command presents a
    different pop-up window. Follow the instructions for each command to
    complete the entry.

#### More options

To add additional information to the meeting, click the
`More Options`{.interpreted-text role="guilabel"} button in the
lower-right corner of the
`New Event <recruitment/schedule_interviews/event-card>`{.interpreted-text
role="ref"} pop-up window. Enter any of the following additional fields:

-   `Duration`{.interpreted-text role="guilabel"}: this field auto
    populates based on the `Start`{.interpreted-text role="guilabel"}
    (and end) date and time. If the meeting time is adjusted, this field
    automatically adjusts to the correct duration length. The default
    length of a meeting is one hour.
-   `Recurrent`{.interpreted-text role="guilabel"}: if the meeting
    should repeat at a selected interval (not typical for a first
    interview), tick the checkbox next to `Recurrent`{.interpreted-text
    role="guilabel"}. Several additional fields appear when this is
    enabled:
    -   `Timezone`{.interpreted-text role="guilabel"}: using the
        drop-down menu, select the `Timezone`{.interpreted-text
        role="guilabel"} for the recurrent meetings.
    -   `Repeat`{.interpreted-text role="guilabel"}: choose
        `Daily`{.interpreted-text role="guilabel"},
        `Weekly`{.interpreted-text role="guilabel"},
        `Monthly`{.interpreted-text role="guilabel"},
        `Yearly`{.interpreted-text role="guilabel"}, or
        `Custom`{.interpreted-text role="guilabel"} recurring meetings.
        If `Custom`{.interpreted-text role="guilabel"} is selected, a
        `Repeat Every`{.interpreted-text role="guilabel"} field appears
        beneath it, along with another time frequency parameter
        (`Days`{.interpreted-text role="guilabel"},
        `Weeks`{.interpreted-text role="guilabel"},
        `Months`{.interpreted-text role="guilabel"}, or
        `Years`{.interpreted-text role="guilabel"}). Enter a number in
        the blank field, then select the time period using the drop-down
        menu.
    -   `Repeat on`{.interpreted-text role="guilabel"}: enabled when the
        `Weekly`{.interpreted-text role="guilabel"} option is selected
        in the `Repeat`{.interpreted-text role="guilabel"} field. Choose
        the day the weekly meeting falls on.
    -   `Day of Month`{.interpreted-text role="guilabel"}: configure the
        two drop-down menu options to select a specific day of the
        month, irrespective of the date (e.g. the first Tuesday of every
        month). To set a specific calendar date, choose
        `Date of Month`{.interpreted-text role="guilabel"} and enter the
        calendar date in the field (e.g. [15]{.title-ref} to set the
        meeting to occur on the fifteenth of every month).
    -   `Until`{.interpreted-text role="guilabel"}: using the drop-down
        menu, select when the meetings stop repeating. The available
        options are `Number of repetitions`{.interpreted-text
        role="guilabel"}, `End date`{.interpreted-text role="guilabel"},
        and `Forever`{.interpreted-text role="guilabel"}. If
        `Number of repetitions`{.interpreted-text role="guilabel"} is
        selected, enter the number of total meetings to occur in the
        blank field to the right. If `End date`{.interpreted-text
        role="guilabel"} is selected, specify the date using the
        calendar pop-up window, or type in a date in a XX/XX/XXXX
        format. `Forever`{.interpreted-text role="guilabel"} schedules
        meetings indefinitely.
-   `Location`{.interpreted-text role="guilabel"}: enter the location
    for the meeting.
-   `Tags`{.interpreted-text role="guilabel"}: select any tags for the
    meeting using the drop-down menu, or add a new tag by typing in the
    tag and clicking `Create "tag"`{.interpreted-text role="guilabel"}.
    There is no limit to the number of tags that can be used.
-   `Appointment`{.interpreted-text role="guilabel"}: if an appointment
    is associated with this meeting, select it from the drop-down menu,
    or create a new appointment by typing in the appointment name, then
    clicking `Create & Edit...`{.interpreted-text role="guilabel"} from
    the resulting drop-down men. A
    `Create Appointment`{.interpreted-text role="guilabel"} form loads.
    Enter the information on the form, then click
    `Save & Close`{.interpreted-text role="guilabel"}.
-   `Privacy`{.interpreted-text role="guilabel"}: select if the
    organizer appears either `Available`{.interpreted-text
    role="guilabel"} or `Busy`{.interpreted-text role="guilabel"} for
    the duration of the meeting. Next, select the visibility of this
    meeting, using the drop-down menu to the right of the first
    selection. Options are `Public`{.interpreted-text role="guilabel"},
    `Private`{.interpreted-text role="guilabel"}, and
    `Only internal users`{.interpreted-text role="guilabel"}.
    `Public`{.interpreted-text role="guilabel"} allows for everyone to
    see the meeting, `Private`{.interpreted-text role="guilabel"} allows
    only the attendees listed on the meeting to see the meeting, and
    `Only internal users`{.interpreted-text role="guilabel"} allows
    anyone logged into the company database to see the meeting.
-   `Organizer`{.interpreted-text role="guilabel"}: the employee who
    created the meeting is populated in this field. Use the drop-down
    menu to change the selected employee.
-   `Reminders`{.interpreted-text role="guilabel"}: select a reminder
    from the drop-down menu. Default options include
    `Notification`{.interpreted-text role="guilabel"},
    `Email`{.interpreted-text role="guilabel"}, and
    `SMS Text Message`{.interpreted-text role="guilabel"}, each with a
    specific time period before the event (hours, days, etc). The chosen
    reminder chosen alerts the meeting participants of the meeting, via
    the selected option at the specified time. Multiple reminders can be
    selected in this field.

{.align-center}

### Send meeting to attendees

Once changes have been entered on the
`New Event <recruitment/schedule_interviews/event-card>`{.interpreted-text
role="ref"} pop-up window, and the meeting details are correct, the
meeting can be sent to the attendees, via email or text message, from
the expanded event form (what is seen when the
`More Options`{.interpreted-text role="guilabel"} button is clicked on
in the `New Event`{.interpreted-text role="guilabel"} pop-up window).

To send the meeting via email, click the `fa-envelope`{.interpreted-text
role="icon"} `Email`{.interpreted-text role="guilabel"} button next to
the `Attendees`{.interpreted-text role="guilabel"} field on the expanded
meeting form.

A `Contact Attendees`{.interpreted-text role="guilabel"} email
configurator pop-up window appears. A pre-formatted email, using the
default `Calendar: Event Update`{.interpreted-text role="guilabel"}
email template, populates the email body field.

The followers of the job application, as well as the user who created
the meeting, are added as `Recipients`{.interpreted-text
role="guilabel"} by default. If needed, add the applicant\'s email
address to the list to send the email to the applicant, as well. Make
any other desired changes to the email. If an attachment is needed,
click the `Attachments`{.interpreted-text role="guilabel"} button,
navigate to the file, then click `Open`{.interpreted-text
role="guilabel"}. Once the email is ready to be sent, click
`Send`{.interpreted-text role="guilabel"}.

{.align-center}

To send the meeting via text message, click the
`fa-mobile`{.interpreted-text role="icon"} `SMS`{.interpreted-text
role="guilabel"} button next to the `Attendees`{.interpreted-text
role="guilabel"} field on the expanded meeting form. A
`Send SMS Text Message`{.interpreted-text role="guilabel"} pop-up window
appears.

At the top, a blue banner appears if any attendees do not have valid
mobile numbers, and lists how many records are invalid. If a contact
does not have a valid mobile number listed, click
`Close`{.interpreted-text role="guilabel"}, and edit the attendee\'s
record, then redo these steps.

When no warning message appears, type in the message to be sent to the
attendees in the `Message`{.interpreted-text role="guilabel"} field. To
add any emojis to the message, click the
`oi-smile-add`{.interpreted-text role="icon"}
`(smile add)`{.interpreted-text role="guilabel"} icon on the right-side
of the pop-up window.

The number of characters, and amount of text messages required to send
the message (according to GSM7 criteria) appears beneath the
`Message`{.interpreted-text role="guilabel"} field. Click
`Put In Queue`{.interpreted-text role="guilabel"} to have the text sent
later, after any other messages are scheduled, or click
`Send Now`{.interpreted-text role="guilabel"} to send the message
immediately.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Sending text messages is **not** a default capability with Odoo. To send
text messages, credits are required, which need to be purchased. For
more information on IAP credits and plans, refer to the
`../../essentials/in_app_purchase`{.interpreted-text role="doc"}
documentation.
:::

Applicant scheduled interviews {#recruitment/schedule_interviews/applicant-scheduled}
------------------------------

By default, the recruitment interview stages are **not** set up for
applicants to schedule their own interviews.

However, if the `First Interview`{.interpreted-text role="guilabel"} or
`Second Interview`{.interpreted-text role="guilabel"} stages are
modified to send the `Recruitment: Schedule Interview`{.interpreted-text
role="guilabel"} email template when an applicant reaches that stage,
the applicant receives a link to the recruitment team\'s calendar, and
can schedule the interview on their own. The recruitment team\'s
availability is reflected in the calendar.

In order for applicants to be able to schedule their own interviews, a
`stage must first be
modified <recruitment/schedule_interviews/modify-stage>`{.interpreted-text
role="ref"} in the *Recruitment* app.

### Modify stage {#recruitment/schedule_interviews/modify-stage}

To modify either the `First Interview`{.interpreted-text
role="guilabel"} or `Second Interview`{.interpreted-text
role="guilabel"} stage, first navigate to the main
`Recruitment`{.interpreted-text role="menuselection"} app dashboard.
Next, click on the desired job card to navigate to the
`Applications`{.interpreted-text role="guilabel"} page for that job
position.

Hover over the name of the stage, and a `fa-cog`{.interpreted-text
role="icon"} `(gear)`{.interpreted-text role="guilabel"} icon appears in
the upper-right hand side of the stage name. Click the
`fa-cog`{.interpreted-text role="icon"} `(gear)`{.interpreted-text
role="guilabel"} icon, and a drop-down menu appears. Then, click on the
`Edit`{.interpreted-text role="guilabel"} option, and an
`Edit: (Stage)`{.interpreted-text role="guilabel"} form appears.

{.align-center}

The `Email Template`{.interpreted-text role="guilabel"} field is blank,
by default. Using the drop-down menu, select
`Recruitment: Schedule interview`{.interpreted-text role="guilabel"} for
the `Email Template`{.interpreted-text role="guilabel"} field, then
click `Save & Close`{.interpreted-text role="guilabel"} when done.

{.align-center}

### Send email

After either the `First Interview`{.interpreted-text role="guilabel"} or
`Second Interview`{.interpreted-text role="guilabel"} stages are
`modified to send the <recruitment/schedule_interviews/modify-stage>`{.interpreted-text
role="ref"} `Recruitment:
Schedule interview`{.interpreted-text role="guilabel"} email to the
applicant upon moving their applicant card to one of those stages, the
following email is received by the applicant:

[Subject: Can we plan an interview together for your (Job Position)
application?]{.title-ref}

[Congratulations! Your application is really interesting and we\'d like
to plan an interview with you. Can you please use the button below to
schedule it with one of our recruiters?]{.title-ref}

[Plan my interview]{.title-ref}

### Schedule interview

When the applicant received the email, they click the
`Plan my interview`{.interpreted-text role="guilabel"} button at the
bottom of the email. This navigates the applicant to a private online
scheduling page, which is **only** accessible through the emailed link.

This page displays the `MEETING DETAILS`{.interpreted-text
role="guilabel"} on the right side of the screen. This includes the
format and length of the meeting. In this example. the interview is
virtual (`fa-video-camera`{.interpreted-text role="icon"}
`Online`{.interpreted-text role="guilabel"}) and the duration is a half
hour (`fa-clock-o`{.interpreted-text role="icon"}
`30 minutes`{.interpreted-text role="guilabel"}).

First, if there is an option of who to meet with, the user selects who
they are scheduling their meeting with, by clicking on their icon and
name. If only one person is available to interview the applicant, this
step is not available. If the applicant does not wish to chose an
interviewer, they can just click
`See all availabilities`{.interpreted-text role="guilabel"}
`fa-arrow-right`{.interpreted-text role="icon"}.

![The first screen seen after clicking \'Plan my interview\', where the applicant selects their
interviewer.](schedule_interviews/select-interviewer.png){.align-center}

::: {.note}
::: {.title}
Note
:::

If the applicant selects an interviewer, the applicant is shown a
`Select a date &
time`{.interpreted-text role="guilabel"} page, and **only** sees the
dates and times that specific person is available. In addition, that
interviewer\'s information (name, email, and phone number) appears on
the right-side of the screen, under the heading
`OPERATOR`{.interpreted-text role="guilabel"}, located beneath the
`MEETING DETAILS`{.interpreted-text role="guilabel"}.

If the applicant clicks `See all availabilities`{.interpreted-text
role="guilabel"} `fa-arrow-right`{.interpreted-text role="icon"}
instead, or if there are no interviewer options available, the user is
navigated to the same `Select a
date & time`{.interpreted-text role="guilabel"} page, but there is no
`OPERATOR`{.interpreted-text role="guilabel"} section visible.
:::

Then the applicant clicks on an available day on the calendar, signified
by a square around the date. Once a day is selected, they click on one
of the available times to select that date and time.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Be sure to check the `Timezone`{.interpreted-text role="guilabel"}
field, beneath the calendar, to ensure it is set to the correct time
zone. Changing the time zone may alter the available times presented.
:::

Once the date and time are selected, the applicant is navigated to an
`Add more details
about you`{.interpreted-text role="guilabel"} page. This page asks the
applicant to enter their `Full name`{.interpreted-text role="guilabel"},
`Email`{.interpreted-text role="guilabel"}, and
`Phone number`{.interpreted-text role="guilabel"}. The contact
information entered on this form is how the applicant is contacted to
remind them about the scheduled interview.

When everything is entered on the
`Add more details about you`{.interpreted-text role="guilabel"} page,
the applicant clicks the `Confirm Appointment`{.interpreted-text
role="guilabel"} button, and the interview is scheduled.

{.align-center}

After confirming the interview, the applicant is taken to a confirmation
page, where all the details of the interview are displayed. The option
to add the meeting to the applicant\'s personal calendars is available,
through the `Add to iCal/Outlook`{.interpreted-text role="guilabel"} and
`Add to Google Agenda`{.interpreted-text role="guilabel"} buttons,
beneath the interview details.

The applicant is also able to cancel or reschedule the interview, if
necessary, with the `Cancel/Reschedule`{.interpreted-text
role="guilabel"} button.
