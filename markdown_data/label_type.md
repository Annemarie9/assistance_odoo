# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/label_type.md

Change shipping label size
==========================

Overview
--------

In Odoo, there are a variety of different types of shipping labels that
can be selected for delivery orders. Depending on the types of shipping
packages used, different label sizes may be more appropriate, and can be
configured to fit the package.

Configuration
-------------

In the `Inventory`{.interpreted-text role="menuselection"} module, go to
`Configuration --> Delivery -->
Shipping Methods.`{.interpreted-text role="menuselection"} Click on a
delivery method to choose it. For the following example, *FedEx
International* will be used.

{.align-center}

In the `Configuration`{.interpreted-text role="guilabel"} tab, under
`Label Type`{.interpreted-text role="guilabel"}, choose one of the label
types available. The availability varies depending on the carrier.

{.align-center}

When a sales order with the corresponding shipping company is confirmed
and a delivery order is validated, the shipping label will be
automatically created as a PDF and appear in the
`Chatter`{.interpreted-text role="guilabel"}.

Create a sales order
--------------------

In the `Sales`{.interpreted-text role="menuselection"} application,
click `Create`{.interpreted-text role="guilabel"} and select an
international customer. Click `Add A Product`{.interpreted-text
role="guilabel"} and select an item. Click
`Add Shipping`{.interpreted-text role="guilabel"}, select a shipping
method, then click `Get Rate`{.interpreted-text role="guilabel"}, and
finally, click `Add`{.interpreted-text role="guilabel"}.

{.align-center}

Once the quotation is confirmed by clicking `Confirm`{.interpreted-text
role="guilabel"}, a `Delivery`{.interpreted-text role="guilabel"} smart
button will appear.

{.align-center}

Once the delivery order is validated by clicking
`Validate`{.interpreted-text role="guilabel"} in the delivery order, the
shipping documents appear in the `Chatter`{.interpreted-text
role="guilabel"}.

{.align-center}

Example labels
--------------

The default `Label Type`{.interpreted-text role="guilabel"} is
`Paper Letter`{.interpreted-text role="guilabel"}. An example of a FedEx
letter sized label is:

{.align-center}

For comparison, an example of a FedEx bottom-half label is:

{.align-center}
