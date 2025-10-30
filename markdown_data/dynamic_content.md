# File: /content/odoo_doc17.0/fr/content/applications/websites/website/web_design/building_blocks/dynamic_content.md

Dynamic content
===============

The `Dynamic Content`{.interpreted-text role="guilabel"}
`building blocks <../building_blocks>`{.interpreted-text role="doc"},
such as `Form <website/dynamic_content/form>`{.interpreted-text
role="ref"},
`Products <website/dynamic_content/products>`{.interpreted-text
role="ref"},
`Embed Code <website/dynamic_content/embed_code>`{.interpreted-text
role="ref"}, or `Blog Posts <../../../blog>`{.interpreted-text
role="doc"}, help you create interactive and visually appealing layouts
for your web `pages <../../pages>`{.interpreted-text role="doc"}.

::: {.note}
::: {.title}
Note
:::

To add a building block, click `Edit`{.interpreted-text
role="guilabel"}, select the desired building block under the
`Blocks`{.interpreted-text role="guilabel"} tab, and drag and drop it
onto the page. To access its settings, click it and go to the
`Customize`{.interpreted-text role="guilabel"} tab, where the available
options depend on the type of block selected.
:::

Form {#website/dynamic_content/form}
----

The `Form`{.interpreted-text role="guilabel"} block is used to collect
information from website visitors and create records in your database.



### Action

By default, submitting the form **sends you an email** containing what
the visitor entered. Depending on the apps installed on your database,
new actions that can automatically create records become available:

-   `Apply for a Job`{.interpreted-text role="guilabel"} (Recruitment)
-   `Create a Customer`{.interpreted-text role="guilabel"} (eCommerce)
-   `Create a Ticket`{.interpreted-text role="guilabel"} (Helpdesk)
-   `Create an Opportunity`{.interpreted-text role="guilabel"} (CRM)
-   `Subscribe to Newsletter`{.interpreted-text role="guilabel"} (Email
    Marketing)
-   `Create a Task`{.interpreted-text role="guilabel"} (Project)

Select another action with the `Action`{.interpreted-text
role="guilabel"} field found under the `Customize`{.interpreted-text
role="guilabel"} tab\'s `Form`{.interpreted-text role="guilabel"}
section.



By default, actions redirect visitors to a *thank you* page after
submitting the form. Use the `URL`{.interpreted-text role="guilabel"}
field to change where they are redirected. It is also possible to let
visitors stay on the form\'s page by selecting
`Nothing`{.interpreted-text role="guilabel"} or
`Show Message`{.interpreted-text role="guilabel"} under the
`On Success`{.interpreted-text role="guilabel"} field.

### Fields

To add a new field to the form, click the `+ Field`{.interpreted-text
role="guilabel"} button found next to the Customize tab\'s
`Form`{.interpreted-text role="guilabel"} or `Field`{.interpreted-text
role="guilabel"} section. By default, new fields are *text* fields. To
change the type, use the `Type`{.interpreted-text role="guilabel"} field
and select an option under the `Custom
Field`{.interpreted-text role="guilabel"} heading.

::: {.spoiler}
Click here to preview all field types



Some fields are visually similar, but the data entered must follow a
specific format.
:::

It is also possible to select an `Existing Field`{.interpreted-text
role="guilabel"} from a database and use the data it contains. The
fields available depend on the selected action.

::: {.tip}
::: {.title}
Tip
:::

Property fields added to the database can also be used.
:::

Products {#website/dynamic_content/products}
--------

The `Products`{.interpreted-text role="guilabel"} block is available
after installing the eCommerce app. It is used to display a selection of
products sold on your website.



By default, the block displays the `Newest Products`{.interpreted-text
role="guilabel"}. To change which products are shown, go to the
`Customize`{.interpreted-text role="guilabel"} tab\'s
`Products`{.interpreted-text role="guilabel"} section and select as
`Filter`{.interpreted-text role="guilabel"} the
`Recently Sold Products`{.interpreted-text role="guilabel"} or
`Recently Viewed Products`{.interpreted-text role="guilabel"} option.

In addition, it is possible to display products from a single category
only by selecting one with the `Category`{.interpreted-text
role="guilabel"} field.

Embed code {#website/dynamic_content/embed_code}
----------

Embedding code allows you to integrate content from third-party services
into a page, such as videos from YouTube, maps from Google Maps, social
media posts from Instagram, etc.



After adding the block to a page, click the `Edit`{.interpreted-text
role="guilabel"} button found under the `Customize`{.interpreted-text
role="guilabel"} tab\'s `Embed Code`{.interpreted-text role="guilabel"}
section and enter the code, replacing the code used to show the block\'s
instructions.
