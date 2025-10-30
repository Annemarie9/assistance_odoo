# File: /content/odoo_doc17.0/fr/content/applications/essentials/contacts.md

show-content

:   

Contacts
========

The *Contacts* application comes installed on all Odoo databases.
Contacts are created for customers the company does business with
through Odoo. A contact is a repository of vital business information,
facilitating communication and business transactions.

Contact form
------------

To create a new contact, navigate to the
`Contacts app`{.interpreted-text role="menuselection"}, and click
`Create`{.interpreted-text role="guilabel"}. A new form appears where
various contact information can be added.

### Contact type

Odoo allows for both `Individual`{.interpreted-text role="guilabel"} and
`Company`{.interpreted-text role="guilabel"} contacts. Select either
`Individual`{.interpreted-text role="guilabel"} or
`Company`{.interpreted-text role="guilabel"}, depending on the type of
contact that is being added.

### Name

First, fill in the name of the `Individual`{.interpreted-text
role="guilabel"} or `Company`{.interpreted-text role="guilabel"}. This
is how the name appears throughout the database. This field is
**mandatory**.

::: {.tip}
::: {.title}
Tip
:::

`Individual`{.interpreted-text role="guilabel"} contacts can have a
`Company`{.interpreted-text role="guilabel"} contact linked to it. After
selecting `Individual`{.interpreted-text role="guilabel"}, a new
`Company Name...`{.interpreted-text role="guilabel"} field appears below
the first name field.
:::

### Address

Next, enter the `Address`{.interpreted-text role="guilabel"} of the
`Company`{.interpreted-text role="guilabel"} or
`Individual`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

If the `Individual`{.interpreted-text role="guilabel"} option is chosen,
then the *type of address* can be chosen from a drop-down menu. Options
for this drop-down menu include: `Contact`{.interpreted-text
role="guilabel"}, `Invoice
Address`{.interpreted-text role="guilabel"},
`Delivery Address`{.interpreted-text role="guilabel"},
`Other Address`{.interpreted-text role="guilabel"}, and `Private
Address`{.interpreted-text role="guilabel"}.
:::

### Additional fields

Additional details are included on the initial form. The following
fields are available:

-   `VAT`{.interpreted-text role="guilabel"}: Value Added Tax number.
-   `Citizen Identification`{.interpreted-text role="guilabel"}: citizen
    or government identification number (only available on
    `Individual`{.interpreted-text role="guilabel"}).
-   `Job Position`{.interpreted-text role="guilabel"}: list the job
    position of the `Individual`{.interpreted-text role="guilabel"}
    (only available on `Individual`{.interpreted-text role="guilabel"}).
-   `Phone`{.interpreted-text role="guilabel"}: list phone number (with
    country code). Make a call, send an SMS, or WhatsApp message by
    hovering over the field on the saved form, and clicking the desired
    option.
-   `Mobile`{.interpreted-text role="guilabel"}: list mobile phone
    number (with country code). Make a call, send an SMS, or WhatsApp
    message by hovering over the field on the saved form, and clicking
    on the desired option.
-   `Email`{.interpreted-text role="guilabel"}: enter the email address
    with the domain.
-   `Website`{.interpreted-text role="guilabel"}: enter the full website
    address, starting with [http]{.title-ref} or [https]{.title-ref}.
-   `Title`{.interpreted-text role="guilabel"}: select
    `Doctor`{.interpreted-text role="guilabel"},
    `Madam`{.interpreted-text role="guilabel"}, `Miss`{.interpreted-text
    role="guilabel"}, `Mister`{.interpreted-text role="guilabel"},
    `Professor`{.interpreted-text role="guilabel"}, or create a new one
    directly from this field.
-   `Tags`{.interpreted-text role="guilabel"}: enter preconfigured tags
    by typing them in the field, or clicking the drop-down menu, and
    selecting one. To create a new one, type the new tag in the field,
    and click `Create`{.interpreted-text role="guilabel"} from the
    resulting drop-down menu.

### Contacts & Addresses tab

At the bottom of the contact form are several tabs. On the
`Contacts & Addresses`{.interpreted-text role="guilabel"} tab, contacts
can be added that are associated with a `Company`{.interpreted-text
role="guilabel"} and related addresses. For example, a specific contact
person for the company can be listed here.

Multiple addresses can be added on both `Individual`{.interpreted-text
role="guilabel"} and `Company`{.interpreted-text role="guilabel"}
contacts. To do so, click `Add`{.interpreted-text role="guilabel"} in
the `Contacts & Addresses`{.interpreted-text role="guilabel"} tab. Doing
so reveals a `Create Contact`{.interpreted-text role="guilabel"} pop-up
form, in which additional addresses can be configured.

{.align-center}

On the `Create Contact`{.interpreted-text role="guilabel"} pop-up form,
start by clicking the default `Other
Address`{.interpreted-text role="guilabel"} field at the top to reveal a
drop-down menu of address-related options.

Select any of the following options:

-   `Contact`{.interpreted-text role="guilabel"}: adds another contact
    to the existing contact form.
