# File: /content/odoo_doc17.0/fr/content/applications/general/iot/devices/printer.md

Connect a printer
=================

Printer installation can be done in a few easy steps. The printer can be
used to print receipts, labels, orders, or even reports from the
different Odoo apps. In addition, printer actions can be assigned as an
*action on a trigger* during the manufacturing process, or added onto a
quality control point or a quality check.

::: {.warning}
::: {.title}
Warning
:::

The **only** way to connect a printer directly to an Odoo database is
through the use of an IoT system. Without an IoT system, printing can
still occur, but it is managed through the printer itself, which is not
the recommended process.
:::

Connection
----------

IoT systems support printers connected through USB, network connection,
or Bluetooth. [Supported
printers](https://www.odoo.com/page/iot-hardware) are detected
automatically, and appear in the `Devices`{.interpreted-text
role="guilabel"} list of the IoT app.



::: {.note}
::: {.title}
Note
:::

Printers can take up to two minutes to appear in the IoT app
`Devices`{.interpreted-text role="guilabel"} list.
:::

Link a printer
--------------

### Link work orders to a printer

Work orders can be linked to printers, via a quality control point, to
print labels for manufactured products.

In the
`Quality app </applications/inventory_and_mrp/quality>`{.interpreted-text
role="doc"}, a device can be set up on a quality control point. To do
so, go to the `Quality --> Quality Control --> Control
Points`{.interpreted-text role="menuselection"}, and open the desired
control point.

::: {.important}
::: {.title}
Important
:::

A manufacturing operation and work order operation need to be attached
to a quality control point before the `Type`{.interpreted-text
role="guilabel"} field allows for the `Print Label`{.interpreted-text
role="guilabel"} option to be selected.
:::

From here, edit the control point by selecting the
`Type`{.interpreted-text role="guilabel"} field, and selecting
`Print Label`{.interpreted-text role="guilabel"} from the dropdown menu
of options. Doing so reveals the `Device`{.interpreted-text
role="guilabel"} field, where the attached device can be selected.

The printer can now be used with the selected quality control point.
When the quality control point is reached during the manufacturing
process, the database presents the option to print labels for a specific
product.

::: {.tip}
::: {.title}
Tip
:::

Quality control points can also be accessed by navigating to `IoT -->
Devices`{.interpreted-text role="menuselection"}, then selecting the
device. Go to the `Quality Control Points`{.interpreted-text
role="guilabel"} tab to add them to the device.
:::

::: {.note}
::: {.title}
Note
:::

On a `quality check form
</applications/inventory_and_mrp/quality/quality_management/quality_checks>`{.interpreted-text
role="doc"}, the `Type`{.interpreted-text role="guilabel"} of check can
also be set to `Print Label`{.interpreted-text role="guilabel"}.
:::

::: {.seealso}
\-
`/applications/inventory_and_mrp/quality/quality_management/quality_control_points`{.interpreted-text
role="doc"} -
`/applications/inventory_and_mrp/quality/quality_management/quality_alerts`{.interpreted-text
role="doc"}
:::

### Link reports to a printer {#iot/link-printer}

It is possible to link report types to a specific printer. To do so:

1.  Go to `IoT --> Devices`{.interpreted-text role="menuselection"} and
    select the desired printer.
2.  Go to the `Printer Reports`{.interpreted-text role="guilabel"} tab
    and click `Add a line`{.interpreted-text role="guilabel"}.
3.  In the pop-up that opens, select the types of reports to be linked
    to the printer and click `Select`{.interpreted-text
    role="guilabel"}.



::: {.tip}
::: {.title}
Tip
:::

Reports can also be configured by
`enabling the developer mode <developer-mode>`{.interpreted-text
role="ref"} and going to
`Settings --> Technical --> Reports`{.interpreted-text
role="menuselection"}. Select the desired report from the list and set
an `IoT Device`{.interpreted-text role="guilabel"}.
:::

The first time a linked report is selected to print, a
`Select Printers`{.interpreted-text role="guilabel"} pop-up window
appears. Tick the checkbox next to the correct printer for the report,
and click `Print`{.interpreted-text role="guilabel"}. At that point, the
report is linked to the printer.

#### Clear device printer cache

After a printer is linked to print a report, the setting is saved in a
browser\'s cache. This means a user can have different devices saved in
their cache for different reports, based on the device they use to
access Odoo. It also means different users can have a report
automatically printed from different printers, based on their
preferences.

To unlink a report from a printer, navigate to
`IoT --> Configuration --> Reset
Linked Printers`{.interpreted-text role="menuselection"}. This generates
a list of reports that are linked to a printer on the current device.
Click the `Unlink`{.interpreted-text role="guilabel"} button next to
each report to remove the link.

::: {.important}
::: {.title}
Important
:::

This step **only** prevents the report from automatically printing to
the listed printer from the current browser. The report is still
`linked <iot/link-printer>`{.interpreted-text role="ref"} on the device,
under the `Printer Reports`{.interpreted-text role="guilabel"} tab.
:::



::: {.seealso}
`POS Order Printing <../../../sales/point_of_sale/restaurant/kitchen_printing>`{.interpreted-text
role="doc"}
:::

Potential issues
----------------

### The printer is not detected

If a printer does not appear in the devices list, go to the
`IoT box's <iot/iot-box/homepage>`{.interpreted-text role="ref"} or
`Windows virtual IoT's <iot/windows-iot/homepage>`{.interpreted-text
role="ref"} homepage, click `Show`{.interpreted-text role="guilabel"} in
the `Devices`{.interpreted-text role="guilabel"} section, and make sure
the printer is listed.

If the printer does not appear on the IoT system\'s homepage, click
`Printer Server`{.interpreted-text role="guilabel"}, then
`Administration`{.interpreted-text role="guilabel"}, and
`Add Printer`{.interpreted-text role="guilabel"}. If the printer is not
in the list, it is likely not connected properly.

### The printer outputs random text

For most printers, the correct driver should be automatically detected
and selected. However, in some cases, the automatic detection mechanism
might not be enough, and if no driver is found, the printer might print
random characters.

The solution is to manually select the corresponding driver. On the IoT
system\'s homepage, click `Printer Server`{.interpreted-text
role="guilabel"}, then `Printers`{.interpreted-text role="guilabel"},
and select the printer in the list. In the
`Administration`{.interpreted-text role="guilabel"} dropdown menu, click
`Modify Printer`{.interpreted-text role="guilabel"}. Follow the steps
and select the printer\'s *make* and *model*.



