# File: /content/odoo_doc17.0/fr/content/applications/services/helpdesk/overview/receiving_tickets.md

Receiving tickets
=================

Odoo *Helpdesk* offers multiple channels where customers can reach out
for assistance, such as email, live chat, and through a website\'s
submission form. The variety of these contact options provides customers
with multiple opportunities to receive support quickly while also
allowing the support team to manage multi-channel support tickets from
one central location.

Enable channel options to submit tickets
----------------------------------------

Go to
`Helpdesk app --> Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"}, and choose an existing team, or click
`New`{.interpreted-text role="guilabel"} to
`create a new team <../../helpdesk>`{.interpreted-text role="doc"}.

On the team\'s settings page, scroll down to the
`Channels`{.interpreted-text role="guilabel"} and
`Help Center`{.interpreted-text role="guilabel"} sections. Enable one or
more channels by checking the respective boxes.

-   `Email Alias <helpdesk/receiving_tickets/email-alias>`{.interpreted-text
    role="ref"}
-   `Live Chat <helpdesk/receiving_tickets/live-chat>`{.interpreted-text
    role="ref"}
-   `Website Form <helpdesk/receiving_tickets/website-form>`{.interpreted-text
    role="ref"}

### Email Alias {#helpdesk/receiving_tickets/email-alias}

The *Email Alias* setting creates tickets from messages sent to that
team\'s specified email alias.

::: {.important}
::: {.title}
Important
:::

The following steps are for **Odoo Online** and **Odoo.sh** databases.
For **On-premise** databases, external servers are required for email
aliases.
:::

When a new *Helpdesk* team is created, an email alias is created for it.
This alias can be changed on the team\'s settings page.

To change a *Helpdesk* team\'s email alias, navigate to
`Helpdesk app -->
Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"}, and click on a team name to open its settings
page.

Then, scroll to `Channels --> Email Alias`{.interpreted-text
role="menuselection"}. In the `Alias`{.interpreted-text role="guilabel"}
field, type the desired name for the team\'s email alias.

![View of the settings page of a Helpdesk team emphasizing the email alias feature in Odoo
Helpdesk.](receiving_tickets/receiving-tickets-email-alias.png){.align-center}

::: {.note}
::: {.title}
Note
:::

Custom email domains are **not** required in order to use an email
alias, however, they can be configured through the *Settings* app.

If the database does not have a custom domain already configured, click
`Set an Alias
Domain`{.interpreted-text role="guilabel"} to be redirected to the
`Settings`{.interpreted-text role="guilabel"} page. From there, enable
`Custom
Email Servers`{.interpreted-text role="guilabel"}.
:::

When an email is received, the subject line becomes the title of a new
*Helpdesk* ticket. The body of the email is also added to the ticket,
under the `Description`{.interpreted-text role="guilabel"} tab, and in
the ticket\'s chatter.

### Live Chat {#helpdesk/receiving_tickets/live-chat}

The *Live Chat* feature lets website visitors connect directly with a
support agent or chatbot. *Helpdesk* tickets can be instantly created
during these conversations using the `response
command </applications/websites/livechat/responses>`{.interpreted-text
role="doc"} [/ticket]{.title-ref}.

To enable *Live Chat*, navigate to the
`Helpdesk app --> Configuration --> Helpdesk
Teams`{.interpreted-text role="menuselection"} list view, select a team,
and on the team\'s settings page, click the checkbox next to
`Live Chat`{.interpreted-text role="guilabel"}, under the
`Channels`{.interpreted-text role="guilabel"} section.

::: {.note}
::: {.title}
Note
:::

If this is the first time
`Live Chat </applications/websites/livechat>`{.interpreted-text
role="doc"} has been enabled on the database, the page may need to be
saved manually and refreshed before any further steps can be taken.
:::

After the `Live Chat`{.interpreted-text role="guilabel"} setting is
enabled on a *Helpdesk* team, a new *Live Chat* channel is created.
Click on `Configure Live Chat Channel`{.interpreted-text
role="guilabel"} to update the channel\'s settings.

#### Live Chat channel configuration

On the channel\'s settings page, `Channel Name`{.interpreted-text
role="guilabel"} can be edited, though, Odoo names the channel to match
the *Helpdesk* team name, by default.

