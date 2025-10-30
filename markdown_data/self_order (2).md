Self-ordering
=============

The self-ordering feature allows customers to browse your menu or
product catalog, place an order, and complete payment using their mobile
device or a self-ordering kiosk.

Configuration
-------------

### Feature activation

To enable this feature and select a self-ordering type, access the
`POS settings
<configuration/settings>`{.interpreted-text role="ref"}, scroll down to
the `Mobile self-order & Kiosk`{.interpreted-text role="guilabel"}
section, and select a `Self Ordering`{.interpreted-text role="guilabel"}
type under the `QR menu & Kiosk activation`{.interpreted-text
role="guilabel"} section.

You can choose from:

::: {.tabs}
::: {.group-tab}
QR menu

Select `QR menu`{.interpreted-text role="guilabel"} or
`QR menu + Ordering`{.interpreted-text role="guilabel"} to give
customers access to your menu or product catalog by scanning a QR code
on their personal device. The latter also allows them to place an order
and make a payment.



-   Click `fa-arrow-right`{.interpreted-text role="icon"}
    `Print QR Codes`{.interpreted-text role="guilabel"} to download a
    .pdf document with the generated QR codes.
-   Click `fa-arrow-right`{.interpreted-text role="icon"}
    `Download QR Codes`{.interpreted-text role="guilabel"} to download a
    compressed file with the generated QR codes.

::: {.note}
::: {.title}
Note
:::

In **restaurants**, printing or downloading QR codes generates as many
QR codes as the number of available tables. In **shops**, it generates
only one generic QR code.
:::

::: {.tip}
::: {.title}
Tip
:::

To customize QR codes,

