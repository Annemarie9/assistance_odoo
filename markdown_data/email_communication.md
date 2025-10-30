# File: /content/odoo_doc17.0/fr/content/applications/general/email_communication.md

show-content

:   

Communication in Odoo by email
==============================

Communication in Odoo related to records such as CRM opportunities,
sales orders, invoices, \... have a discussion thread called
**chatter**, often displayed on the right side of the record.

On the chatter, you can send direct emails or Odoo notifications to the
followers of a document (depending on their notification preferences),
log internal notes, send WhatsApp messages or SMSes, and schedule
activities.

If a follower replies to a message, the reply updates the chatter, and
Odoo relays it to the followers as a notification. All emails - outgoing
and incoming - appear in the same chatter.

Odoo Online and Odoo.sh users {#email-online-sh}
-----------------------------

On Odoo Online and Odoo.sh, outgoing and incoming emails work out of the
box, **nothing needs to be done**. Everything is already configured on
your subdomain.

By default, outgoing emails use the following
`notification email address
<email-outbound-notifications>`{.interpreted-text role="ref"}
[notifications\@company-name.odoo.com]{.title-ref}.

### Using another domain {#email-online-sh-domain}

If you prefer not to have outgoing emails sent from Odoo\'s subdomain
[\@company-name.odoo.com]{.title-ref} but instead
`from your own domain <email-outbound-custom-domain>`{.interpreted-text
role="ref"}, **additional configuration will be necessary** on the
domain and within Odoo. This introduces an extra layer of complexity and
necessitates technical knowledge (mainly regarding DNS and mail
protocols).

By adding a domain and configuring the administration access rights, you
can also access the
`new domain alias <email-outbound-alias-domain>`{.interpreted-text
role="ref"} page to configure the alias of your companies. If only one
domain is configured, this domain will be shared by all companies on the
database.

If you want to keep using Odoo\'s mail server, you will have to
`configure the SPF and DKIM
<email-domain-spf>`{.interpreted-text role="ref"}.

If
`you want to use your own mail server <email-outbound-custom-domain-smtp-server>`{.interpreted-text
role="ref"}, you will have to follow the mail server provider\'s
specific documentation.

For incoming emails, after adding your own domain,
`replies from customers will come back to
your domain <email-inbound-custom-domain>`{.interpreted-text
role="ref"}, and you will need to use one of the three possible ways to
get the emails back into Odoo (using either `incoming mail server
<email-inbound-custom-domain-incoming-server>`{.interpreted-text
role="ref"}, `redirection/forwarding
<email-inbound-custom-domain-redirections>`{.interpreted-text
role="ref"} or `DNS MX record
<email-inbound-custom-domain-mx>`{.interpreted-text role="ref"}).
Everything is covered in the `Manage inbound messages
documentation <email_communication/email_servers_inbound>`{.interpreted-text
role="doc"}.

On-premise users {#email-on-premise}
----------------

If you are on-premise, you will have to completely configure your
outgoing and incoming emails:

-   For outgoing emails, you will need
    `to use an SMTP server and a custom domain
    <email-outbound-custom-domain-odoo-server>`{.interpreted-text
    role="ref"}.
-   For incoming emails, set the frequency at which you fetch new emails
    low enough for responsiveness but high enough in order not to stress
    your system or provider. Due to this reason and the simplicity of
    this configuration, we usually advise on using incoming mail
    servers. To use an SMTP server, check out the
    `"Use a custom domain for inbound messages" documentation
    <email-inbound-custom-domain>`{.interpreted-text role="ref"}.

Using a third-party provider\'s mail server {#email-third-party-server}
-------------------------------------------

Odoo\'s documentation also covers several popular mail servers. As they
require specific authorizations and configuration, they add a layer of
complexity. For this reason, using Odoo\'s outgoing mail server is
recommended.

-   `Outlook documentation <email_communication/azure_oauth>`{.interpreted-text
    role="doc"}
-   `Gmail documentation <email_communication/google_oauth>`{.interpreted-text
    role="doc"}
-   `Mailjet documentation <email_communication/mailjet_api>`{.interpreted-text
    role="doc"}

::: {.note}
::: {.title}
Note
:::

Every provider has its own limitations. Research the desired provider
*before* configuring it. For example, Outlook and Gmail might not be
suitable for large marketing campaigns.
:::

::: {.seealso}
\- `Activities <../essentials/activities>`{.interpreted-text role="doc"}
- `Discuss app <../productivity/discuss>`{.interpreted-text role="doc"}
- `Digest emails <companies/digest_emails>`{.interpreted-text
role="doc"} -
`Email Marketing app <../marketing/email_marketing>`{.interpreted-text
role="doc"} -
`Email templates <companies/email_template>`{.interpreted-text
role="doc"} -
`Expense creation using an email alias <expenses/email_expense>`{.interpreted-text
role="ref"} -
`Helpdesk ticket creation using an email alias <helpdesk/receiving_tickets/email-alias>`{.interpreted-text
role="ref"} -
`Lead creation using an email alias <crm/configure_email_alias>`{.interpreted-text
role="ref"} -
`Project task creation using an email alias <task_creation/email_alias>`{.interpreted-text
role="ref"} - `Technical mail gateway for on-premise users
<../../administration/on_premise/email_gateway>`{.interpreted-text
role="doc"} -
`Technical start of Odoo database with an outgoing mail server configured from the
command-line interface <reference/cmdline/server/emails>`{.interpreted-text
role="ref"}
:::

::: {.toctree titlesonly=""}
email\_communication/email\_servers\_inbound
email\_communication/email\_servers\_outbound
email\_communication/email\_domain email\_communication/azure\_oauth
email\_communication/google\_oauth email\_communication/mailjet\_api
email\_communication/faq
:::
