# File: /content/odoo_doc17.0/fr/content/applications/websites/website/mail_groups.md

Mail groups
===========

The **mail groups** feature allows website visitors to have a public
discussion by email. They can join a group to receive emails from other
group members (i.e., website users who have subscribed to the group) and
send new ones to all group members.

To activate the feature, `install <general/install>`{.interpreted-text
role="ref"} the `Website Mail Group`{.interpreted-text role="guilabel"}
([website\_mail\_group]{.title-ref}) module.

::: {.note}
::: {.title}
Note
:::

The **mail groups** feature is not to be confused with the
`../../marketing/email_marketing/mailing_lists`{.interpreted-text
role="doc"} in the Email Marketing app.
:::

Configuring mail groups {#website/mailing_lists/configure_groups}
-----------------------

To configure mail groups, proceed as follows:

1.  Configure a custom email alias domain by accessing the **General
    settings**, scrolling down to the `Discuss`{.interpreted-text
    role="guilabel"} section, enabling the
    `Custom Email Server`{.interpreted-text role="guilabel"} feature,
    and entering the `Alias domain`{.interpreted-text role="guilabel"}
    (e.g., [\@mycompany.com]{.title-ref}).
2.  Go to
    `Website --> Configuration --> Mailing Lists`{.interpreted-text
    role="menuselection"}, then click `New`{.interpreted-text
    role="guilabel"}.
3.  Specify a `Group Name`{.interpreted-text role="guilabel"}, the
    `Email Alias`{.interpreted-text role="guilabel"}, and a
    `Description`{.interpreted-text role="guilabel"}.
4.  Enable `Moderate this group`{.interpreted-text role="guilabel"} and
    specify the `Moderators`{.interpreted-text role="guilabel"} if you
    wish to
    `moderate messages <website/mailing_lists/moderate>`{.interpreted-text
    role="ref"} from this group. Alternatively, if the group is not
    moderated, you can define `Responsible Users`{.interpreted-text
    role="guilabel"} who can manage the messages in the group.
5.  In the `Privacy`{.interpreted-text role="guilabel"} tab, define who
    can subscribe to the mail group:
    -   `Everyone`{.interpreted-text role="guilabel"}: to make the mail
        group public so anyone can subscribe to it;
    -   `Members only`{.interpreted-text role="guilabel"}: to only allow
        users defined as members to subscribe to the mail group;
    -   `Selected group of users`{.interpreted-text role="guilabel"}: to
        only allow users from the `Authorized group`{.interpreted-text
        role="guilabel"} to subscribe to the mail group.
6.  If the mail group is moderated, you can automatically notify authors
    when their message is pending moderation by enabling
    `Automatic notification`{.interpreted-text role="guilabel"} in the
    `Notify
    Members`{.interpreted-text role="guilabel"} tab and writing the
    `Notification message`{.interpreted-text role="guilabel"}.
7.  If you wish to send out guidelines to new subscribers, enable
    `Send guidelines to new
    subscribers`{.interpreted-text role="guilabel"} and write them in
    the `Guidelines`{.interpreted-text role="guilabel"} tab. This is
    particularly useful when the mail group is moderated.

Using mail groups
-----------------

### Subscribing/unsubscribing

Based on the
`configuration of the mail group <website/mailing_lists/configure_groups>`{.interpreted-text
role="ref"}, users can subscribe to and unsubscribe from mail groups
from the website page ([/groups]{.title-ref} by default).



Internal users can also do this from
`Website --> Configuration --> Mailing Lists`{.interpreted-text
role="menuselection"}, using the `Join`{.interpreted-text
role="guilabel"} and `Leave`{.interpreted-text role="guilabel"} buttons.

### Sending messages

To send messages to a mail group, website users can email the
`mail group's email address
<website/mailing_lists/configure_groups>`{.interpreted-text role="ref"}.
Internal users can also create messages directly from Odoo. To do so, go
to `Website --> Configuration --> Mailing Lists`{.interpreted-text
role="menuselection"}, select the mail group, click the
`Emails`{.interpreted-text role="guilabel"} smart button, and click
`New`{.interpreted-text role="guilabel"}. Then, fill in the fields and
click `Send`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

\- The list of messages can also be accessed by selecting the group from
the [/groups]{.title-ref} website page. - Group members can also
unsubscribe from the group, access the mail group page, and send emails
to the group using the URLs in the footer of any group email they have
received.


:::

Moderating mail group messages {#website/mailing_lists/moderate}
------------------------------

If the `Moderate this group`{.interpreted-text role="guilabel"} feature
has been enabled for the
`mail group <website/mailing_lists/configure_groups>`{.interpreted-text
role="ref"}, one of the `Moderators`{.interpreted-text role="guilabel"}
must approve the group\'s messages before they are dispatched to the
other members.

To moderate messages, go to
`Website --> Configuration --> Mailing Lists`{.interpreted-text
role="menuselection"}, select the mail group, and click the
`To review`{.interpreted-text role="guilabel"} smart button. You can
moderate messages using the buttons at the end of the message line or
select a message to view its content and moderate it accordingly.

> 

The following actions are available:

-   `Accept`{.interpreted-text role="guilabel"}: to accept the email and
    send it to the mail group members.
-   `Reject`{.interpreted-text role="guilabel"}: to reject the email. In
    the pop-up window that opens, click
    `Reject Silently`{.interpreted-text role="guilabel"} to reject the
    email without notifying the author, or specify an explanation for
    rejecting the message, then click `Send & Reject`{.interpreted-text
    role="guilabel"} to reject the message and send the explanation to
    the author.
-   `Whitelist`{.interpreted-text role="guilabel"}: to whitelist the
    author, i.e. automatically accept all of their emails. As a result,
    a
    `moderation rule <website/mailing_lists/moderate>`{.interpreted-text
    role="ref"} is created for the author\'s email address with the
    status `Always allow`{.interpreted-text role="guilabel"}.
-   `Ban`{.interpreted-text role="guilabel"}: to blacklist the author,
    i.e. automatically discard all their emails. In the pop-up window
    that opens, click `Ban`{.interpreted-text role="guilabel"} to ban
    the author without notifying them, or specify an explanation, then
    click `Send & Ban`{.interpreted-text role="guilabel"} to ban the
    author and send them the explanation. As a result, a
    `moderation rule <website/mailing_lists/moderate>`{.interpreted-text
    role="ref"} is created for the author\'s email address with the
    status `Permanent ban`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Messages can also be moderated from the group\'s list of messages. Go to
`Website
--> Groups --> Mailing List Groups`{.interpreted-text
role="menuselection"}, select the mail group and click the
`Emails`{.interpreted-text role="guilabel"} smart button.
:::

Whitelisting/Blacklisting authors {#website/mailing_lists/moderation_rules}
---------------------------------

You can whitelist or blacklist an author either directly
`from a mail group message
<website/mailing_lists/moderate>`{.interpreted-text role="ref"}, or by
creating a moderation rule. To do so, go to
`Website --> Configuration --> Moderation Rules`{.interpreted-text
role="menuselection"} and click `New`{.interpreted-text
role="guilabel"}. Then, select the `Group`{.interpreted-text
role="guilabel"}, specify the author\'s `Email`{.interpreted-text
role="guilabel"} and set the `Status`{.interpreted-text role="guilabel"}
field.

::: {.tip}
::: {.title}
Tip
:::

You can also access the mail group\'s moderation rules by going to
`Website -->
Configuration --> Mailing Lists`{.interpreted-text
role="menuselection"}, selecting the group, then clicking the
`Moderations`{.interpreted-text role="guilabel"} smart button.
:::
