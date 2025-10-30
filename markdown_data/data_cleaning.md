# File: /content/odoo_doc17.0/fr/content/applications/productivity/data_cleaning.md

Data Cleaning
=============

The Odoo **Data Cleaning** app maintains data integrity and consistency
with the following features:

-   `Deduplicates <data_cleaning/deduplication>`{.interpreted-text
    role="ref"}: merges or removes duplicate entries to ensure data is
    unique.
-   `Recycles <data_cleaning/recycle>`{.interpreted-text role="ref"}:
    identifies outdated records to either archive or delete them.
-   `Formats <data_cleaning/field-cleaning>`{.interpreted-text
    role="ref"}: standardizes text data by finding and replacing it
    according to specified needs.

Customizable rules ensure text data stays up-to-date, streamlined,
consistently formatted, and aligned with company-specific formatting
requirements.

Install modules {#data_cleaning/install-modules}
---------------

The **Data Cleaning** application consists of several modules.
`Install <general/install>`{.interpreted-text role="ref"} the following
to access all available features:

+---------------------------+------------------------------------------+
| | Name                    | Description                              |
| | [Technical              |                                          |
|   name]{.title-ref}       |                                          |
+===========================+==========================================+
| | `Data R                 | Base module to enable the recycle        |
| ecycle`{.interpreted-text | feature, available on                    |
|   role="guilabel"}        | `Odoo Community edition                  |
| | [d                      | <install/editions>`{.interpreted-text    |
| ata\_recycle]{.title-ref} | role="ref"}.                             |
+---------------------------+------------------------------------------+
| | `Data Cl                | Enables field cleaning feature to format |
| eaning`{.interpreted-text | text data across multiple records,       |
|   role="guilabel"}        | available **only** on                    |
| | [da                     | `Odoo Enterprise editi                   |
| ta\_cleaning]{.title-ref} | on <install/editions>`{.interpreted-text |
|                           | role="ref"}.                             |
+---------------------------+------------------------------------------+
| | `Data Cleaning (        | Enables the deduplication feature to     |
| merge)`{.interpreted-text | find similar (or duplicate) records, and |
|   role="guilabel"}        | merge them, available **only** on        |
| |                         | `Odoo Enterprise editi                   |
| [data\_merge]{.title-ref} | on <install/editions>`{.interpreted-text |
|                           | role="ref"}.                             |
+---------------------------+------------------------------------------+

::: {.spoiler}
Additionally, several app-specific modules are available

+---------------------------+------------------------------------------+
| | `CRM Dedupli            | Enables the deduplication feature on the |
| cation`{.interpreted-text | **CRM** app, and uses the `CRM default   |
|   role="guilabel"}        | merging feature <../sales/crm/pi         |
| | [data                   | peline/merge_similar>`{.interpreted-text |
| \_merge\_crm]{.title-ref} | role="doc"}.                             |
+---------------------------+------------------------------------------+
| | `Helpdesk Merge         | Enables the merge feature for the        |
| action`{.interpreted-text | **Helpdesk** app.                        |
|   role="guilabel"}        |                                          |
| | [data\_mer              |                                          |
| ge\_helpdesk]{.title-ref} |                                          |
+---------------------------+------------------------------------------+
| | `Project Merge          | Enables the merge feature for the        |
| action`{.interpreted-text | **Projects** app.                        |
|   role="guilabel"}        |                                          |
| | [data\_me               |                                          |
| rge\_project]{.title-ref} |                                          |
+---------------------------+------------------------------------------+
| | `UTM Dedupli            | Enables the merge feature for the **UTM  |
| cation`{.interpreted-text | Tracker** app.                           |
|   role="guilabel"}        |                                          |
| | [data                   |                                          |
| \_merge\_utm]{.title-ref} |                                          |
+---------------------------+------------------------------------------+
| | `WMS Accounting         | Creates a warning in cases of products   |
|  Merge`{.interpreted-text | merging that may affect inventory        |
|   role="guilabel"}        | valuation, if the **Inventory** app is   |
| | [data\_merge\_st        | installed.                               |
| ock\_account]{.title-ref} |                                          |
+---------------------------+------------------------------------------+
:::

Deduplication {#data_cleaning/deduplication}
-------------

The *Duplicates* dashboard groups similar records to be
`merged <data_cleaning/merge-records>`{.interpreted-text role="ref"} by
matching conditions within the records set by the `deduplication rules
<data_cleaning/deduplication-rules>`{.interpreted-text role="ref"}.

Navigate to this dashboard by going to
`Data Cleaning app --> Deduplication`{.interpreted-text
role="menuselection"}.



The `RULE`{.interpreted-text role="guilabel"} sidebar lists each of the
active deduplication rules, and displays the total number of duplicates
detected beside each rule.

By default, the `All`{.interpreted-text role="guilabel"} rule is
selected. Records are grouped by their rule, with a
`Similarity`{.interpreted-text role="guilabel"} rating (out of 100%),
with the following columns:

-   `Created On`{.interpreted-text role="guilabel"}: the date and time
    the original record was created.
-   `Name`{.interpreted-text role="guilabel"}: the name or title of the
    original record.
-   `Field Values`{.interpreted-text role="guilabel"}: the original
    record\'s values for the fields used to detect duplicates.
-   `Used In`{.interpreted-text role="guilabel"}: lists other models
    referencing the original record.
-   `ID`{.interpreted-text role="guilabel"}: the original record\'s
    unique ID.
-   `Is Master`{.interpreted-text role="guilabel"}: the duplicates are
    merged into the *master* record. There can only be **one** master
    record in a grouping of similar records.

Select a specific rule in the `RULE`{.interpreted-text role="guilabel"}
sidebar to filter the duplicate records.

### Merge duplicate records {#data_cleaning/merge-records}

To merge records, first choose a *master* record within the grouping of
similar records. The master record acts as the base, at which any
additional information from similar records are merged into.

Optionally, no master record can be set, leaving Odoo to choose a record
at random to merge into.

Next, click the `Merge`{.interpreted-text role="guilabel"} button at the
top of the similar records grouping. Then, click `Ok`{.interpreted-text
role="guilabel"} to confirm the merge.

Once a record is merged, a message is logged in the chatter of the
master record, describing the merge. Certain records, like **Project**
tasks, are logged in the chatter with a link to the old record as a
convenient reference of the merge.

::: {.tip}
::: {.title}
Tip
:::

Discard groupings by clicking the `DISCARD`{.interpreted-text
role="guilabel"} button. Upon doing so, the grouping is hidden from the
list and archived.

View discarded groupings by selecting the `Discarded`{.interpreted-text
role="guilabel"} filter from the `search bar
<search/filters>`{.interpreted-text role="ref"}.
:::

### Deduplication rules {#data_cleaning/deduplication-rules}

The *Deduplication Rules* set the conditions for how records are
detected as duplicates.

These rules can be configured for each model in the database, and with
varying levels of specificity. To get started, navigate to
`Data Cleaning app --> Configuration -->
Deduplication`{.interpreted-text role="menuselection"}.

::: {.tip}
::: {.title}
Tip
:::

The deduplication rules run once every day, by default, as part of a
scheduled action cron (*Data Merge: Find Duplicate Records*). However,
each rule can be `ran manually
<data_cleaning/run-deduplication-rule>`{.interpreted-text role="ref"}
anytime.
:::

#### Modify a deduplication rule

Select a default rule to edit, or create a new rule by clicking on the
`New`{.interpreted-text role="guilabel"} button.

First, choose a `Model`{.interpreted-text role="guilabel"} for this rule
to target. Selecting a model updates the rule title to the chosen model.

Optionally, configure a `Domain`{.interpreted-text role="guilabel"} to
specify the records eligible for this rule. The number of eligible
records is shown in the `oi-arrow-right`{.interpreted-text role="icon"}
`# record(s)`{.interpreted-text role="guilabel"} link.

Depending on the selected `Model`{.interpreted-text role="guilabel"},
the `Duplicate Removal`{.interpreted-text role="guilabel"} field
appears. Choose whether to `Archive`{.interpreted-text role="guilabel"}
or `Delete`{.interpreted-text role="guilabel"} merged records.

Next, select a `Merge Mode`{.interpreted-text role="guilabel"}:

-   `Manual`{.interpreted-text role="guilabel"}: requires each duplicate
    grouping to be manually merged, also enables the
    `Notify Users`{.interpreted-text role="guilabel"} field.
-   `Automatic`{.interpreted-text role="guilabel"}: automatically merges
    duplicate groupings, without notifying users, based on the records
    with a similarity percentage above the threshold set in the
    `Similarity
    Threshold`{.interpreted-text role="guilabel"} field.

Enable the `Active`{.interpreted-text role="guilabel"} toggle to start
capturing duplicates with this rule as soon as it is saved.

Lastly, create at least one deduplication rule in the
`Deduplication Rules`{.interpreted-text role="guilabel"} field, by
clicking `Add a line`{.interpreted-text role="guilabel"}, under the
`Unique ID Field`{.interpreted-text role="guilabel"} column.

-   Select a field in the model from the
    `Unique ID Field`{.interpreted-text role="guilabel"} drop-down menu.
    This field is referenced for similar records.
-   Select a matching condition in the `Match If`{.interpreted-text
    role="guilabel"} field to apply the deduplication rule, depending on
    the text in the `Unique ID Field`{.interpreted-text
    role="guilabel"}:
    -   `Exact Match`{.interpreted-text role="guilabel"}: the characters
        in the text match exactly.
    -   `Case/Accent Insensitive Match`{.interpreted-text
        role="guilabel"}: the characters in the text match, regardless
        of casing and language-specific accent differences.

::: {.important}
::: {.title}
Important
:::

At least one `Deduplication Rules`{.interpreted-text role="guilabel"}
must be set for the rule to capture duplicates.
:::

::: {.tip}
::: {.title}
Tip
:::

A few more fields are available for an advanced configuration.

If on a multi-company database, the `Cross-Company`{.interpreted-text
role="guilabel"} field is available. When enabled, duplicates across
different companies are suggested.

Activate `developer-mode`{.interpreted-text role="ref"} to display the
`Suggestion Threshold`{.interpreted-text role="guilabel"} field.
Duplicates with a similarity below the threshold set in this field are
**not** suggested.
:::

With the rule\'s configuration complete, either close the rule form, or
`run the rule manually
<data_cleaning/run-deduplication-rule>`{.interpreted-text role="ref"} to
instantly capture duplicate records.

#### Manually run a deduplication rule {#data_cleaning/run-deduplication-rule}

To manually run a specific deduplication rule at any time, navigate to
`Data Cleaning
app --> Configuration --> Deduplication`{.interpreted-text
role="menuselection"}, and select the rule to run.

Then, on the rule form, select the `Deduplicate`{.interpreted-text
role="guilabel"} button on the top-left. Upon doing so, the
`fa-clone`{.interpreted-text role="icon"} `Duplicates`{.interpreted-text
role="guilabel"} smart button displays the number of duplicates
captured.

Click on the `fa-clone`{.interpreted-text role="icon"}
`Duplicates`{.interpreted-text role="guilabel"} smart button to
`manage these records
<data_cleaning/merge-records>`{.interpreted-text role="ref"}.

Recycle records {#data_cleaning/recycle}
---------------

Use the *recycle records* feature to rid the database of old and
outdated records.

The *Field Recycle Records* dashboard displays records that can be
archived or deleted, by matching conditions within the records set by
the
`recycle record's rules <data_cleaning/recylce-rule>`{.interpreted-text
role="ref"}.

Navigate to this dashboard by going to
`Data Cleaning app --> Recycle Records`{.interpreted-text
role="menuselection"}.



The `RECYCLE RULES`{.interpreted-text role="guilabel"} sidebar lists
each of the active recycle record rules.

By default, the `All`{.interpreted-text role="guilabel"} option is
selected. Records are displayed with the following columns:

-   `Record ID`{.interpreted-text role="guilabel"}: the ID of the
    original record.
-   `Record Name`{.interpreted-text role="guilabel"}: the name or title
    of the original record.

Select a specific rule in the `RECYCLE RULES`{.interpreted-text
role="guilabel"} sidebar to filter the records.

To recycle records, click the `fa-check`{.interpreted-text role="icon"}
`Validate`{.interpreted-text role="guilabel"} button on the row of the
record.

Upon doing so, the record is recycled, depending on how the rule is
configured, to be either archived or deleted from the database.

::: {.tip}
::: {.title}
Tip
:::

Discard groupings by clicking the `fa-times`{.interpreted-text
role="icon"} `Discard`{.interpreted-text role="guilabel"} button. Upon
doing so, the record is hidden from the list, and is not detected by the
recycle rule again in the future.

View discarded records by selecting the `Discarded`{.interpreted-text
role="guilabel"} filter from the `search bar
<search/filters>`{.interpreted-text role="ref"} drop-down menu.
:::

### Recycle record rules {#data_cleaning/recylce-rule}

The *Recycle Records Rules* set the conditions for how records are
recycled.

These rules can be configured for each model in the database, and with
varying levels of specificity. To get started, navigate to
`Data Cleaning app --> Configuration -->
Recycle Records`{.interpreted-text role="menuselection"}.

::: {.tip}
::: {.title}
Tip
:::

Recycle rules run once a day, by default, as part of a scheduled action
cron (*Data Recycle: Clean Records*). However, each rule can be
`run manually <data-cleaning/run-recycle-rule>`{.interpreted-text
role="ref"} anytime.
:::

By default, no recycle record rules exist. Click the
`New`{.interpreted-text role="guilabel"} button to create a new rule.

On the recycle record rule form, first choose a
`Model`{.interpreted-text role="guilabel"} for this rule to target.
Selecting a model updates the rule title to the chosen model.

Optionally, configure a `Filter`{.interpreted-text role="guilabel"} to
specify the records eligible for this rule. The number of eligible
records is shown in the `oi-arrow-right`{.interpreted-text role="icon"}
`# record(s)`{.interpreted-text role="guilabel"} link.

Next, configure the field and time range for how the rule detects the
records to recycle:

-   `Time Field`{.interpreted-text role="guilabel"}: select a field from
    the model to base the time (`Delta`{.interpreted-text role="dfn"}).
-   `Delta`{.interpreted-text role="guilabel"}: type the length of time,
    which must be a whole number (e.g. [7]{.title-ref}).
-   `Delta Unit`{.interpreted-text role="guilabel"}: select the unit of
    time (`Days`{.interpreted-text role="guilabel"},
    `Weeks`{.interpreted-text role="guilabel"},
    `Months`{.interpreted-text role="guilabel"}, or
    `Years`{.interpreted-text role="guilabel"}).

Then, select a `Recycle Mode`{.interpreted-text role="guilabel"}:

-   `Manual`{.interpreted-text role="guilabel"}: requires each detected
    record to be manually recycled, and enables the
    `Notify Users`{.interpreted-text role="guilabel"} field.
-   `Automatic`{.interpreted-text role="guilabel"}: automatically merges
    recycled groupings, without notifying users.

Lastly, select a `Recycle Action`{.interpreted-text role="guilabel"} to
either `Archive`{.interpreted-text role="guilabel"} or
`Delete`{.interpreted-text role="guilabel"} records. If
`Delete`{.interpreted-text role="guilabel"} is selected, choose whether
or not to `Include Archived`{.interpreted-text role="guilabel"} records
in the rule.

With the rule\'s configuration complete, either close the rule form, or
`run the rule manually
<data-cleaning/run-recycle-rule>`{.interpreted-text role="ref"} to
instantly capture records to recycle.

::: {.example}
A recycle rule can be configured to delete archived leads and
opportunities that were last updated a year ago, and with a specific
lost reason, by using the following configuration:

-   `Model`{.interpreted-text role="guilabel"}:
    `Lead/Opportunity`{.interpreted-text role="guilabel"}
-   `Filter`{.interpreted-text role="guilabel"}:
    -   [Active]{.title-ref} [is]{.title-ref} [not set]{.title-ref}
    -   [Lost Reason]{.title-ref} [is in]{.title-ref} [Too
        expensive]{.title-ref}
-   `Time Field`{.interpreted-text role="guilabel"}:
    `Last Updated on (Lead/Opportunity)`{.interpreted-text
    role="guilabel"}
-   `Delta`{.interpreted-text role="guilabel"}: [1]{.title-ref}
-   `Delta Unit`{.interpreted-text role="guilabel"}:
    `Years`{.interpreted-text role="guilabel"}
-   `Recycle Mode`{.interpreted-text role="guilabel"}:
    `Automatic`{.interpreted-text role="guilabel"}
-   `Recycle Action`{.interpreted-text role="guilabel"}:
    `Delete`{.interpreted-text role="guilabel"}
-   `Include Archived`{.interpreted-text role="guilabel"}:
    `fa-check-square`{.interpreted-text role="icon"}


:::

#### Manually run a recycle rule {#data-cleaning/run-recycle-rule}

To manually run a specific recycle rule at any time, navigate to
`Data Cleaning app
--> Configuration --> Recycle Records`{.interpreted-text
role="menuselection"}, and select the rule to run.

Then, on the rule form, click the `Run Now`{.interpreted-text
role="guilabel"} button on the top-left. Upon doing so, the
`fa-bars`{.interpreted-text role="icon"} `Records`{.interpreted-text
role="guilabel"} smart button displays the number of records captured.

Click the `fa-bars`{.interpreted-text role="icon"}
`Records`{.interpreted-text role="guilabel"} smart button to
`manage these records
<data_cleaning/recycle>`{.interpreted-text role="ref"}.

Field cleaning {#data_cleaning/field-cleaning}
--------------

Use the field cleaning feature to maintain consistent formatting of
names, phone numbers, IDs and other fields throughout a database.

The *Field Cleaning Records* dashboard displays formatting changes to
data in fields of a record, to follow a convention set by the field
cleaning rules.

Navigate to this dashboard by going to
`Data Cleaning app --> Field Cleaning`{.interpreted-text
role="menuselection"}.



The `CLEANING RULES`{.interpreted-text role="guilabel"} sidebar lists
each of the active cleaning rules.

By default, the `All`{.interpreted-text role="guilabel"} rule is
selected. Records are listed with the following columns:

-   `Record ID`{.interpreted-text role="guilabel"}: the ID of the
    original record.
-   `Record Name`{.interpreted-text role="guilabel"}: the name or title
    of the original record.
-   `Field`{.interpreted-text role="guilabel"}: the original record\'s
    field that contains the value to format.
-   `Current`{.interpreted-text role="guilabel"}: the current value in
    the field of the original record.
-   `Suggested`{.interpreted-text role="guilabel"}: the suggested
    formatted value in the field of the original record.

To clean and format records, click the `fa-check`{.interpreted-text
role="icon"} `Validate`{.interpreted-text role="guilabel"} button on the
row of the record.

Upon doing so, the record is formatted and/or cleaned.

::: {.tip}
::: {.title}
Tip
:::

Discard records by clicking the `fa-times`{.interpreted-text
role="icon"} `Discard`{.interpreted-text role="guilabel"} button. Upon
doing so, the record is hidden from the list and will not be detected by
the field cleaning rule again in the future.

View discarded records by selecting the `Discarded`{.interpreted-text
role="guilabel"} filter from the `search bar
<search/filters>`{.interpreted-text role="ref"}.
:::

### Field cleaning rules {#data_cleaning/field-cleaning-rule}

The *Field Cleaning Rules* set the conditions for fields to be cleaned
and/or formatted.

These rules can be configured for each model in the database, and with
varying levels of specificity. To get started, navigate to
`Data Cleaning app --> Configuration -->
Field Cleaning`{.interpreted-text role="menuselection"}.

::: {.tip}
::: {.title}
Tip
:::

The field cleaning rules run once every day, by default, as part of a
scheduled action cron (*Data Cleaning: Clean Records*). However, each
rule can be `ran manually
<data-cleaning/run-field-cleaning-rule>`{.interpreted-text role="ref"}
anytime.
:::

By default, a `Contact`{.interpreted-text role="guilabel"} rule exists
to format and clean up the **Contacts** app records. Select the
`Contact`{.interpreted-text role="guilabel"} record to make edits, or
select the `New`{.interpreted-text role="guilabel"} button to create a
new rule.

On the field cleaning rule form, first choose a
`Model`{.interpreted-text role="guilabel"} for this rule to target.
Selecting a model updates the rule title to the chosen model.

Next, configure at least one rule by clicking
`Add a line`{.interpreted-text role="guilabel"} in the
`Rules`{.interpreted-text role="guilabel"} section.

Upon doing so, a `Create Rules`{.interpreted-text role="guilabel"}
popover window appears with the following fields to configure:

-   Select a `Field To Clean`{.interpreted-text role="guilabel"} from
    the model to assign to an action.

-   Choose one of the following `Action`{.interpreted-text
    role="guilabel"} options:

    -   `Trim Spaces`{.interpreted-text role="guilabel"} reveals the
        `Trim`{.interpreted-text role="guilabel"} field to select the
        `All Spaces`{.interpreted-text role="guilabel"} or
        `Superfluous Spaces`{.interpreted-text role="guilabel"} option.
        Leading, trailing, and successive spaces are considered
        superfluous.

        ::: {.example}
        The contact name [Dr. John Doe]{.title-ref} can be formatted
        with the following `Trim`{.interpreted-text role="guilabel"}
        options:

        -   `All Spaces`{.interpreted-text role="guilabel"}:
            [DR.JohnDoe]{.title-ref}
        -   `Superfluous Spaces`{.interpreted-text role="guilabel"}:
            [DR. John Doe]{.title-ref}
        :::

    -   `Set Type Case`{.interpreted-text role="guilabel"} reveals the
        `Case`{.interpreted-text role="guilabel"} field to select either
        `First
        Letters to Uppercase`{.interpreted-text role="guilabel"},
        `All Uppercase`{.interpreted-text role="guilabel"}, or
        `All Lowercase`{.interpreted-text role="guilabel"}.

        ::: {.example}
        The lead/opportunity title [lumber inc, Lorraine
        douglas]{.title-ref} can be formatted with the following
        `Case`{.interpreted-text role="guilabel"} options:

        -   `First Letters to Uppercase`{.interpreted-text
            role="guilabel"}: [Lumber Inc, Lorraine Douglas]{.title-ref}
        -   `All Uppercase`{.interpreted-text role="guilabel"}: [LUMBER
            INC, LORRAINE DOUGLAS]{.title-ref}
        -   `All Lowercase`{.interpreted-text role="guilabel"}: [lumber
            inc, lorraine douglas]{.title-ref}
        :::

    -   `Format Phone`{.interpreted-text role="guilabel"} converts the
        phone number to an international country format.

        ::: {.example}
        -   Belgium: [061928374]{.title-ref}
            `fa-long-arrow-right`{.interpreted-text role="icon"} [+32 61
            92 83 74]{.title-ref}
        -   United States: [800 555-0101]{.title-ref}
            `fa-long-arrow-right`{.interpreted-text role="icon"} [+1
            800-555-0101]{.title-ref}
        :::

    -   `Scrap HTML`{.interpreted-text role="guilabel"} converts
        `HTML (HyperText Markup Language)`{.interpreted-text
        role="abbr"} to plain text.

        ::: {.example}
        ``` {.html}
        <h1>John Doe</h1>
        <p>Lorem ipsum dolor sit <a href="https://example.com">amet</a>.</p>
        ```

        ``` {.text}
        **John Doe** Lorem ipsum dolor sit amet [1] .[1] https://example.com
        ```
        :::

    Once a field and action are selected, click `Save`{.interpreted-text
    role="guilabel"} to close the `Create Rules`{.interpreted-text
    role="guilabel"} popover window.

Then, select a `Cleaning Mode`{.interpreted-text role="guilabel"}:

-   `Manual`{.interpreted-text role="guilabel"}: requires each detected
    field to be manually cleaned and enables the
    `Notify Users`{.interpreted-text role="guilabel"} field.
-   `Automatic`{.interpreted-text role="guilabel"}: automatically cleans
    fields without notifying users.

With the rule\'s configuration complete, either close the rule form, or
`run the rule manually
<data-cleaning/run-field-cleaning-rule>`{.interpreted-text role="ref"}
to instantly capture fields to clean.

#### Manually run a field cleaning rule {#data-cleaning/run-field-cleaning-rule}

To manually run a specific field cleaning rule at any time, navigate to
`Data
Cleaning app --> Configuration --> Field Cleaning`{.interpreted-text
role="menuselection"}, and select the rule to run.

Then, on the rule form, select the `Clean`{.interpreted-text
role="guilabel"} button on the top-left. Upon doing so, the
`fa-bars`{.interpreted-text role="icon"} `Records`{.interpreted-text
role="guilabel"} smart button displays the number of records captured.

Click on the `fa-bars`{.interpreted-text role="icon"}
`Records`{.interpreted-text role="guilabel"} smart button to
`manage these records
<data_cleaning/field-cleaning>`{.interpreted-text role="ref"}.

Merge action manager {#data_cleaning/merge-action-manager}
--------------------

The *Merge Action Manager* enables or disables the *Merge* action
available in the *Actions* menu for models in the database.

Enable `developer-mode`{.interpreted-text role="ref"} and navigate to
`Data Cleaning app --> Configuration -->
Merge Action Manager`{.interpreted-text role="menuselection"}.

Models are listed with the following columns:

-   `Model`{.interpreted-text role="guilabel"}: technical name of the
    model.
-   `Model Description`{.interpreted-text role="guilabel"}: display name
    of the model.
-   `Type`{.interpreted-text role="guilabel"}: whether the model is of
    the *Base Object* or *Custom Object* type.
-   `Transient Model`{.interpreted-text role="guilabel"}: the model
    handles temporary data that does not need to be stored long-term in
    the database.
-   `Can Be Merged`{.interpreted-text role="guilabel"}: enables the
    *Merge* action for the model.

To view which models are enabled by default, use the
`search bar <search/filters>`{.interpreted-text role="ref"} to filter
models that `Can Be Merged`{.interpreted-text role="guilabel"}.

::: {.seealso}
`../essentials/contacts/merge`{.interpreted-text role="doc"}
:::
