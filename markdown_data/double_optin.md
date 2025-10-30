# File: /content/odoo_doc17.0/fr/content/applications/marketing/marketing_automation/campaign_templates/double_optin.md

Double Opt-in
=============

A *double opt-in*, also referred to as a *confirmed opt-in*, may be
required in some countries for marketing communications, due to
anti-SPAM laws. Confirming consent has several other benefits, as well:
it validates email addresses, avoids spam/robo subscribers, keeps
mailing lists clean, and only includes engaged contacts in the mailing
list.

When the *Double Opt-in* campaign template is used, a new mailing list
titled, *Confirmed contacts* is created in the *Email Marketing* app,
and any new mailing list contacts that are added to the default
*Newsletter* mailing list are sent a confirmation email to double
opt-in. The contacts that click on the confirmation link in the email
are automatically added to the *Confirmed contacts* mailing list in
Odoo.

::: {.important}
::: {.title}
Important
:::

When using the *Double Opt-in* campaign template, only the contacts in
the *Confirmed contacts mailing* list are considered to have confirmed
their consent.
:::

Use the Double Opt-in campaign template {#marketing_automation/template/using-double-optin}
---------------------------------------

Open the `Marketing Automation`{.interpreted-text role="menuselection"}
app, and select the `Double Opt-in`{.interpreted-text role="guilabel"}
campaign template to create a new campaign for confirming consent.

::: {.tip}
::: {.title}
Tip
:::

The campaign templates do **not** display, by default, when there are
existing *Marketing Automation* campaigns. To display the campaign
templates, type the name of a campaign (that does not exist in the
database) into the `Search...`{.interpreted-text role="guilabel"} bar,
then press `Enter`{.interpreted-text role="kbd"}.

For example, searching for [empty]{.title-ref} displays the campaign
template cards again, as long as there is not a campaign with the name
\"empty\" in the database.
:::

### Campaign configuration

Upon creation of the campaign, the campaign form loads with a new
preconfigured campaign.

The `Target`{.interpreted-text role="guilabel"} and
`Filter`{.interpreted-text role="guilabel"} configurations of the
campaign are as follows:

-   `Name`{.interpreted-text role="guilabel"}: [Double
    Opt-in]{.title-ref}
-   `Responsible`{.interpreted-text role="guilabel"}\*: The user who
    created the campaign.
-   `Target`{.interpreted-text role="guilabel"}:
    `Mailing Contact`{.interpreted-text role="guilabel"}
-   `Unicity based on`{.interpreted-text role="guilabel"}:
    `Email (Mailing Contact)`{.interpreted-text role="guilabel"}
-   `Filter`{.interpreted-text role="guilabel"}:
    -   `Email`{.interpreted-text role="guilabel"}
        `is set`{.interpreted-text role="guilabel"}
    -   `Blacklist`{.interpreted-text role="guilabel"}
        `is not`{.interpreted-text role="guilabel"}
        `set`{.interpreted-text role="guilabel"}
    -   `Mailing lists`{.interpreted-text role="guilabel"}
        `contains`{.interpreted-text role="guilabel"}
        [Newsletter]{.title-ref}

\* The `Responsible`{.interpreted-text role="guilabel"} field is only
visible with `developer-mode`{.interpreted-text role="ref"} activated.

::: {.important}
::: {.title}
Important
:::

The `Target`{.interpreted-text role="guilabel"} model of the campaign
should **not** be modified. Changing the `Target`{.interpreted-text
role="guilabel"} model with activities in the
`Workflow`{.interpreted-text role="guilabel"} invalidates the existing
activities in the `Workflow`{.interpreted-text role="guilabel"}.

The *Double Opt-in* campaign template is intended to **only** use the
`Mailing Contact`{.interpreted-text role="guilabel"} model.
:::

The campaign loads two activities in the `Workflow`{.interpreted-text
role="guilabel"} section of the campaign: an email activity, with a
child server action activity that triggers *on click*.

By default, the [Confirmation]{.title-ref} email activity is set to
trigger `1 Hours`{.interpreted-text role="guilabel"} after the beginning
of the workflow. In other words, the email is sent 1 hour after a new
contact is added to the *Newsletter* mailing list.

The email activity uses the preconfigured *Confirmation* email template,
which contains a button for the contact to click to confirm their
consent.

To modify the email template, select the
`fa-envelope-o`{.interpreted-text role="icon"}
`Templates`{.interpreted-text role="guilabel"} smart button at the top
of the campaign form. Then, in the list of templates, select the
[Confirmation]{.title-ref} email template.

Be sure to personalize the contents of the email template; however, it
is recommended to keep the contents of double opt-in confirmation emails
short and to-the-point.

The default confirmation button, in the body of the template, links
directly to the database\'s website homepage. Click on the button to
edit the button text and URL.

::: {.tip}
::: {.title}
Tip
:::

To provide a streamlined experience for the contact, consider
`creating a page on the
website <../../../websites/website/pages>`{.interpreted-text role="doc"}
that expresses gratitude to the contact for confirming their
subscription to the mailing list. Add the link to that page in the URL
of the confirmation button.
:::

::: {.important}
::: {.title}
Important
:::

The email template should only include a single call-to-action link for
confirmation, other than an unsubscribe link.

Any click on a link (or button) included in the confirmation email,
besides the unsubscribe button, triggers the *Add to list* server
action.

The child activity *Add to list* server action\'s *On click* trigger
cannot differentiate between multiple URLs in an email, besides the
[/unsubscribe\_from\_list]{.title-ref} unsubscribe button that is
included in any one of the footer blocks.
:::

The [Add to list]{.title-ref} server action activity triggers
immediately after a click in the parent [Confirmation]{.title-ref} email
activity is detected.

When triggered, the [Add to list]{.title-ref} activity executes the *Add
To Confirmed List* server action, automatically adding the contact to
the *Confirmed contacts* mailing list, if they are not already in the
mailing list.

To modify the server action, select the title of the activity to open
the `Open:
Activities`{.interpreted-text role="guilabel"} pop-up window and edit
the server action activities configuration.

::: {.tip}
::: {.title}
Tip
:::

Consider setting an `Expiry Duration`{.interpreted-text role="guilabel"}
to prevent executing the activity after a specific amount of time.
:::

::: {.important}
::: {.title}
Important
:::

It is not recommended to modify the preconfigured Python code in the
`Add To Confirmed
List`{.interpreted-text role="guilabel"} server action, as doing so may
trigger a change in the database\'s pricing plan.
:::

Once the campaign configuration is complete, consider
`launching a test <../testing_running>`{.interpreted-text role="doc"} to
verify the campaign executes as expected. If the campaign testing is
successful, `Start`{.interpreted-text role="guilabel"} the campaign to
begin sending double opt-in confirmation emails to *Newsletter* mailing
list contacts, and fill the *Confirmed contacts* mailing list with
engaged contacts.

Double Opt-in use-case {#marketing_automation/template/double-optin-usecase}
----------------------

::: {.example}
To prepare for sending newsletter marketing emails on an Odoo database,
a mailing contact list must be procured. One way of collecting
subscribers is through a sign-up form on the website that adds contacts
to the *Newsletter* mailing list on the form submission.

{.align-center}

Before sending any marketing emails,
`use the Double Opt-in campaign template
<marketing_automation/template/using-double-optin>`{.interpreted-text
role="ref"} in the *Marketing Automation* app to confirm marketing email
consent from the contacts in the *Newsletter* mailing list.

After launching the *Double Opt-in* campaign, view the contacts that
have double opt-in in the *Confirmed contacts* mailing list
(`Email Marketing app --> Mailing Lists -->
Mailing Lists`{.interpreted-text role="menuselection"}).

{.align-center}

Now, the *Confirmed contacts* mailing list is ready to be used for
sending newsletter marketing emails from an Odoo database.
:::

::: {.seealso}
\- `../understanding_metrics`{.interpreted-text role="doc"} -
`../../email_marketing/mailing_lists`{.interpreted-text role="doc"} -
`../../email_marketing`{.interpreted-text role="doc"}
:::
