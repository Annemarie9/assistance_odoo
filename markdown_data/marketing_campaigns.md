# File: /content/odoo_doc17.0/fr/content/applications/marketing/sms_marketing/marketing_campaigns.md

SMS campaign settings
=====================

Utilizing `SMS (Short Message Service)`{.interpreted-text role="abbr"}
campaigns with Odoo *SMS Marketing* isn\'t just an effective
advertisement strategy, it\'s also a great way to remind people about
upcoming events, issued invoices, and so much more.

But, before `SMS (Short Message Service)`{.interpreted-text role="abbr"}
campaigns can be created (and sent), a few specific settings and
features must be enabled first.

SMS campaign setting
--------------------

To enable `SMS (Short Message Service)`{.interpreted-text role="abbr"}
campaigns in Odoo, make sure the *Mailing Campaigns* feature is
activated by going to
`Email Marketing --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and then enable
`Mailing Campaigns`{.interpreted-text role="guilabel"} and
`Save`{.interpreted-text role="guilabel"} the changes.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Activating the *Mailing Campaigns* feature in the *General Settings*
also enables the *A/B Test* feature.
:::

Once the setting is enabled, navigate back to the
`SMS Marketing`{.interpreted-text role="menuselection"} app, and notice
the `Campaigns`{.interpreted-text role="guilabel"} header menu is now
available for use. Similarly, the `A/B Test`{.interpreted-text
role="guilabel"} tab is now also available on every
`SMS (Short Message Service)`{.interpreted-text role="abbr"} template
form.

A/B tests
---------

`A/B Tests`{.interpreted-text role="guilabel"} allows any
`SMS (Short Message Service)`{.interpreted-text role="abbr"} mailings to
be tested against other versions within the same campaign, in order to
compare which version is the most successful in producing engagement
and/or conversion outcomes.

On an `SMS (Short Message Service)`{.interpreted-text role="abbr"}
template form, under the `A/B Tests`{.interpreted-text role="guilabel"}
tab, initially, there\'s only a single checkbox labeled:
`Allow A/B Testing.`{.interpreted-text role="guilabel"}

When clicked, a series of other options appear.

{.align-center}

In the first field, enter a desired percentage of recipients to conduct
the A/B Test on.

Beneath the percentage field is the `Winner Selection`{.interpreted-text
role="guilabel"} field. This is what Odoo will use to determine the
successful result of an A/B Test. In other words, this tells Odoo how to
pick a winning A/B test.

The following sections are available: `Manual`{.interpreted-text
role="guilabel"}, `Highest Click Rate`{.interpreted-text
role="guilabel"}, `Leads`{.interpreted-text role="guilabel"},
`Quotations`{.interpreted-text role="guilabel"}, or
`Revenues`{.interpreted-text role="guilabel"}.

Finally, the `Send Final On`{.interpreted-text role="guilabel"} field is
listed. This represents the date-time that Odoo uses as a deadline to
determine the winning mailing variation. Then, Odoo sends that winning
mailing variation to the remaining recipients, who weren\'t involved in
the test, at that prior date and time.

::: {.tip}
::: {.title}
Tip
:::

Quickly create different versions of the mailing to add to the A/B Test
by clicking the `Create an Alternate Version`{.interpreted-text
role="guilabel"} button.
:::

::: {.note}
::: {.title}
Note
:::

Remember, the winning mailing variation is based on the criteria
selected in the `Winner Selection`{.interpreted-text role="guilabel"}
field.
:::

Campaigns page
--------------

To create, edit, or analyze any campaign, click
`Campaigns`{.interpreted-text role="menuselection"} in the header menu
of the `SMS Marketing`{.interpreted-text role="guilabel"} app. On the
`Campaigns`{.interpreted-text role="guilabel"} page, each campaign
displays various information related to the mailings associated with
that campaign (e.g. number of emails, social posts, SMSs, and push
notifications).

{.align-center}

Campaign templates
------------------

Click `Create`{.interpreted-text role="guilabel"} to create a new
campaign, and Odoo reveals a blank campaign template form to fill out.
Alternatively, select any previously-made campaign in order to
duplicate, review, or edit its campaign template form.

{.align-center}

With each campaign, the options to `Send New Mailing`{.interpreted-text
role="guilabel"}, `Send SMS`{.interpreted-text role="guilabel"},
`Send Social Post`{.interpreted-text role="guilabel"}, and
`Push Notifications`{.interpreted-text role="guilabel"} are available
above the template form.

Whenever one of those communication options is added to the campaign,
Odoo will create a new corresponding tab on the template form, where
those types of messages can be reviewed or edited, along with various
data sets related to each specific mailing.

At the top of the template, there are various analytical smart buttons.
When clicked, Odoo reveals in-depth metrics related to that specific
topic (e.g. `Engagement`{.interpreted-text role="guilabel"},
`Opportunities`{.interpreted-text role="guilabel"}, etc.) on a separate
page.

Beneath the smart buttons, are fields for
`Campaign Name`{.interpreted-text role="guilabel"} and
`Responsible`{.interpreted-text role="guilabel"}. Odoo also allows for
various `Tags`{.interpreted-text role="guilabel"} to be added, as well
(if necessary).

Sending SMSs through the Contacts app
-------------------------------------

Sending `SMS (Short Message Service)`{.interpreted-text role="abbr"}
mailings directly through a contact\'s form is available by default.

In order to send an `SMS (Short Message Service)`{.interpreted-text
role="abbr"} in this fashion, navigate to the
`Contacts`{.interpreted-text role="menuselection"} app, select the
desired contact in the database, and click on the
`SMS`{.interpreted-text role="guilabel"} icon on the contact form (next
to the `Phone Number`{.interpreted-text role="guilabel"} field).

{.align-center}

To send a message to multiple contacts at once, navigate to the main
`Contacts`{.interpreted-text role="menuselection"} app main dashboard,
choose the `List View`{.interpreted-text role="guilabel"}, and select
all the desired contacts to whom the message should be sent. Then, under
`Action`{.interpreted-text role="guilabel"}, select
`Send SMS`{.interpreted-text role="guilabel"}.

{.align-center}

Set up SMS templates for future use
-----------------------------------

In order to set up `SMS Templates`{.interpreted-text role="guilabel"}
for future use, activate `developer mode
<developer-mode>`{.interpreted-text role="ref"}, by navigating to the
main Odoo dashboard that is full of apps, and select the
`Settings app`{.interpreted-text role="menuselection"}. Then, scroll
down to the `Developer Tools`{.interpreted-text role="guilabel"}
section, and click `Activate the Developer Mode`{.interpreted-text
role="guilabel"}.

Once *developer mode* is activated, the main Odoo dashboard appears once
more, with a now-visible bug icon, which is located at the top-right
corner of the dashboard; this bug icon indicates that developer mode is
currently active.

Next return to the `Settings app`{.interpreted-text
role="menuselection"} and, in the now-visible header menus at the top,
choose `Technical --> SMS Templates`{.interpreted-text
role="menuselection"} to begin setting up `SMS (Short Message
Service)`{.interpreted-text role="abbr"} templates for future marketing
campaigns.

{.align-center}

Inside of the `SMS Templates`{.interpreted-text role="guilabel"}
dashboard, Odoo reveals an entire page of `SMS (Short
Message Service)`{.interpreted-text role="abbr"} templates. The default
`List`{.interpreted-text role="guilabel"} view showcases each
template\'s name, and to which recipients it applies.

On this page, `SMS (Short Message Service)`{.interpreted-text
role="abbr"} templates can be edited or created from scratch.

![The SMS Templates page in Odoo is available after enabling developer mode in the General
Settings](marketing_campaigns/sms-template.png){.align-center}
