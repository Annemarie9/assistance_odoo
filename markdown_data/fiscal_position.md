Flexible taxes (fiscal positions)
=================================

When running a business, you may need to apply different taxes and
record transactions on various accounts based on the location and type
of business of your customers and providers.

The **fiscal positions** feature enables you to establish rules that
automatically select the right taxes and accounts used for each
transaction.

::: {.seealso}
\-
`../../../finance/accounting/taxes/fiscal_positions`{.interpreted-text
role="doc"} - `../../../finance/accounting/taxes`{.interpreted-text
role="doc"}
:::

Configuration
-------------

To enable the feature, go to
`Point of Sale --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, scroll down to the `Accounting`{.interpreted-text
role="guilabel"} section, and enable `Flexible Taxes`{.interpreted-text
role="guilabel"}.

Then, set a default fiscal position that should be applied to all sales
in the selected POS in the `Default`{.interpreted-text role="guilabel"}
field. You can also add more fiscal positions to choose from in the
`Allowed`{.interpreted-text role="guilabel"} field.

{.align-center}

According to the
`fiscal localization package <../../../finance/fiscal_localizations>`{.interpreted-text
role="doc"} activated, several fiscal positions are preconfigured and
can be set and used in POS. However, you can also
`create new fiscal positions <fiscal_positions/mapping>`{.interpreted-text
role="ref"}.

::: {.note}
::: {.title}
Note
:::

If you do not set a fiscal position, the tax remains as defined in the
**customer taxes** field on the product form.
:::

Use fiscal positions
--------------------

Open a `POS session <pos/session-start>`{.interpreted-text role="ref"}
to use one of the allowed fiscal positions. Then, click the
`Tax`{.interpreted-text role="guilabel"} button next to the
**book-shaped** icon and select a fiscal position from the list. Doing
so applies the defined rules automatically to all the products subject
to the chosen fiscal position\'s regulations.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If a default fiscal position is set, the tax button displays the name of
the fiscal position.
:::

::: {.seealso}
`../../../finance/accounting/taxes/fiscal_positions`{.interpreted-text
role="doc"}
:::
