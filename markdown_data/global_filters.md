# File: /content/odoo_doc17.0/fr/content/applications/productivity/spreadsheet/global_filters.md

Global filters
==============

Create dynamic views of `inserted data <insert>`{.interpreted-text
role="doc"}, by mapping data source fields to *global filters* in the
Odoo **Spreadsheets** app.

::: {.note}
::: {.title}
Note
:::

The global filters are represented by the
`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 20 20"><path fill="currentColor" d="M1 3h12L7 9M5.5 6h3v11l-3-3M14 4h4v2h-4m-3 3h7v2h-7m0 3h7v2h-7"></path></svg>`{.interpreted-text
role="raw-html"} `(global filter)`{.interpreted-text role="guilabel"}
icon, and enable data that was inserted via a pivot table, list, or
chart to be filtered. Global filters differ from the *sort and filter*
feature for cell ranges represented by the `fa-filter`{.interpreted-text
role="icon"} `(filter)`{.interpreted-text role="guilabel"} icon.
:::

{.align-center}

Add filters
-----------

Navigate to the `Documents app`{.interpreted-text role="menuselection"}
and click on the desired spreadsheet, then open the
`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 20 20"><path fill="currentColor" d="M1 3h12L7 9M5.5 6h3v11l-3-3M14 4h4v2h-4m-3 3h7v2h-7m0 3h7v2h-7"></path></svg>`{.interpreted-text
role="raw-html"} `(global filter)`{.interpreted-text role="guilabel"}
filter menu.

Create a new filter by selecting one of the buttons under the
`Add a new filter...`{.interpreted-text role="guilabel"} section:

-   `Date <spreadsheet/global-filter-date>`{.interpreted-text
    role="ref"}: filter dates by matching data source date fields to a
    time range (e.g., *Month / Quarter*, *Relative Period*, or *From /
    To*).
-   `Relation <spreadsheet/global-filter-relation>`{.interpreted-text
    role="ref"}: filter records by matching data source fields to fields
    in a related model (e.g., *Lead/Opportunity*, *Sales Order*, or
    *Event Registration*).
-   `Text <spreadsheet/global-filter-text>`{.interpreted-text
    role="ref"}: filter text by matching data source text fields to a
    string of text (e.g., *Restrict values to a range* and/or provide a
    *Default value*).

::: {.note}
::: {.title}
Note
:::

Only filters that are able to be applied to the fields in the data
source are shown.
:::

### Date {#spreadsheet/global-filter-date}

The *Date* global filter enables the filtering of data sources by a
specific time range, to automatically filter on the current period, or
to offset the time range relative to the period.

With the
`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 20 20"><path fill="currentColor" d="M1 3h12L7 9M5.5 6h3v11l-3-3M14 4h4v2h-4m-3 3h7v2h-7m0 3h7v2h-7"></path></svg>`{.interpreted-text
role="raw-html"} `(global filter)`{.interpreted-text role="guilabel"}
menu open, select the `Date`{.interpreted-text role="guilabel"} button
to create a new date filter. The `Filter properties`{.interpreted-text
role="guilabel"} menu displays the following fields for configuration
below.

First, enter a name for the new date filter in the
`Label`{.interpreted-text role="guilabel"} field.

Then, select one of the three period options in the
`Time range`{.interpreted-text role="guilabel"} field:

-   `Month / Quarter`{.interpreted-text role="guilabel"}: enables a
    drop-down menu of specific months and quarters of a year (i.e.,
    *Q1*, *Q2*, *January*, etc.).
-   `Relative Period`{.interpreted-text role="guilabel"}: enables a
    drop-down menu of specific moving time frames (i.e., *Year to Date*,
    *Last 7 Days*, *Last 30 Days*, etc.).
-   `From / To`{.interpreted-text role="guilabel"}: enables *Date
    from\...* and *Date to\...* date selection fields to define a
    specific time range (e.g., [06/05/2024]{.title-ref} to
    [06/27/2024]{.title-ref}).

