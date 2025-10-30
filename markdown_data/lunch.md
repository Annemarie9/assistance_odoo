# File: /content/odoo_doc17.0/fr/content/applications/hr/lunch.md

show-content

:   

Lunch
=====

The *Lunch* application in Odoo allows users a convenient way to order
food and pay for their meal directly from the database.

Before employees can use the *Lunch* application, there are a number of
configurations to consider: settings, vendors, locations, products,
product categories, and alerts. Once these are created, employees can
view offerings and order food.

Settings
--------

Only two settings are needed to configure in the *Lunch* app: overdraft
settings and notifications. To access the settings, navigate to
`Lunch app --> Configuration: Settings`{.interpreted-text
role="menuselection"}.

Configure the following:

-   `Lunch Overdraft`{.interpreted-text role="guilabel"}: enter the
    maximum overdraft amount for employees. The currency format is
    determined by the localization setting of the company.
-   `Reception notification`{.interpreted-text role="guilabel"}: set the
    message users receive via the *Discuss* app when their food has been
    delivered. The default message [Your lunch has been delivered. Enjoy
    your meal!]{.title-ref} populates this field, but can be modified,
    if desired.

::: {.tip}
::: {.title}
Tip
:::

If in a database with multiple languages installed, many forms in the
*Lunch* application have the option of entering translations for various
fields.

If translations are available to be configured, a language code appears
next to a translatable field on a form. To add translations for that
field, click the two letter language code (for example,
`EN`{.interpreted-text role="guilabel"} for English) and a translation
pop-up window appears.

The following is an example for the
`Reception notification`{.interpreted-text role="guilabel"} field in the
settings menu:

Navigate to `Lunch app --> Configuration: Settings`{.interpreted-text
role="menuselection"}. Click the `EN`{.interpreted-text role="guilabel"}
In the top-right of the text box beneath the
`Reception notification`{.interpreted-text role="guilabel"} section. A
`Translate: company_lunch_notify_message`{.interpreted-text
role="guilabel"} pop-up window loads with the option to enter a
translation for the other languages used by the database.

The first column lists the different languages in alphabetical order,
with the currently selected language in bold. The second column has the
currently configured message in each column. The last column in the
far-right provides a text box to type in a translation for each
language.

Enter the text that should appear for each language, then click
`Save`{.interpreted-text role="guilabel"}.

![The translation text box, with the current language highlighted, and the Arabic
translation field highlighted.](lunch/translation.png){.align-center}
:::

Locations
---------

By default, Odoo creates an [HQ Office]{.title-ref} location when the
*Lunch* application is installed. If a company has more than one
location, they must be configured.

To add a location, navigate to
`Lunch app --> Configuration: Locations`{.interpreted-text
role="menuselection"}. The currently configured locations appear in a
list view. Click the `New`{.interpreted-text role="guilabel"} button in
the top-left corner and a blank line appears beneath the last location
in the list.

Enter the name of the location in the field. Next, click into the
`Address`{.interpreted-text role="guilabel"} field to the right of the
name, and enter the location\'s address. It is possible to enter
multiple lines in the address field.

Repeat this for all locations that need to be added.

{.align-center}

Alerts
------

It is possible to set up alerts that can either be displayed in the
*Lunch* app, or be sent to specific employees via the *Discuss* app.

No alerts are pre-configured by default. To set up an alert, navigate to
`Lunch app
--> Configuration: Alerts`{.interpreted-text role="menuselection"}.
Click the `New`{.interpreted-text role="guilabel"} button in the
top-left corner and a blank lunch alert form loads. Enter the following
information on the form:

-   `Alert Name`{.interpreted-text role="guilabel"}: enter a name for
    the alert. This should be short and descriptive, such as [New Lunch
    Vendor]{.title-ref} or [Order by 11]{.title-ref}. This field is
    **required**.

-   `Display`{.interpreted-text role="guilabel"}: select whether the
    alert is visible in the *Lunch* app (`Alert in
    app)`{.interpreted-text role="guilabel"} or sent to employees via
    the *Discuss* app in a chat window
    (`Chat notification`{.interpreted-text role="guilabel"}).

    -   `Recipients`{.interpreted-text role="guilabel"}: this field only
        appears if `Chat notification`{.interpreted-text
        role="guilabel"} is selected for the `Display`{.interpreted-text
        role="guilabel"} option. Select who receives the chat alert. The
        options are: `Everyone`{.interpreted-text role="guilabel"},
        `Employee who ordered last week`{.interpreted-text
        role="guilabel"}, `Employee who
        ordered last month`{.interpreted-text role="guilabel"}, or
        `Employee who ordered last year`{.interpreted-text
        role="guilabel"}.

-   `Location`{.interpreted-text role="guilabel"}: select the locations
    the alert should appear for from the drop-down menu. Multiple
    locations can be selected. This field is **required**, therefore, if
    the alert applies to all locations, select all the locations from
    the drop-down menu.

-   `Show Until`{.interpreted-text role="guilabel"}: if the alert should
    expire on a specific date, select the date from the calendar picker.

-   `Active`{.interpreted-text role="guilabel"}: this option is on
    (appears green) by default. To turn off the alert, click the toggle
    so that it no longer appears green.

-   `Message`{.interpreted-text role="guilabel"}: Enter the alert
    message in this field. This field is **required**.

-   `Notification Time`{.interpreted-text role="guilabel"}: select the
    days of the week the alert should be sent. By default, all seven
    days are active. Click on a checkbox to change the setting from
    active to inactive.

    If `Chat notification`{.interpreted-text role="guilabel"} was
    selected for the `Display`{.interpreted-text role="guilabel"}
    option, a `Time`{.interpreted-text role="guilabel"} field also
    appears. Enter the time the chat message should be sent. Next,
    select if the time is either `AM`{.interpreted-text role="guilabel"}
    or `PM`{.interpreted-text role="guilabel"} using the drop-down menu
    to the right of the `Time`{.interpreted-text role="guilabel"} field.

![An alert form with all of the information filled out for a chat alert sent at 10:30 AM,
asking employees to submit orders by 11:30 AM.](lunch/alert.png){.align-center}

::: {.seealso}
\- `lunch/vendors`{.interpreted-text role="doc"} -
`lunch/products`{.interpreted-text role="doc"} -
`lunch/orders`{.interpreted-text role="doc"} -
`lunch/user-accounts`{.interpreted-text role="doc"} -
`lunch/management`{.interpreted-text role="doc"}
:::

::: {.toctree titlesonly=""}
lunch/vendors lunch/products lunch/orders lunch/user-accounts
lunch/management
:::