1.  Scan the relevant QR code to acquire its URL.
2.  Use a QR code generator (e.g., [QR code
    monkey](https://www.qrcode-monkey.com) or [QR code
    generator](https://www.qr-code-generator.com)) to create a custom QR
    code.
:::
:::

::: {.group-tab}
Kiosk

When `Kiosk`{.interpreted-text role="guilabel"} is selected, customers
can access the menu or product catalog, place orders, and pay from a
self-ordering kiosk.


:::
:::

Once a self-ordering type is selected, the
`additional settings <pos/self_order/add-settings>`{.interpreted-text
role="ref"} update to fit the selected type\'s needs.

### Additional settings {#pos/self_order/add-settings}

::: {.tabs}
::: {.tab}
Home buttons

The `Home buttons`{.interpreted-text role="guilabel"} are displayed on
the kiosk or mobile device interfaces when customers are self-ordering.
To set them up, click `fa-arrow-right`{.interpreted-text role="icon"}
`Home
buttons`{.interpreted-text role="guilabel"}. Then,

1.  Click `New`{.interpreted-text role="guilabel"} to add a new button.
2.  Set the `Label`{.interpreted-text role="guilabel"}.
3.  Enter a `URL`{.interpreted-text role="guilabel"} preceded by
    [https://]{.title-ref} to redirect customers to a specific URL when
    clicking the button. For instance, you might want to redirect them
    to a campaign video for a new product or to a contest page.
4.  In the same `URL`{.interpreted-text role="guilabel"} column, enter
    [/products]{.title-ref} to create a button that redirects customers
    to the product catalog.
5.  Select the `Points of Sale`{.interpreted-text role="guilabel"} to
    ensure this button only appears on the selected POS\' self-ordering
    interface.
6.  Select a predefined `Style`{.interpreted-text role="guilabel"} from
    the dropdown menu.

::: {.note}
::: {.title}
Note
:::

\- Leaving the `Points of Sale`{.interpreted-text role="guilabel"} field
empty shares the button with all POS. - The `Preview`{.interpreted-text
role="guilabel"} column automatically updates, giving you a glimpse of
the button\'s appearance based on its configuration.
:::
:::

::: {.tab}
Service location and payment options

-   Set where the service occurs by selecting `Table`{.interpreted-text
    role="guilabel"} or `Pickup zone`{.interpreted-text role="guilabel"}
    under the `Service`{.interpreted-text role="guilabel"} field.
-   Define when and how customers pay in the
    `Pay after`{.interpreted-text role="guilabel"} field. Customers can
    pay after `Each meal`{.interpreted-text role="guilabel"} or for
    `Each order`{.interpreted-text role="guilabel"}.
-   The service location and payment options available depend on the
    type of self-ordering service and POS:
    -   **QR menu + Ordering**:
        -   **Restaurants**: Customers can be served at their table or
            the pickup zone.
            -   When served at their table, they can pay after each meal
                or each order.
            -   When served at the pickup zone, they can only pay after
                each order.
        -   **Shops**: Customers can only be served at the pickup zone
            and pay after each order.
        -   Regardless of the type of POS, customers can pay `online
            </applications/finance/payment_providers>`{.interpreted-text
            role="doc"} or using any configured `payment
            method <payment_methods>`{.interpreted-text role="doc"}.
    -   **Kiosk**:
        -   Regardless of the type of POS, customers can either be
            served at their table or in the pickup zone, but they must
            pay after each order.
        -   The kiosk self-ordering only works with
            `Adyen <payment_methods/terminals/adyen>`{.interpreted-text
            role="doc"} and
            `Stripe <payment_methods/terminals/stripe>`{.interpreted-text
            role="doc"} terminals.
        -   The `Online Payment`{.interpreted-text role="guilabel"}
            feature is not supported.

::: {.seealso}
\- `../../finance/payment_providers`{.interpreted-text role="doc"} -
`payment_methods`{.interpreted-text role="doc"}
:::
:::

::: {.tab}
Language

This option allows you to enable multiple languages for the
self-ordering interface. The suggested languages are those already
installed in Odoo. To expand the selection, add more languages:

1.  Click `fa-arrow-right`{.interpreted-text role="icon"}
    `Add Languages`{.interpreted-text role="guilabel"}.
2.  Add as many languages as needed to the `Languages`{.interpreted-text
    role="guilabel"} field.
3.  Click `Add`{.interpreted-text role="guilabel"}.
4.  Add those languages to the `Available`{.interpreted-text
    role="guilabel"} field.

::: {.seealso}
`../../general/users/language`{.interpreted-text role="doc"}
:::
:::

::: {.tab}
Splash screens

Splash screens are introductory screens displayed when the self-ordering
interface or kiosk is launched. They typically contain branding, welcome
messages, or usage instructions.

-   To add a splash screen image, click `fa-paperclip`{.interpreted-text
    role="icon"} `Add images`{.interpreted-text role="guilabel"}, select
    and open an image.
-   To remove a splash screen image, hover over the image and click
    `fa-times`{.interpreted-text role="icon"}
    (`Delete`{.interpreted-text role="guilabel"}).

::: {.note}
::: {.title}
Note
:::

You can add multiple splash screen images at once.
:::
:::

::: {.tab}
Eat in/ Take out

Activate this setting to
`adjust the tax rate <pricing/fiscal_position>`{.interpreted-text
role="doc"} based on whether customers dine in or take their order to
go. Then,

-   Fill in the field with an existing
    `Alternative Fiscal Position`{.interpreted-text role="guilabel"};
-   Create and set up a new fiscal position by filling in the field and
    clicking `Create & Edit`{.interpreted-text role="guilabel"}; or
-   Create and set up a new fiscal position by clicking
    `fa-arrow-right`{.interpreted-text role="icon"} `Fiscal
    Positions`{.interpreted-text role="guilabel"}.

::: {.seealso}
`pricing/fiscal_position`{.interpreted-text role="doc"}
:::
:::
:::

### Preview

Review the interface before making the self-ordering feature available
to customers to ensure all settings are applied correctly. Click
`fa-arrow-right`{.interpreted-text role="icon"}
`Preview Web interface`{.interpreted-text role="guilabel"} under the
`Self  Ordering`{.interpreted-text role="guilabel"} field to ensure all
`additional settings
<pos/self_order/add-settings>`{.interpreted-text role="ref"} are
correctly applied.

Usage guidelines
----------------

::: {.tabs}
::: {.group-tab}
QR menu

On the POS user\'s end, access the self-ordering interface by

-   Scanning a downloaded or printed QR code; or
-   Clicking the `fa-ellipsis-v`{.interpreted-text role="icon"}
    (`vertical ellipsis`{.interpreted-text role="guilabel"}) icon on the
    POS card, then `Mobile Menu`{.interpreted-text role="guilabel"}.

On the customers\' end,

1.  Access the self-ordering interface by scanning a downloaded or
    printed QR code.
2.  Click the
    `home button <pos/self_order/add-settings>`{.interpreted-text
    role="ref"} to reach the menu or catalog.
3.  Select the items and click `Order`{.interpreted-text
    role="guilabel"} to place an order.
4.  Follow the instructions on-screen to assign a table and pay for the
    order.
:::

::: {.group-tab}
Kiosk

On the POS user\'s end,

1.  Click `Start Kiosk`{.interpreted-text role="guilabel"}.
2.  Open the provided URL on the self-ordering kiosk(s).
    -   Copy and paste it; or
    -   Click `Open in New Tab`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

\- Once a session is open, `Start Kiosk`{.interpreted-text
role="guilabel"} switches to `Open Kiosk`{.interpreted-text
role="guilabel"} on the POS card. - Click `Open Kiosk`{.interpreted-text
role="guilabel"} on the POS card to reopen the popup window and access
the self-ordering interface.
:::

On the customers\' end,

1.  Click the
    `home button <pos/self_order/add-settings>`{.interpreted-text
    role="ref"} from a self-ordering kiosk to reach the menu or product
    catalog.
2.  Select the items and click `Order`{.interpreted-text
    role="guilabel"} to place an order.
3.  Follow the instructions on-screen to assign a table and pay for the
    order.


:::
:::

::: {.important}
::: {.title}
Important
:::

\- A POS session must be open for customers to place an order. - Once an
order is placed, it is automatically sent to `the preparation screen
<preparation>`{.interpreted-text role="doc"} and added to the list of
POS orders.
:::
