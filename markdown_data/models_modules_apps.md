# File: /content/odoo_doc17.0/fr/content/applications/studio/models_modules_apps.md

Models, modules, and apps
=========================

Models determine the logical structure of a database and how data is
stored, organized, and manipulated. In other words, a model is a table
of information that can be linked with other tables. A model usually
represents a business concept, such as a *sales order*, *contact*, or
*product*.

Modules and apps contain various elements, such as models, views, data
files, web controllers, and static web data.

::: {.note}
::: {.title}
Note
:::

All apps are modules. Larger, standalone modules are typically referred
to as apps, whereas other modules usually serve as add-ons to said apps.
:::

Suggested features {#studio/models-modules-apps/suggested-features}
------------------

When you create a new model or app with Studio, you can choose to add up
to 14 features to speed up the creation process. These features bundle
fields, default settings, and views that are usually used together to
provide some standard functionality. Most of these features can be added
later on, but adding them from the start makes the model creation
process much easier. Furthermore, these features interact together in
some cases to increase their usefulness.

::: {.example}
Creating a model with the
`studio/models-modules-apps/suggested-features/picture`{.interpreted-text
role="ref"} and
`studio/models-modules-apps/suggested-features/pipeline-stages`{.interpreted-text
role="ref"} features enabled adds the image in the card layout of the
`Kanban view <studio/views/multiple-records/kanban>`{.interpreted-text
role="ref"}.

{.align-center}
:::

### Contact details {#studio/models-modules-apps/suggested-features/contact-details}

Selecting `Contact details`{.interpreted-text role="guilabel"} adds to
the `Form view <studio/views/general/form>`{.interpreted-text
role="ref"} a
`Many2One field <studio/fields/relational-fields-many2one>`{.interpreted-text
role="ref"} linked to the *Contact* model and two of its
`Related Fields <studio/fields/relational-fields-related-field>`{.interpreted-text
role="ref"}: `Phone`{.interpreted-text role="guilabel"} and
`Email`{.interpreted-text role="guilabel"}. The
`Contact`{.interpreted-text role="guilabel"} field is also added to the
`List view
<studio/views/multiple-records/list>`{.interpreted-text role="ref"}, and
the `Map view <studio/views/multiple-records/map>`{.interpreted-text
role="ref"} is activated.

::: {.example}
{.align-center}
:::

### User assignment {#studio/models-modules-apps/suggested-features/user-assignment}

Selecting `User assignment`{.interpreted-text role="guilabel"} adds to
the `Form view <studio/views/general/form>`{.interpreted-text
role="ref"} a
`Many2One field <studio/fields/relational-fields-many2one>`{.interpreted-text
role="ref"} linked to the *Contact* model, with the following
`Domain`{.interpreted-text role="guilabel"}: [Share User is not
set]{.title-ref} to only allow the selection of *Internal Users*. In
addition, the `many2one_avatar_user`{.interpreted-text role="guilabel"}
widget is used to display the user\'s avatar. The
`Responsible`{.interpreted-text role="guilabel"} field is also added to
the `List view
<studio/views/multiple-records/list>`{.interpreted-text role="ref"}.

::: {.example}
{.align-center}
:::

### Date & Calendar {#studio/models-modules-apps/suggested-features/date-calendar}

Selecting `Date & Calendar`{.interpreted-text role="guilabel"} adds to
the `Form view <studio/views/general/form>`{.interpreted-text
role="ref"} a
`Date field <studio/fields/simple-fields-date>`{.interpreted-text
role="ref"} and activates the `Calendar view
<studio/views/timeline/calendar>`{.interpreted-text role="ref"}.

### Date range & Gantt {#studio/models-modules-apps/suggested-features/date-range-gantt}

Selecting `Date range & Gantt`{.interpreted-text role="guilabel"} adds
to the `Form view <studio/views/general/form>`{.interpreted-text
role="ref"} two
`Date fields <studio/fields/simple-fields-date>`{.interpreted-text
role="ref"} next to each other: one to set a start date, the other to
set an end date, using the `daterange`{.interpreted-text
role="guilabel"} widget, and activates the
`Gantt view <studio/views/timeline/gantt>`{.interpreted-text
role="ref"}.

### Pipeline stages {#studio/models-modules-apps/suggested-features/pipeline-stages}

Selecting `Pipeline stages`{.interpreted-text role="guilabel"} activates
the `Kanban view
<studio/views/multiple-records/kanban>`{.interpreted-text role="ref"},
adds several fields such as `Priority
<studio/fields/simple-fields-priority>`{.interpreted-text role="ref"}
and `Kanban State`{.interpreted-text role="guilabel"}, and three stages:
`New`{.interpreted-text role="guilabel"},
`In Progress`{.interpreted-text role="guilabel"}, and
`Done`{.interpreted-text role="guilabel"}. The
`Pipeline status bar`{.interpreted-text role="guilabel"} and the
`Kanban State`{.interpreted-text role="guilabel"} field are added to the
`Form view
<studio/views/general/form>`{.interpreted-text role="ref"}. The
`Color`{.interpreted-text role="guilabel"} field is added to the
`List view
<studio/views/multiple-records/list>`{.interpreted-text role="ref"}.

::: {.note}
::: {.title}
Note
:::

The `Pipeline stages`{.interpreted-text role="guilabel"} feature can be
added at a later stage.
:::

### Tags {#studio/models-modules-apps/suggested-features/tags}

Selecting `Tags`{.interpreted-text role="guilabel"} adds to the
`studio/views/general/form`{.interpreted-text role="ref"} and
`studio/views/multiple-records/list`{.interpreted-text role="ref"} views
a `Tags field
<studio/fields/relational-fields-tags>`{.interpreted-text role="ref"},
creating a *Tag* model with preconfigured access rights in the process.

### Picture {#studio/models-modules-apps/suggested-features/picture}

Selecting `Picture`{.interpreted-text role="guilabel"} adds to the
top-right of the `Form view
<studio/views/general/form>`{.interpreted-text role="ref"} an
`Image field <studio/fields/simple-fields-image>`{.interpreted-text
role="ref"}.

::: {.note}
::: {.title}
Note
:::

The `Picture`{.interpreted-text role="guilabel"} feature can be added at
a later stage.
:::

### Lines {#studio/models-modules-apps/suggested-features/lines}

Selecting `Lines`{.interpreted-text role="guilabel"}: adds to the
`Form view <studio/views/general/form>`{.interpreted-text role="ref"} a
`Lines
field <studio/fields/relational-fields-lines>`{.interpreted-text
role="ref"} inside a `Tab`{.interpreted-text role="guilabel"} component.

### Notes {#studio/models-modules-apps/suggested-features/notes}

Selecting `Notes`{.interpreted-text role="guilabel"} adds to the
`Form view <studio/views/general/form>`{.interpreted-text role="ref"} an
`Html
field <studio/fields/simple-fields-html>`{.interpreted-text role="ref"}
using the full width of the form.

### Monetary value {#studio/models-modules-apps/suggested-features/monetary-value}

Selecting `Monetary value`{.interpreted-text role="guilabel"} adds to
the `studio/views/general/form`{.interpreted-text role="ref"} and
`studio/views/multiple-records/list`{.interpreted-text role="ref"} views
a `Monetary field
<studio/fields/simple-fields-monetary>`{.interpreted-text role="ref"}.
The `studio/views/reporting/graph`{.interpreted-text role="ref"} and
`studio/views/reporting/pivot`{.interpreted-text role="ref"} views are
also activated.

::: {.note}
::: {.title}
Note
:::

A *Currency* field is added and hidden from the view.
:::

### Company {#studio/models-modules-apps/suggested-features/company}

Selecting `Company`{.interpreted-text role="guilabel"} adds to the
`studio/views/general/form`{.interpreted-text role="ref"} and
`studio/views/multiple-records/list`{.interpreted-text role="ref"} views
a `Many2One field
<studio/fields/relational-fields-many2one>`{.interpreted-text
role="ref"} linked to the *Company* model.

::: {.note}
::: {.title}
Note
:::

This is only useful if you work in a multi-company environment.
:::

### Custom Sorting {#studio/models-modules-apps/suggested-features/custom-sorting}

Selecting `Custom Sorting`{.interpreted-text role="guilabel"} adds to
the `List view
<studio/views/multiple-records/list>`{.interpreted-text role="ref"} a
drag handle icon to manually reorder records.

::: {.example}
{.align-center}
:::

### Chatter {#studio/models-modules-apps/suggested-features/chatter}

Selecting `Chatter`{.interpreted-text role="guilabel"} adds to the
`Form view <studio/views/general/form>`{.interpreted-text role="ref"}
Chatter functionalities (sending messages, logging notes, and scheduling
activities).

::: {.note}
::: {.title}
Note
:::

The `Chatter`{.interpreted-text role="guilabel"} feature can be added at
a later stage.
:::

::: {.example}
{.align-center}
:::

### Archiving {#studio/models-modules-apps/suggested-features/archiving}

Selecting `Archiving`{.interpreted-text role="guilabel"} adds to the
`studio/views/general/form`{.interpreted-text role="ref"} and
`studio/views/multiple-records/list`{.interpreted-text role="ref"} views
the `Archive`{.interpreted-text role="guilabel"} action and hides
archived records from searches and views by default.

Export and import customizations {#studio/export-import}
--------------------------------

When you do any customization with Studio, a new module named
`Studio customizations`{.interpreted-text role="guilabel"} is added to
your database.

To export these customizations, go to
`Main dashboard --> Studio --> Customizations
--> Export`{.interpreted-text role="menuselection"} to download a ZIP
file containing all customizations.

To import and install these customizations in another database, connect
to the destination database and go to
`Main dashboard --> Studio --> Customizations --> Import`{.interpreted-text
role="menuselection"}, then upload the exported ZIP file before clicking
on the `Import`{.interpreted-text role="guilabel"} button.

::: {.warning}
::: {.title}
Warning
:::

Before importing, make sure the destination database contains the same
apps and modules as the source database. Studio does not add the
underlying modules as dependencies of the exported module.
:::
