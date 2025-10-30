# File: /content/odoo_doc17.0/fr/content/applications/hr/payroll/contracts.md

Contracts
=========

Every employee in Odoo is required to have a contract in order to be
paid. A contract outlines the terms of an employee\'s position, their
compensation, working hours, and any other details about their position.

::: {.important}
::: {.title}
Important
:::

Contract documents (PDFs) are uploaded and organized using the
*Documents* application, and are signed using the *Sign* application.
Ensure these applications are installed to send and sign contracts.
Please refer to the `../../productivity/documents`{.interpreted-text
role="doc"} and `../../productivity/sign`{.interpreted-text role="doc"}
documentation.
:::

To view the employee contracts, go to the
`Payroll app --> Contracts --> Contracts`{.interpreted-text
role="menuselection"} from the top menu. All employee contracts, and
their current contract status, are displayed in a Kanban view, by
default. The Kanban view displays running contracts, contracts that
require action, expired contracts, and cancelled contracts.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The list of contracts in the *Payroll* application matches the list of
contracts in the *Employees* application.
:::

::: {#payroll/new-contract}
In order for an employee to be paid, an active contract is required. If
a new contract is needed, click the `Create`{.interpreted-text
role="guilabel"} button on the `Contracts`{.interpreted-text
role="guilabel"} dashboard. A contract form appears where the
information can be entered. Required fields are underlined in bold.
:::

New contract form
-----------------

General information section {#payroll/gen-info}
---------------------------

-   `Contact Reference`{.interpreted-text role="guilabel"}: type in the
    name or title for the contract, such as [John Smith
    Contract]{.title-ref}. This field is **required**.

-   `Employee`{.interpreted-text role="guilabel"}: using the drop-down
    menu, select the employee that the contract applies to.

-   `Contract Start Date`{.interpreted-text role="guilabel"}: the date
    the contract starts. To choose a date, click the drop-down menu,
    navigate to the correct month and year with the
    `< > (arrow)`{.interpreted-text role="guilabel"} icons, then click
    on the desired date. This field is **required**.

-   `Contract End Date`{.interpreted-text role="guilabel"}: if the
    contract has a specific end date, click the drop-down menu, navigate
    to the correct month and year with the
    `< > (arrow)`{.interpreted-text role="guilabel"} icons, then click
    on the desired date.

-   `Working Schedule`{.interpreted-text role="guilabel"}: select one of
    the working schedules from the drop-down menu. This field is
    **required**.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    The `Working Schedule`{.interpreted-text role="guilabel"} drop-down
    menu displays all the working schedules for the selected company. To
    modify or add to this list, go to `Payroll app -->
    Configuration --> Working Schedules`{.interpreted-text
    role="menuselection"}. Click `New`{.interpreted-text
    role="guilabel"}, and create a new working schedule, or click on an
    existing working schedule and make edits.
    :::

-   `Work Entry Source`{.interpreted-text role="guilabel"}: select how
    the `work entries <work_entries>`{.interpreted-text role="doc"} are
    generated. This field is **required**. Click the radio button next
    to the desired selection. The options are:

    -   `Working Schedule`{.interpreted-text role="guilabel"}: work
        entries are generated based on the selected
        `Working Schedule`{.interpreted-text role="guilabel"}.
    -   `Attendances`{.interpreted-text role="guilabel"}: work entries
        are generated based on the employee\'s check-in records in the
        *Attendances* application. (This requires the *Attendances*
        application).
    -   `Planning`{.interpreted-text role="guilabel"}: work entries are
        generated based on the planned schedule for the employee from
        the *Planning* application. (This requires the *Planning*
        application).

-   `Salary Structure Type`{.interpreted-text role="guilabel"}: select
    one of the salary structure types from the drop-down menu. The
    default salary structure types are `Employee`{.interpreted-text
    role="guilabel"} or `Worker`{.interpreted-text role="guilabel"}. A
    `new salary structure type <payroll/new-structure-type>`{.interpreted-text
    role="ref"} can be created, if needed.

-   `Department`{.interpreted-text role="guilabel"}: select the
    department the contract applies to from the drop-down menu.

-   `Job Position`{.interpreted-text role="guilabel"}: select the
    specific job position the contract applies to from the drop-down
    menu.

    ::: {.note}
    ::: {.title}
    Note
    :::

    If the selected `Job Position`{.interpreted-text role="guilabel"}
    has a contract template linked to it with a specific
    `Salary Structure Type`{.interpreted-text role="guilabel"}, the
    `Salary Structure Type`{.interpreted-text role="guilabel"} changes
    to the one associated with that `Job Position`{.interpreted-text
    role="guilabel"}.
    :::

-   `Wage on Payroll`{.interpreted-text role="guilabel"}: enter the
    employee\'s monthly wage.

-   `Contract Type`{.interpreted-text role="guilabel"}: choose either
    `Permanent`{.interpreted-text role="guilabel"},
    `Temporary`{.interpreted-text role="guilabel"},
    `Seasonal`{.interpreted-text role="guilabel"},
    `Full-Time`{.interpreted-text role="guilabel"}, or
    `Part-Time`{.interpreted-text role="guilabel"} from the drop-down
    menu.

{.align-center}

-   `Contact Reference`{.interpreted-text role="guilabel"}: type in the
    name or title for the contract, such as [John Smith
    Contract]{.title-ref}. This field is **required**.
-   `Employee`{.interpreted-text role="guilabel"}: name of the employee
    the contract applies to.
-   `Contract Start Date`{.interpreted-text role="guilabel"}: the date
    the contract starts. Choose a date by clicking on the drop-down
    menu, navigating to the correct month and year by using the
    `fa-chevron-left`{.interpreted-text role="icon"}
    `fa-chevron-right`{.interpreted-text role="icon"}
    `(arrow)`{.interpreted-text role="guilabel"} icons, then clicking on
    the desired date. This field is **required**.
-   `Contract End Date`{.interpreted-text role="guilabel"}: the date the
    contract ends. Choose a date by clicking on the drop-down menu,
    navigating to the correct month and year by using the
    `fa-chevron-left`{.interpreted-text role="icon"}
    `fa-chevron-right`{.interpreted-text role="icon"}
    `(arrow)`{.interpreted-text role="guilabel"} icons, then clicking on
    the desired date. This field is **required**.
-   `Salary Structure Type`{.interpreted-text role="guilabel"}: select
    one of the salary structure types from the drop-down menu. The
    default salary structure types are `Employee`{.interpreted-text
    role="guilabel"} or `Worker`{.interpreted-text role="guilabel"}. A
    new salary structure type can be created by typing the name in the
    field. This field is **required**.
-   `Working Schedule`{.interpreted-text role="guilabel"}: select one of
    the working schedules from the drop-down menu. This field is
    **required**.
-   `Department`{.interpreted-text role="guilabel"}: the department the
    contract applies to.
-   `Job Position`{.interpreted-text role="guilabel"}: the specific job
    position the contract applies to.
-   `Wage on Payroll`{.interpreted-text role="guilabel"}: the amount to
    be paid to the employee each month.
-   `Contract Type`{.interpreted-text role="guilabel"}: choose from
    `CDI`{.interpreted-text role="guilabel"}, `CDD`{.interpreted-text
    role="guilabel"}, or `PFI`{.interpreted-text role="guilabel"} from
    the drop-down menu.
    -   `CDI`{.interpreted-text role="guilabel"} is an open-ended
        contract with only a start date, but no end date.
    -   `CDD`{.interpreted-text role="guilabel"} is a contract with both
        a start date and an end date.
    -   `PFI`{.interpreted-text role="guilabel"} is a Belgian-specific
        contract used when hiring employees that need training, and
        covers the training period specifically.
-   `HR Responsible`{.interpreted-text role="guilabel"}: if there is a
    specific person in HR that is responsible for the contract, select
    the person from the drop-down menu. This field is required.

::: {.tip}
::: {.title}
Tip
:::

The `Working Schedule`{.interpreted-text role="guilabel"} drop-down menu
displays all the working times for the selected
`Company`{.interpreted-text role="guilabel"}. To modify or add to this
list, go to `Payroll app -->
Configuration --> Working Times`{.interpreted-text
role="menuselection"}, and either `Create`{.interpreted-text
role="guilabel"} a new working time, or click on an existing working
time, then edit it by clicking `Edit`{.interpreted-text
role="guilabel"}.
:::

-   `Yearly Cost (Real)`{.interpreted-text role="guilabel"}: this field
    automatically updates after the `Schedule
    Pay`{.interpreted-text role="guilabel"} and `Wage`{.interpreted-text
    role="guilabel"} fields are entered. This amount is the total yearly
    cost for the employer. This field can be modified. However, if this
    is modified, the `Wage`{.interpreted-text role="guilabel"} field
    updates, accordingly. Ensure both the `Wage`{.interpreted-text
    role="guilabel"} and `Yearly Cost (Real)`{.interpreted-text
    role="guilabel"} are correct if this field is modified.

-   `Monthly Cost (Real)`{.interpreted-text role="guilabel"}: this field
    automatically updates after the `Schedule
    Pay`{.interpreted-text role="guilabel"} and `Wage`{.interpreted-text
    role="guilabel"} fields are entered. This amount is the total
    monthly cost for the employer. This field **cannot** be modified,
    and is calculated based on the `Yearly
    Cost (Real)`{.interpreted-text role="guilabel"}.

    {.align-center}

Contract Details tab
--------------------

The `Contract Details`{.interpreted-text role="guilabel"} tab allows for
the addition and editing of a contract, along with specifying which
template to use when a new contract is created. These fields **must** be
populated in order to create a new contract.

::: {.important}
::: {.title}
Important
:::

To access the various contract template fields in the
`Contract Details`{.interpreted-text role="guilabel"} tab, the *Salary
Configurator* ([hr\_contract\_salary]{.title-ref}) module **must** be
`installed
<general/install>`{.interpreted-text role="ref"}.

When the *Salary Configurator* module is installed, the *Salary
Configurator - Holidays* and *Salary Configurator - Payroll* modules
install, as well.

Once the modules are installed, the database reverts to the main
dashboard.
:::

-   `Contract Template`{.interpreted-text role="guilabel"}: select a
    pre-existing contract template from the drop-down menu. Contract
    templates are typically created through the configuration menu, and
    stored in the *Documents* application.

### Sign section

-   `HR Responsible`{.interpreted-text role="guilabel"}: select the
    person who is responsible for validating the contract from the
    drop-down menu. This field is required.
-   `New Contract Document Template`{.interpreted-text role="guilabel"}:
    select a contract from the drop-down menu to be modified for this
    new employee contract. These documents are stored in the *Sign*
    application.
-   `Contract Update Document Template`{.interpreted-text
    role="guilabel"}: select a contract from the drop-down menu, if the
    employee has an existing contract that requires updating. These
    documents are stored in the *Sign* application.

::: {.important}
::: {.title}
Important
:::

The `HR Responsible`{.interpreted-text role="guilabel"},
`New Contract Document Template`{.interpreted-text role="guilabel"}, and
`Contract Update Document Template`{.interpreted-text role="guilabel"}
fields are only visible if the *Sign* application is installed, along
with the [hr\_contract\_salary]{.title-ref} and
[hr\_contract\_salary\_payroll]{.title-ref} `modules
<../../general/apps_modules>`{.interpreted-text role="doc"}. The *Sign*
application is where the contract templates are stored. This application
is required for an employee to sign any contract.
:::

### Accounting section

-   `Analytic Account`{.interpreted-text role="guilabel"}: select the
    account the contract affects from the drop-down menu. It is
    recommended to check with the accounting department to ensure the
    correct account is selected.

### Part Time section

-   `Part Time`{.interpreted-text role="guilabel"}: tick this box if the
    employee is working part-time. When active, additional fields
    appear:
    -   `% (Percentage)`{.interpreted-text role="guilabel"}: enter the
        percent of time the employee works as compared to a full-time
        employee.

    -   `Standard Calendar`{.interpreted-text role="guilabel"}: select
        the working hours that a typical full-time worker uses from the
        drop-down menu.

    -   `Part Time Work Entry Type`{.interpreted-text role="guilabel"}:
        select the work entry type that generates the balance of a
        full-time working schedule.

        ::: {.example}
        If a full-time employee works 40 hours a week, and the employee
        works 20, enter [50]{.title-ref} in the
        `% (Percentage)`{.interpreted-text role="guilabel"} field (50%
        of 40 hours = 20 hours). The employee generates twenty
        \(20\) hours of work entries under the work entry type
        [part-time]{.title-ref}, and another twenty (20) hours of work
        entries under the work entry type [generic time
        off]{.title-ref}, for a total of forty (40) hours worth of work
        entries.
        :::

### Notes section

-   `Notes`{.interpreted-text role="guilabel"}: a text field where any
    notes for the employee contract are entered for future reference.

{.align-center}

-   `Analytic Account`{.interpreted-text role="guilabel"}: this field
    allows a link between the contract and a specific analytic account
    for accounting purposes.
-   `Contract Template`{.interpreted-text role="guilabel"}: select a
    pre-existing contract template from the drop-down menu. Contract
    templates are typically created through the *Recruitment*
    application.
-   `New Contract Document Template`{.interpreted-text role="guilabel"}:
    select a contract from the drop-down menu to be modified for this
    new employee contract.
-   `Contract Update Document Template`{.interpreted-text
    role="guilabel"}: select a contract from the drop-down menu, if the
    employee has an existing contract that requires updating.
-   `Notes`{.interpreted-text role="guilabel"}: the notes field is a
    text field where any notes for the employee contract can be entered
    for future reference.

### Modify a contract template

Click the `fa-external-link`{.interpreted-text role="icon"}
`(external Link)`{.interpreted-text role="guilabel"} icon at the end of
either the `New Contract Document Template`{.interpreted-text
role="guilabel"} or
`Contract Update Document Template`{.interpreted-text role="guilabel"}
to open the corresponding contract template, and proceed to make any
desired changes.

Click the `Upload your file`{.interpreted-text role="guilabel"} button
next to the corresponding document, navigate to the file, then click
`Open`{.interpreted-text role="guilabel"} to select the document and add
it to the tab.

#### Modifying contract templates

Contracts templates can be modified at any point when changes are
needed.

-   `Tags`{.interpreted-text role="guilabel"}: select any tags
    associated with the contract.
-   `Signed Document Workspace`{.interpreted-text role="guilabel"}: this
    is where the signatures are stored. Choose a pre-configured
    workspace, or create a new one. To create a new `Signed Document
    Workspace`{.interpreted-text role="guilabel"}, type in the name of
    the workspace, then click either `Create`{.interpreted-text
    role="guilabel"} to add the new workspace, or
    `Create and Edit`{.interpreted-text role="guilabel"} to add the
    workspace and modify the workspace details.
-   `Signed Document Tags`{.interpreted-text role="guilabel"}: select or
    create any tags that are only associated with the signed contract,
    as opposed to the original unsigned contract.
-   `Redirect Link`{.interpreted-text role="guilabel"}: enter a redirect
    link for the employee to access the contract. A redirect link takes
    the user from one URL to another. In this case, it takes them to the
    newly-updated contract specifically written for them.
-   `Who can Sign`{.interpreted-text role="guilabel"}: select either
    `All Users`{.interpreted-text role="guilabel"} or
    `On Invitation`{.interpreted-text role="guilabel"}.
    -   `All Users`{.interpreted-text role="guilabel"}: any user in the
        organization can sign the contract.
    -   `On Invitation`{.interpreted-text role="guilabel"}: only users
        selected in this field can sign the contract.
-   `Invited Users`{.interpreted-text role="guilabel"}: select the
    person (or people) that can sign the document.
-   `Document`{.interpreted-text role="guilabel"}: the attached document
    can be replaced by clicking the `fa-pencil`{.interpreted-text
    role="icon"} `(pencil)`{.interpreted-text role="guilabel"} icon. A
    pop-up window appears, so another document can be selected for
    upload. The file **must** be a PDF. To remove the document, click
    the `fa-trash-o`{.interpreted-text role="icon"}
    `(trash can)`{.interpreted-text role="guilabel"} icon.

Once the edits are complete, click the `Save`{.interpreted-text
role="guilabel"} button. All the information for the selected contract
template populates the fields in the
`Salary Information`{.interpreted-text role="guilabel"} tab. Any
additional tabs, such as `Personal Documents`{.interpreted-text
role="guilabel"}, appears if applicable.

Salary information
------------------

{.align-center}

This section is where the specific salary details are defined. This
section is country-specific, so these fields vary, depending on where
the company is located.

Enter the amount in the various fields, or tick a checkbox to apply a
benefit. Some options that can be entered here include
`Group Insurance Sacrifice Rate`{.interpreted-text role="guilabel"} and
`Canteen Cost`{.interpreted-text role="guilabel"}, for example.

Some fields may be automatically filled in as other fields are entered.
For example, the `Yearly Cost (Real)`{.interpreted-text role="guilabel"}
and `Monthly Cost (Real)`{.interpreted-text role="guilabel"} updates
once the `Wage`{.interpreted-text role="guilabel"} is populated.

Personal documents
------------------

This tab **only** appears after an `Employee`{.interpreted-text
role="guilabel"} is selected, and houses any documents that are linked
to the employee on their employee record. Documents cannot be added to
this tab, this tab **only** shows documents that are already uploaded
and associated with the employee.

The available documents in this tab can be downloaded. Click the
`fa-download`{.interpreted-text role="icon"}
`(download)`{.interpreted-text role="guilabel"} icon next to the
document to download it.

Save and send the contract
--------------------------

Once a contract has been created and/or modified, save the contract by
clicking the `Save`{.interpreted-text role="guilabel"} button. Next, the
contract must be sent to the employee to be signed.

Click on one of the following buttons to send the contract to the
employee:

{.align-center}

-   `Generate Simulation Link`{.interpreted-text role="guilabel"}: this
    option is **only** for Belgian companies. Clicking this opens a
    pop-up window that contains the basic information from the contract,
    as well as a link for the contract when using the salary
    configurator. Click `Send`{.interpreted-text role="guilabel"} to
    send an email to the employee, so they can sign the contract.

At the bottom of the pop-up form is a
`Link Expiration Date`{.interpreted-text role="guilabel"}. This is the
timeframe that the contract offer is valid for. By default, this field
is pre-populated with [30 days]{.title-ref}, but it can be modified.

> ::: {.note}
> ::: {.title}
> Note
> :::
>
> In order to send a contract using the
> `Generate Simulation Link`{.interpreted-text role="guilabel"}, there
> **must** be a signature field in the contract PDF being sent to the
> employee, so they can sign it.
> :::

-   `Signature Request`{.interpreted-text role="guilabel"}: clicking
    this reveals a pop-up window, where an email can be typed to the
    employee. Select the document (such as a contract, NDA, or
    Homeworking Policy) from the drop-down menu, and fill out the email
    section. Click `Send`{.interpreted-text role="guilabel"} when the
    email is ready to be sent.

::: {.note}
::: {.title}
Note
:::

To send a contract using the
`Generate Simulation Link`{.interpreted-text role="guilabel"}, there
**must** be a signature field in the contract PDF being sent to the
employee, so they can sign it.
:::

Salary attachments
------------------

Any automatic deductions or allocations for an employee, such as child
support payments and wage garnishments, are referred to as a *salary
attachment*. This section is where all of these deductions or
allocations are set.

To add a new deduction, first navigate to
`Payroll app --> Contracts --> Salary
Attachments`{.interpreted-text role="menuselection"}. Next, click
`Create`{.interpreted-text role="guilabel"}, and a new salary attachment
form loads.

{.align-center}

Fill out the following fields on the form:

-   `Employee`{.interpreted-text role="guilabel"}: using the drop-down
    menu, select the employee the salary attachment applies to.
-   `Description`{.interpreted-text role="guilabel"}: enter a short
    description for the salary attachment, such as [Child
    Support]{.title-ref} or [529 Contribution]{.title-ref}.
-   `Type`{.interpreted-text role="guilabel"}: using the drop-down menu,
    select the type of salary attachment being created. Choose from:
    -   `Attachment of Salary`{.interpreted-text role="guilabel"}: any
        payments taken out towards something that is *not* child
        support. Typically any garnishments, such as lawsuit payments,
        payments toward taxes owed, etc.
    -   `Assignment of Salary`{.interpreted-text role="guilabel"}: any
        deduction that is not required, but voluntary, such as a pre-tax
        allocation to a college savings account.
    -   `Child Support`{.interpreted-text role="guilabel"}: any payments
        taken out specifically for child support.
-   `Start Date`{.interpreted-text role="guilabel"}: the date the salary
    attachment starts. Choose a date by clicking on the drop-down menu,
    navigating to the correct month and year by using the
    `fa-chevron-left`{.interpreted-text role="icon"}
    `fa-chevron-right`{.interpreted-text role="icon"}
    `(arrow)`{.interpreted-text role="guilabel"} icons, then clicking on
    the desired date. This field is **required**.
-   `Estimated End Date`{.interpreted-text role="guilabel"}: this field
    automatically populates after both the
    `Monthly Amount`{.interpreted-text role="guilabel"} and
    `Total Amount`{.interpreted-text role="guilabel"} fields are
    populated. This field is **not** modifiable.
-   `Document`{.interpreted-text role="guilabel"}: attach any documents
    relevant to the salary attachment. Click the
    `Upload Your File`{.interpreted-text role="guilabel"} button,
    navigate to the desired document in the file explorer, then click
    `Open`{.interpreted-text role="guilabel"} to select the document,
    and attach it to the form. To change the attached document, click
    the `fa-pencil`{.interpreted-text role="icon"}
    `(pencil)`{.interpreted-text role="guilabel"} icon, and select a
    different document. To remove a document, click the
    `fa-trash-o`{.interpreted-text role="icon"}
    `(trash can)`{.interpreted-text role="guilabel"} icon.
-   `Monthly Amount`{.interpreted-text role="guilabel"}: enter the
    amount to be taken out of the employee\'s paycheck every month for
    this specific salary attachment.
-   `Total Amount`{.interpreted-text role="guilabel"}: enter the total
    amount that the employee pays for the salary attachment to be
    completed.
