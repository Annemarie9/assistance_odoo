# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/zebra.md

Zebra label configuration
=========================

In Odoo, labels printed in the Zebra Programming Language (ZPL) file
format are designed to fit a four-by-six inch label. To resize (or
reformat) text to fit a variety of
`ZPL (Zebra Programming Language)`{.interpreted-text role="abbr"} label
sizes,
`navigate to the ZPL label view <inventory/shipping_receiving/zpl-view>`{.interpreted-text
role="ref"}, and alter the
`ZPL (Zebra Programming Language)`{.interpreted-text role="abbr"} code.

::: {.warning}
::: {.title}
Warning
:::

When customizing code in Odoo, please note that upgrading the database
to newer versions may break custom
`ZPL (Zebra Programming Language)`{.interpreted-text role="abbr"} code.
**Customers are responsible for maintaining their custom code**.
:::

Refer to the following sections for explanations, and example code, for
frequently requested Zebra label customizations.

-   `Adjust margins <inventory/shipping_receiving/margin>`{.interpreted-text
    role="ref"}
-   `Enlarge/minimize barcodes <inventory/shipping_receiving/resize>`{.interpreted-text
    role="ref"}
-   `Rotate elements <inventory/shipping_receiving/rotate>`{.interpreted-text
    role="ref"}

