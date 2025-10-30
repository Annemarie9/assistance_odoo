Ingenico
========

Connecting a payment terminal allows you to offer a fluid payment flow
to your customers and ease the work of your cashiers.

::: {.important}
::: {.title}
Important
:::

\- Ingenico payment terminals require an
`IoT system </applications/general/iot>`{.interpreted-text role="doc"}.
- Ingenico is currently only available in Belgium, the Netherlands and
Luxembourg. - Odoo works with the Ingenico Lane/, Desk/, and Move/
payment terminals as they support the TLV communication protocol through
TCP/IP.
:::

Configuration
-------------

### Connect an IoT system

Connecting an Ingenico payment terminal to Odoo is a feature that
requires an IoT system. For more information on how to connect an IoT
system to your database, please refer to the `IoT
documentation </applications/general/iot>`{.interpreted-text
role="doc"}.

### Configure the Lane/Desk/Move 5000 terminals for Ingenico BENELUX

1.  Press the function button (`F`{.interpreted-text role="guilabel"} on
    Lane/5000, `⦿`{.interpreted-text role="guilabel"} on Desk/5000 and
    Move/5000).
2.  Go to `Kassa menu --> Settings Menu`{.interpreted-text
    role="menuselection"} and enter the settings password (default:
    [2009]{.title-ref}).
3.  Select `Change Connection`{.interpreted-text role="guilabel"} and
    press `OK`{.interpreted-text role="guilabel"} on the next screen.
4.  Select `TCP/IP`{.interpreted-text role="guilabel"} and
    `IP-address`{.interpreted-text role="guilabel"}.
5.  On the next screen, enter the IP address of your IoT system.
6.  Enter [9000]{.title-ref} as port number and press
    `OK`{.interpreted-text role="guilabel"} on the next screen.

At this point, the terminal restarts and should be displayed on the IoT
system\'s form in Odoo.

{.align-center}

### Configure the payment method

Enable the payment terminal
`in the application settings <configuration/settings>`{.interpreted-text
role="ref"} and
`create the related payment method <../../payment_methods>`{.interpreted-text
role="doc"}. Set the journal type as `Bank`{.interpreted-text
role="guilabel"} and select `Ingenico`{.interpreted-text
role="guilabel"} in the `Use a Payment Terminal`{.interpreted-text
role="guilabel"} field. Then, select your terminal device in the
`Payment Terminal Device`{.interpreted-text role="guilabel"} field.



Once the payment method is created, you can select it in your POS
settings. To do so, go to the
`POS' settings <configuration/settings>`{.interpreted-text role="ref"},
click `Edit`{.interpreted-text role="guilabel"}, and add the payment
method under the `Payments`{.interpreted-text role="guilabel"} section.
