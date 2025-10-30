# File: /content/odoo_doc17.0/fr/content/applications/hr/recruitment/recruitment-flow.md

Recruitment flow
================

When a prospective employee applies for a job in Odoo, there is a
preconfigured process from the
`initial inquiry <recruitment/new>`{.interpreted-text role="ref"} to the
`creating of a new employee
<recruitment/new-employee>`{.interpreted-text role="ref"} once hired.
The following outlines the default recruitment process for Odoo\'s
*Recruitment* application.

::: {.important}
::: {.title}
Important
:::

The following is based on Odoo\'s default recruitment pipeline. Be
advised that if
`modifications are made <recruitment/customize-stages>`{.interpreted-text
role="ref"} to the pipeline, the process differs.
:::

New {#recruitment/new}
---

At the start of the process, all applicants appear in the
`New`{.interpreted-text role="guilabel"} stage on the
`Applications`{.interpreted-text role="guilabel"} page, whether
submitted online or if the applicant is `manually
entered by a recruiter <add-new-applicants>`{.interpreted-text
role="doc"}.

When the applicant\'s card is created, Odoo automatically populates the
`Subject/Application`{.interpreted-text role="guilabel"}, the
`Applicant's Name`{.interpreted-text role="guilabel"},
`Email`{.interpreted-text role="guilabel"}, and
`Mobile`{.interpreted-text role="guilabel"} number, on the applicant\'s
card. This information is required when applying for a job position, by
default.

::: {.note}
::: {.title}
Note
:::

If the website application form is modified, different fields may be
populated, based on what information is requested on the website.
:::

If the applicant entered any information in the *Short Introduction*
section of the online application, it populates the
`Application Summary`{.interpreted-text role="guilabel"} tab at the
bottom of the applicant\'s card.

### Resumé

If a resumé was attached to the online application, it appears in the
`Files`{.interpreted-text role="guilabel"} section of the chatter, and
is also stored in the *Documents* application.

To find the recruitment documents, navigate to the main
`Documents app`{.interpreted-text role="menuselection"} dashboard, and
click the `Recruitment`{.interpreted-text role="guilabel"} folder on the
left-hand side. All recruitment documents are stored within that folder.

If the `CV Display <recruitment/cv-display>`{.interpreted-text
role="ref"} option was enabled in the `Settings
<recruitment/settings>`{.interpreted-text role="ref"} of the
*Recruitment* app, the resumé appears on the applicant\'s card, on the
right-hand side.

::: {.note}
::: {.title}
Note
:::

Depending on the browser zoom level, or size of the browser screen, the
resumé may appear below the main applicant card information as a PDF
link.
:::

### Send interview

At any point in the hiring process, an interview can be sent to the
applicant to obtain more information. These interviews are custom-made,
and can be formatted in a variety of ways.

The *Surveys* application is **required** to send interviews to an
applicant, so it **must** be installed.

Odoo uses the term *interview*, but these can be thought of as
questionnaires, surveys, tests, certifications, etc. Custom interviews
can be formatted to suit each individual job position\'s needs. For more
information on creating and editing interviews, refer to the
`../../hr/recruitment/new_job`{.interpreted-text role="doc"}
documentation.

::: {.example}
A job position for a computer programmer could have an interview in the
form of a programming quiz to determine the skill level of the
applicant. A job position for a restaurant server could have a
questionnaire inquiring about the applicant\'s availability, if the
desired applicant needs to be available on weekend evenings.
:::

To send an interview to an applicant, first click the applicant\'s card
from the `Applications`{.interpreted-text role="guilabel"} page, to view
the detailed applicant information. At the top-left of the applicant\'s
card, click the `Send Interview`{.interpreted-text role="guilabel"}
button.

If the applicant\'s card has an email address on file, a
`Send an interview`{.interpreted-text role="guilabel"} pop-up window
appears, with the `Recipients`{.interpreted-text role="guilabel"},
`Subject`{.interpreted-text role="guilabel"}, and email body populated.

::: {.note}
::: {.title}
Note
:::

To send an email to an applicant, there **must** be an
`Email`{.interpreted-text role="guilabel"} address on the applicant\'s
card.

If an email address is not entered on the applicant\'s card, when the
`Send Interview`{.interpreted-text role="guilabel"} button is clicked,
an `Edit: (Applicant's Name)`{.interpreted-text role="guilabel"} pop-up
window appears, *on top of* the `Send an interview`{.interpreted-text
role="guilabel"} pop-up window.

Enter the email address in the `Email`{.interpreted-text
role="guilabel"} field, then click `Save & Close`{.interpreted-text
role="guilabel"}.

Once the applicant\'s information is saved, the
`Edit: (Applicant's Name)`{.interpreted-text role="guilabel"} pop-up
window closes, and the `Send an interview`{.interpreted-text
role="guilabel"} pop-up window remains.
:::

Sometimes, preconfigured email templates in Odoo use dynamic
placeholders, which are automatically filled with specific data when the
email is sent. For example, if a placeholder for the applicant\'s name
is used, it is replaced with the actual name of the applicant in the
email. For more detailed information on email templates, refer to the
`../../general/companies/email_template`{.interpreted-text role="doc"}
documentation.

Add the email addresses of any additional recipients for the survey in
the `Additional
emails`{.interpreted-text role="guilabel"} field, if more people should
receive the email. If an email address is in the database as a contact,
add that contact in the `Recipients`{.interpreted-text role="guilabel"}
field. If an email should be sent to someone who is not in the database
as a contact, and they should **not** be added as a contact, add their
email address in the `Additional emails`{.interpreted-text
role="guilabel"} field.

If any attachments need to be added, click the
`fa-paperclip`{.interpreted-text role="icon"}
`Attachments`{.interpreted-text role="guilabel"} button, and a file
explorer window appears. Navigate to the desired file, and click
`Open`{.interpreted-text role="guilabel"} to attach it to the email. The
attachment loads, and is listed above the
`fa-paperclip`{.interpreted-text role="icon"}
`Attachments`{.interpreted-text role="guilabel"} button.

If the emailed interview must be completed by a specific date, enter
that date in the `Answer deadline`{.interpreted-text role="guilabel"}
field, located in the lower-right area of the pop-up window.

To do so, click the empty field next to
`Answer deadline`{.interpreted-text role="guilabel"}, and a calendar
selector appears. Use the `fa-chevron-left`{.interpreted-text
role="icon"} `(left)`{.interpreted-text role="guilabel"} and
`fa-chevron-right`{.interpreted-text role="icon"}
`(right)`{.interpreted-text role="guilabel"} arrows, on either side of
the month, to navigate to the desired month. Then, click on the desired
day to select the date.

The `Mail Template`{.interpreted-text role="guilabel"} field is
pre-populated, based on the configuration for the interview. A different
template can be chosen from the drop-down menu, if desired. If a new
template is selected, the new email template loads in the email body.

To send the email with the interview link to the applicant, click
`Send`{.interpreted-text role="guilabel"} at the bottom of the email
pop-up window.

![Send a custom survey, also referred to as an interview form, to an applicant using a
pre-configured template.](recruitment-flow/send-survey.png){.align-center}

Initial qualification {#recruitment/initial-qualification}
---------------------

If an applicant seems to be a good potential candidate, they are moved
to the `Initial
Qualification`{.interpreted-text role="guilabel"} stage.

This stage exists to quickly sort candidates that have potential, from
those that do not meet the requirements. No automatic actions, such as
emails, are set for this stage. This stage simply informs the
recruitment team to potentially set up a phone call or an interview with
the candidate.

::: {.note}
::: {.title}
Note
:::

In order to move an applicant\'s card from one stage to another, the
applicant\'s card can either be dragged and dropped in the Kanban view
of the `Applications`{.interpreted-text role="guilabel"} page to the
desired stage, or the stage can be modified on the applicant\'s card.

To change the stage on the applicant\'s card, first click the desired
applicant\'s card from the `Applications`{.interpreted-text
role="guilabel"} page. The current stage for the card is highlighted at
the top on a status bar, above the card.

Click the desired stage for the card, and the stage changes. A log note
indicating the stage change appears in the chatter, as well.

![Change the stage of an applicant by clicking on the desired stage at the top of the
applicant\'s card.](recruitment-flow/stage-change.png){.align-center}
:::

First interview {#recruitment/first-interview}
---------------

After an applicant has passed the
`Initial Qualification`{.interpreted-text role="guilabel"} stage, they
can be manually moved to the `First Interview`{.interpreted-text
role="guilabel"} stage on the `Applications`{.interpreted-text
role="guilabel"} page, while in Kanban view.

To move the applicant to the next stage, drag-and-drop the applicant\'s
card to the `First
Interview`{.interpreted-text role="guilabel"} stage.

Alternatively, open the desired applicant\'s card from the
`Applications`{.interpreted-text role="guilabel"} page, and click the
`First Interview`{.interpreted-text role="guilabel"} stage on the status
bar at the top of the individual applicant\'s card.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

The `First Interview`{.interpreted-text role="guilabel"} stage can be
modified, so when the applicant\'s card moves to the
`First Interview`{.interpreted-text role="guilabel"} stage, an email can
be automatically sent to the applicant, stating an interview is
requested. In this pre-configured email template, a link to the
recruiting team\'s calendar appears, allowing the applicant to schedule
their interview.

`Edit <recruitment/edit-stage>`{.interpreted-text role="ref"} the
`First Interview`{.interpreted-text role="guilabel"} stage, and select
the `Recruitment: Schedule Interview`{.interpreted-text role="guilabel"}
option in the `Email Template`{.interpreted-text role="guilabel"} field,
to automate this action.
:::

Second interview {#recruitment/second-interview}
----------------

After an applicant has passed the `First Interview`{.interpreted-text
role="guilabel"} stage, they can be moved to the
`Second Interview`{.interpreted-text role="guilabel"} stage. To move the
applicant to the next stage, drag-and-drop the applicant\'s card to the
`Second Interview`{.interpreted-text role="guilabel"} stage from the
Kanban view of the `Applications`{.interpreted-text role="guilabel"}
page, or click on the `Second Interview`{.interpreted-text
role="guilabel"} stage at the top of the individual applicant\'s card.

When the applicant\'s card moves to the
`Second Interview`{.interpreted-text role="guilabel"} stage, there are
no automatic activities or emails configured for this stage, by default.
The recruiter can now `schedule a
second interview <recruitment/schedule_interviews/recruitment-scheduled>`{.interpreted-text
role="ref"} with the applicant, following the same process as the first
interview.

Contract Proposal {#recruitment/contract-proposal}
-----------------

After the applicant has completed the various interview processes, the
next step is to `send
the job offer <offer_job_positions>`{.interpreted-text role="doc"}.

Once the offer has been sent, drag-and-drop the applicant\'s card to the
`Contract
Proposal`{.interpreted-text role="guilabel"} stage from the Kanban view
of the `Applications`{.interpreted-text role="guilabel"} page, or click
on the `Contract Proposal`{.interpreted-text role="guilabel"} stage at
the top of the individual applicant\'s card.

Contract Signed
---------------

Once the contract has been signed, and the applicant has been hired, the
applicant\'s card moves to the `Contract Signed`{.interpreted-text
role="guilabel"} stage.

Drag-and-drop the applicant\'s card to the
`Contract Signed`{.interpreted-text role="guilabel"} stage from the
Kanban view of the `Applications`{.interpreted-text role="guilabel"}
page, or click the `fa-ellipsis-h`{.interpreted-text role="icon"}
`(ellipsis)`{.interpreted-text role="guilabel"} icon at the top of the
individual applicant\'s card, then click
`Contract Signed`{.interpreted-text role="guilabel"} on the status bar.

Refuse applicant
----------------

At any point in the recruitment process, a candidate can be
`refused <refuse_applicant>`{.interpreted-text role="doc"}.