Optionally, set a `Default value`{.interpreted-text role="guilabel"} for
the `Time range`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The `Default value`{.interpreted-text role="guilabel"} field only
appears for `Month / Quarter`{.interpreted-text role="guilabel"} or
`Relative Period`{.interpreted-text role="guilabel"} ranges.

If the `Month / Quarter`{.interpreted-text role="guilabel"} range is
selected, tick the `Automatically filter on
the current period`{.interpreted-text role="guilabel"} checkbox to
define the default period of either `Month`{.interpreted-text
role="guilabel"}, `Quarter`{.interpreted-text role="guilabel"}, or
`Year`{.interpreted-text role="guilabel"}.
:::

Next, configure the `Field matching`{.interpreted-text role="guilabel"}
for each data source. To do so, expand the section by clicking on the
`Field matching`{.interpreted-text role="guilabel"} heading, to reveal a
list of the data sources in the spreadsheet where each data source has
two fields for matching:

-   `Date field`{.interpreted-text role="guilabel"}: select a date field
    from the data source model to apply the time range to.

-   `Period offset`{.interpreted-text role="guilabel"}: (optionally)
    select an offset that shifts the time range by a relative period.

    The options available are: `Previous`{.interpreted-text
    role="guilabel"}, `Before Previous`{.interpreted-text
    role="guilabel"}, `Next`{.interpreted-text role="guilabel"},
    `After Next`{.interpreted-text role="guilabel"}.

Lastly, once all the information is entered on the form, click the
`Save`{.interpreted-text role="guilabel"} button. If any of the data
source fields do not match the data type of *date* (or *datetime*), an
error is shown stating
`Some required fields are not valid`{.interpreted-text role="guilabel"}.

::: {.example}
Consider a `Period offset`{.interpreted-text role="guilabel"} of
`Next`{.interpreted-text role="guilabel"} when using the `Month /
Quarter`{.interpreted-text role="guilabel"} range to apply the filter to
the *next* period relative to the set time range.

With this configuration, selecting [January]{.title-ref}
[2024]{.title-ref} as the date, filters data as [February]{.title-ref}
[2024]{.title-ref}; where the selected month is offset to the next
month.

{.align-center}
:::

### Relation {#spreadsheet/global-filter-relation}

The *Relation* global filter enables the filtering of records in data
sources by selecting a field from a related model.

With the
`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 20 20"><path fill="currentColor" d="M1 3h12L7 9M5.5 6h3v11l-3-3M14 4h4v2h-4m-3 3h7v2h-7m0 3h7v2h-7"></path></svg>`{.interpreted-text
role="raw-html"} `(global filter)`{.interpreted-text role="guilabel"}
menu open, select the `Relation`{.interpreted-text role="guilabel"}
button to create a new relation filter. The
`Filter properties`{.interpreted-text role="guilabel"} menu displays the
following fields for configuration.

First, enter a name for the new relation filter in the
`Label`{.interpreted-text role="guilabel"} field.

Then, select or search for a model from the
`Related model`{.interpreted-text role="guilabel"} field.

Once a model is selected, the `Default value`{.interpreted-text
role="guilabel"} and `Field matching`{.interpreted-text role="guilabel"}
fields appear.

Optionally, set a `Default value`{.interpreted-text role="guilabel"} for
the `Related model`{.interpreted-text role="guilabel"}. The available
options are records of the model.

Next, configure the `Field matching`{.interpreted-text role="guilabel"}
for each data source. To do so, expand the section by clicking on the
`Field matching`{.interpreted-text role="guilabel"} heading, to reveal a
list of the data sources in the spreadsheet where each data source has a
field for matching.

Select a field from the data source model from which to apply the
relation filter.

Lastly, once all the information is entered on the form, click the
`Save`{.interpreted-text role="guilabel"} button. If any of the data
source fields do not match the data type of the related model, an error
is shown stating `Some required fields are not valid`{.interpreted-text
role="guilabel"}.

