# File: /content/odoo_doc17.0/fr/content/applications/general/email_communication/mailjet_api.md

Mailjet API
===========

Odoo is compatible with Mailjet\'s
`API (Application Programming Interface)`{.interpreted-text role="abbr"}
for mass mailing. Set up a dedicated mass mailing server through Mailjet
by configuring settings in the Mailjet account and the Odoo database. In
some circumstances, settings need to be configured on the custom
domain\'s `DNS (Domain Name System)`{.interpreted-text role="abbr"}
settings as well.

Set up in Mailjet
-----------------

### Create API credentials

To get started, sign in to the [Mailjet Account
Information](https://app.mailjet.com/account) page. Next, navigate to
the `Senders & Domains`{.interpreted-text role="guilabel"} section and
click on `SMTP and
SEND API Settings`{.interpreted-text role="guilabel"}.



Then, copy the `SMTP (Simple Mail Transfer Protocol)`{.interpreted-text
role="abbr"} configuration settings onto a notepad. They can be found
under the `Configuration (SMTP only)`{.interpreted-text role="guilabel"}
section. The `SMTP (Simple
Mail Transfer Protocol)`{.interpreted-text role="abbr"} configuration
settings include the server address, the security option needed (Use
`SSL (Secure Sockets Layer)`{.interpreted-text
role="abbr"}/`TLS (Transport Layer Security)`{.interpreted-text
role="abbr"}), and the port number. The settings are needed to configure
Mailjet in Odoo, which is covered in the
`last section <maintain/mailjet-api/odoo-setup>`{.interpreted-text
role="ref"}.

::: {.seealso}
[Mailjet: How can I configure my SMTP
parameters?](https://documentation.mailjet.com/hc/articles/360043229473)
:::

::: {.important}
::: {.title}
Important
:::

Odoo
`blocks port 25 <email-outbound-port-restriction>`{.interpreted-text
role="ref"} on Odoo Online and Odoo.sh databases.
:::



Next, click on the button labeled
`Retrieve your API credentials`{.interpreted-text role="guilabel"} to
retrieve the Mailjet API credentials.

Then, click on the eye icon to reveal the `API key`{.interpreted-text
role="guilabel"}. Copy this key to a notepad, as this serves as the
`Username`{.interpreted-text role="guilabel"} in the Odoo configuration.
Next, click on the `Generate Secret Key`{.interpreted-text
role="guilabel"} button to generate the `Secret Key`{.interpreted-text
role="guilabel"}. Copy this key to a notepad, as this serves as the
`Password`{.interpreted-text role="guilabel"} in the Odoo configuration.

### Add verified sender address(es)

The next step is to add a sender address or a domain to the Mailjet
account settings so that the email address or domain is approved to send
emails using Mailjet\'s servers. First, navigate to the [Mailjet Account
Information](https://app.mailjet.com/account) page. Next, click on the
`Add a Sender Domain or Address`{.interpreted-text role="guilabel"} link
under the `Senders & Domains`{.interpreted-text role="guilabel"}
section.



Determine if a sender\'s email address or the entire domain needs to be
added to the Mailjet settings. It may be easier to configure the domain
as a whole if `DNS (Domain Name System)`{.interpreted-text role="abbr"}
access is available. Jump to the
`Add a domain <maintain/mailjet-api/add-domain>`{.interpreted-text
role="ref"} section for steps on adding the domain.

::: {.note}
::: {.title}
Note
:::

Either all email addresses of the Odoo database users who are sending
emails using Mailjet\'s servers need to be configured or the domain(s)
of the users\' email addresses can be configured.
:::

By default, the email address originally set up in the Mailjet account
is added as a trusted sender. To add another email address, click on the
button labeled `Add a sender address`{.interpreted-text
role="guilabel"}. Then, add the email address that is configured to send
from the custom domain.

At minimum the following email addresses should be set up in the
provider and verified in Mailjet:

-   notifications\@yourdomain.com
-   bounce\@yourdomain.com
-   catchall\@yourdomain.com

::: {.note}
::: {.title}
Note
:::

Replace [yourdomain]{.title-ref} with the custom domain for the Odoo
database. If there isn\'t one, then use the
`mail.catchall.domain`{.interpreted-text role="guilabel"} system
parameter.
:::

After that, fill out the `Email Information`{.interpreted-text
role="guilabel"} form, making sure to select the appropriate email type:
transactional email or mass emails. After completing the form, an
activation email is sent to the email address and the trusted sender can
be activated.

It is recommended to set up the
`SPF (Sender Policy Framework)`{.interpreted-text
role="abbr"}/`DKIM (DomainKeys
Identified Mail)`{.interpreted-text
role="abbr"}/`DMARC (Domain-based Message Authentication, Reporting, and
Conformance)`{.interpreted-text role="abbr"} settings on the domain of
the sender.

::: {.seealso}
\- [Mailjet\'s SPF/DKIM
documentation](https://documentation.mailjet.com/hc/en-us/articles/360049641733-Authenticating-Domains-with-SPF-and-DKIM-A-Complete-Guide)
- [Mailjet\'s DMARC
documentation](https://documentation.mailjet.com/hc/en-us/articles/20531905163419-Understanding-DMARC)
:::

::: {.important}
::: {.title}
Important
:::

If the database is not using a custom domain, then in order to verify
the sender\'s address, a temporary alias (of the three email addresses
mentioned above) should be set up in Odoo CRM to create a lead. Then,
the database is able to receive the verification email and verify the
accounts.
:::

### Add a domain {#maintain/mailjet-api/add-domain}

By adding an entire domain to the Mailjet account, all the sender
addresses related to that domain are automatically validated for sending
emails using Mailjet servers. First, navigate to the [Mailjet Account
Information](https://app.mailjet.com/account) page. Next, click on
`Add a Sender Domain or Address`{.interpreted-text role="guilabel"} link
under the `Senders & Domains`{.interpreted-text role="guilabel"}
section. Then, click on `Add domain`{.interpreted-text role="guilabel"}
to add the custom domain.

::: {.note}
::: {.title}
Note
:::

The domain needs to be added to the Mailjet account and then validated
through the `DNS
(Domain Name System)`{.interpreted-text role="abbr"}.
:::

After that, fill out the `Add a new Domain`{.interpreted-text
role="guilabel"} page on Mailjet and click `Continue`{.interpreted-text
role="guilabel"}.

After adding the domain, a validation page will populate. Unless the
Odoo database is on-premise (in which case, choose
`Option 1`{.interpreted-text role="guilabel"}), choose
`Option 2: Create a DNS Record`{.interpreted-text role="guilabel"}. Copy
the TXT record information to a notepad and then navigate to the
domain\'s `DNS (Domain
Name System)`{.interpreted-text role="abbr"} provider to complete
validation.



#### Setup in the domain\'s DNS

After getting the TXT record information from the Mailjet account, add a
TXT record to the domain\'s `DNS (Domain Name System)`{.interpreted-text
role="abbr"}. This process varies depending on the `DNS (Domain Name
System)`{.interpreted-text role="abbr"} provider. Consult the provider
for specific configuration processes. The TXT record information
consists of the `Host`{.interpreted-text role="guilabel"} and
`Value`{.interpreted-text role="guilabel"}. Paste these into the
corresponding fields in the TXT record.

#### Return to Mailjet account information

After adding the TXT record to the domain\'s
`DNS (Domain Name System)`{.interpreted-text role="abbr"}, navigate back
to the Mailjet account. Then, navigate to
`Account Information --> Add a Sender Domain or
Address`{.interpreted-text role="menuselection"}, click the gear icon
next to `Domain`{.interpreted-text role="guilabel"}, and select
`Validate`{.interpreted-text role="guilabel"}.

This action can also be done by going to the [Sender domains & addresses
\<https://app.mailjet.com/ account/sender\>]() page on the Mailjet
account information and clicking on `Manage`{.interpreted-text
role="guilabel"}.

Next, click `Check Now`{.interpreted-text role="guilabel"} to validate
the TXT record that was added on the domain. A success screen will
appear if the domain is configured correctly.



After successfully setting up the domain, there is an option to
`Authenticate this domain
(SPF/DKIM)`{.interpreted-text role="guilabel"}. This button populates
`SPF (Sender Policy Framework)`{.interpreted-text role="abbr"} &
`` DKIM (DomainKeys
Identified Mail) records to input into the :abbr:`DNS (Domain Name System) ``{.interpreted-text
role="abbr"} provider.

::: {.seealso}
[Mailjet\'s SPF/DKIM/DMARC documentation
\<https://documentation.mailjet.com/hc/articles/
360042412734-Authenticating-Domains-with-SPF-DKIM\>]()
:::



Set up in Odoo {#maintain/mailjet-api/odoo-setup}
--------------

To complete the setup, navigate to the Odoo database and go to the
`Settings`{.interpreted-text role="guilabel"}. With
`developer-mode`{.interpreted-text role="ref"} turned on, go to the
`Technical Menu --> Email --> Outgoing
Mail Servers`{.interpreted-text role="menuselection"}. Then, create a
new outgoing server configuration by clicking on the
`Create`{.interpreted-text role="guilabel"} button.

Next, input the [SMTP server]{.title-ref} (in-v3.mailjet.com), [port
number]{.title-ref} (587 or 465), and [Security (SSL/TLS)]{.title-ref}
that was copied earlier from the Mailjet account. They can also be found
. It is recommended to use
`SSL (Secure Sockets
Layer)`{.interpreted-text
role="abbr"}/`TLS (Transport Layer Security)`{.interpreted-text
role="abbr"} even though Mailjet may not require it.

For the `Username`{.interpreted-text role="guilabel"}, input the
`API KEY`{.interpreted-text role="guilabel"}. For the
`Password`{.interpreted-text role="guilabel"}, input the
`SECRET KEY`{.interpreted-text role="guilabel"} that was copied from the
Mailjet account to the notepad earlier. These settings can be found on
`Mailjet -->  Account Settings --> SMTP and SEND API
Settings`{.interpreted-text role="menuselection"}.

Then, if the Mailjet server is used for mass emailing, set the
`Priority`{.interpreted-text role="guilabel"} value higher than that of
any transactional email server(s). Finally, save the settings and
`Test the
Connection`{.interpreted-text role="guilabel"}.