Navigate to ZPL label view {#inventory/shipping_receiving/zpl-view}
--------------------------

To begin customizing a Zebra label in Odoo, turn on
`developer mode <developer-mode>`{.interpreted-text role="ref"}, and on
the main Odoo dashboard, type [Reports]{.title-ref}. From the search
results that appear in the resulting pop-up window, choose
`Settings / Technical / Reporting / Reports`{.interpreted-text
role="guilabel"} to open the `Reports`{.interpreted-text
role="guilabel"} page.

::: {.note}
::: {.title}
Note
:::

To manually navigate to the `Reports`{.interpreted-text role="guilabel"}
page, go to `Settings app -->
Technical --> Reporting: Reports`{.interpreted-text
role="menuselection"}.
:::

{.align-center}

On the `Reports`{.interpreted-text role="guilabel"} page, in the
`Search...`{.interpreted-text role="guilabel"} bar, type
[ZPL]{.title-ref}, and hit `Enter`{.interpreted-text role="kbd"}. Upon
doing so, Odoo presents a list of available Zebra labels in Odoo. Select
the desired Zebra label from the list to modify it on a separate page.

::: {.note}
::: {.title}
Note
:::

Printable ZPL labels in Odoo:

-   `lot/serial number <inventory/shipping_receiving/lot-sn-labels>`{.interpreted-text
    role="ref"}
-   operation type
-   package barcode
-   `product label <inventory/shipping_receiving/product-labels>`{.interpreted-text
    role="ref"}
-   product packaging
-   finished product (Odoo *Manufacturing* app required)
:::

Next, click the `fa-code`{.interpreted-text role="icon"}
`Qweb Views`{.interpreted-text role="guilabel"} smart button, and choose
the desired label
`view <../../../../../developer/reference/user_interface/view_records>`{.interpreted-text
role="doc"}.

![**Lot and Serial Number (ZPL)** report, highlighting the Qweb smart
button.](zebra/qweb-views.png){.align-center}

On the resulting view form, go to the `Architecture`{.interpreted-text
role="guilabel"} tab to view the
`ZPL (Zebra Programming Language)`{.interpreted-text role="abbr"} code.

::: {.important}
::: {.title}
Important
:::

To ensure the customization is **not** overwritten during an update,
click the `fa-bug`{.interpreted-text role="icon"}
`(bug)`{.interpreted-text role="guilabel"} icon on the view page. Then,
select the `View Metadata`{.interpreted-text role="guilabel"} option
from the resulting drop-down menu, in order to open the
`View Metadata`{.interpreted-text role="guilabel"} pop-up window. Then,
ensure the `No Update`{.interpreted-text role="guilabel"} field is set
to `true (change)`{.interpreted-text role="guilabel"}. Click
`Ok`{.interpreted-text role="guilabel"} to exit the
`View Metadata`{.interpreted-text role="guilabel"} pop-up window.
:::

{.align-center}

Adjust margin {#inventory/shipping_receiving/margin}
-------------

Text gets cut off from standard
`ZPL (Zebra Programming Language)`{.interpreted-text role="abbr"} labels
printed in Odoo when the line exceeds fifty-five characters. To fit long
product names, or lot numbers, on a single line, adjust the margin.

To begin, navigate to the
`ZPL code of the label <inventory/shipping_receiving/zpl-view>`{.interpreted-text
role="ref"} in the `Architecture`{.interpreted-text role="guilabel"}
tab. In the `ZPL (Zebra Programming Language)`{.interpreted-text
role="abbr"} code for product labels, look for the [\^FT]{.title-ref}
command, which specifies where to start placing the text, or graphic
element, on the label. The two numbers immediately following
[\^FT]{.title-ref} define the x-coordinate and y-coordinate in dots
(`similar to
pixels for printers`{.interpreted-text role="dfn"}) from the left and
top margins.

::: {.important}
::: {.title}
Important
:::

When customizing lot/serial number labels, look for the
[\^FO]{.title-ref} command, instead of [\^FT]{.title-ref}.
:::

::: {.example}
The following is an example where the product\'s name gets cut off with
Odoo\'s default `ZPL (Zebra Programming Language)`{.interpreted-text
role="abbr"} formatting. In the **Fixed** tab, the x-coordinate of the
starting position of the label is changed from [\^FT100,80]{.title-ref}
to [\^FT0,80]{.title-ref}, to fit the entire name.
:::

::: {.tabs}
::: {.tab}
Default

{.align-center}

**Code**:

``` {.xml}
^XA^CI28
^FT100,80^A0N,40,30^FD[E-COM11] Cabinet with Doors (wood: Cherry, handles: brass)^FS
...
^XZ
```
:::

::: {.tab}
Modified

{.align-center}

**Code**:

``` {.xml}
^XA^CI28
^FT0,80^A0N,40,30^FD[E-COM11] Cabinet with Doors (wood: Cherry, handles: brass)^FS
...
^XZ
```
:::
:::

Resize barcode {#inventory/shipping_receiving/resize}
--------------

To adjust the size of the barcode to scale, begin by navigating to the
`ZPL code of the label
<inventory/shipping_receiving/zpl-view>`{.interpreted-text role="ref"}
in the `Architecture`{.interpreted-text role="guilabel"} tab. Look for
the [\^FO]{.title-ref} command (typically in the third line), which is
the starting point of the margin for the barcode.

The [\^BY]{.title-ref} command configures barcode size, and takes three
numbers: bar width, width of wide bars relative to narrow bars, and bar
height. By default, `ZPL (Zebra Programming Language)`{.interpreted-text
role="abbr"} code in Odoo uses [\^BY3]{.title-ref}, setting the bar
width to three dots, a typical size that is easy for barcode scanners to
read.

::: {.example}
To shrink the barcode to scale, [\^BY3]{.title-ref} is reduced to
[\^BY2]{.title-ref}.
:::

::: {.tabs}
::: {.tab}
Default

{.align-center}

**Code**:

``` {.xml}
^XA^CI28
...
^FO100,160^BY3
...
^XZ
```
:::

::: {.tab}
Modified

{.align-center}

**Code**:

``` {.xml}
^XA^CI28
...
^FO100,160^BY2
...
^XZ
```
:::
:::

Rotate elements {#inventory/shipping_receiving/rotate}
---------------

To rotate elements in
`ZPL (Zebra Programming Language)`{.interpreted-text role="abbr"}, begin
by navigating to the `ZPL code of the label
<inventory/shipping_receiving/zpl-view>`{.interpreted-text role="ref"}
in the `Architecture`{.interpreted-text role="guilabel"} tab.

The [\^BC]{.title-ref} command\'s first parameter
(`information that affects the behavior of the command`{.interpreted-text
role="dfn"}) defines the rotation of an item, which can be:

-   \`N\`: display normally
-   \`R\`: rotate 90 degrees
-   \`I\`: rotate 180 degrees
-   \`B\`: rotate 270 degrees

::: {.example}
To rotate the barcode, [\^BCN]{.title-ref} is changed to
[\^BCB]{.title-ref}.
:::

::: {.tabs}
::: {.tab}
Default

{.align-center}

**Code**:

``` {.xml}
^XA^CI28
...
^BCN,100,Y,N,N
...
^XZ
```
:::

::: {.tab}
Modified

{.align-center}

**Code**:

``` {.xml}
^XA^CI28
...
^BCB,100,Y,N,N
...
^XZ
```
:::
:::
