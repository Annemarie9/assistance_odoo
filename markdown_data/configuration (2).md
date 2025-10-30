show-content

:   

show-toc

:   

Configuration
=============

Access the POS settings {#configuration/settings}
-----------------------

To access the general POS settings, go to
`Point of Sale --> Configuration -->
Settings`{.interpreted-text role="menuselection"}. Then, open the
dropdown menu in the `Point of Sale`{.interpreted-text role="guilabel"}
field and select the POS to configure.



::: {.note}
::: {.title}
Note
:::

These settings are available to users with the
`access rights </applications/general/users>`{.interpreted-text
role="doc"} `Administration`{.interpreted-text role="guilabel"} set as
`Settings`{.interpreted-text role="guilabel"}.
:::

You can also configure some settings from the dashboard by clicking the
vertical ellipsis button (`⋮`{.interpreted-text role="guilabel"}) on a
POS card. Doing so opens a popup window, from which you can:

-   `Enable multiple employees to log in. <employee_login>`{.interpreted-text
    role="doc"}
-   `Connect and set up an IoT sytem. <configuration/pos_iot>`{.interpreted-text
    role="doc"}
-   `Connect and set up an ePOS printer. <configuration/epos_ssc>`{.interpreted-text
    role="doc"}



::: {.note}
::: {.title}
Note
:::

These settings are available to users with the
`access rights </applications/general/users>`{.interpreted-text
role="doc"} `Point of Sale`{.interpreted-text role="guilabel"} set as
`Administrator`{.interpreted-text role="guilabel"}.
:::

Make products available
-----------------------

To make products available for sale, go to
`Point of Sale --> Products --> Products`{.interpreted-text
role="menuselection"}, and select a product to open the product form. In
the `Sales`{.interpreted-text role="guilabel"} tab, enable
`Available in POS`{.interpreted-text role="guilabel"}.



PoS product categories
----------------------

### Configuration

POS product categories allow users to categorize products and get a more
structured and clean POS interface.

To manage PoS categories, go to
`Point of Sale --> Configuration --> PoS Product
Categories`{.interpreted-text role="menuselection"}. To add a new
category, click `Create`{.interpreted-text role="guilabel"}. Then, name
it in the `Category Name`{.interpreted-text role="guilabel"} field.

To associate a category with a parent category, fill in the
`Parent Category`{.interpreted-text role="guilabel"} field. A parent
category groups one or more child categories.

::: {.example alt="The PoS product categories grouped by parent categories"}
.. image:: configuration/parent-categories.png
:::

### Assign PoS product categories

Go to `Point of Sale --> Products --> Products`{.interpreted-text
role="menuselection"} and open a product form. Then, go to the
`Sales`{.interpreted-text role="guilabel"} tab and fill in the
`Category`{.interpreted-text role="guilabel"} field under the `Point of
Sale`{.interpreted-text role="guilabel"} section.



### Adapt the POS interface

#### Start category

You can select one product category to display when
`opening a POS session
<pos/session-start>`{.interpreted-text role="ref"}. To configure it, go
to your `POS settings <configuration/settings>`{.interpreted-text
role="ref"} and select a PoS category from the dropdown menu of the
`Start Category`{.interpreted-text role="guilabel"} field within the
`PoS Interface`{.interpreted-text role="guilabel"} section.



#### Restrict categories

You can also limit the categories displayed on your POS interface. To
achieve this, go to your
`POS settings <configuration/settings>`{.interpreted-text role="ref"}
and choose the specific categories to display in the
`Restrict Categories`{.interpreted-text role="guilabel"} field within
the `PoS Interface`{.interpreted-text role="guilabel"} section.



::: {.toctree titlesonly=""}
configuration/pos\_iot configuration/epos\_printers configuration/https
configuration/epos\_ssc
:::
