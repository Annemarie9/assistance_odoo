Floors and tables
=================

The **Floor plan view** enables you to manage restaurant floors and
table arrangements and monitor table status in real time, including
occupancy, reservations, and kitchen orders.

::: {.example}


-   Table 1: An order has been placed and sent to the kitchen.
-   Table 3: An order of four items has been placed and needs to be sent
    to the kitchen.
-   Tables 2, 4, and 5: These tables are available.
-   Tables 2, 4, and 5: These tables\' total capacity is, respectively,
    2, 4, and 8 people.
-   Table 1: The table of two is full.
-   Table 3: The table of four is taken by one person.
-   Table 5: \"Famous Joe\" has a reservation for 8 people at 12:00.
:::

Configuration
-------------

### From the POS backend

To create floors and tables from the backend, go to
`Point of Sale --> Configuration
--> Floor Plans`{.interpreted-text role="menuselection"}, and click
`New`{.interpreted-text role="guilabel"} to create a floor. Name it,
select the related point(s) of sales, and click
`Add a line`{.interpreted-text role="guilabel"} to create a table. Name
the table and assign a number of seats. You can also link it to an
appointment resource to make the table bookable. Once done, click
`Save & Close`{.interpreted-text role="guilabel"} or
`Save & New`{.interpreted-text role="guilabel"} to confirm.



::: {.note}
::: {.title}
Note
:::

The POS must be opened and
`edited from the frontend <floors_tables/frontend>`{.interpreted-text
role="ref"} to create a map of your restaurant or bar reflecting your
actual floor plan.
:::

::: {.tip}
::: {.title}
Tip
:::

Create floors on the spot:
`access your POS settings <configuration/settings>`{.interpreted-text
role="ref"}, type your floor name in the `Floor`{.interpreted-text
role="guilabel"} field of the `Floors & Tables Map`{.interpreted-text
role="guilabel"} category, and press *enter*.


:::

### From the POS frontend {#floors_tables/frontend}

To create floors and tables from the frontend,
`open a POS session <pos/session-start>`{.interpreted-text role="ref"},
click the hamburger menu icon `≡`{.interpreted-text role="guilabel"} in
the upper right corner, then `Edit Plan`{.interpreted-text
role="guilabel"} to enter the **edit mode**.

Click `+ Add Floor`{.interpreted-text role="guilabel"} to add a floor,
then enter a name in the pop-up window.

Once a floor is created, add a table by clicking
`+ TABLE`{.interpreted-text role="guilabel"}. To move it, select it and
drag and drop it as desired. You can also modify the attributes of the
selected table, such as the number of seats by clicking
`SEATS`{.interpreted-text role="guilabel"}, the table shape using
`SHAPE`{.interpreted-text role="guilabel"}, the table color using
`FILL`{.interpreted-text role="guilabel"}, or the table name by clicking
`RENAME`{.interpreted-text role="guilabel"}. To duplicate an existing
table, select it and click `COPY`{.interpreted-text role="guilabel"}.
You can also remove the table by clicking `DELETE`{.interpreted-text
role="guilabel"}.

After making all the necessary modifications, click
`CLOSE`{.interpreted-text role="guilabel"} to save.



::: {.note}
::: {.title}
Note
:::

If no table is selected, the modifications are applied to the floor.
:::

::: {.warning}
::: {.title}
Warning
:::

Removing a table or a floor cannot be undone.
:::

Table transfer {#floors_tables/transfer}
--------------

To move customers from one table to another, select a table and click
`→ Transfer`{.interpreted-text role="guilabel"} on the POS interface.
This redirects you to the floor plan view, where you can choose the new
table to which you want to transfer the customers.

When you transfer customers, all of the orders they have placed and that
are linked to the original table are also transferred.
