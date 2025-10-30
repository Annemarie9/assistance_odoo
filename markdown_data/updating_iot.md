# File: /content/odoo_doc17.0/fr/content/applications/general/iot/iot_advanced/updating_iot.md

IoT system updates
==================

Due to the complexity of IoT systems, the term *updating* can refer to
several processes, including:

-   `Updating the IoT system's image and/or core code <iot/updating_iot/image-code>`{.interpreted-text
    role="ref"};
-   `Updating the handlers <iot_updating_iot/handlers>`{.interpreted-text
    role="ref"}, which include the interfaces and drivers.

Image and core code update {#iot/updating_iot/image-code}
--------------------------

::: {.tabs}
::: {.group-tab}
IoT box

To check if the IoT box is up-to-date (and update it if needed),
`access the IoT box's
homepage <iot/iot-box/homepage>`{.interpreted-text role="ref"}, click
the `fa-cogs`{.interpreted-text role="icon"} (`cogs`{.interpreted-text
role="guilabel"}) button at the top-right, then
`Update`{.interpreted-text role="guilabel"} in the
`Version`{.interpreted-text role="guilabel"} section.

::: {.tip}
::: {.title}
Tip
:::

`Enable the developer mode <developer-mode>`{.interpreted-text
role="ref"} to view the current versions of the IoT box\'s image and
core code.
:::

**Image update**

To update the IoT box\'s image, flash its SD card. Flashing can be
performed using , a free and
open-source tool for writing disk images to SD cards.

::: {.note}
::: {.title}
Note
:::

\- Updating the IoT system\'s image is often required after upgrading
the Odoo database to a newer version. - A computer with a micro SD card
reader/adapter is required to flash the micro SD card. - An alternative
software for flashing the micro SD card is [Raspberry Pi
Imager](https://www.raspberrypi.com/software/).
:::

1.  
2.  Insert the IoT box\'s micro SD card into the computer or adapter.
3.  Open balenaEtcher, click `Flash from URL`{.interpreted-text
    role="guilabel"}, and enter the following URL:
    [http://nightly.odoo.com/master/iotbox/iotbox-latest.zip]{.title-ref}.
4.  Click `Select target`{.interpreted-text role="guilabel"} and select
    the SD card.
5.  Click `Flash`{.interpreted-text role="guilabel"} and wait for the
    process to finish.



**Core code update**

To update the IoT box\'s core code, click `Update`{.interpreted-text
role="guilabel"} under `IoT Box Update`{.interpreted-text
role="guilabel"} in the `Update`{.interpreted-text role="guilabel"}
popup.

::: {.danger}
::: {.title}
Danger
:::

This process may take over 30 minutes. **Do not turn off or unplug the
IoT box** during this time, as doing so could leave the device in an
inconsistent state, requiring the IoT box to be reflashed with a new
image.
:::
:::

::: {.group-tab}
Windows virtual IoT

To update the Windows virtual IoT\'s image and code,
`uninstall the program
<iot/windows_iot/uninstall>`{.interpreted-text role="ref"} and
`reinstall <iot/windows-iot/installation>`{.interpreted-text role="ref"}
the latest package.
:::
:::

Handler (driver) update {#iot_updating_iot/handlers}
-----------------------

To update the IoT system\'s handlers (i.e., drivers and interfaces) and
synchronize them with the configured server handler\'s code, for
example, to resolve issues where
`devices <../devices>`{.interpreted-text role="doc"} are not functioning
properly with the IoT system, proceed as follows:

1.  Access the `IoT box's <iot/iot-box/homepage>`{.interpreted-text
    role="ref"} or `Windows virtual IoT's
    <iot/windows-iot/homepage>`{.interpreted-text role="ref"} homepage
    and click the `fa-cogs`{.interpreted-text role="icon"}
    (`cogs`{.interpreted-text role="guilabel"}) button at the top-right.
2.  Click `Update`{.interpreted-text role="guilabel"} in the
    `Version`{.interpreted-text role="guilabel"} section.
3.  In the `Update`{.interpreted-text role="guilabel"} popup that opens,
    click `Force Drivers Update`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

If you have an
`on-premise </administration/on_premise>`{.interpreted-text role="doc"}
or `Odoo.sh
</administration/odoo_sh/overview/introduction>`{.interpreted-text
role="doc"} database, the configured server must be up-to-date to ensure
the handlers\' code includes the latest fixes and patches.
:::

::: {.note}
::: {.title}
Note
:::

A handler update is also performed automatically every time the IoT
system is restarted unless the
`Automatic drivers update`{.interpreted-text role="guilabel"} option is
disabled in the `Technical
information`{.interpreted-text role="guilabel"} tab in the
`IoT system's form <iot/connect/IoT-form>`{.interpreted-text role="ref"}
in Odoo.
:::