-   `Invoice Address`{.interpreted-text role="guilabel"}: adds a
    specific invoice address to the existing contact form.
-   `Delivery Address`{.interpreted-text role="guilabel"}: adds a
    specific delivery address to the existing contact form.
-   `Other Address`{.interpreted-text role="guilabel"}: adds an
    alternate address to the existing contact form.
-   `Private Address`{.interpreted-text role="guilabel"}: adds a private
    address to the existing contact form.

{.align-center}

Once an option is selected, enter the corresponding contact information
that should be used for the specified address type.

Add the `Contact Name`{.interpreted-text role="guilabel"},
`Address`{.interpreted-text role="guilabel"}, `Email`{.interpreted-text
role="guilabel"}, along with the `Phone`{.interpreted-text
role="guilabel"} and/or `Mobile`{.interpreted-text role="guilabel"}
numbers below.

Set the `Job Position`{.interpreted-text role="guilabel"}, which appears
if the `Contact`{.interpreted-text role="guilabel"} address type has
been selected. This is similar to the `Individual`{.interpreted-text
role="guilabel"} contact.

To add a note, click on the text field next to `Notes`{.interpreted-text
role="guilabel"}, and write anything that is applicable to the customer
or contact.

Then, click `Save & Close`{.interpreted-text role="guilabel"} to save
the address, and close the `Create Contact`{.interpreted-text
role="guilabel"} window. Or, click `Save & New`{.interpreted-text
role="guilabel"} to save the address, and immediately input another one.

### Sales & Purchase tab

Next, is the `Sales & Purchases`{.interpreted-text role="guilabel"} tab,
which only appears when the *Sales*, *Purchase*, **or** *Point of Sale*
applications are installed.

The `Fiscal Position`{.interpreted-text role="guilabel"} can be set on
the `Sales & Purchases`{.interpreted-text role="guilabel"} tab. Select a
`Fiscal Position`{.interpreted-text role="guilabel"} from the drop-down
menu.

#### Sales section

Under the `Sales`{.interpreted-text role="guilabel"} heading, a specific
`Salesperson`{.interpreted-text role="guilabel"} can be assigned to a
contact. To do that, click the `Salesperson`{.interpreted-text
role="guilabel"} drop-down field, and select one. Create a new
`Salesperson`{.interpreted-text role="guilabel"} by typing the user\'s
name, and making the appropriate selection.

Certain `Payment Terms`{.interpreted-text role="guilabel"}, or a certain
`Pricelist`{.interpreted-text role="guilabel"}, can also be set, if
needed. Click the drop-down menu next to
`Payment Terms`{.interpreted-text role="guilabel"}, and change it to one
of the preselected `Payment Terms`{.interpreted-text role="guilabel"},
or `Create`{.interpreted-text role="guilabel"} a new one. Select the
`Pricelist`{.interpreted-text role="guilabel"} drop-down menu to choose
the appropriate `Pricelist`{.interpreted-text role="guilabel"}.

Click into the `Delivery Method`{.interpreted-text role="guilabel"}
field to select an option from the drop-down menu.

#### Point Of Sale section

Under the `Point Of Sale`{.interpreted-text role="guilabel"} heading,
enter a `Barcode`{.interpreted-text role="guilabel"} that can be used to
identify the contact. Use the `Loyalty Points`{.interpreted-text
role="guilabel"} field to track points the user won as part of a
*Loyalty Program*.

#### Purchase section

Specify `Payment Terms`{.interpreted-text role="guilabel"},
`1099 Box`{.interpreted-text role="guilabel"} information, and a
preferred `Payment Method`{.interpreted-text role="guilabel"} here. A
`Receipt Reminder`{.interpreted-text role="guilabel"} can be set here,
as well.

#### Misc section

Under the `Misc.`{.interpreted-text role="guilabel"} heading, use
`Reference`{.interpreted-text role="guilabel"} field to add any
additional information for this contact. If this contact should only be
accessible for one company in a multi-company database, select it from
the `Company`{.interpreted-text role="guilabel"} field drop-down list.
Use the `Website`{.interpreted-text role="guilabel"} drop-down menu to
restrict the publishing of this contact to one website (if working on a
database with multiple websites). Select one or more
`Website Tags`{.interpreted-text role="guilabel"} to assist in filtering
published customers on the [/customers]{.title-ref} website page. Select
an `Industry`{.interpreted-text role="guilabel"} for this contact from
the drop-down menu. Use the `SLA Policies`{.interpreted-text
role="guilabel"} field to assign a *Helpdesk* SLA policy to this
contact.

### Accounting tab

The `Accounting`{.interpreted-text role="guilabel"} tab appears when the
*Accounting* application is installed. Here, a user can add any related
`Bank Accounts`{.interpreted-text role="guilabel"}, or set default
`Accounting entries`{.interpreted-text role="guilabel"}.

Under the `Miscellaneous`{.interpreted-text role="guilabel"} heading,
use the `LEI`{.interpreted-text role="guilabel"} field to enter a Legal
Entity Identifier, if necessary.

