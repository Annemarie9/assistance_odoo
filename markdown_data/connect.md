# File: /content/odoo_doc17.0/fr/content/applications/general/iot/connect.md

IoT system connection to Odoo
=============================

Prerequisites
-------------

To connect the IoT system to an Odoo database, the following
prerequisites must be met:

-   The Internet of Things (IoT) app must be
    `installed <general/install>`{.interpreted-text role="ref"}.
-   The IoT system must be connected to the network.
-   The computer connecting to Odoo must be on the same network as the
    IoT system.

::: {.note}
::: {.title}
Note
:::

It is recommended to connect the IoT system to a **production**
instance, as other types of environments may cause issues (e.g., with
`HTTPS certificate generation
<iot/https_certificate_iot/iot-eligibility>`{.interpreted-text
role="ref"}).
:::

::: {.seealso}
\- `iot_box`{.interpreted-text role="doc"} -
`windows_iot`{.interpreted-text role="doc"}
:::

Connection
----------

The IoT system can be connected to the Odoo database using a
`pairing code
<iot/connect/pairing-code>`{.interpreted-text role="ref"} or a
`connection token <iot/connect/token>`{.interpreted-text role="ref"}.

### Connection using a pairing code {#iot/connect/pairing-code}

::: {.note}
::: {.title}
Note
:::

\- The pairing code is displayed for up to 5 minutes after the IoT
system starts. If the code is no longer visible, reboot the IoT box or
`restart the Windows virtual IoT service
<iot/windows_iot/restart>`{.interpreted-text role="ref"} to display the
pairing code again. Alternatively, connect the IoT system to the
database using a
`connection token <iot/connect/token>`{.interpreted-text role="ref"}. -
The pairing code is not displayed if the IoT system is already connected
to a database (e.g., a test database).
:::

1.  Retrieve the IoT\'s system pairing code:

    ::: {.tabs}
    ::: {.group-tab}
    IoT box

    Connect the IoT box to an external monitor or printer. If the IoT
    box was already plugged prior to this, reboot it by unplugging it
    for a few seconds and replugging it.

    -   External monitor: The pairing code should be displayed on the
        screen a few minutes after rebooting the IoT box.
    -   Printer: The pairing code should be printed automatically.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    If no external monitor or printer is connected to the IoT box,
    access the `IoT
    box's homepage <iot/iot-box/homepage>`{.interpreted-text
    role="ref"}; the code is displayed in the `Pairing
    Code`{.interpreted-text role="guilabel"} section.
    :::
    :::

    ::: {.group-tab}
    Windows virtual IoT

    On the computer with the Windows virtual IoT installed, open the IoT
    system\'s homepage in a web browser by navigating to the URL
    [http://localhost:8069]{.title-ref}. Then, scroll to the
    `Pairing Code`{.interpreted-text role="guilabel"} section.
    :::
    :::

2.  In Odoo, open the IoT app and click `Connect`{.interpreted-text
    role="guilabel"}.

3.  In the `Connect an IoT Box`{.interpreted-text role="guilabel"} popup
    that opens, enter the `Pairing code`{.interpreted-text
    role="guilabel"}.

4.  Click `Pair`{.interpreted-text role="guilabel"}.

### Connection using a connection token {#iot/connect/token}

1.  In Odoo, open the IoT app and click `Connect`{.interpreted-text
    role="guilabel"}.
2.  In the `Connect an IoT Box`{.interpreted-text role="guilabel"} popup
    that opens, copy the `Token`{.interpreted-text role="guilabel"}.
3.  Access the `IoT box's <iot/iot-box/homepage>`{.interpreted-text
    role="ref"} or `Windows virtual IoT's
    <iot/windows-iot/homepage>`{.interpreted-text role="ref"} homepage.
4.  In the `Odoo database connected`{.interpreted-text role="guilabel"}
    section, click `Configure`{.interpreted-text role="guilabel"}.
5.  Paste the token into the `Server Token`{.interpreted-text
    role="guilabel"} field and click `Connect`{.interpreted-text
    role="guilabel"}.

IoT system form {#iot/connect/IoT-form}
---------------

Once the IoT system is connected to the Odoo database, it is displayed
as a card in the IoT app. Click the IP address on the card to access the
`IoT box's <iot/windows-iot/homepage>`{.interpreted-text role="ref"} or
`Windows virtual IoT's <iot/iot-box/homepage>`{.interpreted-text
role="ref"} homepage. Click the card to access the list of
`devices <devices>`{.interpreted-text role="doc"} connected to the IoT
system.

::: {.tip}
::: {.title}
Tip
:::

`Enable the developer mode <developer-mode>`{.interpreted-text
role="ref"} to access the IoT system\'s
`Technical Information`{.interpreted-text role="guilabel"}, such as its
`Identifier`{.interpreted-text role="guilabel"}, `Domain
address`{.interpreted-text role="guilabel"}, and
`Image version`{.interpreted-text role="guilabel"}.
:::

::: {.note}
::: {.title}
Note
:::

By default, drivers are automatically
`updated <iot_updating_iot/handlers>`{.interpreted-text role="ref"}
every time the IoT system is restarted. To disable automatic updates,
uncheck the `Automatic drivers
update`{.interpreted-text role="guilabel"} option.
:::

Troubleshooting {#iot/connect/troubleshooting}
---------------

### The pairing code does not appear or does not work

The `pairing code <iot/connect/pairing-code>`{.interpreted-text
role="ref"} might not be displayed or printed under the following
circumstances:

-   The IoT system is not connected to the Internet.
-   The IoT system is already connected to an Odoo database.
-   The `pairing code <iot/connect/pairing-code>`{.interpreted-text
    role="ref"} display time has expired. Reboot the IoT box or
    `restart the Windows virtual IoT service <iot/windows_iot/restart>`{.interpreted-text
    role="ref"} to display the pairing code again.
-   The IoT system\'s image version is too old and needs to be `updated
    <iot/updating_iot/image-code>`{.interpreted-text role="ref"}.

### The IoT system is connected but does not appear in the database

The IoT system might take a few minutes to restart when it connects to a
database. If it still does not appear after a few minutes:

-   Verify that the IoT system can reach the database and the server
    does not use a multi-database environment.
-   Reboot the IoT box or
    `restart the Windows virtual IoT service <iot/windows_iot/restart>`{.interpreted-text
    role="ref"}.

### The IoT box is connected to the Odoo database but cannot be reached

Verify that the IoT system and the computer running the Odoo database
are connected to the same network.

### The Windows virtual IoT\'s homepage cannot be accessed from another device

Check the `iot/windows-iot/firewall`{.interpreted-text role="ref"}.

### The IoT system is disconnected from the database after an Odoo upgrade

`Update the IoT system's image <iot/updating_iot/image-code>`{.interpreted-text
role="ref"} by flashing the IoT box\'s card or
`uninstalling the Windows virtual IoT program <iot/windows_iot/uninstall>`{.interpreted-text
role="ref"} and
`reinstalling <iot/windows-iot/installation>`{.interpreted-text
role="ref"} the latest package for Windows **matching your database\'s
version**.
