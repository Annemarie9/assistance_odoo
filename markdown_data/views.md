# File: /content/odoo_doc17.0/fr/content/applications/studio/views.md

Views
=====

Views are the interface that allows displaying the data contained in a
`model
<models_modules_apps>`{.interpreted-text role="doc"}. One model can have
several views, which are simply different ways to show the same data. In
Studio, views are organized into four categories: `general
<studio/views/general>`{.interpreted-text role="ref"},
`multiple records <studio/views/multiple-records>`{.interpreted-text
role="ref"}, `timeline
<studio/views/timeline>`{.interpreted-text role="ref"}, and
`reporting <studio/views/reporting>`{.interpreted-text role="ref"}.

::: {.tip}
::: {.title}
Tip
:::

\- To change the default view of a model,
`access Studio <studio/access>`{.interpreted-text role="ref"}, go to
`Views`{.interpreted-text role="guilabel"}, click the
`fa-ellipsis-v`{.interpreted-text role="icon"}
(`ellipsis`{.interpreted-text role="guilabel"}) icon next to the desired
view, and click `Set as Default`{.interpreted-text role="guilabel"}. -
You can modify views using the built-in XML editor: Activate the
`Developer mode
<developer-mode>`{.interpreted-text role="ref"}, go to the view you want
to edit, select the `View`{.interpreted-text role="guilabel"} tab, and
click `</> XML`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

If you are editing a view using the XML editor, avoid making changes
directly to standard and inherited views, as these would be reset and
lost during updates or module upgrades. Always make sure you select the
right Studio inherited views: When you modify a view in Studio by
dragging and dropping a new field, for example, a specific Studio
inherited view and its corresponding XPath, which defines the modified
part of the view, are automatically generated.
:::
:::

