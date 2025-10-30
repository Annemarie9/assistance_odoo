# File: /content/odoo_doc17.0/fr/content/applications/marketing/marketing_automation/target_audience.md

Audience targeting
==================

The `Target`{.interpreted-text role="guilabel"} and
`Filter`{.interpreted-text role="guilabel"} fields on the campaign form,
also referred to as the *domain*, contain the parameters used to define
the target audience for the campaign\'s reach (i.e., the unique contact
records in the database, and imported list, etc.).

-   `Target`{.interpreted-text role="guilabel"}: specifies the type of
    records available for use in the campaign, such as
    `Lead/Opportunity`{.interpreted-text role="guilabel"},
    `Event Registration`{.interpreted-text role="guilabel"},
    `Contact`{.interpreted-text role="guilabel"}, The assigned records
    model determines the fields that are available throughout the
    campaign, including the fields available in the
    `Filter`{.interpreted-text role="guilabel"} section, and in dynamic
    placeholders.
-   `Save as Favorite Filter`{.interpreted-text role="guilabel"}: saves
    the current `Filter`{.interpreted-text role="guilabel"} for future
    use with the current `Target`{.interpreted-text role="guilabel"}
    model, and can be managed from the `Marketing Automation
    app --> Configuration --> Favorite Filters`{.interpreted-text
    role="menuselection"} menu.
-   `Unicity based on`{.interpreted-text role="guilabel"}: specifies the
    `Target`{.interpreted-text role="guilabel"} model field where
    duplicates should be avoided. Traditionally, the
    `Email`{.interpreted-text role="guilabel"} field is used, but any
    available field can be used.
-   `Filter`{.interpreted-text role="guilabel"}: contains an interactive
    form with configurable logic to further refine the targeting
    parameters under the chosen `Target`{.interpreted-text
    role="guilabel"} model. See more details in the
    `marketing_automation/defining-filters`{.interpreted-text
    role="ref"} section.
-   `Include archived`{.interpreted-text role="guilabel"}: allows or
    disallows the inclusion of archived records in the target audience.

::: {.tip}
::: {.title}
Tip
:::

A `Responsible`{.interpreted-text role="guilabel"} user can be assigned
to the campaign by activating `developer-mode`{.interpreted-text
role="ref"}.
:::

::: {.note}
::: {.title}
Note
:::

Each activity in a campaign\'s workflow can target a subset of the
target audience; see the `workflow_activities`{.interpreted-text
role="doc"} documentation for more information.
:::

Defining filters {#marketing_automation/defining-filters}
----------------

The default campaign `Filter`{.interpreted-text role="guilabel"}
configuration is set to `Match all records`{.interpreted-text
role="guilabel"}, indicating that the campaign is targeting **all**
records of the `Target`{.interpreted-text role="guilabel"} model.

To refine the `Filter`{.interpreted-text role="guilabel"} rules of a
campaign, click the `➕ Add condition`{.interpreted-text role="guilabel"}
button to reveal a new row with configurable rule parameters. See the
`Search, filter, and group
records <search/custom-filters>`{.interpreted-text role="ref"}
documentation for more information on how to create filter rules.

{.align-center}

At the bottom of the filter rules is a `# record(s)`{.interpreted-text
role="guilabel"} button, which indicates the total number of records
targeted by this domain. Select the `# record(s)`{.interpreted-text
role="guilabel"} button to open a `Selected records`{.interpreted-text
role="guilabel"} pop-up window, in which the targeted records can be
viewed.

::: {.tip}
::: {.title}
Tip
:::

Activate `developer-mode`{.interpreted-text role="ref"} to reveal each
field\'s technical name and data type, as well as the
`# Code editor`{.interpreted-text role="guilabel"} text area below the
filter rules, to view and edit the domain manually.
:::

::: {.example}
To target all leads and opportunities from the *CRM* app that are in the
*New* stage, and have an expected revenue greater than \$1,000, the
following should be entered:

-   `Target`{.interpreted-text role="guilabel"}:
    [Lead/Opportunity]{.title-ref}
-   `Unicity based on`{.interpreted-text role="guilabel"}: [Email
    (Lead/Opportunity)]{.title-ref}
-   `Filter`{.interpreted-text role="guilabel"}:
    `Match`{.interpreted-text role="guilabel"}
    `all 🔽 (down arrow)`{.interpreted-text role="guilabel"} `of the
    following rules:`{.interpreted-text role="guilabel"}
    1.  `Stage`{.interpreted-text role="guilabel"}
        `is in`{.interpreted-text role="guilabel"}
        `New`{.interpreted-text role="guilabel"}
    2.  `Expected Revenue`{.interpreted-text role="guilabel"}
        `>`{.interpreted-text role="guilabel"} [1,000]{.title-ref}
    3.  `any 🔽 (down arrow)`{.interpreted-text role="guilabel"}
        `of:`{.interpreted-text role="guilabel"}
        -   `Type`{.interpreted-text role="guilabel"}
            `=`{.interpreted-text role="guilabel"}
            `Lead`{.interpreted-text role="guilabel"}
        -   `Type`{.interpreted-text role="guilabel"}
            `=`{.interpreted-text role="guilabel"}
            `Opportunity`{.interpreted-text role="guilabel"}

With the above configuration, the campaign targets
`157 record(s)`{.interpreted-text role="guilabel"}.

{.align-center}
:::

::: {.seealso}
\-
`Domain developer documentation <reference/orm/domains>`{.interpreted-text
role="ref"} - `workflow_activities`{.interpreted-text role="doc"} -
`testing_running`{.interpreted-text role="doc"} -
`understanding_metrics`{.interpreted-text role="doc"}
:::
