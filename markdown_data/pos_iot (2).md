IoT system connection
=====================

To connect the POS with an
`IoT system </applications/general/iot>`{.interpreted-text role="doc"}:

1.  Make sure both the Point of Sale and Internet of Things (IoT) apps
    are installed on your database.

2.  Set up the `/applications/general/iot/iot_box`{.interpreted-text
    role="doc"} or
    `/applications/general/iot/windows_iot`{.interpreted-text
    role="doc"}.

3.  Connect the peripheral devices to the IoT system:

      Device             Instructions
      ------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      Printer            Connect a supported receipt printer to a `USB (Universal Serial Bus)`{.interpreted-text role="abbr"} port or to the network, and power it on. Refer to `../restaurant/kitchen_printing`{.interpreted-text role="doc"}.
      Cash drawer        The cash drawer should be connected to the printer with an RJ25 cable.
      Barcode scanner    The barcode scanner must end barcodes with an [ENTER]{.title-ref} character (keycode 28) in order for the barcode scanner to be compatible. This is most likely the barcode scanner\'s default configuration.
      Scale              Connect the scale and power it on. Refer to `/applications/general/iot/devices/scale`{.interpreted-text role="doc"}.
      Customer display   Connect a screen to the `IoT (Internet of Things)`{.interpreted-text role="abbr"} box to display the `PoS
                         (Point of Sale)`{.interpreted-text role="abbr"} order. Refer to `/applications/general/iot/devices/screen`{.interpreted-text role="doc"}.
      Payment terminal   The connection process depends on the terminal. Refer to the `payment terminals
                         documentation </applications/sales/point_of_sale/payment_methods>`{.interpreted-text role="doc"}.

4.  `Connect the IoT system to your Odoo database </applications/general/iot/connect>`{.interpreted-text
    role="doc"}.

5.  `Access the POS settings <configuration/settings>`{.interpreted-text
    role="ref"} and select your POS, or click the vertical ellipsis
    button (`⋮`{.interpreted-text role="guilabel"}) on a POS card and
    click `Edit`{.interpreted-text role="guilabel"}. Scroll down to the
    `Connected Devices`{.interpreted-text role="guilabel"} section,
    enable `IoT Box`{.interpreted-text role="guilabel"}, then select the
    devices to be used for the POS. Click `Save`{.interpreted-text
    role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Click `IoT Devices`{.interpreted-text role="guilabel"} to access the
list of `/applications/general/iot/devices`{.interpreted-text
role="doc"} for your POS and view their connection status. Click a card
to access the device\'s form.
:::

::: {.seealso}
\- [List of supported
hardware](https://www.odoo.com/page/point-of-sale-hardware). -
`IoT documentation </applications/general/iot>`{.interpreted-text
role="doc"}
:::

Setup example {#pos/pos_iot/connect_schema}
-------------


