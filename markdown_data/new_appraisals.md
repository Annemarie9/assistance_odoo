# File: /content/odoo_doc17.0/fr/content/applications/hr/appraisals/new_appraisals.md

New appraisals
==============

To create a new appraisal for an employee, first navigate to the main
*Appraisals* dashboard by opening the `Appraisals`{.interpreted-text
role="menuselection"} app. The `Appraisals`{.interpreted-text
role="guilabel"} dashboard is the default view.

Appraisals dashboard
--------------------

All appraisals are displayed on the dashboard in a default Kanban view,
with a list of groupings on the left side of the dashboard, including
`COMPANY`{.interpreted-text role="guilabel"},
`DEPARTMENT`{.interpreted-text role="guilabel"}, and
`STATUS`{.interpreted-text role="guilabel"}.

Click any grouping option to view appraisals for **only** the chosen
selection.

::: {.note}
::: {.title}
Note
:::

Only groupings with multiple selections appear in the list. For example,
if a database only has one company, the `COMPANY`{.interpreted-text
role="guilabel"} grouping does **not** appear, since there is no other
company to select.
:::

Each appraisal card displays the following information:

-   **Name**: the employee\'s name.
-   **Department**: the department the employee is associated with.
-   **Company**: the company the employee works for. This only appears
    in a multi-company database.
-   **Date**: the date the appraisal was requested, or is scheduled for
    in the future.
-   **Activities**: any
    `activities <../../essentials/activities>`{.interpreted-text
    role="doc"} that are scheduled for the appraisal, such as *Meetings*
    or *Phone Calls*.
-   **Manager**: the employee\'s manager, indicated by the profile icon
    in the bottom-right corner of an appraisal card.
-   **Status banner**: the status of the appraisal. A banner appears if
    an appraisal is marked as either *Canceled* or *Done*. If no banner
    is present, that means the appraisal has not happened, or has not
    been scheduled yet.

To view the details of any appraisal, click on the card to open the
appraisal form.

{.align-center}

Create an appraisal
-------------------

To create a new appraisal, click the `New`{.interpreted-text
role="guilabel"} button in the upper-left corner of the
`Appraisals`{.interpreted-text role="guilabel"} dashboard. Doing so
reveals a blank appraisal form. After entering a name in the first blank
field, proceed to enter the following information on the form:

-   `Manager`{.interpreted-text role="guilabel"}: select the employee\'s
    manager from the drop-down menu. The manager is responsible for
    completing the *Manager\'s Feedback* section of the appraisal. This
    field auto-populates after the employee is selected, if they have a
    manager set on their employee profile.
-   `Appraisal Date`{.interpreted-text role="guilabel"}: the current
    date is automatically entered in this field. This field is
    automatically updated once the appraisal is completed or cancelled,
    with the corresponding date of completion or cancellation.
-   `Department`{.interpreted-text role="guilabel"}: select the
    employee\'s department from the drop-down menu. This field
    auto-populates after the employee is selected, if they have a
    department set on their employee profile.
-   `Company`{.interpreted-text role="guilabel"}: select the employee\'s
    company from the drop-down menu. This field auto-populates after the
    employee is selected, if they have a company set on their employee
    profile.

::: {.note}
::: {.title}
Note
:::

The only required fields for the appraisal form are the employee\'s
name, the `Manager`{.interpreted-text role="guilabel"}, and the
`Company`{.interpreted-text role="guilabel"}.
:::

Once the form is complete, click the `Confirm`{.interpreted-text
role="guilabel"} button to confirm the appraisal request.

Once confirmed, the employee receives an email stating that an appraisal
was requested, and is then prompted to schedule an appraisal date.

The status changes to `Confirmed`{.interpreted-text role="guilabel"},
and the `Employee's Feedback`{.interpreted-text role="guilabel"} section
of the `Appraisal`{.interpreted-text role="guilabel"} tab is grayed out.
The information in that section only appears after the self-assessment
is published by the employee. The `Final Rating`{.interpreted-text
role="guilabel"} field also appears once the appraisal request is
confirmed.

If there are any existing appraisals for the employee, an
`Appraisal`{.interpreted-text role="guilabel"} smart button appears at
the top of the page, listing the total number of appraisals there are
for the employee.

### Ask for feedback

As part of the appraisal process, the manager can request feedback on an
employee from anyone in the company. Feedback is usually requested from
co-workers and other people who interact with, or work with, the
employee. This is to get a more well-rounded view of the employee, and
aid in the manager\'s overall assessment.

To request feedback, the appraisal **must** be confirmed. Once
confirmed, an `Ask
Feedback`{.interpreted-text role="guilabel"} button appears at the top
of the form.

