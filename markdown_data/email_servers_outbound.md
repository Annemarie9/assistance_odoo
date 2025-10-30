# File: /content/odoo_doc17.0/fr/content/applications/general/email_communication/email_servers_outbound.md

Manage outbound messages
========================

Sending emails with Odoo\'s default configuration {#email-outbound-default}
-------------------------------------------------

On **Odoo Online** and **Odoo.sh**, sending and receiving emails works
out of the box. No configuration is required.

When a database is created, the subdomain
[company-name.odoo.com]{.title-ref} is used to send and receive emails.
The deliverability is optimized for this subdomain as it uses Odoo's DNS
configuration.

::: {.example}
If the database subdomain is [company-name.odoo.com]{.title-ref} and all
mailing configurations are the default ones, all emails will be sent
from [notifications\@company-name.odoo.com]{.title-ref}.
:::

::: {#email-outbound-default-from-filtering}
This configuration is handled by the system parameter
[mail.default.from\_filter]{.title-ref}. In case where the sender\'s
domain do not match the value of this parameter, the notification
address is used instead. Multiple values can be defined in this system
parameter: comma-separated, domains or full email addresses are all
allowed. Once an `outgoing mail server is configured
<email-outbound-different-servers-personalized>`{.interpreted-text
role="ref"}, the system parameter is no longer considered and the value
used is the `FROM filtering
<email-outbound-different-servers-personalized-from-filtering>`{.interpreted-text
role="ref"} of the mail server.
:::



Emails are sent with [catchall\@company-name.odoo.com]{.title-ref} as
the *reply-to* address. In addition, delivery errors are sent to
[bounce\@company-name.odoo.com]{.title-ref}.

::: {.note}
::: {.title}
Note
:::

The catchall, bounce, and notification addresses do not work like other
aliases. They do not have the vocation to create records in a database.
Emails sent to an alias are automatically routed and will reply to an
existing and linked record or will create a new one in the database.
:::

Using a custom domain to send emails {#email-outbound-custom-domain}
------------------------------------

The database can be configured to use a custom domain, in which case all
default email addresses are built using the custom domain. If the custom
domain is [company-name.com]{.title-ref}, the sender address will be
[notifications\@company-name.com]{.title-ref}, the *reply-to* address
[catchall\@company-name.com]{.title-ref}, and the *bounce* address
[bounce\@company-name.com]{.title-ref}. The custom domain can be
utilized when sending emails either with Odoo's email servers or an
external one.

This section assumes ownership of a custom domain. If not, a custom
domain must be purchased from a domain registrar such as GoDaddy,
Namecheap, or any alternative provider.

### Using a custom domain with Odoo's email server {#email-outbound-custom-domain-odoo-server}

On **Odoo Online** or **Odoo.sh**, some configurations are mandatory in
the custom domain\'s DNS to ensure good deliverability.

::: {.warning}
::: {.title}
Warning
:::

Most of the configuration will be done on the domain provider's side,
and it might require some configuration on the mail server itself.
**Some technical knowledge is required.**
:::

The first step is to configure the
`SPF <email-domain-spf>`{.interpreted-text role="ref"} and
`DKIM <email-domain-dkim>`{.interpreted-text role="ref"} to be compliant
with Odoo's mail server.

Next, the custom domain must be set as the alias domain of a company.
Select the company, open the `Settings`{.interpreted-text
role="guilabel"}, and add the custom domain under the
`Alias Domain`{.interpreted-text role="guilabel"} field.

After adding the alias domain, click the
`oi-arrow-right`{.interpreted-text role="icon"}
(`internal link`{.interpreted-text role="guilabel"}) icon to assign more
companies to the custom domain if needed. Enable the
`developer-mode`{.interpreted-text role="ref"} mode to modify the
default aliases if desired:

-   `Bounce Alias`{.interpreted-text role="guilabel"}: the mailbox used
    to catch delivery errors and populate the `red
    envelope <email-issues-outgoing-delivery-failure>`{.interpreted-text
    role="ref"} on the corresponding message.
-   `Catchall Alias`{.interpreted-text role="guilabel"}: the default
    mailbox used to centralize all replies.
-   `Default From Alias`{.interpreted-text role="guilabel"}: the default
    sender address.

::: {.note}
::: {.title}
Note
:::

At the creation of the first alias domain, all companies will use it. If
you create a new company, the alias domain automatically set is the one
with the lowest priority (ad displayed on the alias domain list in
`developer-mode`{.interpreted-text role="ref"}).
:::

All email aliases (e.g., related to CRM or Helpdesk teams) must have
their corresponding mailbox in the custom domain mail server.



To receive emails in the Odoo database within the corresponding chatter
(CRM, invoices, sales orders, etc.), one of these three methods must be
used:

-   `Redirections/forwarding <email-inbound-custom-domain-redirections>`{.interpreted-text
    role="ref"},
-   `Incoming mail servers <email-inbound-custom-domain-incoming-server>`{.interpreted-text
    role="ref"},
-   `MX record <email-inbound-custom-domain-mx>`{.interpreted-text
    role="ref"} (requires advanced technical knowledge)

Using a custom domain implies that specific `local-parts
<email-outbound-custom-domain-smtp-server-local-part>`{.interpreted-text
role="ref"} might be used by Odoo to send emails.

### Sending emails with an external SMTP server {#email-outbound-custom-domain-smtp-server}

::: {.note}
::: {.title}
Note
:::

If utilizing your own outgoing mail server, it must be paired with your
own domain, as updating the DNS of an Odoo subdomain is not feasible.
:::

To add an external SMTP server in Odoo, open
`Settings`{.interpreted-text role="guilabel"}, and enable the `Use
Custom Email Servers`{.interpreted-text role="guilabel"} option found
under the `Discuss`{.interpreted-text role="guilabel"} section.

Still under the `Discuss`{.interpreted-text role="guilabel"} section,
click `Outgoing Email Servers`{.interpreted-text role="guilabel"}, then
[New]{.title-ref} to create an outgoing mail server record. Most fields
are the common parameters used to set up a connection to an SMTP server;
use the values provided by your email provider.

Once completed, click `Test Connection`{.interpreted-text
role="guilabel"}. Note that a successful test connection does not
confirm that the email will go out as some restriction might remain on
the provider side, thus, it is recommended to consult your provider's
documentation.

#### Local-part values {#email-outbound-custom-domain-smtp-server-local-part}

Below are presented the different local-part values that can be used by
Odoo to send emails. It might be required to whitelist them in your mail
server:

-   The Alias Domain Bounce Alias (default value =
    [bounce]{.title-ref}),
-   The Alias Domain Default From (default value =
    [notifications]{.title-ref}),
-   The default admin address [admin\@company-name.odoo.com]{.title-ref}
    or, if changed, the new value),
-   The default Odoobot address
    [odoobot\@company-name.odoo.com]{.title-ref} or, if changed, the new
    value),