::: {.example}
If a *Helpdesk* team is named [Customer Care]{.title-ref}, a *Live Chat*
channel is created called [Customer Care]{.title-ref}.

{.align-center}
:::

On the channel form, navigate through the tabs to complete the setup.

##### Operators tab

*Operators* are the users who act as agents and respond to live chat
requests from customers. The user who created the live chat channel is
added by default.

To add additional users, click on the `Operators`{.interpreted-text
role="guilabel"} tab, then click `Add`{.interpreted-text
role="guilabel"}.

Click the checkbox next to the users to be added on the
`Add: Operators`{.interpreted-text role="guilabel"} pop-up window that
appears, then click `Select`{.interpreted-text role="guilabel"}.

Click `New`{.interpreted-text role="guilabel"} to create new operators,
if needed.

When the desired addition is complete, click
`Save & Close`{.interpreted-text role="guilabel"}, or
`Save & New`{.interpreted-text role="guilabel"} to add multiple new
operators.

::: {.danger}
::: {.title}
Danger
:::

Creating a new user can impact the status of an Odoo subscription, as
the total number of users in a database counts towards the billing rate.
Proceed with caution before creating a new user. If a user already
exists, adding them as an operator will **not** alter the subscription
or billing rate for a database.
:::

Additionally, current operators can be edited or removed by clicking on
their respective boxes in the `Operators`{.interpreted-text
role="guilabel"} tab, and then adjusting their form values on the pop-up
form that appears, or by using one of the buttons located at the bottom
of the form, such as `Remove`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Users can add themselves as an operator by clicking the
`Join Channel`{.interpreted-text role="guilabel"} button on a *Live
Chat* channel.

{.align-center}
:::

##### Options tab

The `Options`{.interpreted-text role="guilabel"} tab contains the visual
and text settings for the live chat window.

{.align-center}

-   `Notification Text`{.interpreted-text role="guilabel"}: this field
    updates the greeting displayed in the text bubble when the live chat
    button appears on the website.
-   `Livechat Button Color`{.interpreted-text role="guilabel"}: this
    field alters the color of the live chat button as it appears on the
    website. To change the color, click on a color bubble to open the
    color selection window, then click and drag the circle along the
    color gradient. Click out of the selection window once complete.
    Click the refresh icon to the right of the color bubbles to reset
    the colors to the default selection.
-   `Show`{.interpreted-text role="guilabel"}: the chat button displays
    on the selected page.
-   `Show with notification`{.interpreted-text role="guilabel"}: the
    chat button is displayed, with the addition of the
    `Notification text`{.interpreted-text role="guilabel"} from the
    `Options`{.interpreted-text role="guilabel"} tab.
-   `Open automatically`{.interpreted-text role="guilabel"}: the chat
    button is displayed, and automatically opens the chat window after a
    designated amount of time. The amount of time is designated in the
    `Open
    automatically timer`{.interpreted-text role="guilabel"} field, which
    appears only when this display option is selected.
-   `Hide`{.interpreted-text role="guilabel"}: the chat button is hidden
    from display on the webpage.

::: {.tip}
::: {.title}
Tip
:::

Color selection, for the button or header, can be made manually, or
through RGB, HSL, or HEX code selection. Different options are
available, depending on the operating system or browser.
:::

##### Channel Rules tab

The `Channel Rules`{.interpreted-text role="guilabel"} tab determines
when the live chat window opens on the website by logic of when a
`URL Regex`{.interpreted-text role="guilabel"} action is triggered
(e.g., a page visit).

::: {.tip}
::: {.title}
Tip
:::

A regex, or regular expression, is sometimes referred to as a rational
expression. It is a sequence of characters that specifies a match
pattern in text. A match is made within the given range of numbers or
for the set of characters.
:::

Edit existing rules by selecting them from the
`Channel Rules`{.interpreted-text role="guilabel"} tab, or create a new
rule by clicking `Add a line`{.interpreted-text role="guilabel"}.

Then, proceed to configure the details for how the rule should apply on
the pop-up form that appears.

Choose how the *Live Chat Button* displays on the webpage.

-   `Show`{.interpreted-text role="guilabel"}: the chat button displays
    on the selected page.
