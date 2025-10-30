Worldline
=========

Connecting a payment terminal allows you to offer a fluid payment flow
to your customers and ease the work of your cashiers.

::: {.important}
::: {.title}
Important
:::

\- Worldline payment terminals require an
`IoT Box </applications/general/iot>`{.interpreted-text role="doc"}. -
Worldline is currently only available in Belgium, the Netherlands and
Luxembourg. - Odoo is compatible with Worldline terminals that use the
CTEP protocol (e.g., the Yomani XR and Yoximo terminals). If you have
any doubts, contact your payment provider to ensure your terminal\'s
compatibility.
:::

Configuration
-------------

### Connect an IoT system

Connecting a Worldline Payment Terminal to Odoo is a feature that
requires an IoT system. For more information on how to connect one to
your database, please refer to the
`IoT documentation </applications/general/iot>`{.interpreted-text
role="doc"}.

### Configure the protocol

From your terminal, click on
`"." --> 3 --> stop --> 3 --> 0 --> 9`{.interpreted-text
role="menuselection"}. Enter the technician password **\"1235789\"** and
click on `OK --> 4 --> 2`{.interpreted-text role="menuselection"}. Then,
click on `Change --> CTEP (as Protocole ECR) --> OK`{.interpreted-text
role="menuselection"}. Click on **OK** thrice on the subsequent screens
(*CTEP ticket ECR*, *ECR ticket width*, and *Character set*). Finally,
press **Stop** three times; the terminal automatically restarts.

### Set the IP address

From your terminal, click on
`"." --> 3 --> stop --> 3 --> 0 --> 9`{.interpreted-text
role="menuselection"}. Enter the technician password **\"1235789\"** and
click on `OK --> 4 --> 9`{.interpreted-text role="menuselection"}. Then,
click on `Change --> TCP/IP`{.interpreted-text role="menuselection"}
(*TCP physical configuration* screen) `--> OK -->
OK`{.interpreted-text role="menuselection"} (*TCP Configuration client*
screen).

Finally, set up the hostname and port number.

#### Hostname

| To set up the hostname, enter your IoT system\'s IP address\' sequence
  numbers and press **OK** at each \".\" until you reach the colon
  symbol.
| Then, press **OK** twice.

::: {.example}
\| Here\'s an IP address sequence: [10.30.19.4:8069]{.title-ref}. \| On
the *Hostname screen*, type `10 --> OK --> 30 --> OK --> 19 --> OK --> 4
--> OK --> OK`{.interpreted-text role="menuselection"}.
:::

::: {.tip}
::: {.title}
Tip
:::

Your IoT system\'s IP address is available on the
`IoT system's card in the IoT app
<iot/connect/IoT-form>`{.interpreted-text role="ref"}.
:::

#### Port number

On the *Port number* screen, enter **9001** (or **9050** for Windows)
and click on `OK`{.interpreted-text role="menuselection"} (*ECR protocol
SSL no*) `--> OK`{.interpreted-text role="menuselection"}. Click on
**Stop** three times; the terminal automatically restarts.

::: {.warning}
::: {.title}
Warning
:::

For the
`Windows virtual IoT </applications/general/iot>`{.interpreted-text
role="doc"}, the [9050]{.title-ref} port must be added as a
`Windows Firewall exception <iot/windows-iot/firewall>`{.interpreted-text
role="ref"}.
:::

### Configure the payment method

Enable the payment terminal
`in the application settings <configuration/settings>`{.interpreted-text
role="ref"} and
`create the related payment method <../../payment_methods>`{.interpreted-text
role="doc"}. Set the journal type as `Bank`{.interpreted-text
role="guilabel"} and select `Worldline`{.interpreted-text
role="guilabel"} in the `Use a Payment Terminal`{.interpreted-text
role="guilabel"} field. Then, select your terminal device in the
`Payment Terminal Device`{.interpreted-text role="guilabel"} field.



Once the payment method is created, you can select it in your POS
settings. To do so, go to the
`POS' settings <configuration/settings>`{.interpreted-text role="ref"},
click `Edit`{.interpreted-text role="guilabel"}, and add the payment
method under the `Payments`{.interpreted-text role="guilabel"} section.

::: {#worldline/yomani-info}
::: {.tip}
::: {.title}
Tip
:::

\- Technician password: [1235789]{.title-ref} - To reach Wordline\'s
technical assistance, call [02 727 61 11]{.title-ref} and choose
\"merchant\". Your call is automatically transferred to the desired
service. - Configure the cashier terminal if you have both a customer
and a cashier terminal. - To avoid blocking the terminal, check the
initial configuration beforehand. - Set a fixed IP to your IoT Box's
router to prevent losing the connexion.
:::
:::