::: {.note}
::: {.title}
Note
:::

Epson receipt printers and Zebra label printers do not need a driver to
work. Make sure that no driver is selected for those printers.
:::

### The printer is detected but is not recognized correctly

If Odoo and the IoT system do not recognize the printer correctly, go to
`IoT
--> Devices`{.interpreted-text role="menuselection"}, click the
device\'s card to access its form, and set the
`Subtype`{.interpreted-text role="guilabel"} field to the appropriate
option: `Receipt Printer`{.interpreted-text role="guilabel"},
`Label Printer`{.interpreted-text role="guilabel"}, or `Office
Printer`{.interpreted-text role="guilabel"}.

#### Epson configuration special case

Most Epson printers support printing receipts in Odoo Point of Sale
using the [GS v 0]{.title-ref} command. However, the following Epson
printer models do not support this command:

-   TM-U220
-   TM-U230
-   TM-P60
-   TMP-P60II

To bypass this issue, you can configure the printer to use the [ESC
\*]{.title-ref} command.

First, review Epson\'s website for compatibility for both the [GS v
0](https://download4.epson.biz/sec_pubs/pos/reference_en/escpos/gs_lv_0.html)
and [ESC
\*](https://download4.epson.biz/sec_pubs/pos/reference_en/escpos/esc_asterisk.html)
commands.

If the printer is incompatible with [GS v 0]{.title-ref} but supports
[ESC \*]{.title-ref}, configure the IoT system to use the [ESC
\*]{.title-ref} command as follows:

1.  Access the `IoT box's <iot/iot-box/homepage>`{.interpreted-text
    role="ref"} or `Windows virtual IoT's
    <iot/windows-iot/homepage>`{.interpreted-text role="ref"} homepage.

2.  Click the `Printer server`{.interpreted-text role="guilabel"}
    button, then click `Administration`{.interpreted-text
    role="guilabel"} on the CUPS page.

3.  Click `Add Printer`{.interpreted-text role="guilabel"} in the
    `Printers`{.interpreted-text role="guilabel"} section, select the
    printer, and click `Continue`{.interpreted-text role="guilabel"}.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    If the printer\'s name is still uncertain, take the following steps:

    1.  Take note of the listed printers on the CUPS page.
    2.  Turn the printer off and refresh the page.
    3.  Compare the difference with the first list to see which printer
        disappeared.
    4.  Turn the printer back on and refresh the page again.
    5.  Double-check the list again to see if the printer re-appears.
    6.  The printer that disappeared and reappears again on the listed
        printers is the name of the printer in question. It can be
        `Unknown`{.interpreted-text role="guilabel"} under
        `Local printers`{.interpreted-text role="guilabel"}.
    :::

4.  On the `Add Printer`{.interpreted-text role="guilabel"} page,
    specify the printer\'s `Name`{.interpreted-text role="guilabel"}
    using the following convention:
    [\<printer\_name\>\_\_IMC\_\<param\_1\>\_\<param\_2\>\_\...\_\<param\_n\>\_\_]{.title-ref},
    where:

    -   [printer\_name]{.title-ref} is the printer\'s name. It can
        contain any character except [\_]{.title-ref}, [/]{.title-ref},
        [\#]{.title-ref}, or [ ]{.title-ref} (space character).

    -   \`IMC\`: This stands for *Image Mode Column* (the simplified
        name for [ESC \*]{.title-ref}).

    -   \`param\_1\`: This stands for the specific parameter:

        -   \`SCALE\<X\>[: Scale of the picture (with the same aspect
            ratio). \`X]{.title-ref} should be an integer describing the
            scale percentage that should be used. For example,
            [100]{.title-ref} is the original size, [50]{.title-ref} is
            half the size, and [200]{.title-ref} is twice the size.
        -   \`LDV\`: *Low Density Vertical* (will be set to *High
            Density Vertical* if not specified).
        -   \`LDH\`: *Low Density Horizontal* (will be set to *High
            Density Horizontal* if not specified).

        ::: {.note}
        ::: {.title}
        Note
        :::

        \- *Density* parameters might need to be configured in a
        particular way, depending on the printer model.
        \- Refer to [Epson\'s ESC \*
        documentation](https://download4.epson.biz/sec_pubs/pos/reference_en/escpos/esc_asterisk.html)
        to determine if the printer requires these parameters to be set.
        :::

    > ::: {.example}
    > The following are examples of proper and improper name formatting:
    >
    > Proper name formatting:
    >
    > -   [EPSONTMm30II\_\_IMC\_\_]{.title-ref}
    > -   [EPSON\_TM\_U220\_\_IMC\_LDV\_LDH\_SCALE80\_\_]{.title-ref}
    >
    > Improper name formatting (this will not prevent printing, but the
    > result might not have the expected printed output):
    >
    > -   \`EPSON TMm 30II\`: The name cannot contain spaces.
    > -   \`EPSONTMm30II\`: The name itself is correct, but it will not
    >     use [ESC \*]{.title-ref}.
    > -   \`EPSONTMm30II\_\_IMC\`: This name is missing the end
    >     [\_\_]{.title-ref}.
    > -   \`EPSONTMm30II\_\_IMC\_XDV\_\_[: The parameter
    >     \`XDV]{.title-ref} does not match any existing parameters.
    > -   \`EPSONTMm30II\_\_IMC\_SCALE\_\_[: The parameter
    >     \`SCALE]{.title-ref} is missing the scale value.
    > :::

5.  Once the printer\'s name has been defined using the appropriate
    naming convention, click `Continue`{.interpreted-text
    role="guilabel"}.

6.  Set the `Make`{.interpreted-text role="guilabel"} value to
    `Raw`{.interpreted-text role="guilabel"} and the
    `Model`{.interpreted-text role="guilabel"} value to
    `Raw Queue (en)`{.interpreted-text role="guilabel"}.

7.  Click `Add Printer`{.interpreted-text role="guilabel"}. If
    everything was done correctly, the page should redirect to the
    `Banners`{.interpreted-text role="guilabel"} page.

8.  Wait a few minutes for the IoT system to detect the printer and sync
    to Odoo\'s server.

9.  `Access the POS settings <configuration/settings>`{.interpreted-text
    role="ref"} and select your POS, or click the vertical ellipsis
    button (`⋮`{.interpreted-text role="guilabel"}) on a POS card and
    click `Edit`{.interpreted-text role="guilabel"}. Scroll down to the
    `Connected Devices`{.interpreted-text role="guilabel"} section,
    enable `IoT Box`{.interpreted-text role="guilabel"}, and select the
    printer in the `Receipt Printer`{.interpreted-text role="guilabel"}
    field. Click `Save`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

If the printer was set up incorrectly (e.g., it continues to print
random text, or the printed receipt is too large or too small), it
cannot be modified via the printer\'s name in CUPS. Instead, configure a
new printer from scratch with modified parameters, following the steps
above.
:::

::: {.spoiler}
Example

The following is an example of the troubleshooting process for a
TM-U220B printer model using the [ESC \*]{.title-ref} command. The
receipt pictured below is an example of a receipt that is printing
correctly due to proper formatting (in theory):



Printing this receipt immediately without proper formatting will not
work, as the TM-U220B printer model does not support the [GS v
0]{.title-ref} command. Instead, random characters will be printed:



To properly configure formatting for the Epson TM-U220B printer model,
follow these steps:

1.  After checking Epson\'s website for compatibility with both the [GS
    v
    0](https://download4.epson.biz/sec_pubs/pos/reference_en/escpos/gs_lv_0.html)
    and
    
    commands, the TM-U220B printer is indeed incompatible with [GS v
    0]{.title-ref} but supports [ESC \*]{.title-ref}.

    

2.  When adding the printer, CUPS displays the list of available
    printers:

    

    In this case, the printer is connected via USB, so it is not part of
    the `Discovered Network Printers`{.interpreted-text
    role="guilabel"}. Instead, it is likely part of the
    `Unknown`{.interpreted-text role="guilabel"} selection under
    `Local Printers`{.interpreted-text role="guilabel"}. By unplugging
    the printer\'s USB cable from the IoT system and refreshing the
    page, the `Unknown`{.interpreted-text role="guilabel"} printer
    disappears. By plugging it back in, the printer reappears.

3.  For the naming convention, since the printer must print using the
    [ESC \*]{.title-ref} command, it is imperative to add
    [\_\_IMC]{.title-ref}.

    

    For this particular model (TM-U220) [m]{.title-ref} should be equal
    to 0 or 1. While referencing the `Description`{.interpreted-text
    role="guilabel"} table on [Epson\'s ESC \*
    website](https://download4.epson.biz/sec_pubs/pos/reference_en/escpos/esc_asterisk.html),
    the [m]{.title-ref} values could be 0, 1, 32, or 33. So, in this
    case, the [m]{.title-ref} value **cannot** be 32 or 33 (otherwise,
    random characters will be printed).

    The table includes the numeric values 32 and 33; they both occur if
    the `Number of
    bits for vertical data`{.interpreted-text role="guilabel"} is set to
    24, i.e. it has a *High Vertical Density*. In the case of
    configuring the Epson TM-U220, the *Low Vertical Density* will need
    to be forced, as this printer model does not support *High Vertical
    Density* for this command [ESC \*]{.title-ref}.

    To add a *Low Vertical Density*, add the [LDV]{.title-ref} parameter
    to the naming convention.

    

4.  Click `Continue`{.interpreted-text role="guilabel"} to proceed.
    Next, set the `Make`{.interpreted-text role="guilabel"} value to
    `Raw`{.interpreted-text role="guilabel"} and the
    `Model`{.interpreted-text role="guilabel"} value to
    `Raw Queue (en)`{.interpreted-text role="guilabel"}.

    

    However, when trying to print with the naming convention
    [EpsonTMU220B\_\_IMC\_LDV\_\_]{.title-ref}, the receipt is printed,
    but it is too large and outside the margin. To resolve this, add a
    new printer (and naming convention) with the
    [SCALE\<X\>]{.title-ref} parameter to adapt to the receipt\'s size.

    Here are some examples:

      Printer Naming Convention                                 [EpsonTMU220B\_\_IMC\_LDV\_\_]{.title-ref}                                                          [EpsonTMU220B\_\_IMC\_LDV\_SCALE75\_\_]{.title-ref}                                                                  [EpsonTMU220B\_\_IMC\_LDV\_LDH\_\_]{.title-ref}                                                              [EpsonTMU220B\_\_IMC\_LDV\_LDH\_SCALE35\_\_]{.title-ref}
      --------------------------------------------------------- --------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------
                  
:::

### DYMO LabelWriter print issue

The DYMO LabelWriter has a known issue in printing with IoT systems. The
OpenPrinting CUPS server installs the printer using
`Local RAW Printer`{.interpreted-text role="guilabel"} drivers. In order
to print anything, the correct `Make and Model`{.interpreted-text
role="guilabel"} needs to be set to reference the correct driver when
using the device.

Additionally, a new printer needs to be added to reduce the print delay
that occurs after updating the driver.

::: {.important}
::: {.title}
Important
:::

The DYMO LabelWriter 450 DUO printer is the recommended DYMO printer for
use with Odoo and IoT systems. This device combines two printers: a
label printer and a tape printer. When configuring the following
processes, it is essential to select the correct model (either DYMO
LabelWriter 450 DUO Label (en) or DYMO LabelWriter 450 DUO Tape (en)).
For consistency, the following processes outline configuration steps for
the DYMO LabelWriter 450 DUO Label (en) model. Adjust the model
selections as needed.
:::

#### DYMO LabelWriter not printing {#printer/dymo/update_drivers}

If the DYMO LabelWriter fails to print, install a new driver:

1.  Access the IoT system\'s homepage and click
    `Printer server`{.interpreted-text role="menuselection"} to open the
    OpenPrinting CUPS console.

2.  Click `Printers`{.interpreted-text role="menuselection"} in the top
    menu, then click the printer in the list.

3.  Select `Maintenance`{.interpreted-text role="guilabel"} in the first
    dropdown menu.

4.  Select `Modify Printer`{.interpreted-text role="guilabel"} in the
    second dropdown menu.

    ![Modify the make and model of the DYMO LabelWriter. Maintenance and Modify dropdown
    menus highlighted.](printer/main-modify.png)

5.  Select the specific network connection/printer on which the
    modification should be made and click `Continue`{.interpreted-text
    role="guilabel"}.

6.  On the next page, click `Continue`{.interpreted-text
    role="guilabel"}, then select `DYMO`{.interpreted-text
    role="guilabel"} from the `Make`{.interpreted-text role="guilabel"}
    dropdown list.

7.  Click on `Continue`{.interpreted-text role="guilabel"} and set the
    `Model`{.interpreted-text role="guilabel"} to `DYMO LabelWriter 450
    DUO Label (en)`{.interpreted-text role="guilabel"} (or whichever
    DYMO printer model is being used).

8.  Click `Modify Printer`{.interpreted-text role="guilabel"} to set the
    new driver; a confirmation page appears.

9.  Click `Printers`{.interpreted-text role="menuselection"} in the top
    menu; all printers installed on the OpenPrinting CUPS server appear,
    including the newly updated
    `DYMO LabelWriter 450 DUO Label`{.interpreted-text role="guilabel"}
    (or whichever DYMO printer model is being used).

10. Click the newly updated printer, then click the
    `Maintenance`{.interpreted-text role="guilabel"} dropdown menu and
    select `Print Test Page`{.interpreted-text role="guilabel"} to print
    a test label. The test label is printed after a few seconds if the
    driver update was successful.

To reduce this delay, add a new printer using the steps below.

#### DYMO LabelWriter print delay

::: {.tip}
::: {.title}
Tip
:::

If the DYMO LabelWriter 450 DUO printer is not printing at all, or is
not recognized (i.e., it has a `RAW`{.interpreted-text role="guilabel"}
driver type), then `update the drivers on the device
<printer/dymo/update_drivers>`{.interpreted-text role="ref"}.
:::

To resolve the delay issue after modifying the driver, reinstall the
printer:

1.  Access the IoT system\'s homepage and click
    `Printer server`{.interpreted-text role="menuselection"} to open the
    OpenPrinting CUPS console.

2.  Click `Administration`{.interpreted-text role="menuselection"} in
    the top menu, then click `Add a Printer`{.interpreted-text
    role="guilabel"}.

3.  On the next page, in the `Local Printers`{.interpreted-text
    role="guilabel"} section, select `DYMO
    LabelWriter 450 DUO Label (DYMO LabelWriter 450 DUO Label)`{.interpreted-text
    role="guilabel"} (or whichever DYMO printer model is being used)
    pre-installed printer. Click `Continue`{.interpreted-text
    role="guilabel"}.

    ![Add a printer screen on OpenPrinting CUPS with DYMO LabelWriter 450 DUO Label
    highlighted.](printer/local-printer.png)

4.  On the following screen, update the `Name`{.interpreted-text
    role="guilabel"} to something easily identifiable, as the original
    printer will remain in the list. Then, click
    `Continue`{.interpreted-text role="guilabel"}.

    

5.  Set the `Model`{.interpreted-text role="guilabel"} field to
    `DYMO LabelWriter 450 DUO Label (en)`{.interpreted-text
    role="guilabel"} (or whichever DYMO printer model is being used),
    then click `Add Printer`{.interpreted-text role="guilabel"} to
    complete the installation.

    ![Choose model screen on the OpenPrinting CUPS console with model and add a printer
    highlighted.](printer/choose-printer.png)

6.  Click `Printers`{.interpreted-text role="menuselection"} in the top
    menu and click the newly installed printer
    `DYMO LabelWriter 450 DUO Label`{.interpreted-text role="guilabel"}
    (or whichever DYMO printer model is being used) from in the list.

    

7.  Click the `Maintenance`{.interpreted-text role="guilabel"} dropdown
    list and select `Print Test Page`{.interpreted-text role="guilabel"}
    to print a test label. The test label should print out immediately,
    or after one or two seconds.

### The Zebra printer does not print anything

Zebra printers are quite sensitive to the format of the printed Zebra
Programming Language (ZPL) code. If nothing comes out of the printer or
blank labels are printed, try changing the format of the report sent to
the printer. To do so, activate the
`developer mode <developer-mode>`{.interpreted-text role="ref"}, go to
`Settings --> Technical --> User Interface --> Views`{.interpreted-text
role="menuselection"}, and search for the corresponding template.

::: {.seealso}
[Zebra\'s instructions on printing ZPL
files](https://supportcommunity.zebra.com/s/article/Print-a-zpl-file-using-the-Generic-Text-Printer)
:::

### The printer appears multiple times

If the printer appears multiple times on the
`IoT box's <iot/iot-box/homepage>`{.interpreted-text role="ref"} or
`Windows virtual IoT's <iot/windows-iot/homepage>`{.interpreted-text
role="ref"} homepage and/or in the list of `Devices`{.interpreted-text
role="guilabel"} on the
`IoT system's form <iot/connect/IoT-form>`{.interpreted-text
role="ref"}, the cause is usually the CUPS auto-discovery feature. This
feature allows to list all detected printers together with all available
drivers, creating one entry for each printer--driver pair.

Simply select the entry that works best and ignore the others.

::: {.note}
::: {.title}
Note
:::

Workarounds exist to disable the CUPS auto-discovery feature.
:::

Barcode scanner issues
----------------------

### The characters read by the barcode scanner do not match the barcode

By default, most barcode scanners are configured in the US QWERTY
format. If the barcode scanner uses a different layout, go to
`IoT --> Devices`{.interpreted-text role="menuselection"} and click the
barcode device\'s card. Then, select the correct language in the
`Keyboard Layout`{.interpreted-text role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

The `Keyboard Layout`{.interpreted-text role="guilabel"} is
language-specific, with available options varying based on the device
and the language of the database (e.g., `English (UK)`{.interpreted-text
role="guilabel"}, `English
(US)`{.interpreted-text role="guilabel"}, etc.).
:::

### Nothing happens when a barcode is scanned

Make sure the correct device is selected in the `Point of Sale settings
</applications/sales/point_of_sale/configuration/pos_iot>`{.interpreted-text
role="doc"} (when applicable) and the barcode is configured to send an
[ENTER]{.title-ref} character (keycode 28) at the end of every barcode.

### The barcode scanner is detected as a keyboard

::: {.important}
::: {.title}
Important
:::

Some barcode scanners are identified as USB keyboards rather than
barcode scanners and are not recognized by IoT systems.
:::

To change the device type manually, go to
`IoT --> Devices`{.interpreted-text role="menuselection"} and click the
barcode device\'s card. Then, enable `Is scanner`{.interpreted-text
role="guilabel"}.

### The barcode scanner processes barcode characters individually

When accessing the mobile version of Odoo from a mobile device or tablet
paired with a barcode scanner via the IoT system, the scanner might
interpret each character in a barcode as a separate scan. To resolve
this, go to `IoT --> Devices`{.interpreted-text role="menuselection"}
and click the barcode device\'s card. Then, select the correct language
in the `Keyboard Layout`{.interpreted-text role="guilabel"} field.

::: {.note}
::: {.title}
Note
:::

The `Keyboard Layout`{.interpreted-text role="guilabel"} is
language-specific, with available options varying based on the device
and the language of the database (e.g., `English (UK)`{.interpreted-text
role="guilabel"}, `English
(US)`{.interpreted-text role="guilabel"}, etc.).
:::
