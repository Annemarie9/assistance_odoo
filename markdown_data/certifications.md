# File: /content/odoo_doc17.0/fr/content/applications/hr/employees/certifications.md

Certifications
==============

When jobs require specific knowledge, it is necessary to track employee
certifications to ensure the necessary knowledge and certifications are
in place.

Certifications include classes, tests, professional seminars, and more.
There are no restrictions in terms of what type of certification records
can be added in Odoo.

::: {.important}
::: {.title}
Important
:::

To access the *Employee Certifications* report, the **Surveys** app
**must** be installed.
:::

View certifications
-------------------

To view a full list of all employee certifications, navigate to
`Employees app -->
Reporting --> Certifications`{.interpreted-text role="menuselection"}.

All certifications appear in a list view, grouped by employee. Each
certification entry displays the following:

-   `Employee`{.interpreted-text role="guilabel"}: the employee\'s name,
    along with their avatar image.
-   `Name`{.interpreted-text role="guilabel"}: the title of the
    certification.
-   `Validity Start`{.interpreted-text role="guilabel"}: when the
    employee received the certification.
-   `Validity End`{.interpreted-text role="guilabel"}: when the
    certification expires.
-   `Certification`{.interpreted-text role="guilabel"}: the
    corresponding course in the **Surveys** app that was completed by
    the employee, if applicable.

The entries are also color-coded. Current certifications that are still
valid appear in black, expired certifications appear in red, and
certifications that are going to expire within the next 90 days appear
in orange.

{.align-center}

::: {.important}
::: {.title}
Important
:::

**Only** certification records with the *Display Type* set to
*Certification* on their
`certification form <employees/certifications-form>`{.interpreted-text
role="ref"} appear on the `Employee
Certifications`{.interpreted-text role="guilabel"} report. All other
certifications appear in the resume section of the
`employee form <new_employee>`{.interpreted-text role="doc"}.
:::

### View certifications by expiration status

When managing a large number of employees with a variety of
certifications, it can be difficult to determine which employees need to
keep necessary certifications current in the default list view. In this
scenario, it is beneficial to view the certifications by expiration
status.

To do so, navigate to
`Employees app --> Reporting --> Certifications`{.interpreted-text
role="menuselection"}. Next, click the `fa-caret-down`{.interpreted-text
role="icon"} `(down arrow)`{.interpreted-text role="guilabel"} in the
search bar, then click `Add
Custom Group`{.interpreted-text role="guilabel"}, revealing a drop-down
menu. Click `Expiration Status`{.interpreted-text role="guilabel"}, then
click away from the drop-down menu to close it.

After doing so, all the certifications are organized by status, starting
with `Expired`{.interpreted-text role="guilabel"} certifications, then
certifications that are `Expiring`{.interpreted-text role="guilabel"}
soon (within the next 90 days), and lastly, certifications that are
still `Valid`{.interpreted-text role="guilabel"}.

This view provides an easy way to see which employees have
certifications that are going to expire soon, to determine which
employees need to take action to keep their certifications current.

{.align-center}

Log a certification {#employees/certifications-form}
-------------------

To log a certification for an employee, navigate to
`Employees app --> Reporting -->
Certifications`{.interpreted-text role="menuselection"}. Click
`New`{.interpreted-text role="guilabel"}, and a blank certification form
loads. Enter the following information on the form:

-   `Title`{.interpreted-text role="guilabel"}: Enter a short
    description for the certification in this field.

-   `Employee`{.interpreted-text role="guilabel"}: Using the drop-down
    menu, select the employee who received the certification.

-   `Type`{.interpreted-text role="guilabel"}: Using the drop-down menu,
    select the type of certification received. This field determines
    where on the employee\'s resume the certification appears. To create
    a new `Type`{.interpreted-text role="guilabel"}, enter the type in
    the field, then click `Create "type"`{.interpreted-text
    role="guilabel"}.

    The default options are:

    -   `Experience`{.interpreted-text role="guilabel"}: Select this
        option to have the certification appear in the *Experience*
        section of the *Resume* tab on the
        `employee form <new_employee>`{.interpreted-text role="doc"}.
    -   `Education`{.interpreted-text role="guilabel"}: Select this
        option to have the certification appear in the *Education*
        section of the *Resume* tab on the
        `employee form <new_employee>`{.interpreted-text role="doc"}.
    -   `Internal Certification`{.interpreted-text role="guilabel"}:
        Select this option to have the certification appear in the
        *Internal Certification* section of the *Resume* tab on the
        `employee form <new_employee>`{.interpreted-text role="doc"}.
    -   `Completed Internal Training`{.interpreted-text
        role="guilabel"}: Select this option to have the certification
        appear in *Completed Internal Training* section of the *Resume*
        tab on the `employee form
        <new_employee>`{.interpreted-text role="doc"}.

-   `Display Type`{.interpreted-text role="guilabel"}: Select the
    visibility of the certification in this field. The default options
    are:

    -   `Classic`{.interpreted-text role="guilabel"}: Select this option
        to have the certification appear in the *Resume* section of the
        employee form, and **not** appear on the *Employee
        Certifications* report.
    -   `Course`{.interpreted-text role="guilabel"}: Select this option
        to have the certification appear in the *Resume* section of the
        employee form, and **not** appear on the *Employee
        Certifications* report. Once this option is selected, a
        `Course`{.interpreted-text role="guilabel"} field appears
        beneath the `Display Type`{.interpreted-text role="guilabel"}
        field. Using the drop-down menu, select the course the employee
        took. The course is created in the **Surveys** app.
    -   `Certification`{.interpreted-text role="guilabel"}: Select this
        option to have the certification appear in the *Resume* section
        of the employee form, **and** appear on the *Employee
        Certifications* report. Once this is selected, a
        `Certification`{.interpreted-text role="guilabel"} field appears
        beneath the `Display
        Type`{.interpreted-text role="guilabel"} field. Using the
        drop-down menu, select the certification the employee took.

-   `Description`{.interpreted-text role="guilabel"}: Enter a
    description for the certification in this field.

-   `Duration`{.interpreted-text role="guilabel"}: Click into the first
    field, and a calendar pop-over window appears. Click on the start
    and end dates for the certification validity period. When the
    correct dates are selected, click `fa-check`{.interpreted-text
    role="icon"} `Apply`{.interpreted-text role="guilabel"}, and both
    fields are populated.

{.align-center}
