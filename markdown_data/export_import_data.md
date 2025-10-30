# File: /content/odoo_doc17.0/fr/content/applications/essentials/export_import_data.md

Export and import data
======================

In Odoo, it is sometimes necessary to export or import data for running
reports, or for data modification. This document covers the export and
import of data into and out of Odoo.

::: {.important}
::: {.title}
Important
:::

Sometimes, users run into a \'time out\' error, or a record does not
process, due to its size. This can occur with large exports, or in cases
where the import file is too large. To circumvent this limitation
surrounding the size of the records, process exports or imports in
smaller batches.
:::

Export data from Odoo {#export-data}
---------------------

When working with a database, it is sometimes necessary to export data
in a distinct file. Doing so can aid in reporting on activities,
although, Odoo provides a precise and easy reporting tool with each
available application.

With Odoo, the values can be exported from any field in any record. To
do so, activate the list view (`oi-view-list`{.interpreted-text
role="icon"} `(list)`{.interpreted-text role="guilabel"} icon), on the
items that need to be exported, then select the records that should be
exported. To select a record, tick the checkbox next to the
corresponding record. Finally, click on `fa-cog`{.interpreted-text
role="icon"} `Actions`{.interpreted-text role="guilabel"}, then
`Export`{.interpreted-text role="guilabel"}.

{.align-center}

When clicking on `Export`{.interpreted-text role="guilabel"}, an
`Export Data`{.interpreted-text role="guilabel"} pop-over window
appears, with several options for the data to export:

{.align-center}

1.  With the
    `I want to update data (import-compatable export)`{.interpreted-text
    role="guilabel"} option ticked, the system only shows the fields
    that can be imported. This is helpful in the case where the
    `existing
    records need to be updated <essentials/update-data>`{.interpreted-text
    role="ref"}. This works like a filter. Leaving the box unticked,
    gives many more field options because it shows all the fields, not
    just the ones that can be imported.
2.  When exporting, there is the option to export in two formats:
    [.csv]{.title-ref} and [.xls]{.title-ref}. With [.csv]{.title-ref},
    items are separated by a comma, while [.xls]{.title-ref} holds
    information about all the worksheets in a file, including both
    content and formatting.
3.  These are the items that can be exported. Use the
    `> (right arrow)`{.interpreted-text role="guilabel"} icon to display
    more sub-field options. Use the `Search`{.interpreted-text
    role="guilabel"} bar to find specific fields. To use the
    `Search`{.interpreted-text role="guilabel"} option more efficiently,
    click on all the `> (right arrows)`{.interpreted-text
    role="guilabel"} to display all fields.
4.  The `+ (plus sign)`{.interpreted-text role="guilabel"} icon button
    is present to add fields to the `Fields to
    export`{.interpreted-text role="guilabel"} list.
5.  The `↕️ (up-down arrow)`{.interpreted-text role="guilabel"} to the
    left of the selected fields can be used to move the fields up and
    down, to change the order in which they are displayed in the
    exported file. Drag-and-drop using the
    `↕️ (up-down arrow)`{.interpreted-text role="guilabel"} icon.
6.  The `🗑️ (trash can)`{.interpreted-text role="guilabel"} icon is used
    to remove fields. Click on the `🗑️ (trash
    can)`{.interpreted-text role="guilabel"} icon to remove the field.
7.  For recurring reports, it is helpful to save export presets. Select
    all the needed fields, and click on the template drop-down menu.
    Once there, click on `New template`{.interpreted-text
    role="guilabel"}, and give a unique name to the export just created.
    Click the `💾 (floppy drive)`{.interpreted-text role="guilabel"} icon
    to save the configuration. The next time the same list needs to be
    exported, select the related template that was previously saved from
    the drop-down menu.

::: {.tip}
::: {.title}
Tip
:::

It is helpful to know the field\'s external identifier. For example,
`Related Company`{.interpreted-text role="guilabel"} in the export user
interface is equal to *parent\_id* (external identifier). This is
helpful because then, the only data exported is what should be modified
and re-imported.
:::

Import data into Odoo {#import-data}
---------------------

Importing data into Odoo is extremely helpful during implementation, or
in times where data needs to be
`updated in bulk <essentials/update-data>`{.interpreted-text
role="ref"}. The following documentation covers how to import data into
an Odoo database.

::: {.warning}
::: {.title}
Warning
:::

Imports are permanent and **cannot** be undone. However, it is possible
to use filters ([created on]{.title-ref} or [last modified]{.title-ref})
to identify records changed or created by the import.
:::

::: {.tip}
::: {.title}
Tip
:::

Activating `developer mode <developer-mode>`{.interpreted-text
role="ref"} changes the visible import settings in the left menu. Doing
so reveals an `Advanced`{.interpreted-text role="menuselection"} menu.
Included in this advanced menu are two options:
`Track history during import`{.interpreted-text role="guilabel"} and
`Allow matching with subfields`{.interpreted-text role="guilabel"}.

{.align-center}

If the model uses openchatter, the
`Track history during import`{.interpreted-text role="guilabel"} option
sets up subscriptions and sends notifications during the import, but
leads to a slower import.

Should the `Allow matching with subfields`{.interpreted-text
role="guilabel"} option be selected, then all subfields within a field
are used to match under the `Odoo Field`{.interpreted-text
role="guilabel"} while importing.
:::

### Get started

Data can be imported on any Odoo business object using either Excel
([.xlsx]{.title-ref}) or `CSV
(Comma-separated Values)`{.interpreted-text role="abbr"}
([.csv]{.title-ref}) formats. This includes: contacts, products, bank
statements, journal entries, and orders.

Open the view of the object to which the data should be
imported/populated, and click on
`⚙️ (Action) --> Import records`{.interpreted-text
role="menuselection"}.

{.align-center}

After clicking `Import records`{.interpreted-text role="guilabel"}, Odoo
reveals a separate page with templates that can be downloaded and
populated with the company\'s own data. Such templates can be imported
in one click, since the data mapping is already done. To download a
template click `Import Template for
Customers`{.interpreted-text role="guilabel"} at the center of the page.

::: {.important}
::: {.title}
Important
:::

When importing a `CSV (Comma-separated Values)`{.interpreted-text
role="abbr"} file, Odoo provides `Formatting`{.interpreted-text
role="guilabel"} options. These options do **not** appear when importing
the proprietary Excel file type ([.xls]{.title-ref},
[.xlsx]{.title-ref}).

{.align-center}
:::

Make necessary adjustments to the *Formatting* options, and ensure all
columns in the `Odoo field`{.interpreted-text role="guilabel"} and
`File Column`{.interpreted-text role="guilabel"} are free of errors.
Finally, click `Import`{.interpreted-text role="guilabel"} to import the
data.

### Adapt a template

Import templates are provided in the import tool of the most common data
to import (contacts, products, bank statements, etc.). Open them with
any spreadsheet software (*Microsoft Office*, *OpenOffice*, *Google
Drive*, etc.).

Once the template is downloaded, proceed to follow these steps:

-   Add, remove, and sort columns to best fit the data structure.
-   It is strongly advised to **not** remove the
    `External ID`{.interpreted-text role="guilabel"} (ID) column (see
    why in the next section).
-   Set a unique ID to every record by dragging down the ID sequencing
    in the `External ID`{.interpreted-text role="guilabel"} (ID) column.

{.align-center}

::: {.note}
::: {.title}
Note
:::

When a new column is added, Odoo may not be able to map it
automatically, if its label does not fit any field within Odoo. However,
new columns can be mapped manually when the import is tested. Search the
drop-down menu for the corresponding field.

{.align-center}

Then, use this field\'s label in the import file to ensure future
imports are successful.
:::

::: {.tip}
::: {.title}
Tip
:::

Another useful way to find out the proper column names to import is to
export a sample file using the fields that should be imported. This way,
if there is not a sample import template, the names are accurate.
:::

### Import from another application {#essentials/external-id}

The `External ID`{.interpreted-text role="guilabel"} (ID) is a unique
identifier for the line item. Feel free to use one from previous
software to facilitate the transition to Odoo.

Setting an ID is not mandatory when importing, but it helps in many
cases:

-   `Update imports <essentials/update-data>`{.interpreted-text
    role="ref"}: import the same file several times without creating
    duplicates.
-   `Import relation fields <export_import_data/relation-fields>`{.interpreted-text
    role="ref"}.

To recreate relationships between different records, the unique
identifier from the original application should be used to map it to the
`External ID`{.interpreted-text role="guilabel"} (ID) column in Odoo.

When another record is imported that links to the first one, use
**XXX/ID** (XXX/External ID) for the original unique identifier. This
record can also be found using its name.

::: {.warning}
::: {.title}
Warning
:::

It should be noted that conflicts occur if two (or more) records have
the same *External ID*.
:::

### Field missing to map column

Odoo heuristically tries to find the type of field for each column
inside the imported file, based on the first ten lines of the files.

For example, if there is a column only containing numbers, only the
fields with the *integer* type are presented as options.

While this behavior might be beneficial in most cases, it is also
possible that it could fail, or the column may be mapped to a field that
is not proposed by default.

If this happens, check the
`Show fields of relation fields (advanced) option`{.interpreted-text
role="guilabel"}, then a complete list of fields becomes available for
each column.

{.align-center}

### Change data import format

::: {.note}
::: {.title}
Note
:::

Odoo can automatically detect if a column is a date, and tries to guess
the date format from a set of most commonly used date formats. While
this process can work for many date formats, some date formats are not
recognizable. This can cause confusion, due to day-month inversions; it
is difficult to guess which part of a date format is the day, and which
part is the month, in a date, such as [01-03-2016]{.title-ref}.
:::

When importing a `CSV (Comma-separated Values)`{.interpreted-text
role="abbr"} file, Odoo provides `Formatting`{.interpreted-text
role="guilabel"} options.

To view which date format Odoo has found from the file, check the
`Date Format`{.interpreted-text role="guilabel"} that is shown when
clicking on options under the file selector. If this format is
incorrect, change it to the preferred format using *ISO 8601* to define
the format.

::: {.important}
::: {.title}
Important
:::

*ISO 8601* is an international standard, covering the worldwide
exchange, along with the communication of date and time-related data.
For example, the date format should be [YYYY-MM-DD]{.title-ref}. So, in
the case of July 24th 1981, it should be written as
[1981-07-24]{.title-ref}.
:::

::: {.tip}
::: {.title}
Tip
:::

When importing Excel files ([.xls]{.title-ref}, [.xlsx]{.title-ref}),
consider using *date cells* to store dates. This maintains locale date
formats for display, regardless of how the date is formatted in Odoo.
When importing a `CSV (Comma-separated Values)`{.interpreted-text
role="abbr"} file, use Odoo\'s `Formatting`{.interpreted-text
role="guilabel"} section to select the date format columns to import.
:::

### Import numbers with currency signs

Odoo fully supports numbers with parenthesis to represent negative
signs, as well as numbers with currency signs attached to them. Odoo
also automatically detects which thousand/decimal separator is used. If
a currency symbol unknown to Odoo is used, it might not be recognized as
a number, and the import crashes.

::: {.note}
::: {.title}
Note
:::

When importing a `CSV (Comma-separated Values)`{.interpreted-text
role="abbr"} file, the `Formatting`{.interpreted-text role="guilabel"}
menu appears on the left-hand column. Under these options, the
`Thousands Separator`{.interpreted-text role="guilabel"} can be changed.
:::

Examples of supported numbers (using \'thirty-two thousand\' as the
figure):

-   32.000,00
-   32000,00
-   32,000.00
-   -32000.00
-   (32000.00)
-   \$ 32.000,00
-   (32000.00 €)

Example that will not work:

-   ABC 32.000,00
-   \$ (32.000,00)

::: {.important}
::: {.title}
Important
:::

A `() (parenthesis)`{.interpreted-text role="guilabel"} around the
number indicates that the number is a negative value. The currency
symbol **must** be placed within the parenthesis for Odoo to recognize
it as a negative currency value.
:::

### Import preview table not displayed correctly

By default, the import preview is set on commas as field separators, and
quotation marks as text delimiters. If the
`CSV (Comma-separated Values)`{.interpreted-text role="abbr"} file does
not have these settings, modify the `Formatting`{.interpreted-text
role="guilabel"} options (displayed under the `Import`{.interpreted-text
role="guilabel"} `CSV
(Comma-separated Values)`{.interpreted-text role="abbr"} file bar after
selecting the `CSV (Comma-separated Values)`{.interpreted-text
role="abbr"} file).

::: {.important}
::: {.title}
Important
:::

If the `CSV (Comma-separated Values)`{.interpreted-text role="abbr"}
file has a tabulation as a separator, Odoo does **not** detect the
separations. The file format options need to be modified in the
spreadsheet application. See the following
`Change CSV file format <export_import_data/change-csv>`{.interpreted-text
role="ref"} section.
:::

### Change CSV file format in spreadsheet application {#export_import_data/change-csv}

When editing and saving `CSV (Comma-separated Values)`{.interpreted-text
role="abbr"} files in spreadsheet applications, the computer\'s regional
settings are applied for the separator and delimiter. Odoo suggests
using *OpenOffice* or *LibreOffice*, as both applications allow
modifications of all three options (from *LibreOffice* application, go
to `'Save As' dialog box --> Check the box 'Edit filter
settings' --> Save`{.interpreted-text role="menuselection"}).

Microsoft Excel can modify the encoding when saving
(`'Save As' dialog box -->
'Tools' drop-down menu --> Encoding tab`{.interpreted-text
role="menuselection"}).

### Difference between Database ID and External ID

Some fields define a relationship with another object. For example, the
country of a contact is a link to a record of the \'Country\' object.
When such fields are imported, Odoo has to recreate links between the
different records. To help import such fields, Odoo provides three
mechanisms.

::: {.important}
::: {.title}
Important
:::

**Only one** mechanism should be used per field that is imported.
:::

For example, to reference the country of a contact, Odoo proposes three
different fields to import:

-   `Country`{.interpreted-text role="guilabel"}: the name or code of
    the country
-   `Country/Database ID`{.interpreted-text role="guilabel"}: the unique
    Odoo ID for a record, defined by the ID PostgreSQL column
-   `Country/External ID`{.interpreted-text role="guilabel"}: the ID of
    this record referenced in another application (or the
    [.XML]{.title-ref} file that imported it)

For the country of Belgium, for example, use one of these three ways to
import:

-   `Country`{.interpreted-text role="guilabel"}: [Belgium]{.title-ref}
-   `Country/Database ID`{.interpreted-text role="guilabel"}:
    [21]{.title-ref}
-   `Country/External ID`{.interpreted-text role="guilabel"}:
    [base.be]{.title-ref}

According to the company\'s need, use one of these three ways to
reference records in relations. Here is an example when one or the other
should be used, according to the need:

-   Use `Country`{.interpreted-text role="guilabel"}: this is the
    easiest way when data comes from `CSV (Comma-separated
    Values)`{.interpreted-text role="abbr"} files that have been created
    manually.
-   Use `Country/Database ID`{.interpreted-text role="guilabel"}: this
    should rarely be used. It is mostly used by developers as the main
    advantage is to never have conflicts (there may be several records
    with the same name, but they always have a unique Database ID)
-   Use `Country/External ID`{.interpreted-text role="guilabel"}: use
    *External ID* when importing data from a third-party application.

When *External IDs* are used, import
`CSV (Comma-separated Values)`{.interpreted-text role="abbr"} files with
the `External ID`{.interpreted-text role="guilabel"} (ID) column
defining the *External ID* of each record that is imported. Then, a
reference can be made to that record with columns, like [Field/External
ID]{.title-ref}. The following two
`CSV (Comma-separated Values)`{.interpreted-text role="abbr"} files
provide an example for products and their categories.

-   `CSV file for categories
    <export_import_data/External_id_3rd_party_application_product_categories.csv>`{.interpreted-text
    role="download"}
-   `CSV file for Products
    <export_import_data/External_id_3rd_party_application_products.csv>`{.interpreted-text
    role="download"}

### Import relation fields {#export_import_data/relation-fields}

An Odoo object is always related to many other objects (e.g. a product
is linked to product categories, attributes, vendors, etc.). To import
those relations, the records of the related object need to be imported
first, from their own list menu.

This can be achieved by using either the name of the related record, or
its ID, depending on the circumstances. The ID is expected when two
records have the same name. In such a case add [/ ID]{.title-ref} at the
end of the column title (e.g. for product attributes: [Product
Attributes / Attribute / ID]{.title-ref}).

#### Options for multiple matches on fields

If, for example, there are two product categories with the child name
[Sellable]{.title-ref} (e.g. [Misc. Products/Sellable]{.title-ref} &
[Other Products/Sellable]{.title-ref}), the validation is halted, but
the data may still be imported. However, Odoo recommends that the data
is not imported because it will all be linked to the first
[Sellable]{.title-ref} category found in the *Product Category* list
([Misc. Products/Sellable]{.title-ref}). Odoo, instead, recommends
modifying one of the duplicate\'s values, or the product category
hierarchy.

However, if the company does not wish to change the configuration of
product categories, Odoo recommends making use of the *External ID* for
this field, \'Category\'.

#### Import many2many relationship fields

The tags should be separated by a comma, without any spacing. For
example, if a customer needs to be linked to both tags:
[Manufacturer]{.title-ref} and [Retailer]{.title-ref} then
\'Manufacturer,Retailer\' needs to be encoded in the same column of the
`CSV (Comma-separated Values)`{.interpreted-text role="abbr"} file.

-   `CSV file for Manufacturer, Retailer <export_import_data/m2m_customers_tags.csv>`{.interpreted-text
    role="download"}

#### Import one2many relationships

If a company wants to import a sales order with several order lines, a
specific row **must** be reserved in the
`CSV (Comma-separated Values)`{.interpreted-text role="abbr"} file for
each order line. The first order line is imported on the same row as the
information relative to order. Any additional lines need an additional
row that does not have any information in the fields relative to the
order.

As an example, here is a
`CSV (Comma-separated Values)`{.interpreted-text role="abbr"} file of
some quotations that can be imported, based on demo data:

-   `File for some Quotations
    <export_import_data/purchase.order_functional_error_line_cant_adpat.csv>`{.interpreted-text
    role="download"}

The following `CSV (Comma-separated Values)`{.interpreted-text
role="abbr"} file shows how to import purchase orders with their
respective purchase order lines:

-   `Purchase orders with their respective purchase order lines
    <export_import_data/o2m_purchase_order_lines.csv>`{.interpreted-text
    role="download"}

The following `CSV (Comma-separated Values)`{.interpreted-text
role="abbr"} file shows how to import customers and their respective
contacts:

-   `Customers and their respective contacts
    <export_import_data/o2m_customers_contacts.csv>`{.interpreted-text
    role="download"}

### Import records several times

If an imported file contains one of the columns:
`External ID`{.interpreted-text role="guilabel"} or
`Database ID`{.interpreted-text role="guilabel"}, records that have
already been imported are modified, instead of being created. This is
extremely useful as it allows users to import the same
`CSV (Comma-separated Values)`{.interpreted-text role="abbr"} file
several times, while having made some changes in between two imports.

Odoo takes care of creating or modifying each record, depending if it is
new or not.

This feature allows a company to use the *Import/Export tool* in Odoo to
modify a batch of records in a spreadsheet application.

### Value not provided for a specific field

If all fields are not set in the CSV file, Odoo assigns the default
value for every non-defined field. But, if fields are set with empty
values in the `CSV (Comma-separated Values)`{.interpreted-text
role="abbr"} file, Odoo sets the empty value in the field, instead of
assigning the default value.

### Export/import different tables from an SQL application to Odoo

If data needs to be imported from different tables, relations need to be
recreated between records belonging to different tables. For instance,
if companies and people are imported, the link between each person and
the company they work for needs to be recreated.

To manage relations between tables, use the [External ID]{.title-ref}
facilities of Odoo. The [External ID]{.title-ref} of a record is the
unique identifier of this record in another application. The [External
ID]{.title-ref} must be unique across all records of all objects. It is
a good practice to prefix this [External ID]{.title-ref} with the name
of the application or table. (like, \'company\_1\', \'person\_1\' -
instead of \'1\')

As an example, suppose there is an SQL database with two tables that are
to be imported: companies and people. Each person belongs to one
company, so the link between a person and the company they work for must
be recreated.

Test this example, with a `sample of a PostgreSQL database
<export_import_data/database_import_test.sql>`{.interpreted-text
role="download"}.

First, export all companies and their *External ID*. In PSQL, write the
following command:

``` {.sh}
> copy (select 'company_'||id as "External ID",company_name as "Name",'True' as "Is a Company" from companies) TO '/tmp/company.csv' with CSV HEADER;
```

This SQL command creates the following
`CSV (Comma-separated Values)`{.interpreted-text role="abbr"} file:

``` {.text}
External ID,Name,Is a Company
company_1,Bigees,True
company_2,Organi,True
company_3,Boum,True
```

To create the `CSV (Comma-separated Values)`{.interpreted-text
role="abbr"} file for people linked to companies, use the following SQL
command in PSQL:

``` {.sh}
> copy (select 'person_'||id as "External ID",person_name as "Name",'False' as "Is a Company",'company_'||company_id as "Related Company/External ID" from persons) TO '/tmp/person.csv' with CSV
```

It produces the following
`CSV (Comma-separated Values)`{.interpreted-text role="abbr"} file:

``` {.text}
External ID,Name,Is a Company,Related Company/External ID
person_1,Fabien,False,company_1
person_2,Laurence,False,company_1
person_3,Eric,False,company_2
person_4,Ramsy,False,company_3
```

In this file, Fabien and Laurence are working for the Bigees company
([company\_1]{.title-ref}), and Eric is working for the Organi company.
The relation between people and companies is done using the *External
ID* of the companies. The *External ID* is prefixed by the name of the
table to avoid a conflict of ID between people and companies
([person\_1]{.title-ref} and [company\_1]{.title-ref}, who shared the
same ID 1 in the original database).

The two files produced are ready to be imported in Odoo without any
modifications. After having imported these two
`CSV (Comma-separated Values)`{.interpreted-text role="abbr"} files,
there are four contacts and three companies (the first two contacts are
linked to the first company). Keep in mind to first import the
companies, and then the people.

Update data in Odoo {#essentials/update-data}
-------------------

Existing data can be updated in bulk through a data import, as long as
the `External ID
<essentials/external-id>`{.interpreted-text role="ref"} remains
consistent.

### Prepare data export

To update data through an import, first navigate to the data to be
updated, and select the `oi-view-list`{.interpreted-text role="icon"}
`(list)`{.interpreted-text role="guilabel"} icon to activate list view.
On the far-left side of the list, tick the checkbox for any record to be
updated. Then, click `fa-cog`{.interpreted-text role="icon"}
`Actions`{.interpreted-text role="guilabel"}, and select
`fa-upload`{.interpreted-text role="icon"} `Export`{.interpreted-text
role="guilabel"} from the drop-down menu.

On the resulting `Export Data`{.interpreted-text role="guilabel"} pop-up
window, tick the checkbox labeled, `I want
to update data (import-compatible export)`{.interpreted-text
role="guilabel"}. This automatically includes the *External ID* in the
export. Additionally, it limits the `Fields to export`{.interpreted-text
role="guilabel"} list to **only** include fields that are able to be
imported.

::: {.note}
::: {.title}
Note
:::

The `External ID`{.interpreted-text role="guilabel"} field does **not**
appear in the `Fields to export`{.interpreted-text role="guilabel"} list
unless it is manually added, but it is still included in the export.
However, if the `I
want to update data (import-compatible export)`{.interpreted-text
role="guilabel"} checkbox is ticked, it is included in the export.
:::

Select the required fields to be included in the export using the
`options <export-data>`{.interpreted-text role="ref"} on the pop-up
window, then click `Export`{.interpreted-text role="guilabel"}.

### Import updated data

After exporting, make any necessary changes to the data file. When the
file is ready, it can be `imported <import-data>`{.interpreted-text
role="ref"} by following the same process as a normal data import.

::: {.danger}
::: {.title}
Danger
:::

When updating data, it is extremely important that the *External ID*
remain consistent, as this is how the system identifies a record. If an
ID is altered, or removed, the system may add a duplicate record,
instead of updating the existing one.
:::
