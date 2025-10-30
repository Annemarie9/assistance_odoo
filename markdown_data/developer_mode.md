# File: /content/odoo_doc17.0/fr/content/applications/general/developer_mode.md

Developer mode (debug mode) {#developer-mode}
===========================

The developer mode, also known as debug mode, unlocks access to advanced
`tools and settings
<developer-mode/tools>`{.interpreted-text role="ref"} in Odoo.

::: {.warning}
::: {.title}
Warning
:::

Proceed with caution, as some developer tools and technical settings are
considered advanced and may have associated risks. Only use them if you
understand the implications and are confident in your actions.
:::

::: {.note}
::: {.title}
Note
:::

The developer mode is also available with
`assets <frontend/framework/assets_debug_mode>`{.interpreted-text
role="ref"}, which are used to debug JavaScript code, and with
`tests assets
<frontend/framework/tests_debug_mode>`{.interpreted-text role="ref"},
which are used to run test tours.
:::

Activation {#developer-mode/activation}
----------

To activate it, open the `Settings`{.interpreted-text role="guilabel"}
app, scroll down to the `Developer Tools`{.interpreted-text
role="guilabel"} section, and click
`Activate the developer mode`{.interpreted-text role="guilabel"}.

Once activated, the `Deactivate the developer mode`{.interpreted-text
role="guilabel"} option becomes available.



To activate the developer mode **from anywhere in the database**, add
[?debug=1]{.title-ref} to the URL after [/web]{.title-ref} (e.g.,
[https://example.odoo.com/web?debug=1\#action=menu&cids=1]{.title-ref}).
To deactivate it, use [?debug=0]{.title-ref} instead.

Use [?debug=assets]{.title-ref} to activate the developer mode with
assets and [?debug=tests]{.title-ref} to activate it with tests assets.

::: {.tip}
::: {.title}
Tip
:::

Open the **command palette** by pressing [Ctrl + K]{.title-ref} or [Cmd
⌘ + K]{.title-ref}, then type [debug]{.title-ref} to activate the
developer mode with assets or deactivate it.
:::

::: {.admonition}
Browser extension

The  browser extension
adds an icon to toggle developer mode on or off from the browser\'s
toolbar. It is available on the [Chrome Web
Store](https://chromewebstore.google.com/detail/odoo-debug/hmdmhilocobgohohpdpolmibjklfgkbi)
and [Firefox
Add-ons](https://addons.mozilla.org/firefox/addon/odoo-debug/).
:::

Developer tools and technical menu {#developer-mode/tools}
----------------------------------

Once the developer mode is activated, the developer tools can be
accessed by clicking the `fa-bug`{.interpreted-text role="icon"}
`(bug)`{.interpreted-text role="guilabel"} icon. The menu contains tools
useful for understanding or editing technical data, such as a view\'s
field, filters, or actions. The options available depend on where the
menu is accessed from.



Database administrators can access the technical menu from the
`Settings`{.interpreted-text role="guilabel"} app. It contains advanced
database settings, such as ones related to the database structure,
security, actions, etc.


