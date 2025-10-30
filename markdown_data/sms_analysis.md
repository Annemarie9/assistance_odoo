# File: /content/odoo_doc17.0/fr/content/applications/marketing/sms_marketing/sms_analysis.md

SMS analysis
============

On the `Reporting`{.interpreted-text role="guilabel"} page (accessible
via the `Reporting`{.interpreted-text role="menuselection"} option in
the header menu), there are options to apply different combinations of
`Filters`{.interpreted-text role="guilabel"} and
`Measures`{.interpreted-text role="guilabel"} to view metrics in a
number of different layouts (e.g. `Graph`{.interpreted-text
role="guilabel"}, `List`{.interpreted-text role="guilabel"}, and
`Cohort`{.interpreted-text role="guilabel"} views.)

Each `Reporting`{.interpreted-text role="guilabel"} metric view option
allows for more extensive performance analysis of
`SMS (Short Message Service)`{.interpreted-text role="abbr"} mailings.

For example, while in the default `Graph`{.interpreted-text
role="guilabel"} view, `SMS (Short Message Service)`{.interpreted-text
role="abbr"} data is visualized as different graphs and charts, which
can be sorted and grouped in various ways (e.g.
`Measures`{.interpreted-text role="guilabel"} drop down menu).

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

SMS messages can be sent using automation rules in Odoo. Odoo *Studio*
is required to use automation rules.

To install Odoo *Studio*, go to the `Apps application`{.interpreted-text
role="menuselection"}. Then, using the `Search...`{.interpreted-text
role="guilabel"} bar, search for [studio]{.title-ref}.

If it is not already installed, click `Install`{.interpreted-text
role="guilabel"}.

Adding the *Studio* application upgrades the subscription status to
*Custom*, which increases the cost. Consult
, or reach out to the
database\'s customer success manager, with any questions on making the
change.

To use automation rules, navigate in
`developer mode <developer-mode>`{.interpreted-text role="ref"}, to
`Settings app --> Technical menu --> Automation section --> Automation Rules`{.interpreted-text
role="menuselection"}. Then, click `New`{.interpreted-text
role="guilabel"} to create a new rule.

Enter a name for the automation rule, and select a
`Model`{.interpreted-text role="guilabel"} to implement this rule on.

Based on the selection for the `Trigger`{.interpreted-text
role="guilabel"}, additional fields will populate below. Set the
`Trigger`{.interpreted-text role="guilabel"} to one of the following
options:

`Values Updated`{.interpreted-text role="guilabel"}

-   `User is set`{.interpreted-text role="guilabel"}
-   `State is set to`{.interpreted-text role="guilabel"}
-   `On archived`{.interpreted-text role="guilabel"}
-   `On unarchived`{.interpreted-text role="guilabel"}

`Timing Conditions`{.interpreted-text role="guilabel"}

-   `Based on date field`{.interpreted-text role="guilabel"}
-   `After creation`{.interpreted-text role="guilabel"}
-   `After last update`{.interpreted-text role="guilabel"}

`Custom`{.interpreted-text role="guilabel"}

-   `On save`{.interpreted-text role="guilabel"}
-   `On deletion`{.interpreted-text role="guilabel"}
-   `On UI change`{.interpreted-text role="guilabel"}

`External`{.interpreted-text role="guilabel"}

-   `On webhook`{.interpreted-text role="guilabel"}

Other options may appear based on the `Model`{.interpreted-text
role="guilabel"} selected. For example if the
`Calendar Event`{.interpreted-text role="guilabel"} model is selected,
then the following options appear in addition to those above:

`Email Events`{.interpreted-text role="guilabel"}

-   `On incoming message`{.interpreted-text role="guilabel"}
-   `On outgoing message`{.interpreted-text role="guilabel"}

Under the `Before Update Domain`{.interpreted-text role="guilabel"}
field, set a condition to be met before updating the record. Click
`Edit Domain`{.interpreted-text role="guilabel"} to set record
parameters.

Under the `Actions To Do`{.interpreted-text role="guilabel"} tab, select
`Add an action`{.interpreted-text role="guilabel"}. Next, in the
resulting `Create Actions`{.interpreted-text role="guilabel"} pop-up
window, select `Send SMS`{.interpreted-text role="guilabel"}, and set
the `Allowed Groups`{.interpreted-text role="guilabel"}.
`Allowed Groups`{.interpreted-text role="guilabel"} are the access
rights groups that are allowed to execute this rule. Leave the field
empty to allow all groups. See this documentation:
`access-rights/groups`{.interpreted-text role="ref"}.

Next, set the `SMS Template`{.interpreted-text role="guilabel"} and
choose whether the SMS message should be logged as a note, by making a
selection in the drop-down menu: `Send SMS as`{.interpreted-text
role="guilabel"}. Click `Save and Close`{.interpreted-text
role="guilabel"} to save the changes to this new action.

{.align-center}

Add any necessary notes under the `Notes`{.interpreted-text
role="guilabel"} tab. Finally, navigate away from the completed
automation rule, or manually save (by clicking the
`☁️ (cloud)`{.interpreted-text role="guilabel"} icon), to implement the
change.
:::
