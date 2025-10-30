# File: /content/odoo_doc17.0/fr/content/applications/general/iot/iot_advanced/ssh_connect.md

IoT box SSH connection
======================

::: {.note}
::: {.title}
Note
:::

SSH connections are only available for
`IoT boxes <../iot_box>`{.interpreted-text role="doc"}, not the `Windows
virtual IoT <../windows_iot>`{.interpreted-text role="doc"}.
:::

::: {.warning}
::: {.title}
Warning
:::

\- This feature should **only** be used with trusted parties, as it
provides administrative access to the IoT box, which can create security
issues. - Managing an SSH connection is **not** covered under the
standard Odoo support scope. Visit the [Odoo
Support](https://www.odoo.com/help) page for additional information
about what is covered.
:::

To provide an `SSH (secure shell protocol)`{.interpreted-text
role="abbr"} connection to an IoT box, you must generate a password:

1.  Access the IoT box\'s homepage by opening the IoT app and clicking
    the IP address displayed on the IoT box\'s card.

2.  Click the `fa-cogs`{.interpreted-text role="icon"}
    (`cogs`{.interpreted-text role="guilabel"}) button at the top-right,
    then `Remote
    Debug`{.interpreted-text role="guilabel"}.

3.  In the `Remote Debugging`{.interpreted-text role="guilabel"} popup
    that opens, click `Generate`{.interpreted-text role="guilabel"} and
    save the password securely. Once you close the popup, the password
    will no longer be available.

    

4.  Enter the `Authentication Token`{.interpreted-text role="guilabel"}
    provided by the user attempting to connect to the IoT box.

5.  Click `Enable Remote Debugging`{.interpreted-text role="guilabel"}.

::: {.seealso}
\- `../iot_box`{.interpreted-text role="doc"} -
`../connect`{.interpreted-text role="doc"}
:::
