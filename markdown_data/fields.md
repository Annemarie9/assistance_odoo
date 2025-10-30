# File: /content/odoo_doc17.0/fr/content/applications/studio/fields.md

Fields and widgets
==================

Fields structure the models of a database. If you picture a model as a
table or spreadsheet, fields are the columns where data is stored in the
records (i.e., the rows). Fields also define the type of data that is
stored within them. How the data is presented and formatted on the
`UI (User
Interface)`{.interpreted-text role="abbr"} is defined by their widget.

From a technical point of view, there are 15 field types in Odoo.
However, you can choose from 20 fields in Studio, as some field types
are available more than once with a different default widget.

::: {.tip}
::: {.title}
Tip
:::

`New Fields`{.interpreted-text role="guilabel"} can only be added to the
`studio/views/general/form`{.interpreted-text role="ref"} and
`studio/views/multiple-records/list`{.interpreted-text role="ref"}
views. On other views, you can only add
`Existing Fields`{.interpreted-text role="guilabel"}
`(fields already on the model)`{.interpreted-text role="dfn"}.
:::

Simple fields {#studio/fields/simple-fields}
-------------

Simple fields contain basic values, such as text, numbers, files, etc.

::: {.note}
::: {.title}
Note
:::

Non-default widgets, when available, are presented as bullet points or
sub-headings below.
:::

### Text ([char]{.title-ref}) {#studio/fields/simple-fields-text}

The `Text`{.interpreted-text role="guilabel"} field is used for short
text containing any character. One text line is displayed when filling
out the field.

-   `Badge`{.interpreted-text role="guilabel"}: displays the value
    inside a rounded shape, similar to a tag. The value cannot be edited
    on the UI, but a default value can be set.

-   `Copy to Clipboard`{.interpreted-text role="guilabel"}: users can
    copy the value by clicking a button.

-   `E-mail`{.interpreted-text role="guilabel"}: the value becomes a
    clickable *mailto* link.

-   `Image`{.interpreted-text role="guilabel"}: displays an image using
    a URL. The value cannot be edited manually, but a default value can
    be set.

    ::: {.note}
    ::: {.title}
    Note
    :::

    This works differently than selecting the `Image field
    <studio/fields/simple-fields-image>`{.interpreted-text role="ref"}
    directly, as the image is not stored in Odoo when using a
    `Text`{.interpreted-text role="guilabel"} field with the
    `Image`{.interpreted-text role="guilabel"} widget. For example, it
    can be useful if you want to save disk space.
    :::

-   `Phone`{.interpreted-text role="guilabel"}: the value becomes a
    clickable *tel* link.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    Tick `Enable SMS`{.interpreted-text role="guilabel"} to add an
    option to send an SMS directly from Odoo next to the field.
    :::

-   `URL`{.interpreted-text role="guilabel"}: the value becomes a
    clickable URL.

::: {.example}

:::

### Multiline Text ([text]{.title-ref}) {#studio/fields/simple-fields-multiline-text}

The `Multiline Text`{.interpreted-text role="guilabel"} field is used
for longer text containing any type of character. Two text lines are
displayed on the UI when filling out the field.

-   `Copy to Clipboard`{.interpreted-text role="guilabel"}: users can
    copy the value by clicking a button.

::: {.example}

:::

### Integer ([integer]{.title-ref}) {#studio/fields/simple-fields-integer}

The `Integer`{.interpreted-text role="guilabel"} field is used for all
integer numbers (`positive, negative, or zero,
without a decimal`{.interpreted-text role="dfn"}).

-   `Percentage Pie`{.interpreted-text role="guilabel"}: displays the
    value inside a percentage circle, usually for a computed value. The
    value cannot be edited on the UI, but a default value can be set.
-   `Progress Bar`{.interpreted-text role="guilabel"}: displays the
    value next to a percentage bar, usually for a computed value. The
    field cannot be edited manually, but a default value can be set.
-   `Handle`{.interpreted-text role="guilabel"}: displays a drag handle
    icon to order records manually in `List view
    <studio/views/multiple-records/list>`{.interpreted-text role="ref"}.

::: {.example}

:::

### Decimal ([float]{.title-ref}) {#studio/fields/simple-fields-decimal}

The `Decimal`{.interpreted-text role="guilabel"} field is used for all
decimal numbers (`positive, negative, or zero,
with a decimal`{.interpreted-text role="dfn"}).

::: {.note}
::: {.title}
Note
:::

Decimal numbers are displayed with two decimals after the decimal point
on the UI, but they are stored in the database with more precision.
:::

-   `Monetary`{.interpreted-text role="guilabel"}: it is similar to
    using the `Monetary field
    <studio/fields/simple-fields-monetary>`{.interpreted-text
    role="ref"}. It is recommended to use the latter as it offers more
    functionalities.
-   `Percentage`{.interpreted-text role="guilabel"}: displays a percent
    character [%]{.title-ref} after the value.
-   `Percentage Pie`{.interpreted-text role="guilabel"}: displays the
    value inside a percentage circle, usually for a computed value. The
    field cannot be edited manually, but a default value can be set.
-   `Progress Bar`{.interpreted-text role="guilabel"}: displays the
    value next to a percentage bar, usually for a computed value. The
    field cannot be edited manually, but a default value can be set.
-   `Time`{.interpreted-text role="guilabel"}: the value must follow the
    *hh:mm* format, with a maximum of 59 minutes.

::: {.example}

:::

### Monetary ([monetary]{.title-ref}) {#studio/fields/simple-fields-monetary}

The `Monetary`{.interpreted-text role="guilabel"} field is used for all
monetary values.

::: {.note}
::: {.title}
Note
:::

When you first add a `Monetary`{.interpreted-text role="guilabel"}
field, you are prompted to add a `Currency`{.interpreted-text
role="guilabel"} field if none exists already on the model. Odoo offers
to add the `Currency`{.interpreted-text role="guilabel"} field for you.
Once it is added, add the `Monetary`{.interpreted-text role="guilabel"}
field again.
:::

::: {.example}

:::

### Html ([html]{.title-ref}) {#studio/fields/simple-fields-html}

The `Html`{.interpreted-text role="guilabel"} field is used to add text
that can be edited using the Odoo HTML editor.

-   `Multiline Text`{.interpreted-text role="guilabel"}: disables the
    Odoo HTML editor to allow editing raw HTML.

::: {.example}

:::

### Date ([date]{.title-ref}) {#studio/fields/simple-fields-date}

The `Date`{.interpreted-text role="guilabel"} field is used to select a
date on a calendar.

-   `Remaining Days`{.interpreted-text role="guilabel"}: the remaining
    number of days before the selected date is displayed (e.g., *In 5
    days*), based on the current date. This field should be set to
    `Read only`{.interpreted-text role="guilabel"}.

::: {.example}

:::

### Date & Time ([datetime]{.title-ref}) {#studio/fields/simple-fields-date-time}

The `Date & Time`{.interpreted-text role="guilabel"} field is used to
select a date on a calendar and a time on a clock. The user\'s current
time is automatically used if no time is set.

::: {.tip}
::: {.title}
Tip
:::

As well as
`general properties <studio/fields/properties>`{.interpreted-text
role="ref"}, some
`specific properties <studio/fields/properties-date-datetime>`{.interpreted-text
role="ref"} are available for `Date & Time`{.interpreted-text
role="guilabel"} fields that have the `Date & Time`{.interpreted-text
role="guilabel"} or `Date Range`{.interpreted-text role="guilabel"}
widget set.
:::

#### Date Range ([daterange]{.title-ref})

The `Date Range`{.interpreted-text role="guilabel"} widget is used to
display a period of time defined by a start date and an end date in a
single line. A date range can have a mandatory start and end date, e.g.,
for a multi-day event, or allow an optional start or end date, e.g., for
a field service intervention or a project task.

Adding a date range requires two fields: a
`Date & Time`{.interpreted-text role="guilabel"} field with the
`Date Range`{.interpreted-text role="guilabel"} widget set and another
field that is selected as the start date *or* end date. This underlying
field can be an existing
`Date <studio/fields/simple-fields-date>`{.interpreted-text role="ref"}
or `Date & Time`{.interpreted-text role="guilabel"} field, or one
created specifically for this purpose.

To add a date range:

1.  Identify an existing `Date`{.interpreted-text role="guilabel"} or
    `Date & Time`{.interpreted-text role="guilabel"} field that can be
    used as the underlying start/end date field, or add a new one. If
    the date range:

    -   has a mandatory start date and end date, this field can be
        either the start date or end date; the outcome is the same.
    -   allows an optional start or end date, this field is the start
        date or end date, respectively.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    To avoid displaying the same information twice, the underlying
    start/end date field can be made invisible by enabling
    `Invisible`{.interpreted-text role="guilabel"} or removed from the
    view by clicking `Remove from view`{.interpreted-text
    role="guilabel"}.
    :::

2.  Add a `Date & Time`{.interpreted-text role="guilabel"} field and set
    the `Widget`{.interpreted-text role="guilabel"} field to
    `Date Range`{.interpreted-text role="guilabel"}.

3.  Enter an appropriate `Label`{.interpreted-text role="guilabel"}.

4.  Select the underlying start/end date field from the
    `Start date field`{.interpreted-text role="guilabel"} or
    `End date field`{.interpreted-text role="guilabel"} dropdown, as
    relevant.

5.  If the date range should have a mandatory start and end date, enable
    `Always range`{.interpreted-text role="guilabel"}.

6.  Update any other
    `general properties <studio/fields/properties>`{.interpreted-text
    role="ref"} or specific
    `properties for Date & Time fields <studio/fields/properties-date-datetime>`{.interpreted-text
    role="ref"} as needed, then click `Close`{.interpreted-text
    role="guilabel"} in the upper right corner of the screen.

::: {.example}

:::

#### Remaining Days ([remaining\_days]{.title-ref})

The `Remaining Days`{.interpreted-text role="guilabel"} widget displays
the remaining number of days before the selected date (e.g., *In 5
days*), based on the current date and time. This field should be set to
`Read
only`{.interpreted-text role="guilabel"}.

### Checkbox ([boolean]{.title-ref}) {#studio/fields/simple-fields-checkbox}

The `Checkbox`{.interpreted-text role="guilabel"} field is used when a
value should only be true or false, indicated by checking or unchecking
a checkbox.

-   `Button`{.interpreted-text role="guilabel"}: displays a radio
    button. The widget works without switching to the edit mode.
-   `Toggle`{.interpreted-text role="guilabel"}: displays a toggle
    button. The widget works without switching to the edit mode.

::: {.example}

:::

### Selection ([selection]{.title-ref}) {#studio/fields/simple-fields-selection}

The `Selection`{.interpreted-text role="guilabel"} field is used when
users should select a single value from a group of predefined values.

-   `Badge`{.interpreted-text role="guilabel"}: displays the value
    inside a rounded shape, similar to a tag. The value cannot be edited
    on the UI, but a default value can be set.

-   `Badges`{.interpreted-text role="guilabel"}: displays all selectable
    values simultaneously inside rectangular shapes, organized
    horizontally.

-   `Priority`{.interpreted-text role="guilabel"}: displays star symbols
    instead of values, which can be used to indicate an importance or
    satisfaction level, for example. This has the same effect as
    selecting the
    `Priority field <studio/fields/simple-fields-priority>`{.interpreted-text
    role="ref"}, although, for the latter, four priority values are
    already predefined.

-   `Radio`{.interpreted-text role="guilabel"}: displays all selectable
    values at the same time as radio buttons.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    By default, radio buttons are organized vertically. Enable
    `Display horizontally`{.interpreted-text role="guilabel"} to switch
    the way they are displayed.
    :::

-   `Status Bar`{.interpreted-text role="guilabel"}: displays all
    selectable values at the same time as an arrow progress bar.

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    By default, values on the status bar are selectable. Disable
    `Clickable`{.interpreted-text role="guilabel"} to prevent the value
    being edited on the UI.
    :::

::: {.example}

:::

### Priority ([selection]{.title-ref}) {#studio/fields/simple-fields-priority}

The `Priority`{.interpreted-text role="guilabel"} field is used to
display a three-star rating system, which can be used to indicate
importance or satisfaction level. This field type is a `Selection field
<studio/fields/simple-fields-selection>`{.interpreted-text role="ref"}
with the `Priority`{.interpreted-text role="guilabel"} widget selected
by default and four priority values predefined. Consequently, the
`Badge`{.interpreted-text role="guilabel"}, `Badges`{.interpreted-text
role="guilabel"}, `Radio`{.interpreted-text role="guilabel"}, and
`Selection`{.interpreted-text role="guilabel"} widgets have the same
effects as described under
`Selection <studio/fields/simple-fields-selection>`{.interpreted-text
role="ref"}.

::: {.tip}
::: {.title}
Tip
:::

To change the number of available stars by adding or removing values,
click `Edit
Values`{.interpreted-text role="guilabel"}. Note that the first value is
equal to 0 stars (i.e., when no selection is made), so having four
values results in a three-star rating system, for example.
:::

::: {.example}

:::

### File ([binary]{.title-ref}) {#studio/fields/simple-fields-file}

The `File`{.interpreted-text role="guilabel"} field is used to upload
any type of file, or sign a form (`Sign`{.interpreted-text
role="guilabel"} widget).

-   `Image`{.interpreted-text role="guilabel"}: users can upload an
    image file, which is then displayed in `Form view
    <studio/views/general/form>`{.interpreted-text role="ref"}. This has
    the same effect as using the `Image field
    <studio/fields/simple-fields-image>`{.interpreted-text role="ref"}.
-   `PDF Viewer`{.interpreted-text role="guilabel"}: users can upload a
    PDF file, which can be then browsed from the
    `Form view <studio/views/general/form>`{.interpreted-text
    role="ref"}.
-   `Sign`{.interpreted-text role="guilabel"}: users can electronically
    sign the form. This has the same effect as selecting the
    `Sign field <studio/fields/simple-fields-sign>`{.interpreted-text
    role="ref"}.

::: {.example}

:::

### Image ([binary]{.title-ref}) {#studio/fields/simple-fields-image}

The `Image`{.interpreted-text role="guilabel"} field is used to upload
an image and display it in `Form view
<studio/views/general/form>`{.interpreted-text role="ref"}. This field
type is a `File field
<studio/fields/simple-fields-file>`{.interpreted-text role="ref"} with
the `Image`{.interpreted-text role="guilabel"} widget selected by
default. Consequently, the `File`{.interpreted-text role="guilabel"},
`PDF Viewer`{.interpreted-text role="guilabel"}, and
`Sign`{.interpreted-text role="guilabel"} widgets have the same effects
as described under
`File <studio/fields/simple-fields-file>`{.interpreted-text role="ref"}.

::: {.tip}
::: {.title}
Tip
:::

To change the display size of uploaded images, select
`Small`{.interpreted-text role="guilabel"}, `Medium`{.interpreted-text
role="guilabel"}, or `Large`{.interpreted-text role="guilabel"} under
the `Size`{.interpreted-text role="guilabel"} option.
:::

### Sign ([binary]{.title-ref}) {#studio/fields/simple-fields-sign}

The `Sign`{.interpreted-text role="guilabel"} field is used to sign the
form electronically. This field type is a `File
field <studio/fields/simple-fields-file>`{.interpreted-text role="ref"}
with the `Sign`{.interpreted-text role="guilabel"} widget selected by
default. Consequently, the `File`{.interpreted-text role="guilabel"},
`Image`{.interpreted-text role="guilabel"}, and
`PDF Viewer`{.interpreted-text role="guilabel"} widgets have the same
effects as described under
`File <studio/fields/simple-fields-file>`{.interpreted-text role="ref"}.

::: {.tip}
::: {.title}
Tip
:::

To give users the `Auto`{.interpreted-text role="guilabel"} option when
having to draw their signature, select one of the available
`Auto-complete with`{.interpreted-text role="guilabel"} fields
(`Text <studio/fields/simple-fields-text>`{.interpreted-text
role="ref"},
`Many2One <studio/fields/relational-fields-many2one>`{.interpreted-text
role="ref"}, and `Related Field
<studio/fields/relational-fields-related-field>`{.interpreted-text
role="ref"} on the model only). The signature is automatically generated
using the data from the selected field.
:::

Relational fields {#studio/fields/relational-fields}
-----------------

Relational fields are used to link and display the data from records on
another model.

::: {.note}
::: {.title}
Note
:::

Non-default widgets, when available, are presented as bullet points
below.
:::

### Many2One ([many2one]{.title-ref}) {#studio/fields/relational-fields-many2one}

The `Many2One`{.interpreted-text role="guilabel"} field is used to link
another record (from another model) to the record being edited. The
record\'s name from the other model is then displayed on the record
being edited.

::: {.example}
On the *Sales Order* model, the `Customer`{.interpreted-text
role="guilabel"} field is a `Many2One`{.interpreted-text
role="guilabel"} field pointing at the *Contact* model. This allows
**many** sales orders to be linked to **one** contact (customer).


:::

::: {.tip}
::: {.title}
Tip
:::

\- To prevent users from creating a new record in the linked model, tick
`Disable
creation`{.interpreted-text role="guilabel"}. - To prevent users from
opening records in a pop-up window, tick
`Disable opening`{.interpreted-text role="guilabel"}. - To help users
only select the right record, click on `Domain`{.interpreted-text
role="guilabel"} to create a filter.
:::

-   `Badge`{.interpreted-text role="guilabel"}: displays the value
    inside a rounded shape, similar to a tag. The value cannot be edited
    on the UI.
-   `Radio`{.interpreted-text role="guilabel"}: displays all selectable
    values at the same time as radio buttons.

### One2Many ([one2many]{.title-ref}) {#studio/fields/relational-fields-one2many}

The `One2Many`{.interpreted-text role="guilabel"} field is used to
display the existing relations between a record on the current model and
multiple records from another model.

::: {.example}
You could add a `One2Many`{.interpreted-text role="guilabel"} field on
the *Contact* model to look at **one** customer\'s **many** sales
orders.


:::

::: {.note}
::: {.title}
Note
:::

To use a `One2Many`{.interpreted-text role="guilabel"} field, the two
models must have been linked already using a
`Many2One field <studio/fields/relational-fields-many2one>`{.interpreted-text
role="ref"}. One2Many relations do not exist independently: a
reverse-search of existing Many2One relations is performed.
:::

### Lines ([one2many]{.title-ref}) {#studio/fields/relational-fields-lines}

The `Lines`{.interpreted-text role="guilabel"} field is used to create a
table with rows and columns (e.g., the lines of products on a sales
order).

::: {.tip}
::: {.title}
Tip
:::

To modify the columns, click on the `Lines`{.interpreted-text
role="guilabel"} field and then `Edit List View`{.interpreted-text
role="guilabel"}. To edit the form that pops up when a user clicks on
`Add a line`{.interpreted-text role="guilabel"}, click on
`Edit Form View`{.interpreted-text role="guilabel"} instead.
:::

::: {.example}

:::

### Many2Many ([many2many]{.title-ref}) {#studio/fields/relational-fields-many2many}

The `Many2Many`{.interpreted-text role="guilabel"} field is used to link
multiple records from another model to multiple records on the current
model. Many2Many fields can use `Disable creation`{.interpreted-text
role="guilabel"}, `Disable opening`{.interpreted-text role="guilabel"},
`Domain`{.interpreted-text role="guilabel"}, just like `Many2One fields
<studio/fields/relational-fields-many2one>`{.interpreted-text
role="ref"}.

::: {.example}
On the *Task* model, the `Assignees`{.interpreted-text role="guilabel"}
field is a `Many2Many`{.interpreted-text role="guilabel"} field pointing
at the *Contact* model. This allows a single user to be assigned to
**many** tasks and **many** users to be assigned to a single task.


:::

-   `Checkboxes`{.interpreted-text role="guilabel"}: users can select
    several values using checkboxes.
-   `Tags`{.interpreted-text role="guilabel"}: users can select several
    values appearing in rounded shapes, also known as *tags*. This has
    the same effect as selecting the `Tags field
    <studio/fields/relational-fields-tags>`{.interpreted-text
    role="ref"}.

### Tags ([many2many]{.title-ref}) {#studio/fields/relational-fields-tags}

The `Tags`{.interpreted-text role="guilabel"} field is used to display
several values from another model appearing in rounded shapes, also
known as *tags*. This field type is a `Many2Many field
<studio/fields/relational-fields-many2many>`{.interpreted-text
role="ref"} with the `Tags`{.interpreted-text role="guilabel"} widget
selected by default. Consequently, the `Checkboxes`{.interpreted-text
role="guilabel"} and `Many2Many`{.interpreted-text role="guilabel"}
widgets have the same effects as described under
`Many2Many <studio/fields/relational-fields-many2many>`{.interpreted-text
role="ref"}.

::: {.tip}
::: {.title}
Tip
:::

To display tags with different background colors, tick
`Use colors`{.interpreted-text role="guilabel"}.
:::

::: {.example}

:::

### Related Field ([related]{.title-ref}) {#studio/fields/relational-fields-related-field}

A `Related Field`{.interpreted-text role="guilabel"} is not a relational
field per se; no relationship is created between models. It uses an
existing relationship to fetch and display information from another
record.

::: {.example}
To display the email address of a customer on the *Sales Order* model,
use the `Related
Field`{.interpreted-text role="guilabel"}
[partner\_id.email]{.title-ref} by selecting
`Customer`{.interpreted-text role="guilabel"} and then
`Email`{.interpreted-text role="guilabel"}.
:::

Properties {#studio/fields/properties}
----------

### General properties

-   `Invisible`{.interpreted-text role="guilabel"}: Enable this property
    when it is not necessary for users to view a field on the UI. This
    helps declutter the UI by only showing the essential fields
    depending on a specific situation.

    The `Invisible`{.interpreted-text role="guilabel"} attribute also
    applies inside Studio. To view hidden fields in Studio, click on a
    view\'s `View`{.interpreted-text role="guilabel"} tab and enable
    `Show Invisible Elements`{.interpreted-text role="guilabel"}.

-   `Required`{.interpreted-text role="guilabel"}: Enable this property
    if a field should always be completed by the user before being able
    to proceed.

-   `Readonly`{.interpreted-text role="guilabel"}: Enable this property
    if users should not be able to modify a field.

::: {.note}
::: {.title}
Note
:::

You can choose to enable `Invisible`{.interpreted-text role="guilabel"},
`Required`{.interpreted-text role="guilabel"} and
`Readonly`{.interpreted-text role="guilabel"} for specific records only
by clicking on `Conditional`{.interpreted-text role="guilabel"} and
creating a filter.

::: {.example}
On the *Form* view of the *Contact* model, the `Title`{.interpreted-text
role="guilabel"} field only appears when `Individual`{.interpreted-text
role="guilabel"} is selected, as that field would not be helpful for a
`Company`{.interpreted-text role="guilabel"} contact.
:::
:::

-   `Label`{.interpreted-text role="guilabel"}: the field\'s name on the
    UI. This is not the name used in the PostgreSQL database. To view
    and change the latter, activate the
    `developer mode <developer-mode>`{.interpreted-text role="ref"} and
    edit the `Technical Name`{.interpreted-text role="guilabel"}.
-   `Help Tooltip`{.interpreted-text role="guilabel"}: To explain the
    purpose of a field, add a description. The text is displayed inside
    a tooltip box when hovering with your mouse over the question mark
    beside the field\'s label.
-   `Widget`{.interpreted-text role="guilabel"}: To change the default
    appearance or functionality of a field, select one of the available
    widgets.
-   `Placeholder`{.interpreted-text role="guilabel"}: To provide an
    example of how a field should be completed, add placeholder text.
    The text appears in light gray until a value is entered.
-   `Default value`{.interpreted-text role="guilabel"}: To display a
    default value in a field when a record is created, add a value.
-   `Allow visibility to groups`{.interpreted-text role="guilabel"}: To
    limit which users can view the field, select one or more user access
    `groups <access-rights/groups>`{.interpreted-text role="ref"}.
-   `Forbid visibility to groups`{.interpreted-text role="guilabel"}: To
    prevent certain users from seeing the field, select one or more user
    access `groups <access-rights/groups>`{.interpreted-text
    role="ref"}.

### Properties for Date & Time fields {#studio/fields/properties-date-datetime}

For `Date & Time`{.interpreted-text role="guilabel"} fields that have
the `Date & Time`{.interpreted-text role="guilabel"} or
`Date Range`{.interpreted-text role="guilabel"} widget set, some
specific properties are available:

-   `Time interval`{.interpreted-text role="guilabel"}: Enter a value to
    determine the minute intervals shown in the time selector. For
    example, enter 15 to allow quarter-hour intervals. The default value
    is set to 5 minutes.
-   `Warning for future dates`{.interpreted-text role="guilabel"}:
    Enable this property to display a warning icon if a future date is
    selected.
-   `Show time`{.interpreted-text role="guilabel"}: This property is
    enabled by default for `Date & Time`{.interpreted-text
    role="guilabel"} fields. On a read-only field, disable the property
    to show only the date. This can keep a list view less cluttered, for
    example.
-   `Earliest accepted date`{.interpreted-text role="guilabel"}: Enter
    the earliest date that can be selected in the date selector in
    ISO-format, i.e., [YYYY-MM-DD]{.title-ref}. If the current date is
    always the earliest accepted date, enter [today]{.title-ref}. On the
    date selector, dates prior to the earliest accepted date are grayed
    out.
-   `Latest accepted date`{.interpreted-text role="guilabel"}: Enter the
    latest date that can be selected in the date selector in ISO-format,
    i.e., [YYYY-MM-DD]{.title-ref}. If the current date is always the
    latest accepted date, enter [today]{.title-ref}. On the date
    selector, dates later than the latest accepted date are grayed out.
