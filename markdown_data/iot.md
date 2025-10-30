# File: /content/odoo_doc17.0/fr/content/applications/general/iot.md

show-content

:   

hide-page-toc

:   

nosearch

:   

Internet of Things (IoT)
========================

Odoo Internet of Things (IoT) allows to connect physical devices such as
barcode scanners, receipt printers, payment terminals, measurement
tools, etc. to an Odoo database using an IoT system.

The following IoT systems are supported:

-   `IoT box <iot/iot_box>`{.interpreted-text role="doc"}:
    micro-computer, plug-and-play device (i.e., the Odoo IoT program is
    pre-installed);
-   `Windows virtual IoT <iot/windows_iot>`{.interpreted-text
    role="doc"}: Odoo IoT program for Windows that can be installed on a
    Windows computer.

::: {.note}
::: {.title}
Note
:::

\- `MRP (Material Requirement Planning)`{.interpreted-text role="abbr"}
devices, including cameras and measurement tools, are not compatible
with Windows virtual IoT. - Multiple IoT systems can be used at the same
time. - It is also possible to create a Windows Virtual Machine on a
MacOS/Linux computer. However, this option is not supported by Odoo, and
no troubleshooting assistance will be provided.
:::

IoT box subscription {#iot/iot/iot-subscription}
--------------------

An IoT box subscription is required for production use of IoT systems.
If you have issues related to your subscription, contact the database\'s
account manager or Odoo partner for assistance.

::: {.tip}
::: {.title}
Tip
:::

If the subscription is linked to an 
portal user, check the information on the portal\'s subscription page.
:::

::: {.seealso}
\- [Odoo\'s compatible IoT
devices](https://www.odoo.com/app/iot-hardware) - [Odoo Tutorials:
Internet of Things (IoT)
Tutorials](https://www.odoo.com/slides/internet-of-things-iot-175) -

:::

::: {.cards}
::: {.card target="iot/iot_box" large=""}
IoT box

Set up an IoT box.
:::

::: {.card target="iot/windows_iot" large=""}
Windows virtual IoT

Set up Windows virtual IoT.
:::

::: {.card target="iot/connect"}
IoT system connection to Odoo

Connect the IoT system to your Odoo database and troubleshoot potential
connection issues.
:::

::: {.card target="iot/devices"}
Devices

Connect devices such as printers, screens, measurement tools, etc., to
the IoT system.
:::

::: {.card target="iot/iot_advanced/https_certificate_iot"}
HTTPS certificate

Verify your IoT system and database meet the eligibility requirements
for HTTPS certificate generation and address any related issues.
:::

::: {.card target="iot/iot_advanced/updating_iot"}
IoT system updates

Update your IoT system\'s image, core code, and handlers to benefit from
the latest IoT fixes and features or reset the IoT system if needed.
:::
:::

::: {.toctree titlesonly=""}
iot/iot\_box iot/windows\_iot iot/connect iot/iot\_advanced iot/devices
:::
