# File: /content/odoo_doc17.0/fr/content/applications/finance/expenses/log_expenses.md

Log expenses
============

Before expenses can be reimbursed, each individual expense needs to be
logged in the database. Expense records can be created in three
different ways: `manually enter an expense record
<expenses/manual_expense>`{.interpreted-text role="ref"},
`upload a receipt <expenses/upload_receipt>`{.interpreted-text
role="ref"}, or `email a
receipt <expenses/email_expense>`{.interpreted-text role="ref"} to a
preconfigured email address.

Manually enter expenses {#expenses/manual_expense}
-----------------------

To record a new expense, open the `Expenses app`{.interpreted-text
role="menuselection"}, which displays the `My
Expenses`{.interpreted-text role="guilabel"} page, by default.

::: {.tip}
::: {.title}
Tip
:::

This view can also be accessed from `Expenses app --> My Expenses --> My
Expenses`{.interpreted-text role="menuselection"}.
:::

Then, click `New`{.interpreted-text role="guilabel"}, and then fill out
the following fields on the form that appears:

-   `Description`{.interpreted-text role="guilabel"}: Enter a short
    description for the expense. This should be concise and informative,
    such as [lunch with client]{.title-ref} or [hotel for
    conference]{.title-ref}.

-   `Category`{.interpreted-text role="guilabel"}: Select the expense
    category from the drop-down menu that most closely corresponds to
    the expense.

-   `Total`{.interpreted-text role="guilabel"}: Enter the total amount
    paid for the expense in one of two ways:

    1.  If the expense is for a single item/expense, and the category
        selected was for a single item, enter the cost in the
        `Total`{.interpreted-text role="guilabel"} field (the
        `Quantity`{.interpreted-text role="guilabel"} field is hidden).

    2.  If the expense is for multiples of the same item/expense with a
        fixed price, the `Unit Price`{.interpreted-text role="guilabel"}
        is displayed. Enter the quantity in the
        `Quantity`{.interpreted-text role="guilabel"} field, and the
        total cost is automatically updated with the correct total. The
        total cost appears below the `Quantity`{.interpreted-text
        role="guilabel"}.

        ::: {.example}
        In the case of mileage driven, the
        `Unit Price`{.interpreted-text role="guilabel"} is populated as
        the cost *per mile*. Set the `Quantity`{.interpreted-text
        role="guilabel"} to the *number of miles driven*, and the total
        is calculated.
        :::

-   `Included Taxes`{.interpreted-text role="guilabel"}: If taxes were
    configured on the expense category, the tax percentage and amount
    appear automatically after entering either the
    `Total`{.interpreted-text role="guilabel"} or the
    `Quantity`{.interpreted-text role="guilabel"}.

    ::: {.note}
    ::: {.title}
    Note
    :::

    When a tax is configured on an expense category, the
    `Included Taxes`{.interpreted-text role="guilabel"} value updates in
    real time, as the `Total`{.interpreted-text role="guilabel"} or
    `Quantity`{.interpreted-text role="guilabel"} is updated.
    :::

-   `Employee`{.interpreted-text role="guilabel"}: Using the drop-down
    menu, select the employee this expense is for.

-   `Paid By`{.interpreted-text role="guilabel"}: Click the radio button
    to indicate who paid for the expense, and should be reimbursed.
    Select either `Employee (to reimburse)`{.interpreted-text
    role="guilabel"} or `Company`{.interpreted-text role="guilabel"}.
    Depending on the expense category selected, this field may not
    appear.

-   `Expense Date`{.interpreted-text role="guilabel"}: Using the
    calendar popover window that appears when this field is clicked,
    enter the date the expense was incurred.

-   `Account`{.interpreted-text role="guilabel"}: Using the drop-down
    menu, select the expense account the expense should be logged in.

-   `Customer to Reinvoice`{.interpreted-text role="guilabel"}: If the
    expense is something that should be paid for by a customer, select
    the `SO (Sales Order)`{.interpreted-text role="abbr"} and customer
    that should be invoiced for this expense from the drop-down menu.
    All sales orders in the drop-down menu list both the `SO
    (Sales Order)`{.interpreted-text role="abbr"}, as well as the
    company the sales order is written for. After the expense is saved,
    the customer name disappears, and only the
    `SO (Sales Order)`{.interpreted-text role="abbr"} is visible on the
    expense.

    ::: {.example}
    A customer wishes to have an on-site meeting for the design and
    installation of a custom garden, and agrees to pay for the expenses
    associated with it (such as travel, hotel, meals, etc). All expenses
    tied to that meeting would indicate the sales order for the custom
    garden (which also references the customer) as the
    `Customer to Reinvoice`{.interpreted-text role="guilabel"}.
    :::

-   `Analytic Distribution`{.interpreted-text role="guilabel"}: Select
    the account the expense should be written against from the drop-down
    menu for either `Projects`{.interpreted-text role="guilabel"},
    `Departments`{.interpreted-text role="guilabel"}, or both. Multiple
    accounts can be listed for each category, if needed. Adjust the
    percentage for each analytic account by typing in the percentage
    value next to each account.

-   `Company`{.interpreted-text role="guilabel"}: If multiple companies
    are set up, select the company the expense should be filed for from
    the drop-down menu. The current company automatically populates this
    field.

-   `Notes...`{.interpreted-text role="guilabel"}: If any notes are
    needed to clarify the expense, enter them in the notes field.

{.align-center}

### Attach receipts

After the expense record is created, the next step is to attach a
receipt. Click the `Attach Receipt`{.interpreted-text role="guilabel"}
button, and a file explorer appears. Navigate to the receipt to be
attached, and click `Open`{.interpreted-text role="guilabel"}.

The new receipt is recorded in the *chatter*, and the number of receipts
appears next to the `fa-paperclip`{.interpreted-text role="icon"}
`(paperclip)`{.interpreted-text role="guilabel"} icon. Multiple receipts
can be attached to an individual expense record, as needed.

{.align-center}

Upload expenses {#expenses/upload_receipt}
---------------

It is possible to have expense records created automatically, by
uploading a PDF receipt. This feature requires the enabling of a
setting, and the purchasing of
`IAP (in-app purchases)`{.interpreted-text role="abbr"} credits.

### Digitalization settings

To enable receipt scanning, navigate to
`Expenses app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, and tick the checkbox
beside the `Expense Digitization (OCR)`{.interpreted-text
role="guilabel"} option. Then, click `Save`{.interpreted-text
role="guilabel"}. When enabled, additional options appear. Click on the
corresponding radio button to select one of the following options:

-   `Do not digitize`{.interpreted-text role="guilabel"}: turns off
    receipt digitization.
-   `Digitize on demand only`{.interpreted-text role="guilabel"}: only
    digitizes receipts when requested. A
    `Digitize document`{.interpreted-text role="guilabel"} button
    appears on expense records. When clicked, the receipt is scanned and
    the expense record is updated.
-   `Digitize automatically`{.interpreted-text role="guilabel"}:
    automatically digitizes all receipts when they are uploaded.

Beneath these options are two additional links. Click the
`fa-arrow-right`{.interpreted-text role="icon"} `Buy
credits`{.interpreted-text role="guilabel"} link to purchase credits for
receipt digitization. Click the `fa-arrow-right`{.interpreted-text
role="icon"} `View My Services`{.interpreted-text role="guilabel"} link
to view a list of all current services, and their remaining credit
balances.

For more information on document digitization and
`IAPs (in-app purchases)`{.interpreted-text role="abbr"}, refer to the
`In-app purchase (IAP) <../../essentials/in_app_purchase>`{.interpreted-text
role="doc"} documentation.

::: {.note}
::: {.title}
Note
:::

When the `Expense Digitization (OCR)`{.interpreted-text role="guilabel"}
option is enabled, a necessary module is installed, so receipts can be
scanned. Disabling this option uninstalls the module.

If, at some point, there is a desire to temporarily stop digitizing
receipts, select the `Do not digitize`{.interpreted-text
role="guilabel"} option. The reason this option is available is so the
module is not uninstalled, allowing for digitization to be enabled in
the future by selecting one of the other two options.
:::

### Upload receipts

Open the `Expenses app`{.interpreted-text role="guilabel"}, and from the
`My Expenses`{.interpreted-text role="guilabel"} dashboard, click
`Upload`{.interpreted-text role="guilabel"}, and a file explorer
appears. Navigate to the desired receipt, select it, then click
`Open`{.interpreted-text role="guilabel"}.

![Create an expense by scanning a receipt. Click Scan at the top of the Expenses dashboard
view.](log_expenses/upload.png){.align-center}

The receipt is scanned, and a new expense record is created. The
`Expense Date`{.interpreted-text role="guilabel"} field is populated
with today\'s date, along with any other fields based on the scanned
data, such as the `Total`{.interpreted-text role="guilabel"}.

Click on the new entry to open the individual expense form, and make any
changes, if needed. The scanned receipt appears in the *chatter*.

Email expenses {#expenses/email_expense}
--------------

Instead of individually creating each expense in the **Expenses** app,
expenses can be automatically created by sending an email to an email
alias.

To do so, an email alias must first be configured. Navigate to
`Expenses app -->
Configuration --> Settings`{.interpreted-text role="menuselection"}.
Ensure the checkbox beside `Incoming Emails`{.interpreted-text
role="guilabel"} is ticked. The default email alias is
*expense@(domain).com*. Change the email alias by entering the desired
email in the field to the right of `Alias`{.interpreted-text
role="guilabel"}. Then, click `Save`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If the domain alias needs to be set up,
`fa-arrow-right`{.interpreted-text role="icon"} `Setup your domain
alias`{.interpreted-text role="guilabel"} appears beneath the
`Incoming Emails`{.interpreted-text role="guilabel"} checkbox, instead
of the email address field.

{.align-center}

Refer to the
`/applications/websites/website/configuration/domain_names`{.interpreted-text
role="doc"} documentation for setup instructions and more information.

Once the domain alias is configured, the email address field is visible
beneath the `Incoming Emails`{.interpreted-text role="guilabel"} feature
on the `Settings`{.interpreted-text role="guilabel"} page in the
**Expenses** app.
:::

Once the email address has been entered, emails can be sent to that
alias to create new expenses, without having to be in the Odoo database.

To submit an expense via email, create a new email, and enter the
product\'s *internal reference* code (if available) and the amount of
the expense as the subject of the email. Next, attach the receipt to the
email. Odoo creates the expense by taking the information in the email
subject, and combining it with the receipt.

To check an expense category\'s internal reference, go to
`Expenses app -->
Configuration --> Expense Categories`{.interpreted-text
role="menuselection"}. If an internal reference is listed on the expense
category, it is listed in the `Internal Reference`{.interpreted-text
role="guilabel"} column.

{.align-center}

To add an internal reference on an expense category, click on the
category to open the expense category form. Enter the
`Internal Reference`{.interpreted-text role="guilabel"} in the
corresponding field. Beneath the `Internal Reference`{.interpreted-text
role="guilabel"} field, this sentence appears: `Use this reference as a
subject prefix when submitting by email.`{.interpreted-text
role="guilabel"}

{.align-center}

::: {.example}
If submitting an expense, via email, for a \$25.00 meal during a work
trip, the email subject would be [FOOD \$25.00]{.title-ref}.

Explanation:

-   The `Internal Reference`{.interpreted-text role="guilabel"} for the
    expense category [Meals]{.title-ref} is [FOOD]{.title-ref}
-   The `Cost`{.interpreted-text role="guilabel"} for the expense is
    [\$25.00]{.title-ref}
:::

::: {.note}
::: {.title}
Note
:::

For security purposes, only authenticated employee emails are accepted
by Odoo when creating an expense from an email. To confirm an
authenticated employee email address, go to the employee card in the
`Employees app`{.interpreted-text role="menuselection"}, and refer to
the `Work Email`{.interpreted-text role="guilabel"} field.

{.align-center}
:::
