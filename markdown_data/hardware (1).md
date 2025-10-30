# File: /content/odoo_doc17.0/fr/content/applications/hr/attendances/hardware.md

Hardware
========

Employees who are **not** database users, and therefore, do **not** have
access to the *Attendances* app, must sign in and out of work using a
kiosk. The following are the physical requirements for setting up a
kiosk.

Kiosk devices
-------------

A kiosk is a self-service station, where employees can
`check in and out of work
<attendances/kiosk-mode-entry>`{.interpreted-text role="ref"} with
either a `badge <attendances/hardware/badges>`{.interpreted-text
role="ref"} or an
`RFID key fob <attendances/hardware/rfid>`{.interpreted-text
role="ref"}. Typically, these devices are dedicated as kiosks only, but
any device with an internet browser is able to be set up as a kiosk.

A kiosk is used by navigating to the webpage specified in the
`configuration
<attendances/kiosk-settings>`{.interpreted-text role="ref"} section of
the *Attendances* app.

Kiosks are set up using one of the following types of devices:

-   Laptop or Desktop computer
-   Tablet
-   Mobile phone (Android or iOS)

::: {.tip}
::: {.title}
Tip
:::

Touchscreens are easy to use, and tablets and mobile phones take up less
space. That\'s why most consider using a smaller device with a
touchscreen as a kiosk.

It is recommended to place kiosks on a secure stand, or mount them
securely on a wall.
:::

Badges {#attendances/hardware/badges}
------

Badges are a way for employees to quickly sign in and out from a kiosk,
as badges are scanned by the kiosk\'s camera to quickly identify the
employee.

To generate a badge, first navigate to the
`Employees app`{.interpreted-text role="menuselection"}. Next, click on
the desired employee card to open the employee\'s form, then click the
`HR Settings`{.interpreted-text role="guilabel"} tab.

Under the `ATTENDANCE/POINT OF SALE/MANUFACTURING`{.interpreted-text
role="guilabel"} section, there is a `Badge
ID`{.interpreted-text role="guilabel"} field. If this field is blank,
click `Generate`{.interpreted-text role="guilabel"} at the end of the
`Badge
ID`{.interpreted-text role="guilabel"} line, and the field is
automatically populated with a new badge ID number. Then, click
`Print Badge`{.interpreted-text role="guilabel"} at the end of the badge
ID number to create a PDF file of the badge.

If a badge ID number is already present on the employee form, there is
no `Generate`{.interpreted-text role="guilabel"} button, only a
`Print Badge`{.interpreted-text role="guilabel"} button.

The employee\'s badge contains the employee\'s photo, name, job
position, company logo, and a barcode that can be scanned at a kiosk to
check in and out.

Badges can be printed for employees using any thermal or inkjet printer.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Badges are **not** required, as employees can manually identify
themselves on the kiosk.
:::

### Barcode scanners

When using badges to check in and out, the barcode **must** be scanned
to identify the employee. This can be done with the kiosk\'s camera, if
one is available on the device.

If a camera is **not** available on the kiosk device, an external
barcode scanner must be used to scan badges.

Kiosks work with most USB barcode scanners. Bluetooth barcode scanners
are also supported for devices without USB ports, or if a wireless
connection is desired.

Follow the manufacturer\'s instructions on the barcode scanner to
properly connect the barcode scanner to the kiosk device.

::: {.tip}
::: {.title}
Tip
:::

If the barcode scanner is connected directly to a computer, it
`must be configured
<../../inventory_and_mrp/barcode/setup/hardware>`{.interpreted-text
role="doc"} to use the computer\'s keyboard layout.
:::

::: {.note}
::: {.title}
Note
:::

An IoT box is **not** required to use a barcode scanner.
:::

RFID key fob readers {#attendances/hardware/rfid}
--------------------

Instead of using a
`badge <attendances/hardware/badges>`{.interpreted-text role="ref"},
employees can scan a personal RFID key fob with an RFID reader to check
in and out of work.

It is **required** to purchase *both* RFID key fobs and an RFID reader
to use this method to check in and out. Follow the manufacturer\'s
directions to install the RFID reader, and set up the RFID key fob.

{.align-center
width="50.0%"}

::: {.tip}
::: {.title}
Tip
:::

A recommended RFID reader is the [Neuftech USB RFID
Reader](https://neuftech.net/Neuftech-USB-RFID-Reader-ID-Kartenleseger%C3%A4t-Kartenleser-Kontaktlos-Card-Reader-f%C3%BCr-EM4100).
:::

::: {.note}
::: {.title}
Note
:::

An IoT box is **not** required to use RFID key fobs.
:::
