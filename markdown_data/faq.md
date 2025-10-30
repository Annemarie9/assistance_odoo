# File: /content/odoo_doc17.0/fr/content/applications/general/email_communication/faq.md

Common emailing issues and solutions
====================================

This page lists the most common emailing issues and their solutions.

Odoo is not an email provider {#email-issues-provider}
-----------------------------

Odoo does not function like a classic email inbox, such as Gmail,
Outlook, Yahoo, etc.

While Odoo uses emails as a way to notify and communicate with
users/customers, it is, by design, not a replacement for a dedicated
email server. Therefore, it might not behave in the expected way when
compared to a traditional email inbox.

The main differences are the following:

-   By default, once a notification or transactional email (quote,
    invoice, direct message to a contact) is sent out successfully, the
    email object is deleted. The email message\'s content lives in the
    chatter of the related record. It prevents cluttering the database
    with multiple copies of the content of the same email (when sent to
    multiple recipients) if the content is already present in the
    chatter.
-   There is no concept of (blind) carbon copy (\[B\]CC). Odoo uses the
    concept of *followers* added to a chatter to automatically decide
    when and how `a contact is notified
    <email-outbound-notifications>`{.interpreted-text role="ref"} or
    receives a copy of an email.
-   Incoming emails are handled by checking if the *TO* email address is
    a valid email address in the Odoo database or, in case of a reply
    email, if there is a reference in the email header that matches a
    message sent from the Odoo database. All other emails will be
    bounced and **not** temporarily parked in a spam or quarantine
    folder. In other words, any email unrelated to an Odoo database is
    lost.

Outgoing emails {#email-issues-outgoing}
---------------

### Changing the email address of the admin user account {#email-issues-outgoing-admin-address}

When an Odoo database is created, the main admin account is assigned a
placeholder email address. It is recommended to **replace the admin
email address** with a valid email address to prevent outgoing email
issues.

To do so, on the admin account, click the user icon, click
`My Profile`{.interpreted-text role="guilabel"} (or
`Preferences`{.interpreted-text role="guilabel"}), and update the
`Email`{.interpreted-text role="guilabel"} field found under the
`Preferences`{.interpreted-text role="guilabel"} tab. Either use any
other email address or use your Odoo subdomain (e.g.,
[company-name.odoo.com]{.title-ref}) and [admin]{.title-ref} for the
local-part (e.g., [admin\@company-name.odoo.com]{.title-ref}).

### Delivery failure {#email-issues-outgoing-delivery-failure}

When a message is sent, an `fa-envelope-o`{.interpreted-text
role="icon"} `(envelope)`{.interpreted-text role="guilabel"} icon is
displayed in the chatter. The icon turns red when delivery has failed
for at least one recipient.



Left-click the envelope to display information about the delivery, and,
if possible, the relevant
`error messages <email-issues-outgoing-delivery-failure-messages>`{.interpreted-text
role="ref"}.



Click `See Error Details`{.interpreted-text role="guilabel"} to get
extra information for the fail reason, **if** Odoo was able to process
the original error or bounce email.

Click `Send & close`{.interpreted-text role="guilabel"} to retry sending
the email to all **toggled-on** (`fa-toggle-on`{.interpreted-text
role="icon"}) recipients under the `Try Again`{.interpreted-text
role="guilabel"} column. All **toggled-off**
(`fa-toggle-off`{.interpreted-text role="icon"}) recipients will be
ignored.

Click `Ignore all`{.interpreted-text role="guilabel"} to ignore all
currently failing emails and turn the envelope icon from red to white.

Unsent emails also appear in the Odoo email queue. To access it,
activate the `developer mode
<developer-mode>`{.interpreted-text role="ref"} and go to
`Settings --> Technical --> Email: Emails`{.interpreted-text
role="menuselection"}.



Failed emails display the `Delivery Failed`{.interpreted-text
role="guilabel"} status. Click `Retry`{.interpreted-text
role="guilabel"} to put a failed email in the email queue again. It will
then appear with the `Outgoing`{.interpreted-text role="guilabel"}
status. The email will be sent again the next time the scheduled action
for the email queue runs.

Optionally, queued emails can be sent immediately by clicking
`Send Now`{.interpreted-text role="guilabel"}. Click
`Cancel Email`{.interpreted-text role="guilabel"} to remove it from the
email queue.

::: {.note}
::: {.title}
Note
:::

Sent emails are periodically cleaned from the queue. This is controlled
by the *Auto-Vacuum* scheduled action that cleans redundant data on your
Odoo database.
:::

#### Common error messages {#email-issues-outgoing-delivery-failure-messages}

##### Daily limit reached {#email-issues-outgoing-delivery-failure-messages-limit}



Odoo limits the number of emails that can be sent from an Odoo Online
database. Most email service providers (e.g., Google, Yahoo, etc.) will
blacklist Odoo\'s server IP if Odoo\'s email server is sending too many
emails to addresses that do not exist or are no longer valid. It also
applies to unsolicited spam emails sent through an Odoo database.

The default daily email limit varies between **5 and 200 emails**. The
exact limit is depends on several factors (subject to change):

-   Type of database subscription (one app free, trial, paying
    subscription)
-   Apps installed (i.e., Email Marketing, Marketing Automation)
-   If a database migration is ongoing

If the daily limit is reached, you can:

-   Contact `Odoo Support <email-issues-support>`{.interpreted-text
    role="ref"} to increase your email quota. The following factors will
    be taken into account:
    1.  Numbers of users on the database

    2.  Apps installed

    3.  Bounce rate (the percentage of email addresses that did not
        receive emails because they were returned by an email server on
        their way to the final recipient).

    4.  Whether your
        `email aliases are correctly set up and use the appropriate custom domains
        <email-outbound-alias-domain>`{.interpreted-text role="ref"}.

        ::: {.tip}
        ::: {.title}
        Tip
        :::

        When using a custom domain, verify that
        `SPF <email-domain-spf>`{.interpreted-text role="ref"}, `DKIM
        <email-domain-dkim>`{.interpreted-text role="ref"}, and
        `DMARC <email-domain-dmarc>`{.interpreted-text role="ref"} are
        correctly configured so that
        `Odoo's email servers are allowed to send emails on your custom domain's behalf
        <email-outbound-custom-domain-odoo-server>`{.interpreted-text
        role="ref"}.
        :::
-   `Use an external outgoing email server <../email_communication>`{.interpreted-text
    role="doc"} to be independent of Odoo\'s email limit.
-   Wait until the next day, and retry sending the email. To do so,
    activate the `developer mode
    <developer-mode>`{.interpreted-text role="ref"}, go to
    `Settings --> Technical --> Email: Emails`{.interpreted-text
    role="menuselection"}, and click `Retry`{.interpreted-text
    role="guilabel"} next to the unsent email.

::: {.important}
::: {.title}
Important
:::

The daily email limit counts every email leaving your Odoo database,
triggered either manually or automatically. By default, any internal
message, notification, logged note, etc., counts as an email if it
notifies someone via email. This can be mitigated by receiving
`notifications in
Odoo <discuss_app/notification_preferences>`{.interpreted-text
role="ref"} instead of by email.
:::

##### SMTP error {#email-issues-outgoing-delivery-failure-messages-smtp}

[Simple Mail Transport Protocol
(SMTP)](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) is
a standard used to transmit emails between email servers and/or email
clients.

If you use
`an external STMP server to send emails <email-outbound-custom-domain-smtp-server>`{.interpreted-text
role="ref"}, a standard set of [SMTP error codes
exists](https://en.wikipedia.org/wiki/List_of_SMTP_server_return_codes#Common_status_codes).
While the code numbers are not specific to Odoo, the exact content of
the error message might vary from email server to email server.

::: {.example}
A 550 SMTP permanent delivery error from sendgrid.com:

``` {.text}
Mail Delivery Failed
Mail delivery failed via SMTP server 'None'.
SMTPDataError: 550
The from address does not match a verified Sender Identity. Mail cannot be sent until this
error is resolved. Visit https://sendgrid.com/docs/for-developers/sending-email/sender-identity/
to see the Sender Identity requirements
```

The error message indicates that you tried sending an email from an
unverified email address. Investigating the outgoing email server
configuration or the default *FROM* address of your database is a good
starting point to troubleshoot the issue, and verify that you
whitelisted the email address on the side of sendgrid.com.
:::

Usually, inputting the error message content in a Google search can
yield information on what the root cause might be and how to correct the
issue.

If the issue cannot be resolved and keeps occurring, contact
`Odoo Support
<email-issues-support>`{.interpreted-text role="ref"}.

##### No error populated {#email-issues-outgoing-delivery-failure-messages-no-error}

Odoo is not always capable of providing information on the reason a
delivery failed. The different email providers implement their own
policy on bounced emails, and it is not always possible for Odoo to
interpret it correctly.

If there is a recurring problem with the same customer or the same
domain, contact `Odoo
Support <email-issues-support>`{.interpreted-text role="ref"}.

::: {.note}
::: {.title}
Note
:::

One of the most common reasons for an email failing to be sent with no
error message is related to the
`SPF <email-domain-spf>`{.interpreted-text role="ref"} or
`DKIM <email-domain-dkim>`{.interpreted-text role="ref"} configuration.
Also, verify that the implemented email notification setup is adapted to
your business needs. See the
`Communication in Odoo by email documentation <../email_communication>`{.interpreted-text
role="doc"} for more information.
:::

### Execution time {#email-issues-outgoing-execution-time}

The exact time of an email is sent is handled by a system utility *cron*
(scheduled action) that can be used to schedule tasks to run
automatically at predetermined intervals. Odoo uses this approach to
send emails that are considered \"not urgent\" (i.e., newsletters
formats such as mass mailing, marketing automation, and events). This
avoids cluttering the mail servers and, instead, prioritizes individual
communication.

::: {.spoiler}
What is a cron?

A cron is an action that Odoo runs in the background to execute
particular code to complete a task. Odoo also creates cron triggers in
certain workflows that can trigger a scheduled action earlier than its
scheduled date. Running a scheduled action manually or changing its
frequency is generally not recommended, as it might create errors or
break specific workflows.
:::

By default, for the normal email queue, the
`Mail: Email Queue Manager`{.interpreted-text role="guilabel"} cron runs
every 60 minutes. The lowest running interval for a cron is 5 minutes.
Odoo recommends an interval of 15 minutes to ensure proper operation. If
the interval is too short, not all emails may be processed, which may
cause the cron to timeout.

Emails that are considered urgent (from one person to another, such as
sales orders, invoices, purchase orders, etc.) are sent immediately.
They do not show up under `Settings -->
Technical --> Email: Emails`{.interpreted-text role="menuselection"},
unless their delivery fails.



Email campaigns are sent as soon as possible (after clicking the
`Send`{.interpreted-text role="guilabel"} button) or at a scheduled time
(after clicking the `Schedule`{.interpreted-text role="guilabel"}
button).

For the email marketing queue, the
`Mail Marketing: Process queue`{.interpreted-text role="guilabel"} cron
runs once a day, but will be **automatically triggered early** if a
campaign is scheduled outside of this default frequency. If a mailing
list contains a large number of recipients, triggering the cron manually
multiple times is **not recommended**, as it will not accelerate the
processing time and might create errors.

::: {.tip}
::: {.title}
Tip
:::

To edit crons, enable the
`developer mode <developer-mode>`{.interpreted-text role="ref"} and go
to
`Settings --> Technical --> Automation: Scheduled Actions`{.interpreted-text
role="menuselection"}.
:::

::: {.seealso}
For more information about crons when using Odoo.sh, check out
`Odoo.sh frequent technical
questions <../../../administration/odoo_sh/advanced/frequent_technical_questions>`{.interpreted-text
role="doc"}.
:::

#### Email Marketing campaigns stuck in the queue {#email-issues-outgoing-execution-time-campaigns}

If multiple Email Marketing campaigns are put in the queue, they are
processed in chronological order based on their creation date.

::: {.example}
If there are three campaigns: Campaign\_1 (created 1st of January),
Campaign\_2 (created 2nd of January), and Campaign\_3 (created 3rd of
January), they are put in the queue by clicking `Send`{.interpreted-text
role="guilabel"} on all three of them.



The cron will try to process Campaign\_1, then Campaign\_2, and finally
Campaign\_3. It will not start processing Campaign\_2 until it finishes
processing Campaign\_1.

If an email campaign never leaves the queue, there might be an issue
with the campaign at the top of the queue. To troubleshoot, we could
remove Campaign\_1 from the queue by clicking the
`Cancel`{.interpreted-text role="guilabel"} button, and see if the two
other campaigns are sent. Then we could try to fix Campaign\_1 or
contact `Odoo Support <email-issues-support>`{.interpreted-text
role="ref"}.
:::

Incoming emails {#email-issues-incoming}
---------------

When there is an issue with incoming emails, there might not be an
indication, per se, in Odoo. It is the sending email client, who tries
to contact a database, that will get a bounce message (most of the time
a `550: mailbox unavailable`{.interpreted-text role="guilabel"} error
message).

### Email is not received {#email-issues-incoming-not-received}

::: {.tabs}
::: {.tab}
Odoo Online

Contact `Odoo Support <email-issues-support>`{.interpreted-text
role="ref"} if there is a recurring issue with the same client or
domain.
:::

::: {.tab}
Odoo.sh

You can use database logs to understand and fix issues. Logs are a
stored collection of all the tasks completed in a database. They are a
text-only representation, complete with timestamps of every action taken
on the Odoo database. This can be helpful to track emails leaving the
database. Sending failures can also be seen by logs when they indicate
that the message tried to send repeatedly. Logs show every action to the
email servers from the database.

Live logs are located in the `~/logs/`{.interpreted-text role="file"}
folder (accessed by the command line or on the Odoo.sh dashboard). Log
files are created everyday at 5:00 AM (UTC).

::: {.tip}
::: {.title}
Tip
:::

The two most recent files, for the current day and the previous one, are
named `odoo.log`{.interpreted-text role="file"} and
`odoo.log.1`{.interpreted-text role="file"}.

Log files for older dates are named using their dates and are
compressed. Use the commands `grep`{.interpreted-text role="command"}
and `zgrep`{.interpreted-text role="command"} (for the compressed ones)
to search through the files.
:::

::: {.seealso}
For more information on logs and how to access them via the Odoo.sh
dashboard, refer to the
`Odoo.sh logs documentation <odoosh/logs>`{.interpreted-text
role="ref"}.

For more information on accessing logs via the command line, refer to
the `developer
logging documentation <reference/cmdline/server/logging>`{.interpreted-text
role="ref"}.
:::
:::
:::

Information for Odoo Support {#email-issues-support}
----------------------------

Here is a list of helpful information to include when reaching out to
:

1.  An export of the full email from the inbox. These are usually in
    [.eml]{.title-ref} or [.msg]{.title-ref} file formats containing
    technical information required for an investigation. The exact
    process to download the file depends on your third-party email
    provider.

    ::: {.seealso}
    \- [Gmail Help Center: Trace an email with its full
    header](https://support.google.com/mail/answer/29436)
    -   [Microsoft Support: View internet message headers in
        Outlook](https://support.microsoft.com/en-us/office/view-internet-message-headers-in-outlook-cd039382-dc6e-4264-ac74-c048563d212c#tab=Web)
    :::

    When using a local email software (e.g., Thunderbird, Apple Mail,
    Outlook, etc.) to synchronize emails, it is usually possible to
    export the local copies of emails as EML/MSG files. Refer to the
    documentation of the software used for more information.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    If possible, the EML/MSG file should be based on the original email
    that was sent and is failing or is causing issues.

    For **incoming emails**: if possible contact the original email
    sender and request an EML/MSG copy of the original email. Sending a
    copy of the original email (forwarded) only contains partial
    information related to the troubleshooting.

    For **outgoing emails**: either provide the EML/MSG of the email or
    specify what record in the database is affected (e.g., sales order
    number, contact name, invoice number) and the date/time when the
    email was sent (e.g., email sent on the 10th January 2024 11:45 AM
    Central European Time).
    :::

2.  An explanation of the exact flow that is being followed to normally
    receive those emails in Odoo. Try to answer the following questions:

    -   Is this a notification message from a reply being received in
        Odoo?
    -   Is this a message being sent from the Odoo database?
    -   Is there an incoming email server being used, or is the email
        being redirected/forwarded through a custom email server or
        provider?
    -   Is there an example of an email that has been correctly
        forwarded?
    -   Have you changed any email-related settings recently? Did it
        stop working after those changes?

3.  An answer to the following questions:

    -   Is it a generic issue or is it specific to a use case? If
        specific to a use case, which one?
    -   Is it working as expected? In case the email is sent using Odoo,
        the bounce email should reach the Odoo database and display the
        `red envelope <email-issues-outgoing-delivery-failure>`{.interpreted-text
        role="ref"}.
