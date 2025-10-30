# File: /content/odoo_doc17.0/fr/content/applications/hr/recruitment/new_job.md

Job positions
=============

In Odoo *Recruitment*, all job positions are shown on the default
dashboard in the *Recruitment* app. This includes positions that are
being actively recruited for, as well as inactive positions.

Each job position is shown in an individual Kanban card. If the job
position is active, and candidates can apply, a
`Published`{.interpreted-text role="guilabel"} banner appears in the
top-right corner of the card.

View submitted applications by clicking anywhere on a job position card.

{.align-center}

Create a new job position
-------------------------

To create a new job position from the main dashboard in the
*Recruitment* app, click the `New`{.interpreted-text role="guilabel"}
button in the top-left corner, and a
`Create a Job Position`{.interpreted-text role="guilabel"} modal
appears.

First, enter the name of the `Job Position`{.interpreted-text
role="guilabel"} (such as [Sales Manager]{.title-ref}, [Mechanical
Engineer]{.title-ref}, etc.) in the field.

Next, enter an `Application email`{.interpreted-text role="guilabel"} by
typing in the first half of the email address in the first field, then
select the second half of the email using the drop-down menu in the
second field. Applicants can send a resumé to this specific email
address, and Odoo creates an application for them automatically.

When complete, click the `Create`{.interpreted-text role="guilabel"}
button to save the entry, or the `Discard`{.interpreted-text
role="guilabel"} button to delete it.

{.align-center}

Once the job position has been created, it appears as a card in the
Kanban view on the main *Recruitment* app dashboard.

### Edit a new job position {#recruitment/new_job_position/edit}

After the job position is created, it\'s time to enter the details for
the position. Click on the `⋮ (three dots)`{.interpreted-text
role="guilabel"} icon in the upper-right corner of the relevant card to
reveal several options, and then click `Configuration`{.interpreted-text
role="guilabel"} to edit the details.

{.align-center}

All the basic information about the job position is listed under the
`Recruitment`{.interpreted-text role="guilabel"} tab.

None of the fields are required, but it is important to configure and
populate the `Department`{.interpreted-text role="guilabel"},
`Location`{.interpreted-text role="guilabel"},
`Employment Type`{.interpreted-text role="guilabel"}, and `Job
Summary`{.interpreted-text role="guilabel"} fields, as they are all
visible to prospective applicants on the website.

The fields can be filled out as follows:

-   `Department`{.interpreted-text role="guilabel"}: select the relevant
    department for the job position. This is visible on the website.
-   `Job Location`{.interpreted-text role="guilabel"}: select the
    physical address for the job. If the job position is remote, leave
    this field blank. This is visible on the website.
-   `Email Alias`{.interpreted-text role="guilabel"}: enter an email
    address to which applicants can send a resumé. Once emailed, Odoo
    automatically creates an application for them.
-   `Employment Type`{.interpreted-text role="guilabel"}: select what
    type of position the job is, using the drop-down menu. The default
    options are `Permanent`{.interpreted-text role="guilabel"},
    `Temporary`{.interpreted-text role="guilabel"},
    `Seasonal`{.interpreted-text role="guilabel"},
    `Interim`{.interpreted-text role="guilabel"},
    `Full-Time`{.interpreted-text role="guilabel"}, and
    `Part-Time`{.interpreted-text role="guilabel"}. This is visible on
    the website.
-   `Company`{.interpreted-text role="guilabel"}: select the company the
    job is for. This field only appears if using a multi-company
    database.
-   `Target`{.interpreted-text role="guilabel"}: enter the number of
    employees to be hired for this position.
-   `Is Published`{.interpreted-text role="guilabel"}: activate this
    option to publish the job online.
-   `Website`{.interpreted-text role="guilabel"}: select the website the
    job is published on.
-   `Recruiter`{.interpreted-text role="guilabel"}: select the person
    responsible for recruiting this role.
-   `Interviewers`{.interpreted-text role="guilabel"}: select who should
    perform the interviews. Multiple people can be selected.
-   `Interview Form`{.interpreted-text role="guilabel"}: select an
    `Interview form <recruitment/interview>`{.interpreted-text
    role="ref"} that applicants fill out prior to their interview.
-   `Contract Template`{.interpreted-text role="guilabel"}: select a
    contract template to be used when offering the job to a candidate.
-   `Process Details`{.interpreted-text role="guilabel"} section: this
    section contains information that is displayed online for the job
    position. This informs the applicants of the timeline and steps for
    the recruitment process, so they know when to expect a reply.
    -   `Time to Answer`{.interpreted-text role="guilabel"}: enter the
        number of days before the applicant is contacted.
    -   `Process`{.interpreted-text role="guilabel"}: enter the various
        stages the candidate goes through during the recruitment
        process.
    -   `Days to get an Offer`{.interpreted-text role="guilabel"}: enter
        the number of days before the applicant should expect an offer
        after the recruitment process has ended.

::: {.note}
::: {.title}
Note
:::

The `Process Details`{.interpreted-text role="guilabel"} section is a
text field. All answers are typed in rather than selected from a
drop-down menu. The text is displayed on the website exactly as it
appears in this tab.
:::

Finally, enter the job description in the
`Job Summary`{.interpreted-text role="guilabel"} tab.

{.align-center}

### Create interview form {#recruitment/interview}

An *Interview Form* is used to determine if a candidate is a good fit
for a job position. Interview forms can be as specific or general as
desired, and can take the form of a certification, an exam, or a general
questionnaire. Interview forms are determined by the recruitment team.

Before creating an interview form, ensure the proper settings are
enabled. Navigate to
`Recruitment app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and under the
`Recruitment Process`{.interpreted-text role="guilabel"} section, ensure
the `Send Interview Survey`{.interpreted-text role="guilabel"} option is
enabled.

Since there are no pre-configured forms in Odoo, all interview forms
must be created. To create an interview form, start from the
`Recruitment`{.interpreted-text role="guilabel"} tab of the
`Job Position`{.interpreted-text role="guilabel"} form. In the
`Interview Form`{.interpreted-text role="guilabel"} field, enter a name
for the new interview form. As the name is typed, several options
populate beneath the entry:
`Create (interview form name)`{.interpreted-text role="guilabel"},
`Search More...`{.interpreted-text role="guilabel"}, and
`Create and edit...`{.interpreted-text role="guilabel"}. Click
`Create and edit...`{.interpreted-text role="guilabel"} and a
`Create Interview Form`{.interpreted-text role="guilabel"} modal
appears.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The option `Search More...`{.interpreted-text role="guilabel"} only
appears if there are any interview forms already created. If no
interview forms exist, the only options available are `Create (interview
form name)`{.interpreted-text role="guilabel"}, and
`Create and edit...`{.interpreted-text role="guilabel"}.
:::

Proceed to fill out the modal interview form as a typical survey. For
specific directions on how to create a survey, refer to the
`survey essentials <../../marketing/surveys/create>`{.interpreted-text
role="doc"} document, which provides step-by-step instructions on how to
create and configure a survey.
