# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/plm/manage_changes/eco_type.md

ECO type {#plm/eco/eco-type}
========

An *ECO type* is assigned to *engineering change orders* (ECOs) to
organize and track changes to products and bills of materials (BoMs).
Each `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}
type separates `ECOs (Engineering Change Orders)`{.interpreted-text
role="abbr"} into a project in Gantt view, ensuring collaborators and
stakeholders **only** view and assist with relevant
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} improvements.

For example, an electronic chip manufacturer might use \'New Product
Introduction\', \'Product Improvement\', \'Component Change\', and
\'Firmware Update\' `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"} types. Then, designers and engineers can focus on
`ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} in the
\'New Product Introduction\' and \'Product Improvement\' projects,
avoiding unrelated supplier change or firmware update
`ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"}.

Create ECO type
---------------

To access and manage ECO types, navigate to
`PLM app --> Configuration --> ECO
Types`{.interpreted-text role="menuselection"}.

Create a new ECO type by clicking `New`{.interpreted-text
role="guilabel"}. On the new `ECO Types`{.interpreted-text
role="guilabel"} form, fill in the following information:

-   `Name`{.interpreted-text role="guilabel"}: the name of the
    `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}
    type, which will organize all of the
    `ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} of
    this *type* in a project.
-   `Email Alias`{.interpreted-text role="guilabel"}: if this optional
    field is filled, emails submitted to this email address
    automatically generate
    `ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} in
    the left-most stage of this
    `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}
    type.

::: {.example}
The [Formulation change]{.title-ref}
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} type is
used to organize and track related
`ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} in a
single project. Configuring the `Email Alias`{.interpreted-text
role="guilabel"} field generates
`ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} in the
[Formulation change]{.title-ref} project sent to the email address,
[pawlish-change\@pawlished-glam.odoo.com]{.title-ref}.

{.align-center}
:::

Edit ECO type
-------------

Modify existing `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"} type names and email aliases by navigating to the
`PLM app -->
Configuration --> ECO Types`{.interpreted-text role="menuselection"}
page. There, click on the desired
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} type
from the list.

On the form for each `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"} type, proceed to edit the `Name`{.interpreted-text
role="guilabel"} and `Email Alias`{.interpreted-text role="guilabel"}
fields.

Stages {#plm/eco/stage-config}
------

Within an `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"} type project, *stages* are like milestones and are used to
identify the progress of the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} before
the changes are ready to be applied. (e.g. \'Feedback\', \'In
Progress\', \'Approved\', \'Complete\')

Additionally, required approvers can be added to each stage, ensuring
that changes to the production
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} cannot proceed
until the approver reviews and approves the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}. Doing
so prevents errors on the production
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} by enforcing at
least one review of suggested changes before they\'re applied on a
production `BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

For best practice, there should be at least one *verification* stage,
which is a stage with a required approver, and one *closing* stage,
which stores `ECOs (Engineering Change Orders)`{.interpreted-text
role="abbr"} that have been either canceled or approved for use as the
next production `BoM (Bill of Materials)`{.interpreted-text
role="abbr"}.

### Create stage

To add a stage, go to the `PLM`{.interpreted-text role="menuselection"}
app and select the intended project for an
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} type
from the `PLM Overview`{.interpreted-text role="guilabel"} dashboard.

Then, on the `Engineering Change Orders`{.interpreted-text
role="guilabel"} project pipeline for the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} type,
click the `+ Stage`{.interpreted-text role="guilabel"} button. Doing so
reveals a text box to fill in the name of the stage. After filling it
in, click the `Add`{.interpreted-text role="guilabel"} button to finish
adding the stage.

::: {.example}
A new [Assigned]{.title-ref} stage separates assigned
`ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} from
the unassigned ones in the [New]{.title-ref} stage. Adding another stage
helps the product manager track unassigned tasks.

{.align-center}
:::

### Verification stage

Click an ECO type from `PLM app --> Overview`{.interpreted-text
role="menuselection"} to open a kanban view of
`ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} of
this type.

To configure a verification stage, hover over the intended stage, and
select the `⚙️
(gear)`{.interpreted-text role="guilabel"} icon. Then, click
`Edit`{.interpreted-text role="guilabel"} to open a pop-up window.

Configure the verification stage in the edit stage pop-up window, by
checking the box for `Allow to apply changes`{.interpreted-text
role="guilabel"}.

Then, add an approver in the `Approvers`{.interpreted-text
role="guilabel"} section, by clicking `Add a line`{.interpreted-text
role="guilabel"}, and specifying the `Role`{.interpreted-text
role="guilabel"} of the reviewer, their `User`{.interpreted-text
role="guilabel"}, and `Approval
Type`{.interpreted-text role="guilabel"}.

Make sure at least one approver is configured with the
`Approval Type`{.interpreted-text role="guilabel"}: `Is
required to approve`{.interpreted-text role="guilabel"}.

The approver listed is automatically notified when
`ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} are
dropped in the stage specified in the pop-up window. Once finished,
click `Save & Close`{.interpreted-text role="guilabel"}.

::: {.example}
In the `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}
type [New Product Introduction]{.title-ref}, the verification stage
[Validated]{.title-ref} is configured by clicking the
`⚙️ (gear)`{.interpreted-text role="guilabel"} icon, and selecting
`Edit`{.interpreted-text role="guilabel"}. Doing so opens the
`Edit: Validated`{.interpreted-text role="guilabel"} pop-up window.

By adding the [Engineering manager]{.title-ref} as an approver, only
`ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"}
approved by this user can proceed to the next stage, and have the
changes applied on the production
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

Additionally, check the `Allow to apply changes`{.interpreted-text
role="guilabel"} option to ensure proper behavior.

{.align-center}
:::

### Closing stage

Configure a closing stage by opening the
`Edit: [stage]`{.interpreted-text role="guilabel"} pop-up window. To do
so, hover over the intended stage and click the
`⚙️ (gear)`{.interpreted-text role="guilabel"} icon that appears in the
top-right corner. Then, click `Edit`{.interpreted-text role="guilabel"}
from the drop-down menu.

On the `Edit: [stage]`{.interpreted-text role="guilabel"} pop-up window,
select the check boxes for `Folded in
kanban view`{.interpreted-text role="guilabel"},
`Allow to apply changes`{.interpreted-text role="guilabel"} and
`Final Stage`{.interpreted-text role="guilabel"}.

::: {.example}
The closing stage, [Effective]{.title-ref} is configured by checking the
`Folded in kanban view`{.interpreted-text role="guilabel"},
`Allow to apply changes`{.interpreted-text role="guilabel"}, and
`Final Stage`{.interpreted-text role="guilabel"} options
:::

{.align-center}