When the `Ask Feedback`{.interpreted-text role="guilabel"} button is
clicked, an `Ask Feedback`{.interpreted-text role="guilabel"} email
pop-up form appears, using the
`Appraisal: Ask Feedback`{.interpreted-text role="guilabel"} email
template, which sends the `360 Feedback`{.interpreted-text
role="guilabel"} survey.

Enter the employees being asked to complete the survey in the
`Recipients`{.interpreted-text role="guilabel"} field. Multiple
employees may be selected.

The email template has dynamic placeholders to personalize the message.
Add any additional text to the email, if desired.

If required, an `Answer Deadline`{.interpreted-text role="guilabel"} can
be added, as well.

If any attachments are needed, click the
`fa-paperclip`{.interpreted-text role="icon"}
`Attachments`{.interpreted-text role="guilabel"} button, and a file
explorer window appears. Navigate to the file(s), select them, then
click `Open`{.interpreted-text role="guilabel"}.

When the email is ready to send, click `Send.`{.interpreted-text
role="guilabel"}

{.align-center}

### Appraisal form

Once an appraisal is confirmed, the next steps require the employee to
fill out the self-assessment, after which the manager completes their
assessment.

#### Employee\'s feedback {#appraisals/employee-feedback}

To complete their portion of feedback, employees should navigate to the
main `Appraisals application`{.interpreted-text role="menuselection"}
dashboard, where the only entries visible are appraisals for the
employee, themselves, and/or anyone they manage and have to provide
manager feedback for.

Click on the appraisal to open the appraisal form. Enter responses in
the `Employee's
Feedback`{.interpreted-text role="guilabel"} section, under the
`Appraisal`{.interpreted-text role="guilabel"} tab.

When completed, click the `Not Visible to Manager`{.interpreted-text
role="guilabel"} toggle (the default setting once an appraisal is
confirmed). When clicked, the toggle changes to
`Visible to Manager`{.interpreted-text role="guilabel"}.

{.align-center}

#### Manager\'s feedback {#appraisals/manager-feedback}

After the employee has completed the
`Employee's Feedback`{.interpreted-text role="guilabel"} section, under
the `Appraisal`{.interpreted-text role="guilabel"} tab, it is time for
the manager to fill out the `Manager's Feedback`{.interpreted-text
role="guilabel"} section.

The manager enters their responses in the fields in the
`same manner as the employee
<appraisals/employee-feedback>`{.interpreted-text role="ref"}.

When the feedback section is completed, click the
`Not Visible to Employee`{.interpreted-text role="guilabel"} toggle (the
default setting once an appraisal is confirmed). When clicked, the
toggle changes to `Visible to Employee`{.interpreted-text
role="guilabel"}.

{.align-center}

#### Skills tab

Part of an appraisal is evaluating an employee\'s skills, and tracking
their progress over time. The `Skills`{.interpreted-text
role="guilabel"} tab of the appraisal form auto-populates with the
skills from the `employee
form <employees/skills>`{.interpreted-text role="ref"}, once an
appraisal is confirmed.

Each skill is grouped with like skills, and the
`Skill Level`{.interpreted-text role="guilabel"},
`Progress`{.interpreted-text role="guilabel"}, and
`Justification`{.interpreted-text role="guilabel"} are displayed for
each skill.

Update any skills, or add any new skills to the
`Skills`{.interpreted-text role="guilabel"} tab.

If a skill level has increased, a reason for the improved rating can be
entered into the `Justification`{.interpreted-text role="guilabel"}
field, such as [took a fluency language test]{.title-ref} or [received
Javascript certification]{.title-ref}.

::: {.seealso}
Refer to the
`Create a new employee <employees/skills>`{.interpreted-text role="ref"}
document for detailed instructions on adding or updating a skill.
:::

After an appraisal is completed, and the skills have been updated, the
next time an appraisal is confirmed, the updated skills populate the
`Skills`{.interpreted-text role="guilabel"} tab.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The `Skills`{.interpreted-text role="guilabel"} tab can be modified
**after** the employee and their manager have met and discussed the
employee\'s appraisal.

This is a common situation as the manager may not have all the necessary
information to properly assess and update the employee\'s skills before
meeting.
:::

#### Private Note tab

If managers want to leave notes that are only visible to other managers,
they can be entered in the `Private Note`{.interpreted-text
role="guilabel"} tab. This can be done before or after meeting with the
employee to discuss the appraisal.

The employee being evaluated does **not** have access to this tab, and
the tab does **not** appear on their appraisal.

