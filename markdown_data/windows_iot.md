# File: /content/odoo_doc17.0/fr/content/applications/general/iot/windows_iot.md

Windows virtual IoT
===================

To start using the Windows virtual IoT:

1.  Make sure all
    `prerequisites <iot/windows-iot/prerequisites>`{.interpreted-text
    role="ref"} are met.
2.  `Install the Windows virtual IoT <iot/windows-iot/installation>`{.interpreted-text
    role="ref"} on a Windows computer.
3.  `Configure the Windows Firewall <iot/windows-iot/firewall>`{.interpreted-text
    role="ref"}.
4.  Connect your `devices <devices>`{.interpreted-text role="doc"} to
    the Windows virtual IoT.
5.  `Connect the Windows virtual IoT to your Odoo database <connect>`{.interpreted-text
    role="doc"}.

Prerequisites {#iot/windows-iot/prerequisites}
-------------

The following prerequisites must be met before setting up and using the
Windows virtual IoT:

-   A valid
    `IoT box subscription <iot/iot/iot-subscription>`{.interpreted-text
    role="ref"}.
-   An updated and recent version of Windows (i.e., Windows 10 or
    Windows 11) installed on a Windows computer (laptop, desktop, or
    server).

::: {.note}
::: {.title}
Note
:::

\- `MRP (Material Requirement Planning)`{.interpreted-text role="abbr"}
devices, including cameras and measurement tools, are not compatible
with Windows virtual IoT. - It is also possible to create a Windows
Virtual Machine on a MacOS/Linux computer. However, this option is not
supported by Odoo, and no troubleshooting assistance will be provided.
:::

Installation {#iot/windows-iot/installation}
------------

To install the Windows virtual IoT on a Windows computer:

1.  Access  and
    download the **Community** edition of Odoo for Windows **matching
    your database\'s version**.

2.  Open the downloaded `.exe`{.interpreted-text role="file"} file,
    allow the app to make changes to your device, select a language, and
    click `OK`{.interpreted-text role="guilabel"}.

3.  Click `Next`{.interpreted-text role="guilabel"}, then
    `I Agree`{.interpreted-text role="guilabel"} to accept the terms and
    conditions and continue.

4.  Select `Odoo IoT`{.interpreted-text role="guilabel"} from the
    `Select the type of install`{.interpreted-text role="guilabel"}
    dropdown list. The following components should be selected: Odoo
    Server, Odoo IoT, Nginx WebServer, and Ghostscript interpreter.

5.  Verify you have the required space on your computer and click
    `Next`{.interpreted-text role="guilabel"}.

6.  In the `Destination folder`{.interpreted-text role="guilabel"},
    enter C:\\odoo and click `Install`{.interpreted-text
    role="guilabel"}.

    ::: {.warning}
    ::: {.title}
    Warning
    :::

    Do not install Odoo\'s Windows virtual IoT in any Windows user
    directory, as this can cause issues with
    `iot/https_certificate_iot/generation`{.interpreted-text
    role="ref"}.
    :::

7.  Once the installation is complete, click `Next`{.interpreted-text
    role="guilabel"}.

8.  Set up GPL Ghostscript: Click `Next`{.interpreted-text
    role="guilabel"}, agree to the terms and conditions, click
    `Install`{.interpreted-text role="guilabel"}, then
    `Finish`{.interpreted-text role="guilabel"}.

9.  Click `Next`{.interpreted-text role="guilabel"},
    `Next`{.interpreted-text role="guilabel"}, and
    `Finish`{.interpreted-text role="guilabel"} to complete the setup.
    The
    `IoT system's homepage <iot/windows-iot/homepage>`{.interpreted-text
    role="ref"} automatically opens in a web browser with the URL
    [http://localhost:8069]{.title-ref}.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    If the web browser does not show anything,
    `restart <iot/windows_iot/restart>`{.interpreted-text role="ref"}
    the Windows virtual IoT service.
    :::

10. Check that you can access the
    `IoT system's homepage <iot/windows-iot/homepage>`{.interpreted-text
    role="ref"} in a web browser:

    -   on the Windows virtual IoT computer, and

    -   on another device **on the same network as the IoT system** by
        navigating to the URL [http://xxx:8069]{.title-ref} (where
        [xxx]{.title-ref} is the IoT system\'s IP address).

    -   on another device **on the same network as the IoT system** by
        navigating to the URL [https://xxx]{.title-ref} (where
        [xxx]{.title-ref} is the IoT system\'s IP address) to test for
        `HTTPS
        <iot_advanced/https_certificate_iot>`{.interpreted-text
        role="doc"} connection.

        ::: {.tip}
        ::: {.title}
        Tip
        :::

        If you cannot access the
        `IoT system's homepage <iot/windows-iot/homepage>`{.interpreted-text
        role="ref"} from another device, create a
        `Windows Firewall <iot/windows-iot/firewall>`{.interpreted-text
        role="ref"} rule to allow communication through port
        [8069]{.title-ref}.
        :::

Windows Firewall configuration {#iot/windows-iot/firewall}
------------------------------

Firewalls help keep devices secure but can sometimes block legitimate
connections. If the Windows virtual IoT isn\'t accessible on the
`LAN (Local Area Network)`{.interpreted-text role="abbr"}, for example
from another device, it could be due to a firewall blocking the
connection. To prevent this issue, configure exceptions for network
discovery in the `OS (Operating System)`{.interpreted-text role="abbr"}
or firewall settings.

::: {.note}
::: {.title}
Note
:::

If third-party firewall software is installed on the Windows computer,
refer to the software\'s documentation to configure firewall exceptions.
:::

To create a rule on Windows Defender and allow communication through
port [8069]{.title-ref}, follow these steps:

1.  Search the Windows start menu for [firewall]{.title-ref} and select
    the `Windows Defender Firewall
    with Advanced Security`{.interpreted-text role="guilabel"} app.

2.  In the left part of the window, select
    `Inbound Rules`{.interpreted-text role="guilabel"}.

3.  In the right part of the window, under `Actions`{.interpreted-text
    role="guilabel"}, click `New Rule`{.interpreted-text
    role="guilabel"}.

4.  In the `New Inbound Rule Wizard`{.interpreted-text role="guilabel"}
    that opens, select the `Port`{.interpreted-text role="guilabel"}
    type of rule and click `Next`{.interpreted-text role="guilabel"}.

5.  On the `Protocols and Ports`{.interpreted-text role="guilabel"}
    page, make sure `TCP`{.interpreted-text role="guilabel"} and
    `Specified
    local ports`{.interpreted-text role="guilabel"} are selected, enter
    the following in the field: [8069, 80, 443]{.title-ref}, and click
    `Next`{.interpreted-text role="guilabel"}.

    ::: {.note}
    ::: {.title}
    Note
    :::

    Other ports may be necessary depending on your IoT devices. For
    example, for the
    `/applications/sales/point_of_sale/payment_methods/terminals/worldline`{.interpreted-text
    role="doc"} payment terminal, add the [9050]{.title-ref} port.
    :::

6.  On the `Action`{.interpreted-text role="guilabel"} page, select
    `Allow the connection`{.interpreted-text role="guilabel"} and click
    `Next`{.interpreted-text role="guilabel"}.

7.  On the `Profile`{.interpreted-text role="guilabel"} page, disable
    any connection type(s) that don\'t apply to your Windows computer
    and click `Next`{.interpreted-text role="guilabel"}.

8.  On the `Name`{.interpreted-text role="guilabel"} page, provide a
    `Name`{.interpreted-text role="guilabel"} (e.g., [Odoo]{.title-ref})
    and, optionally, a brief `Description`{.interpreted-text
    role="guilabel"}, then click `Finish`{.interpreted-text
    role="guilabel"}.

::: {.seealso}
[Windows Firewall rules
documentation](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/rules)
:::

Windows virtual IoT homepage {#iot/windows-iot/homepage}
----------------------------

To access the Windows virtual IoT\'s homepage, navigate to the URL
[http://localhost:8069]{.title-ref} on the Windows virtual IoT computer
or open a web browser from another computer **on the same network as the
IoT system** and navigate to the URL [http://xxx:8069]{.title-ref}
(where [xxx]{.title-ref} is the IoT system\'s IP address).

Once the Windows virtual IoT is
`connected to the Odoo database <connect>`{.interpreted-text
role="doc"}, its homepage can be accessed from Odoo by opening the IoT
app and clicking the URL displayed on the IoT system\'s card.



::: {.note}
::: {.title}
Note
:::

Make sure the
`Windows Firewall is configured <iot/windows-iot/firewall>`{.interpreted-text
role="ref"} to allow access.
:::

Device connection
-----------------

Most `devices <devices>`{.interpreted-text role="doc"} automatically
connect to the Windows computer used for the Windows Virtual IoT through
[Windows Plug and Play
(PnP)](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/introduction-to-plug-and-play).
However, if Windows does not recognize the device automatically upon
connection, the administrator may need to manually install the
appropriate drivers.

::: {.tip}
::: {.title}
Tip
:::

After connecting the devices to the computer, refresh the
`IoT system's homepage
<iot/windows-iot/homepage>`{.interpreted-text role="ref"} to verify that
the device is listed. If the device does not appear,
`reload the handlers <iot_updating_iot/handlers>`{.interpreted-text
role="ref"} from the `IoT system's homepage
<iot/windows-iot/homepage>`{.interpreted-text role="ref"}.
:::

Windows virtual IoT restart {#iot/windows_iot/restart}
---------------------------

To manually restart the Windows IoT server, search the Windows start
menu for [services]{.title-ref} and select the
`Services`{.interpreted-text role="guilabel"} app. Scroll down to the
`odoo-server-xxx`{.interpreted-text role="guilabel"} service (where
[xxx]{.title-ref} is the odoo version), right-click it, and select
`Start`{.interpreted-text role="guilabel"} or
`Restart`{.interpreted-text role="guilabel"}.

Windows virtual IoT uninstall {#iot/windows_iot/uninstall}
-----------------------------

To uninstall the Windows virtual IoT,

the Odoo program on your Windows computer. Confirm the uninstallation
and complete the steps in the `Odoo Uninstall`{.interpreted-text
role="guilabel"} dialog.
