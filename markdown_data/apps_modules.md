# File: /content/odoo_doc17.0/fr/content/applications/general/apps_modules.md

Apps and modules
================

You can `install <general/install>`{.interpreted-text role="ref"},
`upgrade <general/upgrade>`{.interpreted-text role="ref"} and `uninstall
<general/uninstall>`{.interpreted-text role="ref"} all apps and modules
from the `Apps`{.interpreted-text role="menuselection"} dashboard.

By default, an *Apps* filter is applied. If you want to search for
modules, click on *Filters* and select *Extra*.

{.align-center}

::: {.warning}
::: {.title}
Warning
:::

Odoo is *not a smartphone*, and its apps shouldn\'t be installed or
uninstalled carelessly. Apply caution when adding or removing apps and
modules on your database since this may impact your subscription costs.

-   | **Installing or uninstalling apps and managing users is up to
      you.**
    | As the administrator of your database, you are responsible for its
      usage, as you know best how your organization works.

-   | **Odoo apps have dependencies.**
    | Installing some apps and features with dependencies may also
      install additional apps and modules that are technically required,
      even if you won\'t actively use them.

-   | **Test app installation/removal on a duplicate of your database.**
    | This way, you can know what app dependencies may be required or
      what data may be erased.
:::

Install apps and modules {#general/install}
------------------------

Go to `Apps`{.interpreted-text role="menuselection"}, and click on the
*Install* button of the app you want to install.

::: {.note}
::: {.title}
Note
:::

If the module you are looking for is not listed, you can **update the
app list**.

To do so, activate the
`developer mode <developer-mode>`{.interpreted-text role="ref"}, then go
to `Apps
--> Update Apps List`{.interpreted-text role="menuselection"} and click
on *Update*.
:::

Upgrade apps and modules {#general/upgrade}
------------------------

On some occasions, new improvements or app features are added to
`supported versions of Odoo
</administration/supported_versions>`{.interpreted-text role="doc"}. To
be able to use them, you must **upgrade** your app.

Go to `Apps`{.interpreted-text role="menuselection"}, click on the
*dropdown menu* of the app you want to upgrade, then on *Upgrade*.

Uninstall apps and modules {#general/uninstall}
--------------------------

Go to `Apps`{.interpreted-text role="menuselection"}, click on the
*dropdown menu* of the app you want to uninstall, then on *Uninstall*.

{.align-center}

Some apps have dependencies, meaning that one app requires another.
Therefore, uninstalling one app may uninstall multiple apps and modules.
Odoo warns you which dependent apps and modules are affected by it.

{.align-center}

To complete the uninstallation, click on *Confirm*.

::: {.danger}
::: {.title}
Danger
:::

Uninstalling an app also uninstalls all its dependencies and permanently
erases their data.
:::