::: {.example}
Consider a *Relation* filter with the `Related model`{.interpreted-text
role="guilabel"} set as `Contact`{.interpreted-text role="guilabel"}.
The `Field matching`{.interpreted-text role="guilabel"} *CRM* lead
([crm.lead]{.title-ref}) pivot data sources are set to
`Customer`{.interpreted-text role="guilabel"}.

With this configuration, selecting a customer record filters the pivot
table to only leads that are related to the selected customer record.

{.align-center}
:::

### Text {#spreadsheet/global-filter-text}

The *Text* global filter enables the filtering of text by matching data
source text fields to a string of text or to a range of predefined
values.

With the
`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 20 20"><path fill="currentColor" d="M1 3h12L7 9M5.5 6h3v11l-3-3M14 4h4v2h-4m-3 3h7v2h-7m0 3h7v2h-7"></path></svg>`{.interpreted-text
role="raw-html"} `(global filter)`{.interpreted-text role="guilabel"}
menu open, select the `Text`{.interpreted-text role="guilabel"} button
to create a new text filter. The `Filter properties`{.interpreted-text
role="guilabel"} menu displays the following fields for configuration.

First, enter a name for the new text filter in the
`Label`{.interpreted-text role="guilabel"} field.

Then, choose whether or not to
`Restrict values to a range`{.interpreted-text role="guilabel"} by
ticking the checkbox. Doing so, reveals a field to input a range within
the spreadsheet. Either type in or select the range.

Next, configure the `Field matching`{.interpreted-text role="guilabel"}
for each data source. To do so, expand the section by clicking on the
`Field matching`{.interpreted-text role="guilabel"} heading, to reveal a
list of the data sources in the spreadsheet where each data source has a
field for matching.

Select a field from the data source model from which to apply the text
filter.

Lastly, once all the information is entered on the form, click the
`Save`{.interpreted-text role="guilabel"} button. If any of the data
source fields do not match the data type of the related model, an error
is shown stating `Some required fields are not valid`{.interpreted-text
role="guilabel"}.

::: {.example}
Consider a text filter with the range [A2:A6]{.title-ref} added to the
`Restrict values to a range`{.interpreted-text role="guilabel"} field.
The spreadsheet has five different product names listed as values in the
cells of column [A]{.title-ref}, rows [2]{.title-ref} though
[6]{.title-ref}.

With the above configuration, a pivot table of products can be filtered
by product name by selecting one of the 5 predefined values available in
the text filter.

Furthermore, if the values in the range [A2:A6]{.title-ref} are added
dynamically-- the text filter becomes dynamic as well.

{.align-center}
:::

Manage filters
--------------

Open the
`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 20 20"><path fill="currentColor" d="M1 3h12L7 9M5.5 6h3v11l-3-3M14 4h4v2h-4m-3 3h7v2h-7m0 3h7v2h-7"></path></svg>`{.interpreted-text
role="raw-html"} `(global filter)`{.interpreted-text role="guilabel"}
filter menu by navigating to the `Documents app`{.interpreted-text
role="menuselection"} and clicking on the desired spreadsheet.

Existing global filters appear under the `Filters`{.interpreted-text
role="guilabel"} section. Filters can be used individually, or at the
same time.

::: {.tip}
::: {.title}
Tip
:::

The order of existing filters can be changed by hovering over a filter
and using the
`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 4 16" fill="currentColor"><circle cx="2" cy="3.5" r="1"></circle><circle cx="2" cy="6.5" r="1"></circle><circle cx="2" cy="9.5" r="1"></circle><circle cx="2" cy="12.5" r="1"></circle></svg>`{.interpreted-text
role="raw-html"} `(drag handle)`{.interpreted-text role="guilabel"} icon
to change the position.
:::

To reset a filter with set values back to default, click on the
`fa-times`{.interpreted-text role="icon"} (clear) icon next to the value
in the filter.

To edit an existing filter, select the `fa-cog`{.interpreted-text
role="icon"} `(gear)`{.interpreted-text role="guilabel"} icon to open
the filter\'s `Filter properties`{.interpreted-text role="guilabel"}
menu. From here, edits can be made or the filter can be deleted by
clicking the `Remove`{.interpreted-text role="guilabel"} button.