General views {#studio/views/general}
-------------

::: {.note}
::: {.title}
Note
:::

The settings described below are found under the view\'s
`View`{.interpreted-text role="guilabel"} tab unless specified
otherwise.
:::

### Form {#studio/views/general/form}

The `Form`{.interpreted-text role="guilabel"}
`fa-address-card`{.interpreted-text role="icon"} view is used when
creating and editing records, such as contacts, sales orders, products,
etc.

-   To structure a form, drag and drop the
    `Tabs and Columns`{.interpreted-text role="guilabel"} element found
    under the `+ Add`{.interpreted-text role="guilabel"} tab.
-   To prevent users from creating, editing, or deleting records, untick
    `Can Create`{.interpreted-text role="guilabel"},
    `Can Edit`{.interpreted-text role="guilabel"}, or
    `Can Delete`{.interpreted-text role="guilabel"}.
-   To add a button, click `Add a button`{.interpreted-text
    role="guilabel"} at the top of the form, enter a
    `Label`{.interpreted-text role="guilabel"}, and select the button\'s
    action:
    -   `Run a Server Action`{.interpreted-text role="guilabel"}: select
        the `server action <reference/actions/server>`{.interpreted-text
        role="ref"} to be executed from the dropdown list;
    -   `Call a method`{.interpreted-text role="guilabel"}: specify an
        existing Python method already defined in Odoo.
-   To add a smart button, click the `fa-plus-square`{.interpreted-text
    role="icon"} (`plus`{.interpreted-text role="guilabel"}) icon in the
    top-right corner of the form. Enter a `Label`{.interpreted-text
    role="guilabel"}, choose an `Icon`{.interpreted-text
    role="guilabel"}, and select a
    `related field <studio/fields/relational-fields-related-field>`{.interpreted-text
    role="ref"}.

::: {.example}

:::

### Activity {#studio/views/general/activity}

The `Activity`{.interpreted-text role="guilabel"}
`fa-clock-o`{.interpreted-text role="icon"} view is used to schedule and
have an overview of activities (emails, calls, etc.) linked to records.

::: {.note}
::: {.title}
Note
:::

This view can only be modified within Studio by editing the XML code.
:::

::: {.example}

:::

### Search {#studio/views/general/search}

The `Search`{.interpreted-text role="guilabel"}
`oi-search`{.interpreted-text role="icon"} view is added on top of other
views to filter, group, and search records.

-   To add custom `Filters`{.interpreted-text role="guilabel"} and
    structure them using `Separators`{.interpreted-text
    role="guilabel"}, go to the `+ Add`{.interpreted-text
    role="guilabel"} tab and drag and drop them under
    `Filters`{.interpreted-text role="guilabel"}.
-   To add an existing field under the search dropdown menu, go to the
    `+ Add`{.interpreted-text role="guilabel"} tab and drag and drop it
    under `Autocompletion Fields`{.interpreted-text role="guilabel"}.

::: {.example}

:::

Multiple records views {#studio/views/multiple-records}
----------------------

::: {.note}
::: {.title}
Note
:::

The settings described below are found under the view\'s
`View`{.interpreted-text role="guilabel"} tab unless specified
otherwise.
:::

### Kanban {#studio/views/multiple-records/kanban}

The `Kanban`{.interpreted-text role="guilabel"}
`oi-view-kanban`{.interpreted-text role="icon"} view is often used to
support business flows by moving records across stages or as an
alternative way to display records inside *cards*.

::: {.note}
::: {.title}
Note
:::

If the `Kanban`{.interpreted-text role="guilabel"} view exists, it is
used by default to display data on mobile devices instead of the
`List view <studio/views/multiple-records/list>`{.interpreted-text
role="ref"}.
:::

-   To prevent users from creating new records, untick
    `Can Create`{.interpreted-text role="guilabel"}.
-   To create records directly within the view, in a minimalistic form,
    enable `Quick
    Create`{.interpreted-text role="guilabel"}.
-   To set a default grouping for records, select a field under
    `Default Group By`{.interpreted-text role="guilabel"}.

::: {.example}

:::

### List {#studio/views/multiple-records/list}

The `List`{.interpreted-text role="guilabel"}
`oi-view-list`{.interpreted-text role="icon"} view is used to overview
many records at once, look for records, and edit simple records.

-   To prevent users from creating, editing, or deleting records, untick
    `Can Create`{.interpreted-text role="guilabel"},
    `Can Edit`{.interpreted-text role="guilabel"}, or
    `Can Delete`{.interpreted-text role="guilabel"}.

-   To create and edit records directly within the view, select either
    `Add record at the
    bottom`{.interpreted-text role="guilabel"},
    `Add record on top`{.interpreted-text role="guilabel"} or
    `Open form view`{.interpreted-text role="guilabel"} under
    `When Creating Record`{.interpreted-text role="guilabel"}.

    ::: {.note}
    ::: {.title}
    Note
    :::

    This prevents users from opening records in
    `Form view <studio/views/general/form>`{.interpreted-text
    role="ref"} from the `List`{.interpreted-text role="guilabel"} view.
    :::

-   To edit several records at once, tick
    `Enable Mass Editing`{.interpreted-text role="guilabel"}.

-   To change the way records are sorted by default, select a field
    under `Sort By`{.interpreted-text role="guilabel"}.

-   To set a default grouping for records, select a field under
    `Default Group By`{.interpreted-text role="guilabel"}.

-   To add a button, click `Add a button`{.interpreted-text
    role="guilabel"} at the top of the list, enter a
    `Label`{.interpreted-text role="guilabel"}, and select the button\'s
    action:

    -   `Run a Server Action`{.interpreted-text role="guilabel"}: select
        the `server action <reference/actions/server>`{.interpreted-text
        role="ref"} to be executed from the dropdown list;
    -   `Call a method`{.interpreted-text role="guilabel"}: specify an
        existing Python method already defined in Odoo.

::: {.tip}
::: {.title}
Tip
:::

To add a `oi-draggable`{.interpreted-text role="icon"}
(`drag handle`{.interpreted-text role="guilabel"}) icon to reorder
records manually, add an
`Integer field <studio/fields/simple-fields-integer>`{.interpreted-text
role="ref"} with the `Handle`{.interpreted-text role="guilabel"} widget.


:::

::: {.example}

:::

### Map {#studio/views/multiple-records/map}

The `Map`{.interpreted-text role="guilabel"}
`fa-map-marker`{.interpreted-text role="icon"} view is used to display
records on a map. For example, it is used in the Field Service app to
plan an itinerary between different tasks.

::: {.note}
::: {.title}
Note
:::

A
`Many2One field <studio/fields/relational-fields-many2one>`{.interpreted-text
role="ref"} linked to the *Contact* model is required to activate the
view, as the contact address is used to position records on the map.
:::

-   To select which kind of contact should be used on the map, select it
    under `Contact
    Field`{.interpreted-text role="guilabel"}.
-   To hide the name or the address of the record, tick
    `Hide Name`{.interpreted-text role="guilabel"} or `Hide
    Address`{.interpreted-text role="guilabel"}.
-   To add information from other fields, select them under
    `Additional Fields`{.interpreted-text role="guilabel"}.
-   To have a route suggested between the different records, tick
    `Enable Routing`{.interpreted-text role="guilabel"} and select which
    field should be used to sort records for the routing.

::: {.example}

:::

Timeline views {#studio/views/timeline}
--------------

::: {.note}
::: {.title}
Note
:::

\- When you first activate one of the timeline views, you need to select
which `Date
<studio/fields/simple-fields-date>`{.interpreted-text role="ref"} or
`Date & Time
<studio/fields/simple-fields-date-time>`{.interpreted-text role="ref"}
fields on your model should be used to define when the records start and
stop in order to display them on the view. You can modify the
`Start Date Field`{.interpreted-text role="guilabel"} and
`Stop Date Field`{.interpreted-text role="guilabel"} after activating
the view. - The settings described below are found under the view\'s
`View`{.interpreted-text role="guilabel"} tab unless specified
otherwise.
:::

### Calendar {#studio/views/timeline/calendar}

The `Calendar`{.interpreted-text role="guilabel"}
`fa-calendar`{.interpreted-text role="icon"} view is used to overview
and manage records inside a calendar.

-   To create records directly within the view instead of opening the
    `Form view
    <studio/views/general/form>`{.interpreted-text role="ref"}, enable
    `Quick Create`{.interpreted-text role="guilabel"}.

    ::: {.note}
    ::: {.title}
    Note
    :::

    This only works on specific models that can be *quick-created* using
    only a *name*. However, most models do not support quick creation
    and open the `Form`{.interpreted-text role="guilabel"} view to fill
    in the required fields.
    :::

-   To color records on the calendar, select a field under
    `Color`{.interpreted-text role="guilabel"}. All the records sharing
    the same value for that field are displayed using the same color.

    ::: {.note}
    ::: {.title}
    Note
    :::

    As the number of colors is limited, the same color can end up being
    assigned to different values.
    :::

-   To display events lasting the whole day at the top of the calendar,
    select a `Checkbox field
    <studio/fields/simple-fields-checkbox>`{.interpreted-text
    role="ref"} that specifies if the event lasts the whole day.

-   To choose the default time scale used to display events, select
    `Day`{.interpreted-text role="guilabel"}, `Week`{.interpreted-text
    role="guilabel"}, `Month`{.interpreted-text role="guilabel"}, or
    `Year`{.interpreted-text role="guilabel"} under
    `Default Display Mode`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

You can also use a `Delay Field`{.interpreted-text role="guilabel"} to
display the duration of the event in hours by selecting a
`Decimal <studio/fields/simple-fields-decimal>`{.interpreted-text
role="ref"} or `Integer
<studio/fields/simple-fields-integer>`{.interpreted-text role="ref"}
field on the model which specifies the duration of the event. However,
if you set an `End Date Field`{.interpreted-text role="guilabel"}, the
`Delay Field`{.interpreted-text role="guilabel"} will not be taken into
account.
:::

::: {.example}

:::

### Cohort {#studio/views/timeline/cohort}

The `Cohort`{.interpreted-text role="guilabel"}
`oi-view-cohort`{.interpreted-text role="icon"} view is used to examine
the life cycle of records over a time period. For example, it is used in
the Subscriptions app to view the subscriptions\' retention rate.

-   To display a measure (i.e., the aggregated value of a given field)
    by default on the view, select a `Measure Field`{.interpreted-text
    role="guilabel"}.
-   To choose which time interval is used by default to group results,
    select `Day`{.interpreted-text role="guilabel"},
    `Week`{.interpreted-text role="guilabel"}, `Month`{.interpreted-text
    role="guilabel"}, or `Year`{.interpreted-text role="guilabel"} under
    `Interval`{.interpreted-text role="guilabel"}.
-   To change the cohort `Mode`{.interpreted-text role="guilabel"},
    select either `Retention`{.interpreted-text role="guilabel"}
    `the percentage
    of records staying over a period of time, it starts at 100% and decreases with time`{.interpreted-text
    role="dfn"} or `Churn`{.interpreted-text role="guilabel"}
    `the percentage of records moving out over a period of time - it starts at
    0% and increases with time`{.interpreted-text role="dfn"}.
-   To change the way the `Timeline`{.interpreted-text role="guilabel"}
    (i.e., the columns) progresses, select either
    `Forward`{.interpreted-text role="guilabel"} (from 0 to +15) or
    `Backward`{.interpreted-text role="guilabel"} (from -15 to 0). For
    most purposes, the `Forward`{.interpreted-text role="guilabel"}
    timeline is used.

::: {.example}

:::

### Gantt {#studio/views/timeline/gantt}

The `Gantt`{.interpreted-text role="guilabel"}
`fa-tasks`{.interpreted-text role="icon"} view is used to forecast and
examine the overall progress of records. Records are represented by a
bar under a time scale.

-   To prevent users from creating or editing records, untick
    `Can Create`{.interpreted-text role="guilabel"} or `Can
    Edit`{.interpreted-text role="guilabel"}.

-   To fill cells in gray whenever a record should not be created there
    (e.g., on weekends for employees), tick
    `Display Unavailability`{.interpreted-text role="guilabel"}.

    ::: {.note}
    ::: {.title}
    Note
    :::

    The underlying model must support this feature, and support for it
    cannot be added using Studio. It is supported for the Project, Time
    Off, Planning, and Manufacturing apps.
    :::

-   To show a total row at the bottom, tick
    `Display Total row`{.interpreted-text role="guilabel"}.

-   To collapse multiple records in a single row, tick
    `Collapse First Level`{.interpreted-text role="guilabel"}.

-   To choose which way records are grouped by default on rows (e.g.,
    per employee or project), select a field under
    `Default Group by`{.interpreted-text role="guilabel"}.

-   To define a default time scale to view records, select
    `Day`{.interpreted-text role="guilabel"}, `Week`{.interpreted-text
    role="guilabel"}, `Month`{.interpreted-text role="guilabel"}, or
    `Year`{.interpreted-text role="guilabel"} under
    `Default Scale`{.interpreted-text role="guilabel"}.

-   To color records on the view, select a field under
    `Color`{.interpreted-text role="guilabel"}. All the records sharing
    the same value for that field are displayed using the same color.

    ::: {.note}
    ::: {.title}
    Note
    :::

    As the number of colors is limited, the same color can be assigned
    to different values.
    :::

-   To specify with which degree of precision each time scale should be
    divided by, select `Quarter Hour`{.interpreted-text
    role="guilabel"}, `Half Hour`{.interpreted-text role="guilabel"}, or
    `Hour`{.interpreted-text role="guilabel"} under `Day
    Precision`{.interpreted-text role="guilabel"},
    `Half Day`{.interpreted-text role="guilabel"} or
    `Day`{.interpreted-text role="guilabel"} under
    `Week Precision`{.interpreted-text role="guilabel"}, and
    `Month Precision`{.interpreted-text role="guilabel"}.

::: {.example}

:::

Reporting views {#studio/views/reporting}
---------------

::: {.note}
::: {.title}
Note
:::

The settings described below are found under the view\'s
`View`{.interpreted-text role="guilabel"} tab unless specified
otherwise.
:::

### Pivot {#studio/views/reporting/pivot}

The `Pivot`{.interpreted-text role="guilabel"}
`oi-view-pivot`{.interpreted-text role="icon"} view is used to explore
and analyze the data contained in records in an interactive manner. It
is especially useful to aggregate numeric data, create categories, and
drill down the data by expanding and collapsing different levels of
data.

-   To access all records whose data is aggregated under a cell, tick
    `Access records from
    cell`{.interpreted-text role="guilabel"}.
-   To divide the data into different categories, select field(s) under
    `Column grouping`{.interpreted-text role="guilabel"},
    `Row grouping - First level`{.interpreted-text role="guilabel"}, or
    `Row grouping - Second level`{.interpreted-text role="guilabel"}.
-   To add different types of data to be measured using the view, select
    a field under `Measures`{.interpreted-text role="guilabel"}.
-   To display a count of records that made up the aggregated data in a
    cell, tick `Display
    count`{.interpreted-text role="guilabel"}.

::: {.example}

:::

### Graph {#studio/views/reporting/graph}

The `Graph`{.interpreted-text role="guilabel"}
`fa-area-chart`{.interpreted-text role="icon"} view is used to showcase
data from records in a bar, line, or pie chart.

-   To change the default chart, select `Bar`{.interpreted-text
    role="guilabel"}, `Line`{.interpreted-text role="guilabel"}, or
    `Pie`{.interpreted-text role="guilabel"} under
    `Type`{.interpreted-text role="guilabel"}.
-   To choose a default data dimension (category), select a field under
    `First dimension`{.interpreted-text role="guilabel"} and, if needed,
    another under `Second dimension`{.interpreted-text role="guilabel"}.
-   To select a default type of data to be measured using the view,
    select a field under `Measure`{.interpreted-text role="guilabel"}.
-   *For Bar and Line charts only*: To sort the different data
    categories by their value, select `Ascending`{.interpreted-text
    role="guilabel"} (from lowest to highest value) or
    `Descending`{.interpreted-text role="guilabel"} (from highest to
    lowest) under `Sorting`{.interpreted-text role="guilabel"}.
-   *For Bar and Pie charts only*: To access all records whose data is
    aggregated under a data category on the chart, tick
    `Access records from graph`{.interpreted-text role="guilabel"}.
-   *For Bar charts only*: When using two data dimensions (categories),
    display the two columns on top of each other by default by ticking
    `Stacked graph`{.interpreted-text role="guilabel"}.

::: {.example}

:::
