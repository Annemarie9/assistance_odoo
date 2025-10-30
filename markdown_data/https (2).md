Secure connection (HTTPS)
=========================

If **Direct Devices** is enabled in a Point of Sale settings (for
example, if you use an `ePos
printer <epos_printers>`{.interpreted-text role="doc"}), HTTP becomes
the default protocol.

Force your Point of Sale to use a secure connection (HTTPS)
-----------------------------------------------------------

Add a new **key** in the **System Parameters** to force your Point of
Sale to use a secure connection with the HTTPS protocol.

To do so, activate the
`developer mode <developer-mode>`{.interpreted-text role="ref"}, go to
`Settings -->
Technical --> Parameters --> System Parameters`{.interpreted-text
role="menuselection"}, then create a new parameter, add the following
values and click on *Save*.

-   **Key**: [point\_of\_sale.enforce\_https]{.title-ref}
-   **Value**: [True]{.title-ref}

::: {.seealso}
\- `epos_ssc`{.interpreted-text role="doc"}
:::
