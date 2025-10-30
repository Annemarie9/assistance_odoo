Tips
====

Tipping is customary in multiple countries. Point of Sale allows tipping
in `shops <pos/sell>`{.interpreted-text role="ref"},
`bars <../restaurant>`{.interpreted-text role="doc"}, or
`restaurants <../restaurant>`{.interpreted-text role="doc"}.

Configuration
-------------

To allow tipping in your POS, activate the `Tips`{.interpreted-text
role="guilabel"} feature in `Point of Sale
--> Configuration --> Settings`{.interpreted-text role="menuselection"}.
At the top of the page, select the POS in which you wish to allow
**tipping**, scroll down to the `Payment`{.interpreted-text
role="guilabel"} section and check `Tips`{.interpreted-text
role="guilabel"}. Once enabled, add a `Tip Product`{.interpreted-text
role="guilabel"} in the corresponding field, and save. The designated
product will be used as a reference on customers\' receipts.



### Tip products {#tip-product}

**Tip products** can be created on the spot. To do so, enter a
product\'s name in the `Tip
Product <configuration>`{.interpreted-text role="ref"} field and click
`Create`{.interpreted-text role="guilabel"} or press **enter**. The
product is automatically configured to be used as a tip at the payment
screen.

However, if you wish to be able to select the tip product in a POS
session, you must activate the **Available in POS** setting. To do so,
click `Create and edit...`{.interpreted-text role="guilabel"} to open
the product configuration form. Then, go to the
`Sales`{.interpreted-text role="guilabel"} tab, tick the
`Available in POS`{.interpreted-text role="guilabel"} checkbox, and
click `Save & Close`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

\- When you create a product to use as a tip, leave the **product type**
as `Consumable`{.interpreted-text role="guilabel"} to avoid unnecessary
inventory movements. - You can only select one tip product per POS, but
you can choose a different one for each.
:::

### Tip using an Adyen terminal

If you use an
`Adyen <../payment_methods/terminals/adyen>`{.interpreted-text
role="doc"} payment terminal and wish to enable **tips** using the
terminal, check
`Add tip through payment terminal (Adyen)`{.interpreted-text
role="guilabel"} below the
`tip settings <configuration>`{.interpreted-text role="ref"}.

### Tip after payment

If you use a POS system in a bar or a restaurant, you can enable
`Add tip after payment
(North America specific)`{.interpreted-text role="guilabel"}. Doing so
generates a bill to print and complete manually by the customer and the
waiter. That bill indicates the tip value the customer chooses to give
after the payment.

::: {.important}
::: {.title}
Important
:::

To use this feature, the selected payment method must have a bank
journal attributed.
:::

Add tips
--------

To add tips to an order,
`access the payment screen <pos/sell>`{.interpreted-text role="ref"} and
click `♥ Tip`{.interpreted-text role="guilabel"}. Then, enter the
tipping amount, click `Confirm`{.interpreted-text role="guilabel"} to
validate, and process the payment.



Alternatively, you can select the
`tip product <tip-product>`{.interpreted-text role="ref"} on the POS
interface to add it to the cart. When selected, the product is
automatically set as a tip, and its default value equals its **Sales
Price**.

### Tip using an Adyen terminal

During checkout, select **Adyen** as the payment terminal, and send the
payment request to the device by clicking `Send`{.interpreted-text
role="guilabel"}. The customers are asked to enter the desired tipping
amount on the terminal\'s screen before proceeding to the payment.

### Tip after payment

At checkout, select a card payment method and click
`Close Tab`{.interpreted-text role="guilabel"}. Doing so generates a
bill to complete by the customer.



On the following screen, click the percentage (`15%`{.interpreted-text
role="guilabel"}, `20%`{.interpreted-text role="guilabel"},
`25%`{.interpreted-text role="guilabel"}), `No Tip`{.interpreted-text
role="guilabel"}, or enter the tipping amount the customer chose to
give. Then, click `Settle`{.interpreted-text role="guilabel"} to move to
the following order.