-   `Show with notification`{.interpreted-text role="guilabel"}: the
    chat button is displayed, with the addition of the
    `Notification text`{.interpreted-text role="guilabel"} from the
    `Options`{.interpreted-text role="guilabel"} tab.
-   `Open automatically`{.interpreted-text role="guilabel"}: the chat
    button is displayed, and automatically opens the chat window after a
    designated amount of time. The amount of time is designated in the
    `Open
    automatically timer`{.interpreted-text role="guilabel"} field, which
    appears only when this display option is selected.
-   `Hide`{.interpreted-text role="guilabel"}: the chat button is hidden
    from display on the webpage.

To include a `Chatbot`{.interpreted-text role="guilabel"} on this
channel, select it from the drop-down menu. If the chatbot should only
be active when no operators are available, check the box labeled
`Enabled only
if no operator`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

If a
`chatbot </applications/websites/livechat/chatbots>`{.interpreted-text
role="doc"} is added to a live chat channel, a new
`Chatbots`{.interpreted-text role="guilabel"} smart button appears on
the channel settings form. Click here to create and update the chatbot
*script*.

Each line in the script contains a `Message`{.interpreted-text
role="guilabel"}, `Step Type`{.interpreted-text role="guilabel"},
`Answers`{.interpreted-text role="guilabel"}, and conditional *Only If*
logic that applies when certain pre-filled answers are chosen.

To create more steps in the script, click `Add a line`{.interpreted-text
role="guilabel"}, and fill out the script steps form, according to the
desired logic.
:::

Add the URLs for the pages where the channel should appear in the
`URL Regex`{.interpreted-text role="guilabel"} field. Only the path from
the root domain is needed, not the full URL.

If this channel should only be available to users in specific countries,
add those countries to the `Country`{.interpreted-text role="guilabel"}
field. If this field is left blank, the channel is available to all site
visitors.

{.align-center}

##### Widget tab

The `Widget`{.interpreted-text role="guilabel"} tab on the live chat
channel form offers a website widget that can be added to third-party
websites. Additionally, a URL is available, that can provide instant
access to a live chat window.

The live chat `Widget`{.interpreted-text role="guilabel"} can be applied
to websites created through Odoo by navigating to the
`Website app --> Configuration --> Settings --> Email & Marketing`{.interpreted-text
role="menuselection"}. Then, scroll to the `Live Chat`{.interpreted-text
role="guilabel"} field, and select the channel to add to the site. Click
`Save`{.interpreted-text role="guilabel"} to apply.

To add the widget to a website created on a third-party website, click
the `Copy`{.interpreted-text role="guilabel"} button next to the first
listed code, and paste the code into the [\<head\>]{.title-ref} tag on
the site.

To send a live chat session to a customer or supplier, click the
`Copy`{.interpreted-text role="guilabel"} button next to the second
listed code, and send the URL via email.

#### Create a support ticket from a live chat session

Operators who have joined a live chat channel are able to communicate
with site visitors in real-time.

During the conversation, an operator can use the shortcut `command
</applications/websites/livechat/responses>`{.interpreted-text
role="doc"} [/ticket]{.title-ref} to create a ticket without leaving the
chat window. The transcript from the conversation is added to the new
ticket, under the `Description`{.interpreted-text role="guilabel"} tab.

::: {.tip}
::: {.title}
Tip
:::

*Helpdesk* tickets can also be created through the `WhatsApp
</applications/productivity/whatsapp>`{.interpreted-text role="doc"} app
using the same [/ticket]{.title-ref} command.
:::

### Website Form {#helpdesk/receiving_tickets/website-form}

Enabling the *Website Form* setting adds a new page to the website with
a customizable form. A new ticket is created once the required form
fields are filled out and submitted.

