# File: /content/odoo_doc17.0/fr/content/applications/hr/attendances/kiosks.md

Kiosks
======

Odoo\'s *Attendances* app allows employees to check in and out of work
directly from the database, or from a kiosk.

A kiosk is a `dedicated device <hardware>`{.interpreted-text role="doc"}
(a PC, tablet, or mobile phone) for employees to use when they check in
and out.

Kiosks are needed for employees who do **not** have access to the
database.

Only employees with access to the database can check in and out from the
*Attendances* app, and they are referred to as *users*.

::: {.important}
::: {.title}
Important
:::

If employees
`check in and out <attendances/kiosk-mode-entry>`{.interpreted-text
role="ref"} using a badge or an RFID, then an
`accessible device <hardware>`{.interpreted-text role="doc"} in
`Kiosk Mode <attendances/kiosk-mode>`{.interpreted-text role="ref"}
**must** be available in order to use these two methods.
:::

Configuration
-------------

There are only a few configurations needed to use kiosks in the
*Attendances* application. Navigate to
`Attendances app --> Configuration`{.interpreted-text
role="menuselection"} to access the `Settings`{.interpreted-text
role="guilabel"} page to configure the
`attendances/kiosk-mode`{.interpreted-text role="ref"} and the
`attendances/kiosk-settings`{.interpreted-text role="ref"}.

Once all desired settings have been configured, click the
`Save`{.interpreted-text role="guilabel"} button on the
`Settings`{.interpreted-text role="guilabel"} page, to activate and
enable them.

### Kiosk Mode section {#attendances/kiosk-mode}

Using the drop-down menu, select how an employee checks in when using a
kiosk. Options are `Barcode/RFID`{.interpreted-text role="guilabel"},
`Barcode/RFID and Manual Selection`{.interpreted-text role="guilabel"},
or `Manual
Selection`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The *Barcode* application **does not** need to be installed to use one
of the Barcode/RFID settings.
:::

### Kiosk Settings section {#attendances/kiosk-settings}

The various settings in the `Kiosk Settings`{.interpreted-text
role="guilabel"} section determine how employees check in and out with
kiosks.

-   `Barcode Source`{.interpreted-text role="guilabel"}: this setting
    **only** appears if one of the two *Barcode/RFID* selections were
    configured for the
    `Kiosk Mode <attendances/kiosk-mode>`{.interpreted-text role="ref"}
    setting.

    If available, select how barcodes are scanned at the kiosk, via one
    of the drop-down menu options. Barcodes can be scanned with a
    dedicated `Scanner`{.interpreted-text role="guilabel"}, or with a
    device\'s camera (`Front Camera`{.interpreted-text role="guilabel"}
    or `Back Camera`{.interpreted-text role="guilabel"}).

-   `Employee PIN Identification`{.interpreted-text role="guilabel"}:
    tick this checkbox if employees should use a unique PIN to check in.
    PINs are configured on each individual employee record. Refer to the
    `new
    employee documentation <employees/hr-settings>`{.interpreted-text
    role="ref"} documentation for more information on setting up PINs.

-   `Display Time`{.interpreted-text role="guilabel"}: determine how
    many seconds a check-in/check-out confirmation message remains on
    the kiosk screen before returning to the main check in screen.

-   `Attendance Kiosk Url`{.interpreted-text role="guilabel"}: Odoo
    generates a unique web address (URL) to use a device as a kiosk,
    without having to sign in to the Odoo database. When setting up a
    kiosk device, navigate to this unique web address in a web browser
    to present the *Attendances* app kiosk.

    ::: {.important}
    ::: {.title}
    Important
    :::

    These kiosk URLs are **not** secured with any type of access code.
    Anyone who has the URL can access the *Attendances* app kiosk. If
    the URL is compromised for any reason, such as in the event of a
    security breach, click
    `Generate a new Kiosk Mode URL`{.interpreted-text role="guilabel"},
    located beneath the link, to generate a new URL, and update the
    kiosk, accordingly.
    :::

Kiosk mode
----------

Entering *Kiosk Mode* is **only** available for users with specific
`access rights
<attendances/access-rights>`{.interpreted-text role="ref"}.

*Kiosk Mode* can be activated in two different ways:

1.  Navigate to the `Attendances app`{.interpreted-text
    role="menuselection"}, and click `Kiosk Mode`{.interpreted-text
    role="guilabel"} in the top menu. The device then signs out of Odoo
    and enters *Kiosk Mode*.
