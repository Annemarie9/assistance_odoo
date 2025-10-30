# File: /content/odoo_doc17.0/fr/content/applications/hr/recruitment/add-new-applicants.md

Add new applicants
==================

Once an applicant submits an application, either using the online
application, or emailing a job position alias, an applicant card is
automatically created in the *Recruitment* application.

However, in some instances, applicants may need to be created manually
in the database. This could be necessary if, for example, a company
accepts paper applications in the mail, or is meeting prospective
applicants at an in-person job fair.

To view current applicants, navigate to the
`Recruitment`{.interpreted-text role="menuselection"} app, then click
the desired job position card. Doing so reveals the
`Applications`{.interpreted-text role="guilabel"} page, which displays
all applicants for that specific role, in a default Kanban view,
organized by stage.

Add new applicants from a job position\'s
`Applications`{.interpreted-text role="guilabel"} page by using either:
the `New <recruitment/create-new-applicant>`{.interpreted-text
role="ref"} button or the `quick add
<recruitment/quick-add-applicant>`{.interpreted-text role="ref"} button.

Quick add {#recruitment/quick-add-applicant}
---------

On the `Applications`{.interpreted-text role="guilabel"} page, click the
on the quick add button, represented by a small
`fa-plus`{.interpreted-text role="icon"} `(plus)`{.interpreted-text
role="guilabel"} icon in the top-right corner of each stage to quickly
add a new applicant to that stage.

Enter the following information on the card:

-   `Subject/Application`{.interpreted-text role="guilabel"}: enter the
    title for the card. Typically, this is the applicant\'s name, and
    job position being applied to. For example: [Laura Smith - HR
    Manager]{.title-ref}. The text entered in this field is **not**
    visible in the Kanban view of the `Applications`{.interpreted-text
    role="guilabel"} page, unless the
    `Applicant's Name`{.interpreted-text role="guilabel"} field is left
    blank.
-   `Applicant's Name`{.interpreted-text role="guilabel"}: enter the
    applicant\'s name. Displays as the card title in the Kanban view of
    the `Applications`{.interpreted-text role="guilabel"} page.
-   `Email`{.interpreted-text role="guilabel"}: enter the applicant\'s
    email address.
-   `Applied Job`{.interpreted-text role="guilabel"}: the current job
    position populates this field. If needed, the job position can be
    changed by selecting a different position from the drop-down menu.
    If a different job position is selected, after the card is created,
    the card appears on the `Applications`{.interpreted-text
    role="guilabel"} page for that newly-selected job position.

After the information is entered, click `Add`{.interpreted-text
role="guilabel"}. The applicant appears in the list, and a new blank
applicant card appears.

If preferred, after entering the `Applicant's Name`{.interpreted-text
role="guilabel"} in the Kanban card that appears, click
`Edit`{.interpreted-text role="guilabel"}, and a detailed applicant form
loads. Refer to the `New applicant form
<recruitment/applicant-details>`{.interpreted-text role="ref"} section
for details about filling out the form.

When doing a quick add, clicking away from an empty card, or clicking
the `fa-trash-o`{.interpreted-text role="icon"}
(`trash`{.interpreted-text role="guilabel"}) icon, discards the
applicant.

{.align-center}

New applicant form {#recruitment/create-new-applicant}
------------------

On the new applicant form, the `Subject / Application`{.interpreted-text
role="guilabel"} field is populated with the pre-selected job position,
by default. Certain fields on the applicant card may also be
pre-populated, depending on how the job position is configured.
Typically, the `Job`{.interpreted-text role="guilabel"} section, as well
as the `Recruiter`{.interpreted-text role="guilabel"} field, are
pre-populated.

Complete the fields in the following sections on the new applicant form.

::: {.note}
::: {.title}
Note
:::

Depending on installed applications and configurations, some fields may
**not** be displayed.
:::

{.align-center}

### Applicant section {#recruitment/applicant-details}

-   `Subject/Application Name`{.interpreted-text role="guilabel"}: this
    is the **only** required field. Enter the title for the card in this
    field. Typically, this is the applicant\'s name, and the job
    position being applied to. For example: [John Smith - Experienced
    Developer]{.title-ref}. This field is **not** visible in the Kanban
    view of the `Applications`{.interpreted-text role="guilabel"} page,
    unless the `Applicant's Name`{.interpreted-text role="guilabel"} is
    left blank.
-   `Applicant's Name`{.interpreted-text role="guilabel"}: enter the
    applicant\'s name. This field is displayed as the card title in the
    Kanban view of the `Applications`{.interpreted-text role="guilabel"}
    page.
-   `Email`{.interpreted-text role="guilabel"}: enter the applicant\'s
    email address.
-   `Phone`{.interpreted-text role="guilabel"}: enter the applicant\'s
    phone number.
-   `Mobile`{.interpreted-text role="guilabel"}: enter the applicant\'s
    mobile number.
-   `LinkedIn Profile`{.interpreted-text role="guilabel"}: enter the web
    address for the applicant\'s personal profile on LinkedIn.
-   `Degree`{.interpreted-text role="guilabel"}: select the applicant\'s
    highest level of education from the drop-down menu. Options are:
    `Graduate`{.interpreted-text role="guilabel"},
    `Bachelor Degree`{.interpreted-text role="guilabel"},
    `Master Degree`{.interpreted-text role="guilabel"}, or
    `Doctoral Degree`{.interpreted-text role="guilabel"}. The
    `Graduate`{.interpreted-text role="guilabel"} option indicates the
    applicant graduated at the highest level of school before a
    Bachelor\'s degree, such as a high school or secondary school
    diploma, depending on the country.
-   `Interviewers`{.interpreted-text role="guilabel"}: using the
    drop-down menu, select the people to conduct the interviews. The
    selected people **must** have either *recruiter* or *officer* rights
    configured for the *Recruitment* application to appear in the
    drop-down list. Refer to the `Access rights
    <../../general/users/access_rights>`{.interpreted-text role="doc"}
    documentation for more information.
-   `Recruiter`{.interpreted-text role="guilabel"}: select the user
    responsible for the entire recruitment process for the job position.
-   `Evaluation`{.interpreted-text role="guilabel"}: represents a rating
    for the applicant: one star (`fa-star`{.interpreted-text
    role="icon"} `fa-star-o`{.interpreted-text role="icon"}
    `fa-star-o`{.interpreted-text role="icon"}) is
    `Good`{.interpreted-text role="guilabel"}, two stars
    (`fa-star`{.interpreted-text role="icon"}
    `fa-star`{.interpreted-text role="icon"}
    `fa-star-o`{.interpreted-text role="icon"}) is
    `Very Good`{.interpreted-text role="guilabel"}, and three stars
    (`fa-star`{.interpreted-text role="icon"}
    `fa-star`{.interpreted-text role="icon"} `fa-star`{.interpreted-text
    role="icon"})is `Excellent.`{.interpreted-text role="guilabel"}
-   `Source`{.interpreted-text role="guilabel"}: using the drop-down
    menu, select where the applicant learned about the job position. The
    following options come pre-configured in Odoo:
    `Search engine`{.interpreted-text role="guilabel"},
    `Lead Recall`{.interpreted-text role="guilabel"},
    `Newsletter`{.interpreted-text role="guilabel"},
    `Facebook`{.interpreted-text role="guilabel"},
    `Twitter`{.interpreted-text role="guilabel"},
    `LinkedIn`{.interpreted-text role="guilabel"},
    `Monster`{.interpreted-text role="guilabel"},
    `Glassdoor`{.interpreted-text role="guilabel"}, and
    `Craigslist`{.interpreted-text role="guilabel"}. To add a new
    `Source`{.interpreted-text role="guilabel"}, type in the source,
    then click `Create "(new source)"`{.interpreted-text
    role="guilabel"}.
-   `Medium`{.interpreted-text role="guilabel"}: using the drop-down
    menu, specify how the job listing was found. The pre-configured
    options are: `Banner`{.interpreted-text role="guilabel"},
    `Direct`{.interpreted-text role="guilabel"},
    `Email`{.interpreted-text role="guilabel"},
    `Facebook`{.interpreted-text role="guilabel"},
    `Google Adwords`{.interpreted-text role="guilabel"},
    `LinkedIn`{.interpreted-text role="guilabel"},
    `Phone`{.interpreted-text role="guilabel"},
    `Television`{.interpreted-text role="guilabel"},
    `Twitter`{.interpreted-text role="guilabel"} (now known as \"X\"),
    or `Website`{.interpreted-text role="guilabel"}. To add a new
    `Medium`{.interpreted-text role="guilabel"}, type in the medium,
    then click `Create "(new medium)"`{.interpreted-text
    role="guilabel"}.
-   `Referred By User`{.interpreted-text role="guilabel"}: if referral
    points are to be earned for this job position in the *Referrals*
    application, select the user who referred the applicant from the
    drop-down menu. The *Referrals* application **must** be installed
    for this field to appear.
-   `Availability`{.interpreted-text role="guilabel"}: select the
    available start date for the applicant. To select a date, click on
    the field to reveal a popover calendar. Use the
    `fa-angle-left`{.interpreted-text role="icon"}
    `(left)`{.interpreted-text role="guilabel"} and
    `fa-angle-right`{.interpreted-text role="icon"}
    `(right)`{.interpreted-text role="guilabel"} arrows on either side
    of the month to navigate to the desired month, then click the
    desired date. Leaving this field blank indicates the applicant can
    start immediately.
-   `Tags`{.interpreted-text role="guilabel"}: select as many tags as
    desired from the drop-down menu. To add a tag that does not exist,
    type in the tag name, then click
    `Create "new tag"`{.interpreted-text role="guilabel"} from the
    resulting drop-down menu.

### Job section

The following fields are pre-populated when creating a new applicant, as
long as these field are specified on the job position form. Editing the
fields is possible, if desired.

-   `Applied Job`{.interpreted-text role="guilabel"}: select the job
    position the applicant is applying to from the drop-down menu.
-   `Department`{.interpreted-text role="guilabel"}: select the
    department the job position falls under from the drop-down menu.
-   `Company`{.interpreted-text role="guilabel"}: select the company the
    job position is for using the drop-down menu. This field **only**
    appears when in a multi-company database.

### Contract section

-   `Expected Salary`{.interpreted-text role="guilabel"}: enter the
    amount the applicant is requesting in this field. The number should
    be in a [XX,XXX.XX]{.title-ref} format. The currency is determined
    by the localization setting for the company.
    -   `Extra advantages...`{.interpreted-text role="guilabel"}: if any
        extra advantages are requested by the applicant, enter it in the
        `Extra advantages...`{.interpreted-text role="guilabel"} field
        to the right of the `Expected Salary`{.interpreted-text
        role="guilabel"} field. This should be short and descriptive,
        such as [1 week extra vacation]{.title-ref} or [dental
        plan]{.title-ref}.
-   `Proposed Salary`{.interpreted-text role="guilabel"}: enter the
    amount to be offered to the applicant for the role in this field.
    The number should be in a [XX,XXX.XX]{.title-ref} format.
    -   `Extra advantages...`{.interpreted-text role="guilabel"}: if any
        extra advantages are offered to the applicant, enter it in the
        `Extra advantages...`{.interpreted-text role="guilabel"} field
        to the right of the `Proposed Salary`{.interpreted-text
        role="guilabel"} field. This should be short and descriptive,
        such as [unlimited sick time]{.title-ref} or [retirement
        plan]{.title-ref}.

### Application Summary tab

Any additional details or notes that should be added to the applicant\'s
card can be typed into this field.

### Skills tab

Skills can be added to the applicant\'s card. For details on adding
skills, refer to the
`Create new employees <employees/skills>`{.interpreted-text role="ref"}
document.