To activate the website form, navigate to a team\'s settings page under
`Helpdesk app
--> Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"}, and selecting the desired team from the list.

Then, locate the `Website Form`{.interpreted-text role="guilabel"}
feature, under the `Help Center`{.interpreted-text role="guilabel"}
section, and check the box.

If more than one website is active on the database, confirm the correct
website is listed in the `Website`{.interpreted-text role="guilabel"}
field. If not, select the correct one from the drop-down list.

After the feature is activated, click the
`Go to Website`{.interpreted-text role="guilabel"} smart button at the
top of the `Teams`{.interpreted-text role="guilabel"} settings page to
view and edit the new website form, which is created automatically by
Odoo.

::: {.note}
::: {.title}
Note
:::

After enabling the `Website Form`{.interpreted-text role="guilabel"}
setting, the team\'s settings page may need to be refreshed before the
`Go to Website`{.interpreted-text role="guilabel"} smart button appears.

Additionally, if a *Help Center* is published, the smart button
navigates there first. Simply click the `Contact Us`{.interpreted-text
role="guilabel"} button, at the bottom of the forum, to navigate to the
ticket submission form.
:::

![View of the settings page of a helpdesk team emphasizing the Go to Website button in
Odoo Helpdesk.](receiving_tickets/receiving-tickets-go-to-website.png){.align-center}

#### Website ticket form customization

To customize the default ticket submission form, while on the website,
click the `Edit`{.interpreted-text role="guilabel"} button in the
upper-right corner of the page. This opens the editing sidebar on the
right side. Then, click on one of the fields in the form, on the body of
the website, to edit it.

To add a new field, go to the `Field`{.interpreted-text role="guilabel"}
section of the sidebar, and click `+
Field`{.interpreted-text role="guilabel"}.

Click the `🗑️ (trash can)`{.interpreted-text role="guilabel"} icon to
delete the field, if necessary.

Edit the other options for the new field in the sidebar, as desired:

-   `Type`{.interpreted-text role="guilabel"}: matches an Odoo model
    value to the field (e.g. [Customer Name]{.title-ref}).
-   `Input Type`{.interpreted-text role="guilabel"}: determine what type
    of input the field should be, like [Text]{.title-ref},
    [Email]{.title-ref}, [Telephone]{.title-ref}, or [URL]{.title-ref}.
-   `Label`{.interpreted-text role="guilabel"}: give the form field a
    label (e.g. [Full Name]{.title-ref}, [Email Address]{.title-ref},
    etc.). Also control the label position on the form by using the
    nested `Position`{.interpreted-text role="guilabel"} options.
-   `Description`{.interpreted-text role="guilabel"}: determine whether
    or not to add an editable line under the input box to provide
    additional contextual information related to the field.
-   `Placeholder`{.interpreted-text role="guilabel"}: add a sample input
    value.
-   `Default Value`{.interpreted-text role="guilabel"}: add common use
    case values that most customers would find valuable. For example,
    this can include prompts of information customers should include to
    make it easier to solve their issue, such as an account number, or
    product number.
-   `Required`{.interpreted-text role="guilabel"}: determine whether or
    not to mark a field as required, in order for the form to be
    submitted. Toggle the switch from gray to blue.
-   `Visibility`{.interpreted-text role="guilabel"}: allow for absolute
    or conditional visibility of the field. Nested options, such as,
    device visibility, appear when certain options are selected.
-   `Animation`{.interpreted-text role="guilabel"}: choose whether or
    not the field should include animation.

{.align-center}

Once the form has been optimized, and is ready for public use, click
`Save`{.interpreted-text role="guilabel"} to apply the changes. Then,
publish the form by toggling the `Unpublished`{.interpreted-text
role="guilabel"} switch to `Published`{.interpreted-text
role="guilabel"} at the top of the page, if necessary.

Prioritizing tickets
--------------------

All tickets include a `Priority`{.interpreted-text role="guilabel"}
field. The highest priority tickets appear at the top of the Kanban and
list views.

{.align-center}

The priority levels are represented by stars:

-   0 stars = *Low Priority*
-   1 star = *Medium Priority*
-   2 stars = *High Priority*
-   3 stars = *Urgent*

Tickets are set to low priority (0 stars) by default. To change the
priority level, select the appropriate number of stars on the Kanban
card, or on the ticket.

::: {.warning}
::: {.title}
Warning
:::

As priority levels can be used as criteria for assigning
`SLAs <sla>`{.interpreted-text role="doc"}, changing the priority level
of a ticket can alter the
`SLA (Service Level Agreement)`{.interpreted-text role="abbr"} deadline.
:::

::: {.seealso}
\-
`/applications/services/helpdesk/advanced/close_tickets`{.interpreted-text
role="doc"} - `../../../general/email_communication`{.interpreted-text
role="doc"} - `/applications/websites/livechat`{.interpreted-text
role="doc"}
:::
