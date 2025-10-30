# File: /content/odoo_doc17.0/fr/content/applications/productivity/knowledge/properties.md

Properties
==========

Properties are fields containing data and that can be added to articles
by any user with **write** access. These fields are shared between all
the child articles and article items under the same parent.

::: {.note}
::: {.title}
Note
:::

To be able to add properties, an article must be either a **child
article** or an **article item**.
:::

Add property fields
-------------------

Hover above the first-level header to make the buttons appear. Click
`⚙ Add
Properties --> Field Type`{.interpreted-text role="menuselection"},
select the type and add a default value if needed. To make the fields
appear in **kanban views**, check `View in Kanban`{.interpreted-text
role="guilabel"} as well. To validate and close the property creation
window, click anywhere.

{.align-center}

The different types assess what the field content can be:

  ------------------------------------------------------------------------------------------
  Types                             Uses
  --------------------------------- --------------------------------------------------------
  `Text`{.interpreted-text          Allows adding any content with no restriction.
  role="guilabel"}                  

  `Checkbox`{.interpreted-text      Add a checkbox.
  role="guilabel"}                  

  `Integer`{.interpreted-text       Allows adding integer numbers.
  role="guilabel"}                  

  `Decimal`{.interpreted-text       Allows adding any number.
  role="guilabel"}                  

  `Date`{.interpreted-text          Allows selecting a date.
  role="guilabel"}                  

  `Date & Time`{.interpreted-text   Allows selecting a date and time.
  role="guilabel"}                  
  ------------------------------------------------------------------------------------------

Some **field types** need to be configured:

{.align-center}

+-------------+--------------------------------------------------------+
| Types       | Uses                                                   |
+=============+========================================================+
| `Select     | Add a drop-down selection menu with restricted values  |
| ion`{.inter | that have been set at the property creation.           |
| preted-text |                                                        |
| role=       | To set it up, click `Add a Value`{.interpreted-text    |
| "guilabel"} | role="guilabel"} next to the                           |
|             | `Values`{.interpreted-text role="guilabel"} field.     |
|             | Enter predetermined values and press **enter** to      |
|             | validate; you can enter as many values as needed.      |
|             | Click anywhere to close the property creation window.  |
+-------------+--------------------------------------------------------+
| `T          | Allows creating and applying as many tags as needed.   |
| ags`{.inter |                                                        |
| preted-text | To set it up, enter your [new\_tag]{.title-ref} in the |
| role=       | `Tags`{.interpreted-text role="guilabel"} field, and   |
| "guilabel"} | press **enter** or click                               |
|             | `Create "new_tag"`{.interpreted-text role="guilabel"}. |
|             | Click anywhere to close the window. Then, add the tags |
|             | into the property field. To do so, click the property  |
|             | field and choose from the created tags; enter the      |
|             | tags\' name and press **enter**; enter a new tag\'s    |
|             | name and create a new one on the spot.                 |
+-------------+--------------------------------------------------------+
| `Many2      | Choose from a list of records that result from a       |
| one`{.inter | model\'s domain. You can only select one result.       |
| preted-text |                                                        |
| role=       | To set it up, click `Search a Model`{.interpreted-text |
| "guilabel"} | role="guilabel"} in the `Model`{.interpreted-text      |
|             | role="guilabel"} field, select the model. Match all    |
|             | records by clicking `## Record(s)`{.interpreted-text   |
|             | role="guilabel"}, or filter the results by clicking    |
|             | `+ Add Filter`{.interpreted-text role="guilabel"} and  |
|             | show the records by clicking                           |
|             | `## Record(s)`{.interpreted-text role="guilabel"}.     |
+-------------+--------------------------------------------------------+
| `Many2m     | Choose from a list of records that result from a       |
| any`{.inter | model\'s domain. You can select as many results as     |
| preted-text | needed.                                                |
| role=       |                                                        |
| "guilabel"} | To set it up, click `Search a Model`{.interpreted-text |
|             | role="guilabel"} in the `Model`{.interpreted-text      |
|             | role="guilabel"} field, select the model. Match all    |
|             | records by clicking `## Record(s)`{.interpreted-text   |
|             | role="guilabel"}, or filter the results by clicking    |
|             | `+ Add Filter`{.interpreted-text role="guilabel"} and  |
|             | show the records by clicking                           |
|             | `## Record(s)`{.interpreted-text role="guilabel"}.     |
+-------------+--------------------------------------------------------+

Delete property fields
----------------------

To remove a property, click the **pencil** icon next to the targeted
property, then click `Delete --> Delete`{.interpreted-text
role="menuselection"}.

::: {.warning}
::: {.title}
Warning
:::

Once a property field is deleted, you cannot retrieve it.
:::

Hide the property panel
-----------------------

To hide the property sidebar panel, click the gear
`(⚙)`{.interpreted-text role="guilabel"} button.