### Internal Notes tab

Following the `Accounting`{.interpreted-text role="guilabel"} tab is the
`Internal Notes`{.interpreted-text role="guilabel"} tab, where notes can
be left on this contact form, just like on the contact form noted above.

### Partner Assignment tab

Next is the `Partner Assignment`{.interpreted-text role="guilabel"} tab,
which by default, includes a `Geolocation`{.interpreted-text
role="guilabel"} section, and other partner options, including
`Partner Activation`{.interpreted-text role="guilabel"} and `Partner
Review`{.interpreted-text role="guilabel"} configurations. These are
**only** present when the *Resellers* module is installed.

::: {.seealso}
Follow the
`Resellers documentation <../sales/crm/track_leads/resellers>`{.interpreted-text
role="doc"} for more information on publishing partners on the website.
:::

### Membership tab

Finally, there is the `Membership`{.interpreted-text role="guilabel"}
tab on contact forms, which can help users manage any memberships that
are being offered to this specific contact. It should be noted that this
tab **only** appears when the *Members* application is installed.

#### Activate membership

To activate a contact\'s membership, click
`Buy Membership`{.interpreted-text role="guilabel"} in the
`Membership`{.interpreted-text role="guilabel"} tab of a contact form.
On the pop-up window that appears, select a
`Membership`{.interpreted-text role="guilabel"} from the drop-down menu.
Then, configure a `Member Price`{.interpreted-text role="guilabel"}.
Click `Invoice Membership`{.interpreted-text role="guilabel"} when both
fields are filled in.

Alternatively, to offer a free membership, tick the
`Free Member`{.interpreted-text role="guilabel"} checkbox, in the
`Membership`{.interpreted-text role="guilabel"} tab of a contact form.

::: {.seealso}
Follow the `Members documentation <../sales/members>`{.interpreted-text
role="doc"} for more information on publishing members on the website.
:::

Smart buttons
-------------

At the top of the contact form, there are some additional options
available, known as *smart buttons*.

Here, Odoo displays a variety of records, related to this contact, that
were created on other apps. Odoo integrates information from every
single app, so there are many smart buttons.

::: {.example}
For example, there is an `Opportunities`{.interpreted-text
role="guilabel"} smart button, where all the opportunities related to
this customer from the *CRM* app are accessible.
:::

::: {.tip}
::: {.title}
Tip
:::

If the corresponding applications are installed, their related smart
buttons appear automatically on a contact form.
:::

A user can see any `Meetings`{.interpreted-text role="guilabel"},
`Sales`{.interpreted-text role="guilabel"},
`POS Orders`{.interpreted-text role="guilabel"},
`Subscriptions`{.interpreted-text role="guilabel"}, project
`Tasks`{.interpreted-text role="guilabel"}, and the
`More`{.interpreted-text role="guilabel"} smart button reveals
additional options, via a drop-down menu. A user can even quickly access
`Purchases`{.interpreted-text role="guilabel"},
`Helpdesk`{.interpreted-text role="guilabel"} tasks,
`On-time Rate`{.interpreted-text role="guilabel"} for deliveries,
`Invoiced`{.interpreted-text role="guilabel"} information,
`Vendor Bills`{.interpreted-text role="guilabel"}, and the
`Partner Ledger`{.interpreted-text role="guilabel"} connected to this
contact.

Deliveries, documents, loyalty cards, and direct debits are *also*
linked to smart buttons, like this, should there be any
outstanding/on-file for this contact.

If the contact is a partner, the user can visit their partner page on
the Odoo-built website by clicking the `Go to Website`{.interpreted-text
role="guilabel"} smart button.

### Archive contacts

If a user decides they no longer want to have this contact active, the
record can be archived. To do that, go to the `fa-cog`{.interpreted-text
role="icon"} `Action`{.interpreted-text role="guilabel"} menu at the top
of the contact form, and click `Archive`{.interpreted-text
role="guilabel"}.

Then, click `OK`{.interpreted-text role="guilabel"} from the resulting
`Confirmation`{.interpreted-text role="guilabel"} pop-up window.

With this contact successfully archived, as indicated by a banner at the
top, they do not show up in the main contacts page, but they can still
be searched for with the `Archived`{.interpreted-text role="guilabel"}
filter.

::: {.tip}
::: {.title}
Tip
:::

A contact can be *unarchived*, if the user decides to work with them
again. To do that, just click the `fa-cog`{.interpreted-text
role="icon"} `Action`{.interpreted-text role="guilabel"} menu again at
the top of the archived contact form, and click
`Unarchive`{.interpreted-text role="guilabel"}. Upon doing so, the
`Archived`{.interpreted-text role="guilabel"} banner is removed, and the
contact is restored.
:::

::: {.seealso}
\-
`Add different addresses in CRM <../sales/sales/send_quotations/different_addresses>`{.interpreted-text
role="doc"} - [Odoo\'s eLearning Contacts
tutorial](https://www.odoo.com/slides/slide/contacts-2527?fullscreen=1)
:::

::: {.toctree titlesonly=""}
contacts/merge
:::
