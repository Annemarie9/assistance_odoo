# File: /content/odoo_doc17.0/fr/content/applications/general/iot/iot_advanced/https_certificate_iot.md

HTTPS certificate (IoT) {#iot/https_certificate_iot}
=======================

*Hypertext Transfer Protocol Secure* (HTTPS) is the secure and encrypted
version of *Hypertext Transfer Protocol* (HTTP), which is the primary
protocol used for data communication between a web browser and a
website. It secures communications by using an encryption protocol known
as *Transport Layer Security* (TLS), previously called *Secure Sockets
Layer* (SSL). The security of
`HTTPS (Hypertext Transfer Protocol Secure)`{.interpreted-text
role="abbr"} relies on
`TLS (Transport Layer Security)`{.interpreted-text role="abbr"}
/`SSL (Secure Sockets Layer)`{.interpreted-text role="abbr"}
certificates, which authenticate the provider and verify their identity.

The use of HTTPS is required to communicate with certain network
devices, particularly payment terminals. If the HTTPS certificate is not
valid, some devices cannot interact with the IoT system.

::: {.note}
::: {.title}
Note
:::

In this documentation and throughout Odoo, the term *HTTPS certificate*
refers to a valid SSL certificate that allows an HTTPS connection.
:::

HTTPS certificate generation {#iot/https_certificate_iot/generation}
----------------------------

The HTTPS certificate is generated automatically. When the IoT system is
(re-)started (e.g., after it is connected to the Odoo database), a
request is sent to <https://www.odoo.com>, which returns the HTTPS
certificate if the IoT system and database meet the eligibility
criteria:

::: {#iot/https_certificate_iot/iot-eligibility}
-   The database must be a **production** instance. The database
    instance should not be a copy, a duplicate, a staging, or a
    development environment.
-   The Odoo subscription must be ongoing
    (`In Progress`{.interpreted-text role="guilabel"} status) and have
    an `IoT
    box subscription <iot/iot/iot-subscription>`{.interpreted-text
    role="ref"} line.
:::

When the certificate has been received:

-   The IoT system\'s homepage address is updated to a new HTTPS URL
    ending with [.odoo-iot.com]{.title-ref}. Click the URL to establish
    a secure HTTPS connection.

    

-   The `HTTPS certificate`{.interpreted-text role="guilabel"} banner
    displays the certificate\'s validity period. To view this
    information, click the `fa-cogs`{.interpreted-text role="icon"}
    (`cogs`{.interpreted-text role="guilabel"}) button on the IoT
    system\'s homepage.

    

HTTPS certificate generation issues and errors
----------------------------------------------

### The HTTPS certificate does not generate

Potential causes include the following:

-   No
    `IoT box subscription <iot/iot/iot-subscription>`{.interpreted-text
    role="ref"} is linked to your account.

-   The
    `IoT box subscription <iot/iot/iot-subscription>`{.interpreted-text
    role="ref"} was added *after* connecting the IoT system to the
    database. In this case, refresh the IoT system\'s homepage or
    reboot/`restart
    <iot/windows_iot/restart>`{.interpreted-text role="ref"} the IoT
    system to regenerate the HTTPS certificate.

-   The firewall is preventing the HTTPS certificate from generating
    correctly. In this case, deactivate the firewall until the
    certificate is successfully generated.

    ::: {.note}
    ::: {.title}
    Note
    :::

    Some devices, such as routers with a built-in firewall, can prevent
    the HTTPS certificate from generating.
    :::

### The IoT system\'s homepage can be accessed using its IP address but not the [xxx.odoo-iot.com]{.title-ref} URL

Contact your system or network administrator to address the issue.
Network-related problems are beyond the scope of Odoo support services.

-   If the router allows manual
    `DNS (Domain Name System)`{.interpreted-text role="abbr"}
    configuration, update the settings to use [Google
    DNS](https://developers.google.com/speed/public-dns).
-   If the router does not support this, you need to update the DNS
    settings directly on each device that interacts with the IoT system
    to use .
    Instructions for configuring DNS on individual devices can be found
    on the respective manufacturer\'s website.

::: {.note}
::: {.title}
Note
:::

\- Some IoT devices, such as payment terminals, likely do not require
DNS changes, as they are typically pre-configured with custom DNS
settings. - On some browsers, an error code mentioning the DNS (such as
[DNS\_PROBE\_FINISHED\_NXDOMAIN]{.title-ref}) is displayed.
:::

### Errors

A specific error code is displayed on the IoT system\'s homepage if any
issues occur during the generation or reception of the HTTPS
certificate.

::: {.tip}
::: {.title}
Tip
:::

When you access the IoT system\'s homepage, it automatically checks for
an HTTPS certificate and attempts to generate one if it is missing. If
an error appears, refresh the page to see if the issue is resolved.
:::

#### [ERR\_IOT\_HTTPS\_CHECK\_NO\_SERVER]{.title-ref}

The server configuration is missing, i.e., the Odoo instance is not
`connected <../connect>`{.interpreted-text role="doc"} to the IoT
system.

#### [ERR\_IOT\_HTTPS\_CHECK\_CERT\_READ\_EXCEPTION]{.title-ref}

An error occurred while attempting to read the existing HTTPS
certificate. Verify that the HTTPS certificate file is readable.

#### [ERR\_IOT\_HTTPS\_LOAD\_NO\_CREDENTIAL]{.title-ref}

The contract and/or database
`UUID (Universal Unique Identifier)`{.interpreted-text role="abbr"} is
missing form the IoT.

Verify that both values are correctly configured. To update them,
`access the IoT box's
<iot/iot-box/homepage>`{.interpreted-text role="ref"} or
`Windows virtual IoT's homepage <iot/windows-iot/homepage>`{.interpreted-text
role="ref"}, click the `fa-cogs`{.interpreted-text role="icon"}
(`cogs`{.interpreted-text role="guilabel"}) button, then click
`Credential`{.interpreted-text role="guilabel"}.

#### [ERR\_IOT\_HTTPS\_LOAD\_REQUEST\_EXCEPTION]{.title-ref}

An unexpected error occurred while the IoT system tried to reach
<https://www.odoo.com>. This is likely due to network-related issues,
such as:

-   The IoT system does not have Internet access.
-   Network restrictions (e.g., firewalls or VPNs) are preventing
    communication with <https://www.odoo.com>.

::: {.note}
::: {.title}
Note
:::

\- To access the full request exception details with information
regarding the error, `enable
the developer mode <developer-mode>`{.interpreted-text role="ref"},
click the IoT system\'s card in the IoT app, and click
`Download logs`{.interpreted-text role="guilabel"} on the
`IoT system's form <iot/connect/IoT-form>`{.interpreted-text
role="ref"}. To define the log levels recorded in the IoT system\'s log
file, `access the IoT box's
<iot/windows-iot/homepage>`{.interpreted-text role="ref"} or
`Windows virtual IoT's <iot/iot-box/homepage>`{.interpreted-text
role="ref"} homepage, click the `fa-cogs`{.interpreted-text role="icon"}
(`cogs`{.interpreted-text role="guilabel"}) button, then
`Log level`{.interpreted-text role="guilabel"} at the bottom of the
page. - To address network-related issues, contact your system or
network administrator; these issues are beyond the scope of Odoo support
services.
:::

#### [ERR\_IOT\_HTTPS\_LOAD\_REQUEST\_STATUS]{.title-ref}

The IoT system successfully reached <https://www.odoo.com> but received
an unexpected [HTTP response (status
codes)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).

This error code includes the HTTP status. For example,
[ERR\_IOT\_HTTPS\_LOAD\_REQUEST\_STATUS 404]{.title-ref} means the
server returned a \"Page Not Found\" response.

To solve this issue:

1.  Open <https://www.odoo.com> in a web browser to check if the website
    is temporarily down for maintenance.

2.  | If <https://www.odoo.com> is down for maintenance, wait for it to
      resume.
    | If the website is operational, open a [support
      ticket](https://www.odoo.com/help) and make sure to include the
      3-digit HTTPS status code in the ticket.

#### [ERR\_IOT\_HTTPS\_LOAD\_REQUEST\_NO\_RESULT]{.title-ref}

The IoT system successfully connected to <https://www.odoo.com>, but the
server refused to provide the HTTPS certificate.

Check that the IoT system and database meet the
`eligibility requirements
<iot/https_certificate_iot/iot-eligibility>`{.interpreted-text
role="ref"} for an HTTPS certificate.
