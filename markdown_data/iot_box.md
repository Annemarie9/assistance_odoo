# File: /content/odoo_doc17.0/fr/content/applications/general/iot/iot_box.md

IoT box
=======

To start using an IoT box:

1.  Make sure you have a
    `valid IoT box subscription <iot/iot/iot-subscription>`{.interpreted-text
    role="ref"} in addition to your Odoo subscription.
2.  Connect your `devices <devices>`{.interpreted-text role="doc"} to
    the IoT box.
3.  `Connect the IoT box to the network <iot/iot_box/network>`{.interpreted-text
    role="ref"}.
4.  `Connect the IoT box to your Odoo database <connect>`{.interpreted-text
    role="doc"}.

::: {.note}
::: {.title}
Note
:::

Devices can also be connected after the IoT box is added to the network
and/or connected to the database; however, a reboot of the IoT box might
be required.
:::

Network connection {#iot/iot_box/network}
------------------

The IoT box can be connected to the network via
`Ethernet <iot/iot_box/network-ethernet>`{.interpreted-text role="ref"}
or `Wi-Fi <iot/iot_box/network-wifi>`{.interpreted-text role="ref"}.

::: {.important}
::: {.title}
Important
:::

**All** devices must be connected to the **same network**: the IoT box,
the device(s) connected to the IoT box, and the computer connected to
Odoo.
:::

### Ethernet {#iot/iot_box/network-ethernet}

Plug the Ethernet cable into the IoT box\'s Ethernet port and an
available port on your router, then connect the IoT box to a power
source.

### Wi-Fi {#iot/iot_box/network-wifi}

Make sure no Ethernet cable is connected to the IoT box and follow these
steps:

> 1.  Connect the IoT box to a power source and wait a few minutes for
>     it to power on.
>
> 2.  Access your computer\'s Wi-Fi settings and select the IoT box\'s
>     network. The network name is in the format
>     [IoTBox-xxxxxxxxxxxx]{.title-ref} (where
>     [xxxxxxxxxxxx]{.title-ref} is a unique identifier).
>
> 3.  Connect to the IoT box\'s Wi-Fi network and sign into it; your
>     browser should automatically open and redirect to the
>     `IoT box's homepage <iot/iot-box/homepage>`{.interpreted-text
>     role="ref"}.
>
>     ::: {.note}
>     ::: {.title}
>     Note
>     :::
>
>     Depending on your operating system, the browser might not open and
>     redirect to the IoT box\'s homepage. In this case, open your
>     browser manually and navigate to [http://10.11.12.1]{.title-ref}.
>     :::
>
> 4.  On the IoT box\'s homepage, click `Configure`{.interpreted-text
>     role="guilabel"} next to the `Internet Status`{.interpreted-text
>     role="guilabel"} section.
>
> 5.  Wait a few minutes for the available networks to be scanned,
>     select the network, enter the Wi-Fi\'s password, and click
>     `Connect`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Once connected to the Wi-Fi network, the IoT box stops emitting its
Wi-Fi signal, and the computer should automatically reconnect to its
original network. If it does not, reconnect to it manually.
:::

IoT box homepage {#iot/iot-box/homepage}
----------------

To access the IoT box\'s homepage, open a web browser **on the same
network as the IoT box** and navigate to the IoT box\'s IP address.



The IoT box\'s IP address can be retrieved by:

-   connecting the IoT box to an external monitor: the IP address is
    displayed on the screen.

    

-   connecting the IoT box to a printer: the IP address is automatically
    printed.

-   accessing the administrator interface of the router to which the IoT
    box is connected or using third-party software to scan the network.

Once the IoT box is
`connected to the Odoo database <connect>`{.interpreted-text
role="doc"}, its homepage can be accessed from Odoo by opening the IoT
app and clicking the URL displayed on the IoT box\'s card.
