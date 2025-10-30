# File: /content/odoo_doc17.0/fr/content/applications/hr/employees/offboarding.md

Offboarding
===========

When an employee leaves the company, it is important to ensure their
employee record is updated to reflect their departure, log the reason
why, close any open activities associated with the employee, and provide
them with any important documents.

Archive an employee
-------------------

In Odoo, when an employee leaves the company they must be *archived*. To
archive an employee, first navigate to the
`Employees app`{.interpreted-text role="menuselection"}. From here,
locate the employee who is leaving the company, and click on their
employee card.

The employee form loads, displaying all their information. Click the
`fa-gear`{.interpreted-text role="icon"} `(gear)`{.interpreted-text
role="guilabel"} icon in the top-left corner, and a drop-down menu
appears. Click `oi-archive`{.interpreted-text role="icon"}
`Archive`{.interpreted-text role="guilabel"}, and an
`Employee Termination`{.interpreted-text role="guilabel"} pop-up window
appears.

Fill out the following fields on the form:

-   `Departure Reason`{.interpreted-text role="guilabel"}: Select a
    reason the employee is leaving from the drop-down menu. The default
    options are:
    -   `Fired`{.interpreted-text role="guilabel"}: Select this option
        when an employee is being let go, and the company has given
        notice.
    -   `Resigned`{.interpreted-text role="guilabel"}: Select this
        option when the employee no longer wishes to be employed, and
        the employee has given notice.
    -   `Retired`{.interpreted-text role="guilabel"}: Select this option
        when the employee is retiring.
    -   `Became Freelance`{.interpreted-text role="guilabel"}: Select
        this option when the employee is no longer working for the
        company, but is becoming a freelance worker instead.
-   `Contract End Date`{.interpreted-text role="guilabel"}: Using the
    calendar selector, select the last day the employee is working for
    the company.
-   `Detailed Reason`{.interpreted-text role="guilabel"}: Enter a short
    description for the employee\'s departure in this field.
-   `Close Activities`{.interpreted-text role="guilabel"}: Tick the
    checkbox next to each type of activity to close or delete any open
    activities associated with it. It is recommended to tick **all**
    checkboxes that are applicable. The available options are:
    -   `Appraisals`{.interpreted-text role="guilabel"}: cancels all
        appraisals scheduled after the contract end date.
    -   `Contract`{.interpreted-text role="guilabel"}: applies an end
        date for the current contract.
    -   `Company Car`{.interpreted-text role="guilabel"}: removes the
        employee as the driver for their current company car, and
        `assigns the next driver <fleet/new_vehicle/new-driver>`{.interpreted-text
        role="ref"}, if applicable.
    -   `Time Off`{.interpreted-text role="guilabel"}: cancels any time
        off requests after the contract end date.
    -   `Allocations`{.interpreted-text role="guilabel"}: removes the
        employee from any accrual plans they are on.
-   `HR Info`{.interpreted-text role="guilabel"}: Tick the checkbox next
    to `Send Access Link`{.interpreted-text role="guilabel"} to send a
    download link to the employee\'s personal email address, containing
    all their personal HR files.
-   `Private Email`{.interpreted-text role="guilabel"}: This field
    appears if the `HR Info`{.interpreted-text role="guilabel"} checkbox
    is ticked. Enter the private email address for the employee.

When the form is complete, click `Apply`{.interpreted-text
role="guilabel"}. The employee record is archived, an email with a
download link to their personal documents is sent to the employee\'s
private email address (if selected), and a red
`Archived`{.interpreted-text role="guilabel"} banner appears in the
top-right corner of the employee form. The chatter logs the
`Departure Date`{.interpreted-text role="guilabel"} and
`Departure Reason`{.interpreted-text role="guilabel"}, and if an access
link was emailed.

{.align-center}

::: {.note}
::: {.title}
Note
:::

While attempting to send the HR documents access link, an
`Invalid Operation`{.interpreted-text role="guilabel"} pop-up window may
appear, displaying the following error message:

`Employee's related user and private email must be set to use "Send Access Link"
function: (Employee Name)`{.interpreted-text role="guilabel"}

If this error appears, click `Close`{.interpreted-text role="guilabel"}
to close the pop-up window, then tick the
`Send Access Link`{.interpreted-text role="guilabel"} checkbox to
deselect it on the `Employee Termination`{.interpreted-text
role="guilabel"} pop-up window.

Click `Apply`{.interpreted-text role="guilabel"} to archive the employee
and close the selected activities on the
`Employee Termination`{.interpreted-text role="guilabel"} pop-up window,
returning to the employee form.

Once the employee form, ensure the following fields are populated:

-   `Private Information`{.interpreted-text role="guilabel"} tab: Ensure
    an email address is entered in the `Email`{.interpreted-text
    role="guilabel"} field.
-   `HR Settings`{.interpreted-text role="guilabel"} tab: Ensure a
    `Related User`{.interpreted-text role="guilabel"} is selected in the
    corresponding field.

After the necessary information is entered,
`resend the HR documents access link
<employees/send-link>`{.interpreted-text role="ref"}
:::

### Send HR documents access link {#employees/send-link}

If the access link was not sent when first archiving the employee on the
*Employee Termination* form, it can be sent after the employee is
archived at any point.

After an employee is archived, they are no longer visible on the main
**Employees** app dashboard. To view the archived employees, navigate to
the `Employees app`{.interpreted-text role="menuselection"} dashboard,
and click the `fa-caret-down`{.interpreted-text role="icon"}
`(down arrow)`{.interpreted-text role="guilabel"} in the search bar to
reveal a drop-down menu. Select `Archived`{.interpreted-text
role="guilabel"}, towards the bottom of the
`fa-filter`{.interpreted-text role="icon"} `Filters`{.interpreted-text
role="guilabel"} column, then click away from the drop-down window to
close it.

Now, only archived employees appear on the dashboard. Click on the
desired employee to open their employee form. On this form, click the
`fa-gear`{.interpreted-text role="icon"} `(gear)`{.interpreted-text
role="guilabel"} icon in the top-left corner, then click
`Send HR Documents Access Link`{.interpreted-text role="guilabel"} from
the resulting drop-down menu. The chatter logs that the link was sent.
