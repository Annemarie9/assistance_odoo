# File: /content/odoo_doc17.0/fr/content/applications/websites/livechat.md

show-content

:   

Live Chat
=========

Odoo **Live Chat** allows users to communicate with website visitors in
real-time. With **Live Chat**, leads can be qualified for their sales
potential, support questions can be answered quickly, and issues can be
directed to the appropriate team for further investigation or follow up.
**Live Chat** also provides the opportunity for instant feedback from
customers.

Enable Live Chat
----------------

The **Live Chat** application can be installed multiple ways:

-   Go to `Apps application`{.interpreted-text role="menuselection"},
    search [Live Chat]{.title-ref}, and click
    `Install`{.interpreted-text role="guilabel"}.

-   Go to the
    `Helpdesk app --> Configuration --> Helpdesk Teams`{.interpreted-text
    role="menuselection"} list view, select a team, and on the team\'s
    settings page, click the checkbox next to
    `Live Chat`{.interpreted-text role="guilabel"}, under the
    `Channels`{.interpreted-text role="guilabel"} section.

-   In the `Website`{.interpreted-text role="menuselection"} app, go to
    `Configuration --> Settings`{.interpreted-text
    role="menuselection"}, scroll to the
    `Email & Marketing`{.interpreted-text role="guilabel"} section,
    check the box next to `Livechat`{.interpreted-text role="guilabel"},
    and click `Save`{.interpreted-text role="guilabel"}.

    {.align-center}

::: {.note}
::: {.title}
Note
:::

After the **Live Chat** application is installed, a live chat *Channel*
is created, by default.
:::

Create live chat channels
-------------------------

To create a new live chat *Channel*, go to
`Main Odoo Dashboard --> Live Chat app -->
New`{.interpreted-text role="menuselection"}. This opens a blank channel
detail form. Enter the name of the new channel in the
`Channel Name`{.interpreted-text role="guilabel"} field.

{.align-center}

To configure the remaining tabs on the channel detail form (`Operators
<livechat/operators-tab>`{.interpreted-text role="ref"},
`Options <livechat/options-tab>`{.interpreted-text role="ref"},
`Channel Rules
<livechat/channel-rules-tab>`{.interpreted-text role="ref"}, and
`Widget <livechat/widget-tab>`{.interpreted-text role="ref"}), follow
the steps below.

::: {.tip}
::: {.title}
Tip
:::

The channel detail form for any channel can be accessed by navigating
back to the `Website Live Chat Channels`{.interpreted-text
role="guilabel"} dashboard, via the breadcrumbs. Find the Kanban card
for the appropriate live chat channel, hover over it, and then click on
the `fa-ellipsis-v`{.interpreted-text role="icon"}
`(vertical ellipsis)`{.interpreted-text role="guilabel"} icon to open
the drop-down menu. Click `Configure
Channel`{.interpreted-text role="guilabel"} to open the channel detail
form.
:::

### Operators tab {#livechat/operators-tab}

*Operators* are the users who act as agents and respond to live chat
requests from customers. When a user is added as an operator in a live
chat channel, they can receive chats from website visitors wherever they
are in the database. Chat windows open in the bottom-right corner of the
screen.

{.align-center}

On the channel detail form, click the `Operators`{.interpreted-text
role="guilabel"} tab. The user who originally created the live chat
channel has been added as an operator by default.

::: {.note}
::: {.title}
Note
:::

Current operators can be edited, or removed, by clicking on their
respective boxes in the `Operators`{.interpreted-text role="guilabel"}
tab, which reveals a separate `Open: Operators`{.interpreted-text
role="guilabel"} modal. In that modal, adjust any information, as
needed. Then, click `Save`{.interpreted-text role="guilabel"}, or click
`Remove`{.interpreted-text role="guilabel"} to remove that operator from
the channel.
:::

Click `Add`{.interpreted-text role="guilabel"} to reveal an
`Add: Operators`{.interpreted-text role="guilabel"} pop-up window.

In the pop-up window, scroll to find the desired users, or enter their
name in the search bar. Then, tick the checkbox next to the users to be
added, and click `Select`{.interpreted-text role="guilabel"}.

New operators can be created and added to the list directly from this
pop-up window, as well, by clicking `New`{.interpreted-text
role="guilabel"}, and filling out the
`Create Operators`{.interpreted-text role="guilabel"} form. When the
form is complete, click `Save & Close`{.interpreted-text
role="guilabel"}, or `Save & New`{.interpreted-text role="guilabel"} for
multiple record creations.

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

### Options tab {#livechat/options-tab}

The `Options`{.interpreted-text role="guilabel"} tab on the live chat
channel detail form contains the visual and text settings for the live
chat window.

#### Livechat button {#livechat/livechat-button}

The *Livechat Button* is the icon that appears in the bottom-right
corner of the website.

{.align-center}

Change the text in the `Notification text`{.interpreted-text
role="guilabel"} field to update the greeting displayed in the text
bubble when the live chat button appears on the website.

The `Livechat Button Color`{.interpreted-text role="guilabel"} alters
the color of the live chat button as it appears on the website. To
change the color, click on a color bubble to open the color selection
window, then click and drag the circle along the color gradient. Click
out of the selection window once complete. Click the
`fa-refresh`{.interpreted-text role="icon"}
`(refresh)`{.interpreted-text role="guilabel"} icon to the right of the
color bubbles to reset the colors to the default selection.

::: {.tip}
::: {.title}
Tip
:::

Color selection, for the button or header, can be made manually using a
slider or through RGB, HSL, or HEX color code entries from the pop-up
color selection window that appears when either of the color bubbles are
clicked. Different options are available, depending on the operating
system.
:::

#### Livechat Window

