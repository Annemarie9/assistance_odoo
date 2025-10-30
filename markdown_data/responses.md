# File: /content/odoo_doc17.0/fr/content/applications/websites/livechat/responses.md

Commands and canned responses
=============================

In the Odoo **Live Chat** application, *commands* allow the user to
perform specific actions both inside the chat window, and through other
Odoo applications. The **Live Chat** app also includes *canned
responses*. These are customized, preconfigured substitutions that allow
users to replace shortcut entries in place of longer, well-thought out
responses to some of the most common questions and comments.

Both commands and canned responses save time, and allow users to
maintain a level of consistency throughout their conversations.

Execute a command
-----------------

Live chat *commands* are keywords that trigger preconfigured actions.
When a live chat *operator* is participating in a conversation with a
customer or website visitor, they can execute a command by typing
[/]{.title-ref}, followed by the command.

Commands, and the resulting actions, are only visible in the
conversation window for the live chat operator. A customer does not see
any commands that an operator uses in a conversation from their view of
the chat.

::: {.example}
During a conversation with a customer, a live chat operator executes the
command to `create
a ticket <live-chat/ticket>`{.interpreted-text role="ref"}. After
entering the command, [/ticket]{.title-ref}, the system automatically
creates a ticket with the information from the conversation. It also
includes a link to the new ticket, so the operator can go there directly
to add any additional information, if necessary.

{.align-center}
:::

More information about each available command can be found below.

### Help

If an operator types [/help]{.title-ref} in the chat window, an
informative message that includes the potential entry types an operator
can make is displayed.

-   Type [\@username]{.title-ref} to mention a user in the conversation.
    A notification will be sent to that user\'s inbox or email,
    depending on their notification settings.
-   Type [/command]{.title-ref} to execute a command.
-   Type [:shortcut]{.title-ref} to insert a
    `canned response <live-chat/canned-responses>`{.interpreted-text
    role="ref"}.

::: {.seealso}
\- `/applications/productivity/discuss`{.interpreted-text role="doc"} -
`/applications/productivity/discuss/team_communication`{.interpreted-text
role="doc"}
:::

### Ticket & search tickets

The [/ticket]{.title-ref} and [/search\_tickets]{.title-ref} commands
allow operators to create helpdesk tickets directly from a conversation,
and search through existing tickets by keyword or ticket number.

::: {.important}
::: {.title}
Important
:::

The [/ticket]{.title-ref} and [/search\_tickets]{.title-ref} commands
can **only** be used if the **Helpdesk** app has been installed, and
*Live Chat* has been activated on a *Helpdesk* team. To activate *Live
Chat*, go to
`Helpdesk app --> Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"}, and select a team. Scroll to the
`Channels`{.interpreted-text role="guilabel"} section, and check the box
labeled, `Live Chat`{.interpreted-text role="guilabel"}.
:::

#### Create a ticket from a live chat {#live-chat/ticket}

If an operator types [/ticket]{.title-ref} in the chat window, the
conversation is used to create a *Helpdesk* ticket.

After entering the [/ticket]{.title-ref} command, type a title for the
ticket into the chat window, then press [Enter]{.title-ref}.

{.align-center}

The newly created ticket will be added to the *Helpdesk* team that has
live chat enabled. If more than one team has live chat enabled, the
ticket will automatically be assigned based on the team\'s priority.

The transcript from the conversation will be added to the new ticket,
under the `Description`{.interpreted-text role="guilabel"} tab.

To access the new ticket, click on the link in the chat window, or go to
the `Helpdesk app`{.interpreted-text role="menuselection"} and click the
`Tickets`{.interpreted-text role="guilabel"} button on the Kanban card
for the appropriate team.

#### Search for a ticket from a live chat

If an operator types [/search\_tickets]{.title-ref} in the chat window,
they can search through *Helpdesk* tickets, either by ticket number or
keyword.

After entering the [/search\_tickets]{.title-ref} command, type a
keyword or ticket number, then press `Enter`{.interpreted-text
role="kbd"}. If one or more related tickets are found, a list of links
is generated in the conversation window.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Results from the search command will only be seen by the operator, not
the customer.
:::

### History

If an operator types [/history]{.title-ref} in the chat window, it
generates a list of the most recent pages the visitor has viewed on the
website (up to 15).

{.align-center}

### Lead

By typing [/lead]{.title-ref} in the chat window, an operator can create
a *lead* in the **CRM** application.

{.align-center}

::: {.important}
::: {.title}
Important
:::

The [/lead]{.title-ref} command can only be used if the **CRM** app has
been installed.
:::

After typing [/lead]{.title-ref}, create a title for this new lead, then
press [Enter]{.title-ref}. A link with the lead title appears. Click the
link, or navigate to the `CRM`{.interpreted-text role="menuselection"}
app to view the `Pipeline`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The link to the new lead can only be seen and accessed by the operator,
not the customer.
:::

The transcript of that specific live chat conversation (where the lead
was created) is added to the `Internal Notes`{.interpreted-text
role="guilabel"} tab of the lead form.

On the `Extra Information`{.interpreted-text role="guilabel"} tab of the
lead form, the `Source`{.interpreted-text role="guilabel"} will be
listed as `Livechat`{.interpreted-text role="guilabel"}.

### Leave

If an operator types [/leave]{.title-ref} in the chat window, they can
automatically exit the conversation. This command does not cause the
customer to be removed from the conversation, nor does it automatically
end the conversation.

::: {.seealso}
\- `/applications/sales/crm/acquire_leads`{.interpreted-text role="doc"}
- `../../services/helpdesk`{.interpreted-text role="doc"}
:::

Canned responses {#live-chat/canned-responses}
----------------

*Canned responses* are customizable inputs where a *shortcut* stands in
for a longer response. An operator will enter the shortcut, and it is
automatically replaced by the expanded *substitution* response in the
conversation.

### Create canned responses

To create a new canned response, go to
`Live Chat app --> Configuration --> Canned
Responses --> New`{.interpreted-text role="menuselection"}.

Type a shortcut command in the `Shortcut`{.interpreted-text
role="guilabel"} field. Next, click the `Substitution`{.interpreted-text
role="guilabel"} field, and type the message that should replace the
shortcut.

::: {.tip}
::: {.title}
Tip
:::

Try to connect the shortcut to the topic of the substitution. The easier
it is for the operators to remember, the easier it is to use the canned
responses in conversations.
:::

### Use canned responses in a live chat conversation

To use a canned response during a live chat conversation, type a colon
([:]{.title-ref}) into the chat window, followed by the shortcut.

::: {.example}
An operator is chatting with a visitor. As soon as they type
[:]{.title-ref} they would see a list of available responses. They can
manually select one from the list, or continue to type. If they want to
use the canned response [\'I am sorry to hear that.\']{.title-ref}, they
would type [:sorry]{.title-ref}.
:::

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

Typing [:]{.title-ref} into a chat window on its own will generate a
list of available canned responses. Responses can be manually selected
from the list, in addition to the use of shortcuts.

{.align-center}
:::