### Schedule a meeting

Once both portions of an appraisal are completed (the
`employee <appraisals/employee-feedback>`{.interpreted-text role="ref"}
and `manager <appraisals/manager-feedback>`{.interpreted-text
role="ref"} feedback sections), it is time for the employee and manager
to meet and discuss the appraisal.

A meeting can be scheduled in one of two ways: either from the
*Appraisals* application dashboard, or from an individual appraisal
card.

To schedule an appraisal from the dashboard of the *Appraisals*
application, first navigate to
`Appraisals app --> Appraisals`{.interpreted-text role="menuselection"}.

Click the `fa-clock-o`{.interpreted-text role="icon"}
`(clock)`{.interpreted-text role="guilabel"} icon, beneath the appraisal
date on the desired appraisal card, and a pop-up window appears. Then,
click `fa-plus`{.interpreted-text role="icon"} `Schedule an
activity`{.interpreted-text role="guilabel"} to create an activity from
a `Schedule Activity`{.interpreted-text role="guilabel"} pop-up form
that appears.

Select `Meeting`{.interpreted-text role="guilabel"} for the
`Activity Type`{.interpreted-text role="guilabel"} from the drop-down
menu. Doing so causes the form to change, so only the
`Activity Type`{.interpreted-text role="guilabel"} and
`Summary`{.interpreted-text role="guilabel"} fields appear.

Enter a brief description in the `Summary`{.interpreted-text
role="guilabel"} field of the `Schedule Activity`{.interpreted-text
role="guilabel"} pop-up form, such as [Annual Appraisal for
(Employee)]{.title-ref}.

Next, click the `Open Calendar`{.interpreted-text role="guilabel"}
button. From the calendar page that appears, navigate to, and
double-click on, the desired date and time for the meeting.

Doing so opens a `New Event`{.interpreted-text role="guilabel"} pop-up
form. From this pop-up form, make any desired modifications, such as
designating a `Start`{.interpreted-text role="guilabel"} time, or
modifying the default `Title`{.interpreted-text role="guilabel"} to the
meeting.

Add the appraisee in the `Attendees`{.interpreted-text role="guilabel"}
section, and include anyone else who should also be in the meeting, if
necessary.

To make the meeting a video call, instead of an in-person meeting, click
`fa-plus`{.interpreted-text role="icon"}
`Odoo meeting`{.interpreted-text role="guilabel"}, and a
`Videocall URL`{.interpreted-text role="guilabel"} link appears in the
field.

Once all the desired changes are complete, click
`Save & Close`{.interpreted-text role="guilabel"}.

The meeting now appears on the calendar, and the invited parties are
informed, via email.

{.align-center}

The other way to schedule a meeting is from the individual appraisal
form. To do this, navigate to the `Appraisal app`{.interpreted-text
role="menuselection"} dashboard, then click on an appraisal card.

Next, click on the `fa-calendar`{.interpreted-text role="icon"}
`Meeting`{.interpreted-text role="guilabel"} smart button, and the
calendar loads. Follow the same directions above to create the meeting.

For more detailed information on how to schedule activities, refer to
the `activities
<../../essentials/activities>`{.interpreted-text role="doc"}
documentation.

::: {.note}
::: {.title}
Note
:::

If no meetings are scheduled, the `Meeting`{.interpreted-text
role="guilabel"} smart button reads `No Meeting`{.interpreted-text
role="guilabel"}.
:::

Complete an appraisal
---------------------

After the appraisal is complete, and both the manager and employee have
met to discuss the appraisal, the appraisal can be marked as *Done*.
When completed, click the `Mark as Done`{.interpreted-text
role="guilabel"} button on the appraisal form, located in the top-left
corner.

Once the appraisal is marked as *Done*, the
`Mark as Done`{.interpreted-text role="guilabel"} button disappears, and
a `Reopen`{.interpreted-text role="guilabel"} button appears.

::: {.tip}
::: {.title}
Tip
:::

Modifications are **not** possible once the appraisal is marked as done.

To make any changes to an appraisal that is marked as *Done*, click the
`Reopen`{.interpreted-text role="guilabel"} button.

Then, click the `Confirm`{.interpreted-text role="guilabel"} button that
appears, and make any modifications needed. Once all modifications are
complete, click the `Mark as Done`{.interpreted-text role="guilabel"}
button again.
:::

::: {.seealso}
\- `../appraisals/goals`{.interpreted-text role="doc"} -
`../appraisals/appraisal_analysis`{.interpreted-text role="doc"} -
`../appraisals/skills_evolution`{.interpreted-text role="doc"}
:::
