# File: /content/odoo_doc17.0/fr/content/applications/websites/website/configuration/domain_names.md

Domain names
============

Domain names are text-based addresses identifying online locations, such
as websites. They provide a more memorable and recognizable way for
people to navigate the internet than numerical IP addresses.

**Odoo Online** and **Odoo.sh** databases use a **subdomain** of the
[odoo.com]{.title-ref} **domain** by default (e.g.,
[mycompany.odoo.com]{.title-ref}).

However, you can use a custom domain name instead by
`registering a free domain name
<domain-name/register>`{.interpreted-text role="ref"} (only available
for Odoo Online databases) or by `configuring a
domain name you already own <domain-name/existing>`{.interpreted-text
role="ref"}.

::: {.seealso}
[Odoo Tutorials: Register a free domain name
\
:::

Register a free domain name with Odoo {#domain-name/register}
-------------------------------------

To register a one-year free domain name for your Odoo Online database,
sign in to your account and go to the [database
manager](https://www.odoo.com/my/databases). Click the
`fa-gear`{.interpreted-text role="icon"} (`gear`{.interpreted-text
role="guilabel"}) button next to the database name and select
`fa-globe`{.interpreted-text role="icon"} `Domain
Names`{.interpreted-text role="guilabel"}.



Search for the desired domain name and check its availability.



::: {.tip}
::: {.title}
Tip
:::

Ensure the Website app is installed if the domain name registration
option does not appear.
:::

Select the desired domain name, fill in the
`Domain Owner`{.interpreted-text role="guilabel"} form, and click
`Register`{.interpreted-text role="guilabel"}. The chosen domain name is
directly linked to the database.



Next, you should
`map your domain name to your Odoo website <domain-name/website-map>`{.interpreted-text
role="ref"}.

::: {.important}
::: {.title}
Important
:::

A verification email from
[noreply\@domainnameverification.net]{.title-ref} will be sent to the
email address provided in the `Domain Owner`{.interpreted-text
role="guilabel"} form. It is essential to verify your email address to
keep the domain active and receive the renewal quote before expiration.
:::

The domain name registration is free for the first year. After this
period, Odoo will continue to manage the domain in partnership with
**Gandi.net**, the domain name registrar, and you will be charged
. Odoo sends
a renewal quotation every year to the email address mentioned in the
`Domain Owner`{.interpreted-text role="guilabel"} form several weeks
before the expiration date of the domain. The domain is renewed
automatically when the quotation is confirmed.

::: {.note}
::: {.title}
Note
:::

\- The offer is only available for **Odoo Online** databases. - The
offer is limited to **one** domain name per client. - The offer is
limited to the registration of a **new** domain name. - The offer is
available to *One App Free* plans. Ensure that your website contains
enough original content for Odoo to verify that your request is
legitimate and respects [Odoo\'s Acceptable Use
Policy](https://www.odoo.com/acceptable-use). Given the high number of
requests, it can take Odoo several days to review them.
:::

### DNS records {#domain-name/register-dns}

To manage your free domain name
`DNS (domain name system)`{.interpreted-text role="abbr"} records, open
the , click the
`fa-gear`{.interpreted-text role="icon"} (`gear`{.interpreted-text
role="guilabel"}) button next to the database name, select
`fa-globe`{.interpreted-text role="icon"}
`Domain Names`{.interpreted-text role="guilabel"}, and click
`DNS`{.interpreted-text role="guilabel"}.

-   `A`{.interpreted-text role="guilabel"}: the A record holds the IP
    address of the domain. It is automatically created and **cannot** be
    edited or deleted.
-   `CNAME`{.interpreted-text role="guilabel"}: CNAME records forward
    one domain or subdomain to another domain. One is automatically
    created to map the [www.]{.title-ref} subdomain to the database. If
    the database is renamed, the CNAME record **must** also be renamed.
-   `MX`{.interpreted-text role="guilabel"}: MX records instruct servers
    on where to deliver emails.
-   `TXT`{.interpreted-text role="guilabel"}: TXT records can be used
    for different purposes (e.g., to verify domain name ownership).

Any modification to the DNS records can take up to **72 hours** to
propagate worldwide on all servers.

::: {.note}
::: {.title}
Note
:::

 if you need assistance
to manage your domain name.
:::

### Mailbox

The one-year free domain name offer does **not** include a mailbox.
There are two options to link your domain name with a mailbox.

#### Use a subdomain

You can create a subdomain (e.g.,
[subdomain.yourdomain.com]{.title-ref}) to use as an alias domain for
the database. It allows users to create records in the database from
emails received on their [email\@subdomain.yourdomain.com]{.title-ref}
alias.

To do so, open the [database
manager](https://www.odoo.com/my/databases), click the
`fa-gear`{.interpreted-text role="icon"} (`gear`{.interpreted-text
role="guilabel"}) button next to the database name and select
`fa-globe`{.interpreted-text role="icon"}
`Domain Names`{.interpreted-text role="guilabel"}. Click
`DNS`{.interpreted-text role="guilabel"}, then
`Add DNS record`{.interpreted-text role="guilabel"} and select
`CNAME`{.interpreted-text role="guilabel"}. Next, enter the desired
subdomain in the `Name`{.interpreted-text role="guilabel"} field (e.g.,
[subdomain]{.title-ref}), the original database domain with a period at
the end (e.g., [mycompany.odoo.com.]{.title-ref}) in the
`Content`{.interpreted-text role="guilabel"} field, and click
`Add record`{.interpreted-text role="guilabel"}.

Then, add the alias domain as your *own domain* by clicking
`Use my own domain`{.interpreted-text role="guilabel"}, entering the
alias domain (e.g., [subdomain.yourdomain.com]{.title-ref}), clicking
`Verify`{.interpreted-text role="guilabel"}, and then
`I confirm, it's done`{.interpreted-text role="guilabel"}.

Finally, go to your database and open the `Settings`{.interpreted-text
role="guilabel"}. Under the `Alias Domain`{.interpreted-text
role="guilabel"} field, enter the alias domain (e.g.,
[subdomain.yourdomain.com]{.title-ref}), click
`Create`{.interpreted-text role="guilabel"}, and then
`Save`{.interpreted-text role="guilabel"}.

#### Use an external email provider

To use an external email provider, you should configure an MX record. To
do so, open the ,
click the `fa-gear`{.interpreted-text role="icon"}
(`gear`{.interpreted-text role="guilabel"}) button next to the database
name and select `fa-globe`{.interpreted-text role="icon"}
`Domain Names`{.interpreted-text role="guilabel"}. Click
`DNS`{.interpreted-text role="guilabel"}, then
`Add DNS record`{.interpreted-text role="guilabel"} and select
`MX`{.interpreted-text role="guilabel"}. The values you should enter for
the `Name`{.interpreted-text role="guilabel"},
`Content`{.interpreted-text role="guilabel"}, and
`Priority`{.interpreted-text role="guilabel"} fields depend on the
external email provider.

::: {.seealso}
\- [Google Workspace: MX record
values](https://support.google.com/a/answer/174125?hl=en) - [Outlook and
Exchange Online: Add an MX record for
email](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider?view=o365-worldwide#add-an-mx-record-for-email-outlook-exchange-online)
:::

##### Google Workspace

To use your free domain name on Gmail, register to [Google
Workspace](https://workspace.google.com).

During the registration process, select
`Set up using your existing domain`{.interpreted-text role="guilabel"}
when asked to `Choose a way to set up your account`{.interpreted-text
role="guilabel"}, and enter your domain (e.g.,
[yourdomain.com]{.title-ref}) when asked
`What's your business's domain name?`{.interpreted-text
role="guilabel"}.

###### Domain ownership verification

1.  Sign in to Google Workspace. When asked to verify you own your
    domain, click `Switch to
    manual verification`{.interpreted-text role="guilabel"}.

    

2.  Select [gandi.net]{.title-ref} as the
    `Domain host`{.interpreted-text role="guilabel"} and click
    `Continue`{.interpreted-text role="guilabel"}.

    

3.  Copy the content of the `Value`{.interpreted-text role="guilabel"}
    field under `TXT record`{.interpreted-text role="guilabel"}. Leave
    the window open.

    

4.  Open the ,
    click the `fa-gear`{.interpreted-text role="icon"}
    (`gear`{.interpreted-text role="guilabel"}) button next to the
    database name and select `fa-globe`{.interpreted-text role="icon"}
    `Domain
    Names`{.interpreted-text role="guilabel"}. Click
    `DNS`{.interpreted-text role="guilabel"}, then
    `Add DNS record`{.interpreted-text role="guilabel"} and select
    `TXT`{.interpreted-text role="guilabel"}.

5.  Enter [@]{.title-ref} in the `Name`{.interpreted-text
    role="guilabel"} field, paste the `Value`{.interpreted-text
    role="guilabel"} provided by Google in the
    `Content`{.interpreted-text role="guilabel"} field, and click
    `Add record`{.interpreted-text role="guilabel"}.

    

6.  Go back to Google Workspace, tick the box at the bottom, and click
    `Confirm`{.interpreted-text role="guilabel"}.

::: {.seealso}
[Google Workspace Admin Help: Verify your domain with a TXT
record](https://support.google.com/a/answer/16018515)
:::

###### Redirect emails to Gmail

1.  Open the ,
    click the `fa-gear`{.interpreted-text role="icon"}
    (`gear`{.interpreted-text role="guilabel"}) button next to the
    database name and select `fa-globe`{.interpreted-text role="icon"}
    `Domain
    Names`{.interpreted-text role="guilabel"}. Click
    `DNS`{.interpreted-text role="guilabel"}, then
    `Add DNS record`{.interpreted-text role="guilabel"}, and select
    `MX`{.interpreted-text role="guilabel"}.

2.  Enter [@]{.title-ref} in the `Name`{.interpreted-text
    role="guilabel"} field, [1]{.title-ref} in the
    `Priority`{.interpreted-text role="guilabel"} field,
    [smtp.google.com.]{.title-ref} in the `Content`{.interpreted-text
    role="guilabel"} field, and click `Add record`{.interpreted-text
    role="guilabel"}.

    

3.  Open the [Google Workspace Admin
    console](https://admin.google.com/ac/domains/manage), click
    `Activate Gmail`{.interpreted-text role="guilabel"} for your domain,
    and follow the steps.

::: {.seealso}
[Google Workspace Admin Help: Set up MX records for Google
Workspace](https://support.google.com/a/answer/16004259)
:::

Configure an existing domain name {#domain-name/existing}
---------------------------------

If you already have a domain name, you can use it for your Odoo website.

::: {.warning}
::: {.title}
Warning
:::

It is strongly recommended to follow **in order** these three steps to
avoid any `SSL
certificate validation <domain-name/ssl>`{.interpreted-text role="ref"}
issues:

1.  `Add a CNAME record <domain-name/cname>`{.interpreted-text
    role="ref"}
2.  `Redirect your naked domain name <domain-name/naked>`{.interpreted-text
    role="ref"} (optional, but recommended)
3.  `Map your domain name to your Odoo database <domain-name/db-map>`{.interpreted-text
    role="ref"}
4.  `Map your domain name to your Odoo website <domain-name/website-map>`{.interpreted-text
    role="ref"}
:::

### Add a CNAME record {#domain-name/cname}

Adding a CNAME record to forward your domain name to the address of your
Odoo database is required.

::: {.tabs}
::: {.group-tab}
Odoo Online

The CNAME record\'s target address should be your database\'s address as
defined at its creation (e.g., [mycompany.odoo.com]{.title-ref}).
:::

::: {.group-tab}
Odoo.sh

The CNAME record\'s target address should be the project\'s main
address, which can be found on Odoo.sh by going to
`Settings --> Project Name`{.interpreted-text role="menuselection"}, or
a specific branch (production, staging or development) by going to
`Branches --> select the
branch --> Settings --> Custom domains`{.interpreted-text
role="menuselection"}, and clicking
`How to set up my domain?`{.interpreted-text role="guilabel"}. A message
indicates which address your CNAME record should target.
:::
:::

The specific instructions depend on your DNS hosting service.

::: {.seealso}
\- [GoDaddy: Add a CNAME
record](https://www.godaddy.com/help/add-a-cname-record-19236) -
[Namecheap: How to create a CNAME record for your
domain](https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain)
- [OVHcloud: Add a new DNS
record](https://docs.ovh.com/us/en/domains/web_hosting_how_to_edit_my_dns_zone/#add-a-new-dns-record)
- [Cloudflare: Manage DNS
records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/)
:::

### Redirect a naked domain {#domain-name/naked}

::: {.note}
::: {.title}
Note
:::

Although optional, completing this step is advised.
:::

To let visitors use your naked domain name
`(a domain name without any subdomains or prefixes)`{.interpreted-text
role="dfn"} ([yourdomain.com]{.title-ref}), creating a 301 redirect
`(a permanent redirect from one URL to another)`{.interpreted-text
role="dfn"} to [www.yourdomain.com]{.title-ref} is required:

-   from [http://yourdomain.com]{.title-ref} to
    [https://www.yourdomain.com]{.title-ref}, and
-   from [https://yourdomain.com]{.title-ref} to
    [https://www.yourdomain.com]{.title-ref}.

The specific instructions depend on your DNS hosting service. However,
not all of them offer to redirect a naked domain with a secure HTTPS
connection. If you encounter any issue, we recommend
`using Cloudflare <domain-name/naked/cloudflare>`{.interpreted-text
role="ref"}.

#### Using Cloudflare to secure and redirect a naked domain {#domain-name/naked/cloudflare}

1.  [Sign up and log in to
    Cloudflare](https://dash.cloudflare.com/sign-up).

2.  Enter your domain name on [Cloudflare\'s
    dashboard](https://dash.cloudflare.com/login) and select
    `Quick scan for DNS records`{.interpreted-text role="guilabel"}.

3.  Choose a plan (the free plan is sufficient).

4.  Follow Cloudflare\'s instructions and recommendations to complete
    the activation.

5.  Add a CNAME record to redirect your naked domain
    ([yourdomain.com]{.title-ref}) to the [www]{.title-ref} subdomain
    (e.g., [www.yourdomain.com]{.title-ref}) by clicking
    `DNS`{.interpreted-text role="guilabel"} in the navigation menu,
    then clicking the `Add record`{.interpreted-text role="guilabel"}
    button, and using the following configuration:

    -   `Type`{.interpreted-text role="guilabel"}: CNAME
    -   `Name`{.interpreted-text role="guilabel"}: [@]{.title-ref} (or
        [yourdomain.com]{.title-ref})
    -   `Target`{.interpreted-text role="guilabel"}: e.g.,
        [www.yourdomain.com]{.title-ref}
    -   `Proxy status`{.interpreted-text role="guilabel"}: Proxied

    

6.  Add another second CNAME record to redirect the [www]{.title-ref}
    subdomain (e.g., [www.yourdomain.com]{.title-ref}) to your database
    address (e.g., [mycompany.odoo.com]{.title-ref}) using the following
    configuration:

    -   `Type`{.interpreted-text role="guilabel"}: CNAME
    -   `Name`{.interpreted-text role="guilabel"}: e.g.,
        [www.yourdomain.com]{.title-ref}
    -   `Target`{.interpreted-text role="guilabel"}: e.g.,
        [mycompany.odoo.com]{.title-ref}
    -   `Proxy status`{.interpreted-text role="guilabel"}: DNS only

    

7.  Define a redirect rule to permanently redirect (301) your naked
    domain (e.g., [yourdomain.com]{.title-ref}) to both
    [http://]{.title-ref} and [https://]{.title-ref} by going to
    `Rules --> Create rule --> Products`{.interpreted-text
    role="menuselection"}, and clicking
    `Create a Rule`{.interpreted-text role="guilabel"} under
    `Redirect Rules`{.interpreted-text role="guilabel"}:

    -   Enter any `Rule name`{.interpreted-text role="guilabel"}.
    -   Under the `If incoming requests match...`{.interpreted-text
        role="guilabel"} section, select `Custom filter
        expression`{.interpreted-text role="guilabel"} and use the
        following configuration:
        -   `Field`{.interpreted-text role="guilabel"}: Hostname
        -   `Operator`{.interpreted-text role="guilabel"}: equals
        -   `Value`{.interpreted-text role="guilabel"}: e.g.,
            [yourdomain.com]{.title-ref}
    -   Under the `Then...`{.interpreted-text role="guilabel"} section,
        use the following configuration:
        -   `Type`{.interpreted-text role="guilabel"}: Dynamic
        -   `Expression`{.interpreted-text role="guilabel"}: e.g.,
            [concat(\"https://www.yourdomain.com\",
            http.request.uri.path)]{.title-ref}
        -   `Status code`{.interpreted-text role="guilabel"}: 301
        -   `Preserve query string`{.interpreted-text role="guilabel"}:
            enabled

    

8.  Go to `SSL/TLS`{.interpreted-text role="guilabel"} and set the
    encryption mode to `Full`{.interpreted-text role="guilabel"}.

    

### Map a domain name to an Odoo database {#domain-name/db-map}

::: {.warning}
::: {.title}
Warning
:::

Ensure you have
`added a CNAME record <domain-name/cname>`{.interpreted-text role="ref"}
to your domain name\'s DNS **before** mapping your domain name to your
Odoo database.

Failing to do so may prevent the validation of the
`SSL certificate <domain-name/ssl>`{.interpreted-text role="ref"} and
could result in a *certificate name mismatch* error. Web browsers often
display this as a warning, such as *\"Your connection is not private\"*.

If you encounter this error after mapping the domain name to your
database, wait up to five days, as the validation may still happen. If
not, you can ,
including screenshots of your CNAME records.
:::

::: {.tabs}
::: {.group-tab}
Odoo Online

Open the , click
the `fa-gear`{.interpreted-text role="icon"} (`gear`{.interpreted-text
role="guilabel"}) button next to the database name, select
`fa-globe`{.interpreted-text role="icon"} `Domain
Names`{.interpreted-text role="guilabel"}, and click
`Use my own domain`{.interpreted-text role="guilabel"}. Then, enter the
domain name (e.g., [www.yourdomain.com]{.title-ref}), click
`Verify`{.interpreted-text role="guilabel"} and
`I confirm, it's done`{.interpreted-text role="guilabel"}.


:::

::: {.group-tab}
Odoo.sh

On Odoo.sh, go to
`Branches --> select your branch --> Settings --> Custom
domains`{.interpreted-text role="menuselection"}, type the domain name
to add, then click `Add domain`{.interpreted-text role="guilabel"}.



::: {.seealso}
`Odoo.sh branches: settings tab <odoosh-gettingstarted-branches-tabs-settings>`{.interpreted-text
role="ref"}
:::
:::
:::

#### SSL encryption (HTTPS protocol) {#domain-name/ssl}

**SSL encryption** allows visitors to navigate a website through a
secure connection, which appears as the *https://* protocol at the
beginning of a web address rather than the non-secure *http://*
protocol.

Odoo generates a separate SSL certificate for each domain
`mapped to a database
<domain-name/db-map>`{.interpreted-text role="ref"} using [Let\'s
Encrypt\'s certificate authority and ACME
protocol](https://letsencrypt.org/how-it-works/).

::: {.note}
::: {.title}
Note
:::

\- Certificate generation may take up to 24 hours. - Several attempts to
validate your certificate are made for five days after you map your
domain name to your database. - If you use another service, you can keep
using it or change to Odoo\'s.
:::

::: {.important}
::: {.title}
Important
:::

No SSL certificate is generated for naked domains
`(domain names without any subdomains
or prefixes)`{.interpreted-text role="dfn"}.
:::

#### Web base URL of a database {#domain-name/web-base-url}

::: {.note}
::: {.title}
Note
:::

If the Website app is installed on your database, skip this section and
continue from the
`Map a domain name to a website <domain-name/website-map>`{.interpreted-text
role="ref"} section.
:::

The *web base URL* or root URL of a database affects your main website
address and all the links sent to your customers (e.g., quotations,
portal links, etc.).

To make your custom domain name the *web base URL* of your database,
access your database using your custom domain name and log in as an
administrator `(a user part of the Settings access right
group under Administration)`{.interpreted-text role="dfn"}.

::: {.important}
::: {.title}
Important
:::

If you access your database with the original Odoo address (e.g.,
[mycompany.odoo.com]{.title-ref}), the *web base URL* of your database
will be updated accordingly. To prevent the automatic update of the *web
base URL* when an administrator logs in to the database, activate the
`developer mode
<developer-mode>`{.interpreted-text role="ref"}, go to
`Settings --> Technical --> System Parameters --> New`{.interpreted-text
role="menuselection"}, and enter [web.base.url.freeze]{.title-ref} as
the `Key`{.interpreted-text role="guilabel"} and [True]{.title-ref} as
the `Value`{.interpreted-text role="guilabel"}.
:::

::: {.note}
::: {.title}
Note
:::

You can also set the web base URL manually. To do so, activate the
`developer mode
<developer-mode>`{.interpreted-text role="ref"}, go to
`Settings --> Technical --> System Parameters`{.interpreted-text
role="menuselection"}, and search for the [web.base.url]{.title-ref} key
(create it if necessary) and enter the full address of your website as
the value (e.g., [https://www.yourdomain.com]{.title-ref}). The URL must
include the protocol [https://]{.title-ref} (or [http://]{.title-ref})
and *not* end with a slash ([/]{.title-ref}).
:::

### Map a domain name to an Odoo website {#domain-name/website-map}

Mapping your domain name to your website is different than mapping it to
your database:

-   It defines your domain name as the main one for your website,
    helping search engines to index your website correctly.
-   It defines your domain name as the base URL for your database,
    including portal links sent by email to your customers.
-   If you have multiple websites, it maps your domain name to the
    appropriate website.

Go to `Website --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. If you have multiple websites, select the one you
want to configure. In the `Domain`{.interpreted-text role="guilabel"}
field, enter the address of your website (e.g.,
[https://www.yourdomain.com]{.title-ref}) and `Save`{.interpreted-text
role="guilabel"}.

::: {.warning}
::: {.title}
Warning
:::

Mapping your domain name to your Odoo website prevents Google Search
from indexing your original database address (e.g.,
[mycompany.odoo.com]{.title-ref}).

If both addresses are already indexed, it may take some time before the
indexation of the second address is removed from Google Search. You can
use the [Google Search
Console](https://search.google.com/search-console/welcome) to fix the
issue.
:::

::: {.note}
::: {.title}
Note
:::

If you have multiple websites and companies on your database, make sure
to select the right `Company`{.interpreted-text role="guilabel"} under
`Website --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Doing so indicates Odoo which URL to use as the
`base URL <domain-name/web-base-url>`{.interpreted-text role="ref"}
according to the company in use.
:::