2.  Navigate to the
    `Attendances app --> Configuration`{.interpreted-text
    role="menuselection"}. In the `Kiosk
    Settings`{.interpreted-text role="guilabel"} section, use the link
    in the `Attendance Kiosk Url`{.interpreted-text role="guilabel"}
    field to open *Kiosk Mode* on any device.

{.align-center}

As a security measure, once a device is in *Kiosk Mode*, it is not
possible to go back into the database without signing back in.

::: {.note}
::: {.title}
Note
:::

At any time, a new kiosk URL can be generated, if needed. Click the
`fa-refresh`{.interpreted-text role="icon"}
`Generate a new Kiosk Mode URL`{.interpreted-text role="guilabel"}
:::

To exit *Kiosk Mode*, just close the tab in the web browser or return to
the main log-in screen of Odoo.

Check in and out with a kiosk {#attendances/kiosk-mode-entry}
-----------------------------

### Badge

To check in or out using a badge, tap the `fa-camera`{.interpreted-text
role="icon"} `Tap to scan`{.interpreted-text role="guilabel"} image in
the center of the kiosk.

{.align-center}

Then, scan the barcode on the badge using the method configured in the
`Kiosk Settings
<attendances/kiosk-settings>`{.interpreted-text role="ref"} section of
the configuration menu.

Once the barcode is scanned, the employee is checked in or out, and a
`confirmation message
<attendances/confirmation>`{.interpreted-text role="ref"} appears with
all the information.

### RFID

To check in or out using an RFID key fob, simply scan the fob with an
RFID reader.

Once scanned, the employee is either checked in or checked out, and a
`confirmation message
<attendances/confirmation>`{.interpreted-text role="ref"} appears with
all the information.

### Manually

Users who do not have a scannable badge, or an RFID fob, can manually
check in and out at a kiosk.

Tap the `Identify Manually`{.interpreted-text role="guilabel"} button on
the kiosk, and a screen appears with all the employees that can be
checked in or out. The *Employees* application dashboard has the same
display.

Tap on a person to check them in or out, and a `confirmation message
<attendances/confirmation>`{.interpreted-text role="ref"} appears.

There are two ways to quickly find a specific person:

-   `Search...`{.interpreted-text role="guilabel"}: tap on the
    `Search...`{.interpreted-text role="guilabel"} field, and enter the
    desired person\'s name. As the name is typed in, the matching
    results are displayed on the screen.
-   `Department`{.interpreted-text role="guilabel"}: tap on any desired
    selection in the `Department`{.interpreted-text role="guilabel"}
    section, located on the left-side of the screen, to **only** view
    employees from that specific department. The number at the end of
    each listed `Department`{.interpreted-text role="guilabel"}
    represents how many employees that department has.

#### PIN

If the `Employee PIN Identification`{.interpreted-text role="guilabel"}
checkbox was ticked in the `Kiosk Settings
<attendances/kiosk-settings>`{.interpreted-text role="ref"} section of
the configuration menu, the employee is prompted to enter a PIN when
manually checking in or out.

After the employee is selected, a number pad appears with a message.
When checking in,
`(Employee) Welcome! Please enter your PIN to check in`{.interpreted-text
role="guilabel"} appears above the numbers. When checking out,
`(Employee) Want to check out? Please enter your PIN to check out`{.interpreted-text
role="guilabel"} appears above the numbers.

Tap in the PIN using the number pad, then tap `OK`{.interpreted-text
role="guilabel"} when done. The employee is then checked in or out, and
a `confirmation message <attendances/confirmation>`{.interpreted-text
role="ref"} appears.

{.align-center}

### Confirmation message {#attendances/confirmation}

When an employee checks in or out, a confirmation message appears, with
all the check in or check out information. When checking in, a welcome
message appears, as well as the date and time of check in.

An `Hours Previously Today: HH:MM`{.interpreted-text role="guilabel"}
field also appears, displaying any time that has already been logged for
that employee for the day. If no time has been logged, the value
displayed is: [00:00]{.title-ref}. Beneath the message is an
`OK`{.interpreted-text role="guilabel"} button.

To exit the screen before the preset time in the kiosk, tap the
`OK`{.interpreted-text role="guilabel"} button.

When checking out, the screen displays a goodbye message, with the date
and time of check out, and the total hours logged for the day. Beneath
the message is a `Goodbye`{.interpreted-text role="guilabel"} button. To
exit the screen before the preset time, tap the
`Goodbye`{.interpreted-text role="guilabel"} button.

{.align-center}
