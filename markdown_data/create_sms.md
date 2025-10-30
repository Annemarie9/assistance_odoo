# File: /content/odoo_doc17.0/fr/content/applications/marketing/sms_marketing/create_sms.md

Create SMS messages
===================

To start, click `Create`{.interpreted-text role="guilabel"} on the main
`SMS Marketing`{.interpreted-text role="guilabel"} dashboard, and Odoo
reveals a blank SMS template form, which can be configured in a number
of different ways.

{.align-center}

First, give the mailing a `Subject`{.interpreted-text role="guilabel"},
which describes what the mailing is about.

Next, in the `Recipients`{.interpreted-text role="guilabel"} field,
choose to whom this `SMS (Short Message Service)`{.interpreted-text
role="abbr"} will be sent. By default, Odoo has
`Mailing List`{.interpreted-text role="guilabel"} selected. If this is
the desired `Recipients`{.interpreted-text role="guilabel"} field
option, specify which mailing list Odoo should send this `SMS
(Short Message Service)`{.interpreted-text role="abbr"} to in the
`Select Mailing List`{.interpreted-text role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

To create (or edit) a mailing list, go to
`Mailing Lists --> Mailing List`{.interpreted-text
role="menuselection"}. There, Odoo displays all previously created
mailing lists, along with various types of data related to that specific
list (e.g. number of contacts, mailings, recipients, etc.).

To learn more about mailing lists and contacts, check out
`mailing_lists_blacklists`{.interpreted-text role="doc"}.
:::

{.align-center}

To reveal all the possible options in the `Recipients`{.interpreted-text
role="guilabel"} field, click the field to see all the choices Odoo
makes available.

When another field (other than `Mailing List`{.interpreted-text
role="guilabel"}) is selected, the option to specify that chosen field
even further becomes available --- either with a default recipient
filter equation that appears automatically (which can be customized to
fit any business need), or, if no default recipient filter equation is
present, an `Add Filter`{.interpreted-text role="guilabel"} button will
appear.

Clicking the `Add Filter`{.interpreted-text role="guilabel"} button,
reveals fully customizable domain rule fields, which can be configured
similar to an equation. You can create multiple recipient rules, if
necessary.

Then, Odoo will only send the
`SMS (Short Message Service)`{.interpreted-text role="abbr"} to
recipients who fit into whatever criteria is configured in those fields.
Multiple rules can be added.

::: {.example}
If `Contact`{.interpreted-text role="guilabel"} is chosen, all of the
*Contacts* records in the Odoo database (vendors, customers, etc.) will
receive the `SMS (Short Message Service)`{.interpreted-text
role="abbr"}, by default --- unless more specific recipient rules are
entered.

For instance, the message below will only be sent to contacts in the
database that are located in the United States (e.g.
[Country]{.title-ref} \> [Country Name]{.title-ref} equals [United
States]{.title-ref}), and they haven\'t blacklisted themselves from any
mailings (e.g. [Blacklist]{.title-ref} \> [is]{.title-ref} \> [not
set]{.title-ref}).

{.align-center}
:::

Writing SMS messages
--------------------

Enter the content of the `SMS (Short Message Service)`{.interpreted-text
role="abbr"} in the text field, found in the
`SMS Content`{.interpreted-text role="guilabel"} tab. Links and emojis
can also be included. Beneath the text field, Odoo displays how many
characters are used in the message, along with how many
`SMS (Short Message
Service)`{.interpreted-text role="abbr"} mailings it will take to
deliver the complete message.

::: {.tip}
::: {.title}
Tip
:::

To check the price of sending an
`SMS (Short Message Service)`{.interpreted-text role="abbr"} for a
country, click on the `Information`{.interpreted-text role="guilabel"}
icon.
:::

{.align-center}

::: {.note}
::: {.title}
Note
:::

Credits must be purchased from Odoo in order to take advantage of the
*SMS Marketing* app; `SMS (Short Message Service)`{.interpreted-text
role="abbr"} messages will not be sent without credits.
:::

::: {.seealso}

:::

Track links used in SMS messages
--------------------------------

When links are used in `SMS (Short Message Service)`{.interpreted-text
role="abbr"} messages, Odoo automatically generates link trackers to
gather analytical data and metrics related to those specific links,
which can be found by going to
`Configuration --> Link Tracker`{.interpreted-text
role="menuselection"}.

{.align-center}

### Adjust SMS settings

Under the `Settings`{.interpreted-text role="guilabel"} tab of the SMS
template, there is an option to `Include
opt-out link`{.interpreted-text role="guilabel"}. If activated, the
recipient is able to unsubscribe from the mailing list, thus avoiding
all future mailings.

An employee can be designated as the `Responsible`{.interpreted-text
role="guilabel"} in the `Tracking`{.interpreted-text role="guilabel"}
section of the `Settings`{.interpreted-text role="guilabel"} tab, as
well.

{.align-center}

### Send SMS messages

Once a mailing is created, choose when Odoo should deliver the message
from the following options:

-   `Send`{.interpreted-text role="guilabel"}: sends the message
    immediately. Consider using this option if the recipient list is
    highly refined, or in cases that involve fast approaching deadlines,
    such as a \"flash sale.\"
-   `Schedule`{.interpreted-text role="guilabel"}: choose a day (and
    time) for Odoo to send the mailing. This is typically the best
    option for mailings related to a specific event. Such a method can
    also be used to promote a limited-time offer, or to help plan a
    company\'s content strategy in advance.
-   `Test`{.interpreted-text role="guilabel"}: allows for an
    `SMS (Short Message Service)`{.interpreted-text role="abbr"} to be
    sent to one or multiple numbers for test purposes. Remember to use a
    comma between phone numbers if multiple numbers are used as
    recipients.