The *Livechat Window* is the space where the live chat conversation with
website visitors takes place.

Edit the `Welcome Message`{.interpreted-text role="guilabel"} to change
the message a visitor sees when they open a new chat session. This
message appears as though it is sent by a live chat operator, and acts
as both a greeting and an invitation to continue the conversation.

Edit the `Chat Input Placeholder`{.interpreted-text role="guilabel"} to
alter the text that appears in the box where visitors type their
replies. This message prompts the visitor to initiate the chat.

The *Channel Header* is the colored bar at the top of the chat window.
The `Channel Header
Color`{.interpreted-text role="guilabel"} can be changed following the
same steps as the `Livechat button
<livechat/livechat-button>`{.interpreted-text role="ref"}.

![The live chat window with a purple channel header and placeholder text
that reads, \"Say
Something\...\"](livechat/chat-window.png){.align-center}

### Channel Rules tab {#livechat/channel-rules-tab}

To configure which website user actions open the live chat window, go to
the `Channel
Rules`{.interpreted-text role="guilabel"} tab on the live chat channel
detail form.

To create a new channel rule, click `Add a line`{.interpreted-text
role="guilabel"}. This opens the `Create Rules`{.interpreted-text
role="guilabel"} pop-up window.

{.align-center}

#### Create new rules

Fill out the fields on the `Create Rules`{.interpreted-text
role="guilabel"} pop-up window as instructed below, then click
`Save & Close`{.interpreted-text role="guilabel"}.

::: {.tabs}
::: {.tab}
Live Chat Button

The *Livechat Button* is the icon that appears in the bottom-right
corner of the website. Select from one of the following display options:

-   `Show`{.interpreted-text role="guilabel"}: displays the chat button
    on the page.
-   `Show with notification`{.interpreted-text role="guilabel"}:
    displays the chat button, as well as a floating text bubble next to
    the button.
-   `Open automatically`{.interpreted-text role="guilabel"}: displays
    the button, and automatically opens the chat window after a
    specified amount of time (designated in the
    `Open automatically timer`{.interpreted-text role="guilabel"} field,
    that appears when this option is selected).
-   `Hide`{.interpreted-text role="guilabel"}: hides the chat button on
    the page.
:::

::: {.tab}
Chatbot

To include a `Chatbot <livechat/chatbots>`{.interpreted-text role="doc"}
on this channel, select it from the drop-down menu. If the chatbot
should only be active when no operators are active, check the box
labeled `Enabled only if no operator`{.interpreted-text
role="guilabel"}.

The `Enabled only if no operator`{.interpreted-text role="guilabel"}
field is **only** visible if a chatbot is selected in the
`Chatbot`{.interpreted-text role="guilabel"} field.
:::

::: {.tab}
URL Regex

The *URL Regex* specifies the web pages where this rule should be
applied. In the `URL Regex`{.interpreted-text role="guilabel"} field,
input the relative URL of the page where the chat button should appear.

For example, to apply the rule to the URL,
[https://mydatabse.odoo.com/shop]{.title-ref}, enter [/shop]{.title-ref}
to the `URL Regex`{.interpreted-text role="guilabel"} field.

To apply the rule to *all* pages on the database, enter [/]{.title-ref}
in the `URL Regex`{.interpreted-text role="guilabel"} field.
:::

::: {.tab}
Open automatically timer

This field designates the amount of time (in seconds) a page should be
open before the chat window opens. This field **only** appears if the
`Live Chat Button`{.interpreted-text role="guilabel"} for this rule is
set to `Open automatically`{.interpreted-text role="guilabel"}.
:::

::: {.tab}
Country

If this channel should **only** be available to site visitors in
specific countries, add them to the `Country`{.interpreted-text
role="guilabel"} field. If this field is left blank, the channel is
available to all site visitors, regardless of location.
:::
:::

::: {.note}
::: {.title}
Note
:::

In order to track the geographical location of visitors, *GeoIP*
**must** be installed on the database. While this feature is installed
by default on *Odoo Online* databases, *On-Premise* databases require
additional
`setup steps </administration/on_premise/geo_ip>`{.interpreted-text
role="doc"}.
:::

### Widget tab {#livechat/widget-tab}

The `Widget`{.interpreted-text role="guilabel"} tab on the live chat
channel detail form provides the code for a website widget. This code
can be added to a website to provide access to a live chat window.

::: {.tip}
::: {.title}
Tip
:::

The live chat widget can be added to websites created through Odoo by
navigating to
`Website app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Then, scroll to the
`Email & Marketing`{.interpreted-text role="menuselection"} section. In
the `Channel`{.interpreted-text role="guilabel"} field, select the
channel to add to the site. Click `Save`{.interpreted-text
role="guilabel"} to apply.
:::

To add the widget to a website created on a third-party platform, click
the first `COPY`{.interpreted-text role="guilabel"} button on the
`Widget`{.interpreted-text role="guilabel"} tab, and paste the code into
the [\<head\>]{.title-ref} tag on the site.

Likewise, to send a live chat session to a customer, click the second
`COPY`{.interpreted-text role="guilabel"} button on the
`Widget`{.interpreted-text role="guilabel"} tab. This link can be sent
directly to a customer. When they click the link, they are redirected to
a new chat window.

{.align-center}

::: {.seealso}
\- `../productivity/discuss`{.interpreted-text role="doc"} -
`livechat/responses`{.interpreted-text role="doc"} -
`livechat/ratings`{.interpreted-text role="doc"} -
`livechat/chatbots`{.interpreted-text role="doc"} -
`livechat/participate`{.interpreted-text role="doc"}
:::

::: {.toctree titlesonly=""}
livechat/ratings livechat/responses livechat/chatbots livechat/reports
livechat/participate
:::
