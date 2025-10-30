# File: /content/odoo_doc17.0/fr/content/applications/general/integrations/unsplash.md

Unsplash
========

**Unsplash** is a recognized stock photography library integrated with
Odoo.

If your database is hosted on **Odoo Online**, you can access Unsplash
pictures without configuration.

If your database is hosted on **Odoo.sh or on-premise**, proceed as
follows:

1.  To **generate an Unsplash access key**, create or sign in to an
    .
2.  Access your [applications
    dashboard](https://unsplash.com/oauth/applications), click
    `New Application`{.interpreted-text role="guilabel"}, select all
    checkboxes, and click `Accept terms`{.interpreted-text
    role="guilabel"}.
3.  In the pop-up window, enter your
    `Application Name`{.interpreted-text role="guilabel"}, starting with
    the prefix [Odoo:]{.title-ref} (e.g., [Odoo:
    connection]{.title-ref}), so Unsplash recognizes it as an Odoo
    instance. Then, add a `Description`{.interpreted-text
    role="guilabel"} and click `Create application`{.interpreted-text
    role="guilabel"}.
4.  On the application details page, scroll down to the
    `Keys`{.interpreted-text role="guilabel"} section and copy the
    `Access Key`{.interpreted-text role="guilabel"} and
    `Application ID`{.interpreted-text role="guilabel"}.
5.  In Odoo, go to `General Settings`{.interpreted-text
    role="menuselection"} and enable the `Unsplash Image
    Library`{.interpreted-text role="guilabel"} feature. Then, enter the
    Unsplash `Access Key`{.interpreted-text role="guilabel"} and
    `Application ID`{.interpreted-text role="guilabel"}.

::: {.warning}
::: {.title}
Warning
:::

As a non-Odoo Online user, you are limited to a test key with a maximum
of 50 Unsplash requests per hour.
:::