-   The specific FROM defined on an email marketing campaign,
-   The specific FROM that can be defined in an email template.

::: {.seealso}
\- `google_oauth`{.interpreted-text role="doc"} -
`azure_oauth`{.interpreted-text role="doc"}
:::

Setting up different servers for transactional and mass emails {#email-outbound-different-servers}
--------------------------------------------------------------

### Personalized mail servers {#email-outbound-different-servers-personalized}

Transactional emails and mass mailings can be sent using separate email
servers in Odoo. Doing so means day-to-day emails, quotations, or
invoices sent to clients will be handled as *transactional emails*.
*Mass mailing emails*, including the sending of batches of invoices or
quotations, will be managed by the Marketing Automation or Email
Marketing application.

::: {.example}
You can use services like Gmail, Amazon SES, or Brevo for transactional
emails, and services like Mailgun, Sendgrid, or Mailjet for mass
mailings.
:::

First, activate the `developer-mode`{.interpreted-text role="ref"} and
go to `Settings --> Technical -->
Email: Outgoing Mail Servers`{.interpreted-text role="menuselection"}.
There, add two outgoing email server records, one for the transactional
emails server and one for the mass mailings server. Enter a lower
`Priority`{.interpreted-text role="guilabel"} value for the
transactional server (e.g., [1]{.title-ref}) over the mass mailings
server (e.g., [2]{.title-ref}) so transactional emails are given
priority.



Now, go to
`Email Marketing --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, enable `Dedicated Server`{.interpreted-text
role="guilabel"}, and select the appropriate email server. Odoo uses the
server with the lowest priority value for transactional emails, and the
server selected here for mass mailings.



#### FROM filtering {#email-outbound-different-servers-personalized-from-filtering}

::: {.important}
::: {.title}
Important
:::

It's **highly recommended** to configure the FROM Filtering on the
outgoing mail servers as per the instructions of your provider.
:::

The `FROM Filtering`{.interpreted-text role="guilabel"} field allows for
the use of a specific outgoing email server depending on the *From*
email address or domain that Odoo is sending on behalf of. The **value
must be a domain or a complete address** that matches the sender's email
address and is trusted on the outgoing mail server provider\'s side.

If FROM filtering is not used, emails will go out using the notification
address.

::: {.warning}
::: {.title}
Warning
:::

Some outgoing mail servers require a specific configuration of the FROM
filter.
:::

When an email is sent from Odoo, the following sequence is used to
choose the outgoing email server:

-   First, Odoo searches for a server that has the same FROM filtering
    value as the From value (i.e., email address) defined in the
    outgoing email. This configuration is ideal if all users of a
    company share the same domain but have different local-parts.

::: {.example}
If the sender\'s email address is [test\@example.com]{.title-ref}, only
an email server having a FROM filtering value equal to
[test\@example.com]{.title-ref} or [example.com]{.title-ref} can be
used.
:::

-   If no server is found based on the first criteria, Odoo looks for
    the first server without a FROM filtering value set. The email will
    be overridden with the notification address.
-   If no server is found based on the second criteria, Odoo uses the
    first server, and the email will be overridden with the notification
    address.

::: {.note}
::: {.title}
Note
:::

To determine which server is first, Odoo uses the priority value (the
lower the value is, the higher the priority is). Failing to do so, the
first server is determined by the servers\' names, using alphabetical
order.
:::

-   If there is no mail server, Odoo relies on the `system parameter
    <email-outbound-default-from-filtering>`{.interpreted-text
    role="ref"} value.

It is also possible to use Odoo\'s mail server for transactional emails
in addition to mass mailings.

### Using an external email server and Odoo's default server {#email-outbound-different-servers-external-odoo}

On Odoo Online and Odoo.sh, databases are started with Odoo\'s SMTP
server. If no outgoing mail server is set, the default Odoo\'s SMTP
server will be used.



::: {.example}
If an outgoing mail server is used simultaneously with Odoo's default
server (CLI), the FROM filter of the outgoing mail server must contain a
custom domain, and the FROM filter of the CLI must contain Odoo's
subdomain. If there is no FROM filtering, the email will go out using
the notification address.
:::



::: {.note}
::: {.title}
Note
:::

On Odoo Online, the command line interface is equivalent to the default
Odoo mail server, using the same limit as if there was no outgoing mail
server in place.
:::

::: {.tip}
::: {.title}
Tip
:::

On Odoo Online, the page also shows your daily email usage and your
daily limit. On Odoo.sh, you need to check on the monitor page the
number of outgoing emails that were sent.
:::

::: {.note}
::: {.title}
Note
:::

On Odoo.sh, to use the command-line interface, an outgoing mail server
can be configured on the configuration file.
:::

::: {.warning}
::: {.title}
Warning
:::

Odoo's mail server is meant for transactional emails and small-scale
marketing campaigns. The
`daily limit <email-issues-outgoing-delivery-failure-messages-limit>`{.interpreted-text
role="ref"} depends on the database type and the applications used.
:::

Using a custom domain with an external email server {#email-outbound-custom-domain-external-server}
---------------------------------------------------

Similar to the
`previous chapter <email-outbound-different-servers-external-odoo>`{.interpreted-text
role="ref"}, proper configuration might be needed to ensure that the
external email server is allowed to send emails using your custom
domain. Refer to your provider's documentation to properly set up the
relevant records (SPF, DKIM, and DMARC). A list of the
`most common providers is available
<email-domain-providers-documentation>`{.interpreted-text role="ref"}.

::: {.note}
::: {.title}
Note
:::

DNS configuration is required when you use your own domain. If an
external outgoing mail server is used, configuring the records as
described in the `Odoo DNS configuration for our mail
servers documentation <email_domain>`{.interpreted-text role="doc"}
**will not have the desired effect**, as it is independent of Odoo when
using a custom email server. Odoo does not allow the configuration of
Odoo\'s subdomain.
:::

Port restriction {#email-outbound-port-restriction}
----------------

Port 25 is blocked for security reasons on Odoo Online and Odoo.sh. Try
using port 465, 587, or 2525 instead.

Alias domain {#email-outbound-alias-domain}
------------

The catchall domain is company-specific. By default, all companies share
Odoo's subdomain (e.g., [company-name.odoo.com]{.title-ref}), but each
company may have its own custom email domain.

When the `developer-mode`{.interpreted-text role="ref"} is activated,
the alias domain options are available by going to
`Settings --> Technical --> Email: Alias Domains`{.interpreted-text
role="menuselection"}.

::: {.warning}
::: {.title}
Warning
:::

Any modification of the alias domain must be done very carefully. If one
of the aliases (bounce, catchall, default from) is changed, all previous
emails that are not properly redirected to the new aliases will be lost.
:::

The `Default From Alias`{.interpreted-text role="guilabel"} field can be
filled with a local-part of the email address (by default
[notifications]{.title-ref}) or a full email address. Configure it to
determine the [FROM]{.title-ref} header of your emails. If a full email
address is used, all outgoing emails will be overwritten with this
address.

Notification system {#email-outbound-notifications}
-------------------

When an email is sent from the chatter, customers can reply directly to
it. If a customer replies directly to an email, the answer is logged in
the same chatter, thus functioning as a message thread related to the
record.

Upon receiving the reply, Odoo then uses the subscribed followers (based
on the subscribed subtypes) to send them a notification by email, or in
the Odoo inbox, depending on the user's preferences.

::: {.example}
If a customer with the email address ["Mary"
\<mary\@customer.example.com\>]{.title-ref} makes a direct reply to an
email coming from the Odoo database, Odoo\'s default behavior is to
redistribute the email\'s content to all other followers within the
thread.

As Mary's domain does not belong to the alias domain, Odoo overrides the
email address and uses the notification email address to notify the
followers. This override depends on the configuration done in the
database. By default, on Odoo Online and Odoo.sh, the email
[FROM]{.title-ref} address will be overridden with the value
[notifications\@company-name.odoo.com]{.title-ref} instead of
[mary\@customer.example.com]{.title-ref}.

The address is constructed using the name of the sender and [{alias
domain, default from alias}]{.title-ref}@\`{alias domain, domain name}[,
by default, \`notifications\@company-name.odoo.com]{.title-ref}.
:::

Using a unique email address for all outgoing emails {#email-outbound-unique-address}
----------------------------------------------------

To force the email address from which emails are sent, activate the
`developer-mode`{.interpreted-text role="ref"}, and go to
`Settings --> Technical --> Email: Alias Domains`{.interpreted-text
role="menuselection"}. On the `Default From
Alias`{.interpreted-text role="guilabel"}, use the local-part or a
complete email address as the value.

::: {.warning}
::: {.title}
Warning
:::

If a **complete address** is used as the
`Default From Alias`{.interpreted-text role="guilabel"} value, **all**
outgoing emails will be overwritten by this address.
:::
