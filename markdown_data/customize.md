# File: /content/odoo_doc17.0/fr/content/applications/finance/accounting/reporting/customize.md

Custom reports
==============

Odoo comes with a powerful and easy-to-use reporting framework. The
engine allows you to create new reports, such as **tax reports**, or
**balance sheets** and **income statements** with **specific groupings**
and **layouts**.

::: {.important}
::: {.title}
Important
:::

Activate the `developer mode <developer-mode>`{.interpreted-text
role="ref"} to access the accounting report creation interface.
:::

To create a new report, go to
`Accounting --> Configuration --> Management:
Accounting Reports`{.interpreted-text role="menuselection"}. From here,
you can either create a
`root report <customize-reports/root>`{.interpreted-text role="ref"} or
a `variant <customize-reports/variants>`{.interpreted-text role="ref"}.

{.align-center}

Root reports {#customize-reports/root}
------------

Root reports can be regarded as generic, neutral accounting reports.
They serve as models on which local accounting versions are built. If a
report has no root report, it is considered to be a root report itself.

::: {.example}
A tax report for Belgium and the US would both use the same generic
version as a base and adapt it for their domestic regulations.
:::

When creating a new root report, you need to create a **menu item** for
it. To do so, open the report and then, on that same report, click on
`Action --> Create Menu Item`{.interpreted-text role="menuselection"}.
Refresh the page; the report is now available under
`Accounting --> Reporting`{.interpreted-text role="menuselection"}.

::: {.note}
::: {.title}
Note
:::

Cases that require creating a new root report are rare, such as when a
country\'s tax authorities require a new and specific type of report.
:::

{.align-center}

Variants {#customize-reports/variants}
--------

Variants are country-specific versions of root reports and, therefore,
always refer to a root report. To create a variant, select a generic
(root) report in the `Root Report`{.interpreted-text role="guilabel"}
field when creating a new report.

When a root report is opened from one of the accounting app\'s main
menus, all its variants are displayed in the variant selector in the top
right corner of the view.

::: {.example}
In the following image, `VAT Report (BE)`{.interpreted-text
role="guilabel"} is the variant of the root `Generic
Tax report`{.interpreted-text role="guilabel"}.

{.align-center}
:::

Lines
-----

After having created a report (either root or variant), you need to fill
it with lines. You can either create a new one by clicking on
`Add a line`{.interpreted-text role="guilabel"}, or modify an existing
line by clicking on it. All lines *require* a `Name`{.interpreted-text
role="guilabel"}, and can have an optional additional
`Code`{.interpreted-text role="guilabel"} (of your choice) if you wish
to use their value in formulas.

{.align-center}

Expressions
-----------

Each line can contain one or multiple **expressions**. Expressions can
be seen as **sub-variables** needed by a report line. To create an
expression, click on `Add a line`{.interpreted-text role="guilabel"}
*within* a line report.

When creating an expression, you must attribute a
`label`{.interpreted-text role="guilabel"} used to refer to that
expression. Therefore, it has to be **unique** among the expressions of
each line. Both a `Computation Engine`{.interpreted-text
role="guilabel"} and a `Formula`{.interpreted-text role="guilabel"} must
also be indicated. The **engine** defines how your **formula(s)** and
**subformula(s)** are interpreted. It is possible to mix expressions
using different computation engines under the same line if you need to.

::: {.note}
::: {.title}
Note
:::

Depending on the engine, `subformulas`{.interpreted-text
role="guilabel"} may also be required.
:::

### \'Odoo Domain\' engine

With this engine, a formula is interpreted as an
`Odoo domain <reference/orm/domains>`{.interpreted-text role="ref"}
targeting [account.move.line]{.title-ref} objects.

The subformula allows you to define how the move lines matching the
domain are used to compute the value of the expression:

[sum]{.title-ref}

:   The result is the sum of all the balances of the matched move lines.

[sum\_if\_pos]{.title-ref}

:   The result is the sum of all the balances of the matched move lines
    if this amount is positive. Otherwise, it is [0]{.title-ref}.

[sum\_if\_neg]{.title-ref}

:   The result is the sum of all the balances of the matched move lines
    if this amount is negative. Otherwise, it is [0]{.title-ref}.

[count\_rows]{.title-ref}

:   The result is the number of sub-lines of this expression. If the
    parent line has a group-by value, this will correspond to the number
    of distinct grouping keys in the matched move lines. Otherwise, it
    will be the number of matched move lines.

You can also put a [-]{.title-ref} sign at the beginning of the
subformula to **reverse** the sign of the result.

{.align-center}

### \'Tax Tags\' engine

A formula made for this engine consists of a name used to match tax
tags. If such tags do not exist when creating the expression, they will
be created.

When evaluating the expression, the expression computation can roughly
be expressed as: **(amount of the move lines with** [+]{.title-ref}
**tag)** [-]{.title-ref} **(amount of the move lines with**
[-]{.title-ref} **tag)**.

::: {.example}
If the formula is [tag\_name]{.title-ref}, the engine matches tax tags
[+tag\_name]{.title-ref} and [-tag\_name]{.title-ref}, creating them if
necessary. To exemplify further: two tags are matched by the formula. If
the formula is [A]{.title-ref}, it will require (and create, if needed)
tags [+A]{.title-ref} and [-A]{.title-ref}.
:::

### \'Aggregate Other Formulas\' engine

Use this engine when you need to perform arithmetic operations on the
amounts obtained for other expressions. Formulas here are composed of
references to expressions separated by one of the four basic arithmetic
operators (addition [+]{.title-ref}, subtraction [-]{.title-ref},
division [/]{.title-ref}, and multiplication [\*]{.title-ref}). To refer
to an expression, type in its parent line\'s **code** followed by a
period [.]{.title-ref} and the expression\'s **label** (ex.
**code.label**).

**Subformulas** can be one of the following:

[if\_above(CUR(amount))]{.title-ref}

:   The value of the arithmetic expression will be returned only if it
    is greater than the provided bound. Otherwise, the result will be
    [0]{.title-ref}.

[if\_below(CUR(amount))]{.title-ref}

:   The value of the arithmetic expression will be returned only if it
    is lower than the provided bound. Otherwise, the result will be
    [0]{.title-ref}.

[if\_between(CUR1(amount1), CUR2(amount2))]{.title-ref}

:   The value of the arithmetic expression will be returned only if it
    is strictly between the provided bounds. Otherwise, it will be
    brought back to the closest bound.

[if\_other\_expr\_above(LINE\_CODE.EXPRESSION\_LABEL, CUR(amount))]{.title-ref}

:   The value of the arithmetic expression will be returned only if the
    value of the expression denoted by the provided line code and
    expression label is greater than the provided bound. Otherwise, the
    result will be [0]{.title-ref}.

[if\_other\_expr\_below(LINE\_CODE.EXPRESSION\_LABEL, CUR(amount))]{.title-ref}

:   The value of the arithmetic expression will be returned only if the
    value of the expression denoted by the provided line code and
    expression label is lower than the provided bound. Otherwise, the
    result will be [0]{.title-ref}.

[CUR]{.title-ref} is the currency code in capital letters, and
[amount]{.title-ref} is the amount of the bound expressed in that
currency.

You can also use the [cross\_report]{.title-ref} subformula to match an
expression found in another report.

### \'Prefix of Account Codes\' engine

This engine is used to match amounts made on accounts using the prefixes
of these accounts\' codes as variables in an arithmetic expression.

::: {.example}
\| [21]{.title-ref} \| Arithmetic expressions can also be a single
prefix, such as here.
:::

::: {.example}
\| [21 + 10 - 5]{.title-ref} \| This formula adds the balances of the
move lines made on accounts whose codes start with [21]{.title-ref} and
[10]{.title-ref}, and subtracts the balance of the ones on accounts with
the prefix [5]{.title-ref}.
:::

It is also possible to ignore a selection of sub-prefixes.

::: {.example}
\| [21 + 10(101, 102) - 5(57)]{.title-ref} \| This formula works the
same way as the previous example but ignores the prefixes
[101]{.title-ref}, [102]{.title-ref}, and [57]{.title-ref}.
:::

You can apply \'sub-filtering\' on **credits and debits** using the
[C]{.title-ref} and [D]{.title-ref} suffixes. In this case, an account
will only be considered if its prefix matches, *and* if the total
balance of the move lines made on this account is **credit/debit**.

::: {.example}
Account [210001]{.title-ref} has a balance of -42 and account
[210002]{.title-ref} has a balance of 25. The formula [21D]{.title-ref}
only matches the account [210002]{.title-ref}, and hence returns 25.
[210001]{.title-ref} is not matched, as its balance is *credit*.
:::

Prefix exclusions can be mixed with the [C]{.title-ref} and
[D]{.title-ref} suffixes.

::: {.example}
\| [21D + 10(101, 102)C - 5(57)]{.title-ref} \| This formula adds the
balances of the move lines made on accounts whose code starts with
[21]{.title-ref} *if* it is debit ([D]{.title-ref}) and [10]{.title-ref}
*if* it is credit ([C]{.title-ref}), but ignores prefixes
[101]{.title-ref}, [102]{.title-ref}, and subtracts the balance of the
ones on accounts with the prefix [5]{.title-ref}, ignoring the prefix
[57]{.title-ref}.
:::

To match the letter [C]{.title-ref} or [D]{.title-ref} in a prefix and
not use it as a suffix, use an empty exclusion [()]{.title-ref}.

::: {.example}
\| [21D()]{.title-ref} \| This formula matches accounts whose code
starts with [21D]{.title-ref}, regardless of their balance sign.
:::

In addition to using code prefixes to include accounts, you can also
match them with **account tags**. This is especially useful, for
example, if your country lacks a standardized chart of accounts, where
the same prefix might be used for different purposes across companies.

::: {.example}
\| [tag(25)]{.title-ref} \| This formula matches accounts whose
associated tags contain the one with id *25*.
:::

If the tag you reference is defined in a data file, an xmlid can be used
instead of the id.

::: {.example}
\| [tag(my\_module.my\_tag)]{.title-ref} \| This formula matches
accounts whose associated tags include the tag denoted by
*my\_module.my\_tag*.
:::

You can also use arithmetic expressions with tags, possibly combining
them with prefix selections.

::: {.example}
\| [tag(my\_module.my\_tag) + tag(42) + 10]{.title-ref} \| The balances
of accounts tagged as *my\_module.my\_tag* will be summed with those of
accounts linked to the tag with ID *42* and accounts with the code
prefix [10]{.title-ref}
:::

[C]{.title-ref} and [D]{.title-ref} suffixes can be used in the same way
with tags.

::: {.example}
\| [tag(my\_module.my\_tag)C]{.title-ref} \| This formula matches
accounts with the tag *my\_module.my\_tag* and a credit balance.
:::

Prefix exclusion also works with tags.

::: {.example}
\| [tag(my\_module.my\_tag)(10)]{.title-ref} \| This formula matches
accounts with the tag *my\_module.my\_tag* and a code not starting with
[10]{.title-ref}.
:::

### \'External Value\' engine

The \'external value\' engine is used to refer to **manual** and
**carryover values**. Those values are not stored using
[account.move.line]{.title-ref}, but with
[account.report.external.value]{.title-ref}. Each of these objects
directly points to the expression it impacts, so very little needs to be
done about their selection here.

**Formulas** can be one of the following:

[sum]{.title-ref}

:   If the result must be the sum of all the external values in the
    period.

[most\_recent]{.title-ref}

:   If the result must be the value of the latest external value in the
    period.

In addition, **subformulas** can be used in two ways:

[rounding=X]{.title-ref}

:   Replacing [X]{.title-ref} with a number instructs to round the
    amount to X decimals.

[editable]{.title-ref}

:   Indicates this expression can be edited manually, triggering the
    display of an icon in the report, allowing the user to perform this
    action.

::: {.note}
::: {.title}
Note
:::

Manual values are created at the [date\_to]{.title-ref} currently
selected in the report.
:::

Both subformulas can be mixed by separating them with a [;]{.title-ref}.

::: {.example}
\| [editable;rounding=2]{.title-ref} \| is a correct subformula mixing
both behaviors.
:::

### \'Custom Python Function\' engine

This engine is a means for developers to introduce custom computation of
expressions on a case-by-case basis. The formula is the name of a
**python function** to call, and the subformula is a **key** to fetch in
the **dictionary** returned by this function. Use it only if you are
making a custom module of your own.

Columns
-------

Reports can have an **indefinite number** of columns to display. Each
column gets its values from the **expressions** declared on the
**lines**. The field `expression_label`{.interpreted-text
role="guilabel"} of the column gives the label of the expressions whose
value is displayed. If a line has no **expression** in that field, then
nothing is displayed for it in this column. If multiple columns are
required, you must use different **expression** labels.

{.align-center}

When using the **period comparison** feature found under the
`Options`{.interpreted-text role="guilabel"} tab of an accounting
report, all columns are repeated in and for each period.
