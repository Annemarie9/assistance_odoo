Preparation display
===================

The preparation display feature allows you to handle POS orders
requiring preparation. Concretely,

-   **For retail**: The preparation team is notified after a payment is
    completed at the POS to gather the purchased items for customer
    pickup.
-   **For restaurants**: POS orders inform the kitchen of the meals to
    be prepared.

Configuration
-------------

To enable the preparation display feature,

1.  Go to the `POS settings <configuration/settings>`{.interpreted-text
    role="ref"}.
2.  Scroll down to the `Connected Devices`{.interpreted-text
    role="guilabel"} section.
3.  Check the `Preparation Display`{.interpreted-text role="guilabel"}
    option.



To create and set up a preparation display,

1.  Go to
    `Point of Sale --> Orders --> Preparation Display`{.interpreted-text
    role="menuselection"}
2.  Click `New`{.interpreted-text role="guilabel"}.
3.  Give the display a descriptive `Name`{.interpreted-text
    role="guilabel"} (e.g., [Main Kitchen]{.title-ref},
    [Bar]{.title-ref})
4.  Set it up:
    1.  `Point of Sale`{.interpreted-text role="guilabel"}: Select the
        POS that sends orders to this display.
    2.  `Product categories`{.interpreted-text role="guilabel"}: Specify
        the POS `Product categories`{.interpreted-text role="guilabel"}
        sent to this display.
    3.  `Stages`{.interpreted-text role="guilabel"}: Define the steps
        required for the orders to be ready.
        -   Click `Add a line`{.interpreted-text role="guilabel"} to add
            a stage.
        -   Assign specific colors to each stage for clarity (optional).
        -   Define an `Alert timer (min)`{.interpreted-text
            role="guilabel"} for each stage to indicate the expected
            processing time.



::: {.note}
::: {.title}
Note
:::

To edit a pre-existing preparation display, click the vertical ellipsis
button (`fa-ellipsis-v`{.interpreted-text role="icon"}) on the
display\'s card and select `Configure`{.interpreted-text
role="guilabel"}.
:::

Practical application
---------------------

Go to
`Point of Sale --> Orders --> Preparation Display`{.interpreted-text
role="menuselection"} to get an overview of all your displays.



The display card shows:

-   The configured stages.
-   The number of orders currently `In progress`{.interpreted-text
    role="guilabel"}.
-   The `Average time`{.interpreted-text role="guilabel"} employees
    usually take to complete an order.

::: {.tip}
::: {.title}
Tip
:::

Click the `Kitchen Display`{.interpreted-text role="guilabel"} app icon
on your Odoo Dashboard for quicker access.
:::

### Using the preparation display

To access the preparation display, click
`Open Preparation Display`{.interpreted-text role="guilabel"}. This
interface, designed for employees, shows:

-   **Stages and order count**: Displays the progress of orders across
    stages such as [To prepare]{.title-ref}, [Ready]{.title-ref}, and
    [Completed]{.title-ref}, along with the number of orders in each
    stage.
-   **Ordered products by category**: Lists all items in progress,
    grouped by POS categories (e.g., [Drinks]{.title-ref},
    [Food]{.title-ref}).
-   **Order cards**: Summarizes individual orders, including:
    -   Associated tables and order numbers.
    -   Status, such as [Ready]{.title-ref}, highlighted with the
        defined colors.
    -   Waiting time, with visual indicators.

::: {.note}
::: {.title}
Note
:::

The duration indicator turns red if the elapsed time exceeds the
predefined alert time.
:::



To update order progress:

-   Click items on the order card to cross them off individually.
-   Click the order card itself to mark all items at once.
-   The card automatically moves to the next stage once every item is
    crossed off.
-   Click `fa-undo`{.interpreted-text role="icon"}
    `Recall`{.interpreted-text role="guilabel"} to move an order back to
    the previous stage if you mistakenly sent it to the next stage.

### Customer display

In parallel, click `Open customer display`{.interpreted-text
role="guilabel"} to open the customer interface. This interface,
designed for customers, provides an overview of orders that are:

-   `Ready`{.interpreted-text role="guilabel"} for pickup.
-   `Almost there`{.interpreted-text role="guilabel"}, indicating they
    are taken care of.

::: {.note}
::: {.title}
Note
:::

The order number can be found at the top of the customer\'s receipt.
:::
