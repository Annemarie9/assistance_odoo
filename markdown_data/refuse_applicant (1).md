# File: /content/odoo_doc17.0/fr/content/applications/hr/recruitment/refuse_applicant.md

Refuse applicants
=================

At any point in the recruitment process, an applicant can be refused for
a job position.

To refuse an applicant, start by navigating to the applicant\'s card in
the *Recruitment* app. This is done in one of two ways:

-   Navigate to
    `Recruitment app --> Applications --> All Applications`{.interpreted-text
    role="menuselection"}. In the `Applications`{.interpreted-text
    role="guilabel"} list, click anywhere on the desired applicant\'s
    line to open that specific applicant\'s card.
-   Navigate to the main *ob Positions* dashboard by navigating to
    `Recruitment app
    --> Applications --> By Job Position`{.interpreted-text
    role="menuselection"}. Next, click on the desired job position card,
    then click on the individual applicant card from the
    `Applications`{.interpreted-text role="guilabel"} page.

At the top of the applicant\'s card, there are several buttons. Click
the one labeled `Refuse`{.interpreted-text role="guilabel"}.

Refuse reasons {#recruitment/refuse-reasons}
--------------

*Refuse reasons* allow recruiters to document why an applicant was not a
good fit, and send specific refusal reason email templates to the
applicant.

Clicking `Refuse`{.interpreted-text role="guilabel"} on an applicant\'s
form makes the `Refuse Reason`{.interpreted-text role="guilabel"} pop-up
window appear.

The default refuse reasons in Odoo, and their corresponding email
templates, are:

+----------------------------------+----------------------------------+
| Email Template                   | Refusal Reason                   |
+==================================+==================================+
| `Recrui                          | | `Doesn't fit the job           |
| tment: Refuse`{.interpreted-text |  requirements`{.interpreted-text |
| role="guilabel"}                 |   role="guilabel"}               |
|                                  | | `La                            |
|                                  | nguage issues`{.interpreted-text |
|                                  |   role="guilabel"}               |
|                                  | | `Role alre                     |
|                                  | ady fulfilled`{.interpreted-text |
|                                  |   role="guilabel"}               |
|                                  | | `Duplicate`{.interpreted-text  |
|                                  |   role="guilabel"}               |
|                                  | | `Spam`{.interpreted-text       |
|                                  |   role="guilabel"}               |
+----------------------------------+----------------------------------+
| `Recruitment: Not inter          | | `Refused by Applicant: d       |
| ested anymore`{.interpreted-text | on't like job`{.interpreted-text |
| role="guilabel"}                 |   role="guilabel"}               |
|                                  | | `Refused by Applicant:         |
|                                  |  better offer`{.interpreted-text |
|                                  |   role="guilabel"}               |
|                                  | | `Refused by Appl               |
|                                  | icant: salary`{.interpreted-text |
|                                  |   role="guilabel"}               |
+----------------------------------+----------------------------------+

Additional refusal reasons
`can be created, and existing ones can be modified (or deleted)
<recruitment/new-refuse>`{.interpreted-text role="ref"}.

Select a refusal reason to
`send a refusal email <recruitment/send-refusal-email>`{.interpreted-text
role="ref"}.

### Create or modify refuse reasons {#recruitment/new-refuse}

To view and configure refuse reasons, navigate to
`Recruitment app --> Configuration
--> Applications: Refuse Reasons`{.interpreted-text
role="menuselection"}. Doing so reveals the
`Refuse Reasons`{.interpreted-text role="guilabel"} page, where all the
existing refuse reasons are listed.

To create a new refuse reason from the
`Refuse Reasons`{.interpreted-text role="guilabel"} page, click the
`New`{.interpreted-text role="guilabel"} button in the top-left corner.
A blank line appears at the bottom of the list, with an empty field
present in the `Description`{.interpreted-text role="guilabel"} column.

Type in the new refuse reason in the field. It is recommended to enter a
reason that is short and concise, such as [Offer expired]{.title-ref} or
[Withdrew application]{.title-ref}.

