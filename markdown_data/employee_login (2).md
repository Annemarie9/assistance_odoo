Multi-employee management
=========================

Odoo Point of Sale (POS) offers a **Multi Employees per Session**
feature, allowing multiple users to
`log into a POS session <pos/employee_login/use>`{.interpreted-text
role="ref"}. Activating this feature enables the following actions:

-   Select specific users who can
    `log into the POS <pos/employee_login/use>`{.interpreted-text
    role="ref"}.
-   `Assign basic or advanced permissions <pos/employee_login/configuration>`{.interpreted-text
    role="ref"} to these users.
-   `Track the employees involved in each order for enhanced analytics <pos/analytics>`{.interpreted-text
    role="ref"}.

Configuration {#pos/employee_login/configuration}
-------------

Access the multi-employee setting from the
`PoS Interface`{.interpreted-text role="guilabel"} section of the `POS
settings <configuration/settings>`{.interpreted-text role="ref"}. Then,

1.  Activate the `Multi Employees per Session`{.interpreted-text
    role="guilabel"} feature.
2.  Add the employees with **basic POS functionality** access in the
    `Basic rights`{.interpreted-text role="guilabel"} field.
3.  Add the employees with **extended POS functionalities** in the
    `Advanced rights`{.interpreted-text role="guilabel"} field.



::: {.note}
::: {.title}
Note
:::

\- Leaving the `Basic rights`{.interpreted-text role="guilabel"} field
empty allows all employees to log in. - Leaving the
`Advanced rights`{.interpreted-text role="guilabel"} field empty grants
extended rights to Odoo users only.
:::

::: {.tip}
::: {.title}
Tip
:::

Click the `fa-ellipsis-v`{.interpreted-text role="icon"}
(`vertical ellipsis`{.interpreted-text role="guilabel"}) button on the
top right corner of a POS card and `Edit`{.interpreted-text
role="guilabel"} to access the setting from the main POS dashboard.
:::

::: {.seealso}
`../../general/users/access_rights`{.interpreted-text role="doc"}
:::

::: {.tabs}
.. tab:: Basic rights

Employees with basic rights can perform the following actions within the
POS:

**Session management:**

-   `Open a POS session <pos/session-start>`{.interpreted-text
    role="ref"}.
-   Lock the current POS session.
-   Toggle the visibility of product and category images.

**Sales transactions:**

-   `Process standard sales transactions <pos/sell>`{.interpreted-text
    role="ref"}.
-   `Process refunds <pos/refund>`{.interpreted-text role="ref"}.
-   `Access and handle sales orders <shop/sales_order>`{.interpreted-text
    role="doc"}.
-   `Set customers <pos/customers>`{.interpreted-text role="ref"}.
-   Access past and current order history.

**Pricing and discounts:**

-   Manually select another
    `pricelist <pricing/pricelists>`{.interpreted-text role="doc"}.
-   Enter promotional codes.
-   `Manually apply discounts <pricing/discounts>`{.interpreted-text
    role="doc"}.
-   Manually `change a product's price <pos/sell>`{.interpreted-text
    role="ref"}.

::: {.tab}
Advanced rights
:::

In addition to the basic rights, employees with advanced rights can
also:

-   `Perform cash-in and cash-out operations <pos/cash-register>`{.interpreted-text
    role="ref"}.
-   Access the Odoo backend interface.
-   `Close the current POS session <pos/session-close>`{.interpreted-text
    role="ref"}.
:::

Usage guidelines {#pos/employee_login/use}
----------------

### Logging in

Once the **Multi Employees per Session** feature is enabled, employees
must log in to `open a
POS session <pos/session-start>`{.interpreted-text role="ref"} and
access the POS interface. They can `scan their employee
badge <pos/employee_login/badge>`{.interpreted-text role="ref"} or click
`Select Cashier`{.interpreted-text role="guilabel"} to select their name
from the list of authorized users.



To switch between users during an
`active session <pos/session-start>`{.interpreted-text role="ref"},
click on the currently logged-in employee\'s name at the top right of
the POS screen and select the user to switch to.

### Logging in with badges {#pos/employee_login/badge}

Employees can log in using their badge. To configure badge-based login,
assign a unique badge ID to the employee\'s profile in the **Employees**
module:

1.  Navigate to the **Employees** module.
2.  Open the form view of the specific employee.
3.  Go to the `HR Settings`{.interpreted-text role="guilabel"} tab.
4.  The `Attendance/Point of Sale`{.interpreted-text role="guilabel"}
    category offers two options:
    -   Manually enter any badge ID in the `Badge ID`{.interpreted-text
        role="guilabel"} field.
    -   Click `Generate`{.interpreted-text role="guilabel"} to create a
        unique badge ID automatically.
5.  Click `Print Badge`{.interpreted-text role="guilabel"} to generate a
    barcode representation of the assigned badge ID.

To switch users within an open POS session using a badge, you must first
lock the session. To do so, click the `fa-bars`{.interpreted-text
role="icon"} icon (`hamburger menu`{.interpreted-text role="guilabel"})
and `Lock`{.interpreted-text role="guilabel"} to return to the login
screen. Then, the new employee can scan their badge to log in.

### Adding a PIN Code

For enhanced security, employees may be forced to enter a PIN code each
time they log into a POS session. To set up a PIN code for an employee:

1.  Navigate to the **Employees** module.
2.  Open the form view of the relevant employee.
3.  Go to the `HR Settings`{.interpreted-text role="guilabel"} tab.
4.  Enter a desired numerical code in the `PIN Code`{.interpreted-text
    role="guilabel"} field of the
    `Attendance/Point of Sale`{.interpreted-text role="guilabel"}
    category.

::: {.note}
::: {.title}
Note
:::

The PIN code must consist of a sequence of digits only.
:::
