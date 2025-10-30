# File: /content/odoo_doc17.0/fr/content/applications/general/iot/devices/scale.md

Connect a scale
===============

::: {.important}
::: {.title}
Important
:::

\- In EU member states, [certification is legally
required](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.096.01.0107.01.ENG)
to use a scale as an integrated device. - Odoo is not certified in
several countries, including France, Germany, and Switzerland. If you
reside in one of these countries, you can still use a scale but without
integration into your Odoo database. Alternatively, you can acquire a
*non-integrated* certified scale that prints certified labels, which can
then be scanned into your Odoo database.
:::

To connect a scale to the IoT system, use a USB cable. In some cases,
you may need a serial-to-US adapter to complete the connection. If the
scale is [compatible with an IoT
system](https://www.odoo.com/page/iot-hardware), no additional setup is
required; the scale is automatically detected as soon as it is
connected. If the scale is not detected, reboot the IoT box or
`restart the Windows virtual IoT service <iot/windows_iot/restart>`{.interpreted-text
role="ref"} and `update the
scale's drivers <iot_updating_iot/handlers>`{.interpreted-text
role="ref"}.

::: {.note}
::: {.title}
Note
:::

If the scale still does not function after updating the drivers, it
might not be [compatible with the Odoo IoT
system](https://www.odoo.com/page/iot-hardware). In such cases, a
different scale must be used.
:::

Once the scale is connected to the IoT system, follow these steps to
configure it in the POS settings:

1.  `Access the POS settings <configuration/settings>`{.interpreted-text
    role="ref"} and select your POS, or click the vertical ellipsis
    button (`⋮`{.interpreted-text role="guilabel"}) on a POS card and
    click `Edit`{.interpreted-text role="guilabel"}.
2.  Scroll down to the `Connected Devices`{.interpreted-text
    role="guilabel"} section and enable `IoT Box`{.interpreted-text
    role="guilabel"}.
3.  Select the scale in the `Electronic Scale`{.interpreted-text
    role="guilabel"} field.
4.  Click `Save`{.interpreted-text role="guilabel"}.

::: {.seealso}
`Connect an IoT system to a POS </applications/sales/point_of_sale/configuration/pos_iot>`{.interpreted-text
role="doc"}
:::

The scale is then available in all the
`POS's sessions </applications/sales/point_of_sale>`{.interpreted-text
role="doc"}. If a product is configured with a price per weight,
selecting it on the `PoS screen`{.interpreted-text role="guilabel"}
opens the scale popup. The cashier can then weigh the product to
automatically add the correct price to the cart.



Ariva S scales
--------------

For Ariva S series scales (manufactured by Mettler-Toledo, LLC.) to
function with IoT systems, a specific setting must be modified, and a
dedicated Mettler USB-to-proprietary RJ45 cable is required.

::: {.important}
::: {.title}
Important
:::

The official Mettler USB-to-RJ45 cable (Mettler part number 72256236)
must be used. Contact Mettler or a partner to purchase an authentic
cable. **No other** cable works for this configuration.
:::

To configure the Ariva S scale for IoT system recognition, refer to page
17 of [Mettler\'s Setup Guide for Ariva S series
scales](https://www.mt.com/dam/RET_DOCS/Ariv.pdf) and follow these
steps:

1.  Hold the **\>T\<** button for eight seconds, or until
    `CONF`{.interpreted-text role="guilabel"} appears.

2.  Press **\>T\<** until `GRP 3`{.interpreted-text role="guilabel"}
    appears, then press **\>0\<** to confirm.

3.  At step `3.1`{.interpreted-text role="guilabel"}, make sure the
    value is set to `1`{.interpreted-text role="guilabel"} (USB Virtual
    COM ports) by pressing **\>T\<** to cycle through the options.

4.  Press **\>0\<** until `3.6`{.interpreted-text role="guilabel"} (if
    available, otherwise skip the next step).

5.  At step `3.6`{.interpreted-text role="guilabel"}, make sure the
    value is set to `3`{.interpreted-text role="guilabel"} (8217
    Mettler-Toledo (WO)) by pressing **\>T\<** to cycle through the
    options.

6.  Press **\>0\<** (multiple times if necessary) until
    `GRP 4`{.interpreted-text role="guilabel"} appears.

7.  Press **\>T\<** until `EXIT`{.interpreted-text role="guilabel"}
    appears.

    ::: {.important}
    ::: {.title}
    Important
    :::

    Do **not** make any other changes unless otherwise needed.
    :::

8.  Press **\>0\<**.

9.  Press **\>0\<** again to `SAVE`{.interpreted-text role="guilabel"};
    the scale restarts.

10. Reboot the IoT box or
    `restart the Windows virtual IoT service <iot/windows_iot/restart>`{.interpreted-text
    role="ref"}. The scale should then appear as [Toledo
    8217]{.title-ref}, as opposed to the previous display, where it
    appeared as [Adam Equipment Serial]{.title-ref}.