Then, in the `Email Template`{.interpreted-text role="guilabel"} field,
click on the field to reveal a drop-down menu. Select an
`Email Template`{.interpreted-text role="guilabel"} from the list to be
used when this refuse reason is selected.

If a new `Email Template`{.interpreted-text role="guilabel"} is desired,
type in the name for the new template in the field. Then, click
`Create and edit...`{.interpreted-text role="guilabel"}, and a
`Create Email Template`{.interpreted-text role="guilabel"} form pop-up
window appears.

In the `Create Email Template`{.interpreted-text role="guilabel"} pop-up
window, enter a `Name`{.interpreted-text role="guilabel"} for the form,
and an email `Subject`{.interpreted-text role="guilabel"} in the
corresponding fields.

Enter the desired email content in the `Content`{.interpreted-text
role="guilabel"} tab. Proceed to make any other modifications to the
template in the `Email Configuration`{.interpreted-text role="guilabel"}
and `Settings`{.interpreted-text role="guilabel"} tabs, then click
`Save & Close`{.interpreted-text role="guilabel"} to save the template.
Upon clicking that, Odoo returns to the
`Refuse Reasons`{.interpreted-text role="guilabel"} list.

The new template appears in the new refuse reason
`Email Template`{.interpreted-text role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

Pre-configured recruitment refusal email templates in Odoo use dynamic
placeholders, which are personalized placeholders that populate data
from the applicant\'s record in the email body.

For example, if the applicant\'s name is a used in a dynamic
placeholder, the applicant\'s name appears anytime that dynamic
placeholder appears on the email template.

For more detailed information on email templates, refer to the
`../../general/companies/email_template`{.interpreted-text role="doc"}
documentation.
:::

Send refusal email {#recruitment/send-refusal-email}
------------------

After clicking the `Refuse`{.interpreted-text role="guilabel"} button on
an applicant form, a `Refuse Reason
<recruitment/refuse-reasons>`{.interpreted-text role="ref"} can be
selected from the `refuse reason`{.interpreted-text role="guilabel"}
pop-up window. Then, two fields appear below the selected refusal
reason: `Send Email`{.interpreted-text role="guilabel"} and
`Email Template`{.interpreted-text role="guilabel"}.

{.align-center}

The applicant\'s email address automatically populates the
`Send Email`{.interpreted-text role="guilabel"} field; additional email
recipients **cannot** be added.

If an email should **not** be sent to the applicant, uncheck the
`Send Email`{.interpreted-text role="guilabel"} checkbox.

The email template associated with the refusal reason populates the
`Email Template`{.interpreted-text role="guilabel"} field. If a
different email template is desired, select a different template from
the `Email Template`{.interpreted-text role="guilabel"} drop-down menu.

To send the refusal email to the applicant, ensure the
`Send Email`{.interpreted-text role="guilabel"} checkbox is ticked, then
click `Refuse`{.interpreted-text role="guilabel"} at the bottom of the
`Refuse Reason`{.interpreted-text role="guilabel"} pop-up window. The
refusal email is sent to the applicant, and a red
`Refused`{.interpreted-text role="guilabel"} banner appears on the
applicant\'s card in the top-right corner.

{.align-center}

View refused applicants
-----------------------

After refusal, the applicant\'s card is no longer visible in the job
position\'s Kanban view. However, it is still possible to view
applicants who have been refused.

To view only the refused applicants, go to
`Recruitment app --> Applications --> By
Job Positions`{.interpreted-text role="menuselection"}, or
`Recruitment app --> Applications --> All Applications`{.interpreted-text
role="menuselection"}.

On the `Applications`{.interpreted-text role="guilabel"} page, click the
`fa-caret-down`{.interpreted-text role="icon"}
`(caret down)`{.interpreted-text role="guilabel"} button in the
`Search...`{.interpreted-text role="guilabel"} bar, then click
`Refused`{.interpreted-text role="guilabel"}, located under the
`Filters`{.interpreted-text role="guilabel"} section.

All applicants that have been refused for the job position appear on the
`Applications`{.interpreted-text role="guilabel"} page for that
position, organized by the stage they were in when they were refused.
