# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/plm/manage_changes/engineering_change_orders.md

Engineering change orders
=========================

::: {#plm/eco}
Utilize *engineering change orders* (*ECOs*) to track, implement, and
revert change versions made to products, and
`bills of materials <../../manufacturing/basic_setup/bill_configuration>`{.interpreted-text
role="doc"}.
:::

Engineering change orders can be created:

1.  `directly in the ECO type <plm/eco/create-eco>`{.interpreted-text
    role="ref"}.
2.  by an operator in the
    `tablet view <plm/eco/tablet-view>`{.interpreted-text role="ref"} of
    an operation.
3.  automatically from feedback submitted to the
    `ECO type's email alias <plm/eco/eco-type>`{.interpreted-text
    role="ref"}.

Create ECO {#plm/eco/create-eco}
----------

To create a new `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"}, begin by navigating to the *PLM* app. Then, select the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} type
card that will be used to track the progress of the change. On the
`Engineering Change Orders`{.interpreted-text role="guilabel"} page,
click the `New`{.interpreted-text role="guilabel"} button in the
top-left corner.

::: {.note}
::: {.title}
Note
:::

Learn how to create new `ECO types <plm/eco/eco-type>`{.interpreted-text
role="ref"} to categorize and organize change orders. Doing so ensures
employees only view the
`ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"}
related to their responsibilities, whether it involves new product
introductions, targeted product line updates, or regulatory compliance
fulfillment.
:::

On the `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}
form, fill in the following fields accordingly:

-   `Description`{.interpreted-text role="guilabel"} is a brief summary
    of the improvement.

-   `Type`{.interpreted-text role="guilabel"}: specifies the
    `ECO (Engineering Change Order)`{.interpreted-text role="abbr"} type
    project for organizing the
    `ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"}.

-   `Apply on`{.interpreted-text role="guilabel"} determines if the
    `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}
    changes the `Bill of Materials`{.interpreted-text role="guilabel"}
    or the `Product Only`{.interpreted-text role="guilabel"}.

-   `Product`{.interpreted-text role="guilabel"} indicates the product
    being improved.

-   `Bill of Materials`{.interpreted-text role="guilabel"} specifies the
    changed `BoM (Bill of Materials)`{.interpreted-text role="abbr"}. It
    auto-populates if the product in `Product`{.interpreted-text
    role="guilabel"} field has an existing
    `BoM (Bill of Materials)`{.interpreted-text role="abbr"}. If
    multiple `BoMs (Bills of Materials)`{.interpreted-text role="abbr"}
    exist, select the intended radio options from the drop-down menu.

-   `Company`{.interpreted-text role="guilabel"} field is used in
    multi-company databases. Specify if the change applies to products
    in a specific company, or leave blank if the change applies to all
    companies.

-   `Responsible`{.interpreted-text role="guilabel"} represents the
    assignee in charge of this
    `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}.
    (Optional)

-   `Effective`{.interpreted-text role="guilabel"} specifies when the
    `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}
    becomes live. Choosing `As soon as
    possible`{.interpreted-text role="guilabel"} means the
    `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}
    applies to the production
    `BoM (Bill of Materials)`{.interpreted-text role="abbr"} as soon as
    an authorized user
    `applies the changes <plm/eco/apply-changes>`{.interpreted-text
    role="ref"}.

    On the other hand, choosing `At Date`{.interpreted-text
    role="guilabel"}, and setting a specific date, leaves a date that
    makes it easier to track the version history of the
    `BoM (Bill of Materials)`{.interpreted-text role="abbr"}, and the
    specific date `BoMs (Bills of Materials)`{.interpreted-text
    role="abbr"}, used for production.

-   `Tags`{.interpreted-text role="guilabel"} are assigned to
    `ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"}
    for prioritization and organization. Create a new tag by typing the
    name in the field and selecting `Create`{.interpreted-text
    role="guilabel"} from the drop-down menu. (Optional)

After filling out the `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"} form, click the `Start Revision`{.interpreted-text
role="guilabel"} button to begin implementing the changes.

By pressing `Start Revision`{.interpreted-text role="guilabel"}, three
actions occur:

1.  The `Documents`{.interpreted-text role="guilabel"} smart button
    appears, storing relevant files of the
    `BoM (Bill of Materials)`{.interpreted-text role="abbr"}.
2.  A copy of the production `BoM (Bill of Materials)`{.interpreted-text
    role="abbr"} is stored in the newly-appeared
    `Revision`{.interpreted-text role="guilabel"} smart button of the
    `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}. The
    next available version number (e.g., [V2]{.title-ref},
    [V3]{.title-ref}, \...) is also assigned to keep track of all
    `BoM (Bill of Materials)`{.interpreted-text role="abbr"} versions.
3.  The stages of the `ECO (Engineering Change Order)`{.interpreted-text
    role="abbr"} `Type`{.interpreted-text role="guilabel"} are displayed
    in the top-right corner of the
    `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}.

::: {.note}
::: {.title}
Note
:::

The `Revision`{.interpreted-text role="guilabel"} smart button is
available **only** when the `Bill of
Materials`{.interpreted-text role="guilabel"} radio button is selected
in the `Apply on`{.interpreted-text role="guilabel"} field, and the
`Start
Revision`{.interpreted-text role="guilabel"} button has been pressed.
:::

{.align-center}

Change components
-----------------

To modify the components in a
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, click the
`Revision`{.interpreted-text role="guilabel"} smart button on an
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} to
access the new version of the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}. Odoo
distinguishes the non-production version of the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} from the
current version, by flagging the test
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} with a large
`Archived`{.interpreted-text role="guilabel"} tag.

::: {.example}
After clicking the `Start Revision`{.interpreted-text role="guilabel"}
button for an `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"} for the product, [\[D\_0045 Stool\]]{.title-ref}, make
changes to the product\'s `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} by clicking the `Revision`{.interpreted-text
role="guilabel"} smart button. Doing so opens the archived
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, marked with a
large red `Archived`{.interpreted-text role="guilabel"} flag.

{.align-center}
:::

On the new `BoM (Bill of Materials)`{.interpreted-text role="abbr"}, in
the `Components`{.interpreted-text role="guilabel"} tab, proceed to
modify the components list, by changing the `Quantity`{.interpreted-text
role="guilabel"} of existing components, adding new components using the
`Add a line`{.interpreted-text role="guilabel"} button, and removing
components with the `🗑️ (trash)`{.interpreted-text role="guilabel"}
icon.

::: {#plm/eco/example-keyboard}
::: {.example}
In version two of the `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} for a keyboard, the component quantities are reduced, and
an additional component, [Stabilizers]{.title-ref}, is added.

{.align-center}
:::
:::

### Compare changes

Once the changes are complete, navigate back to the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}, by
clicking [ECO00X]{.title-ref} in the breadcrumbs located in the top-left
corner. On the `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"} form, a new `BoM Changes`{.interpreted-text
role="guilabel"} tab displays the differences between the current
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} and the new
version.

Blue text indicates new components added to the revised
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} that are not in
the production `BoM (Bill of Materials)`{.interpreted-text role="abbr"}.
Black text represents updates shared by both
`BoMs (Bills of Materials)`{.interpreted-text role="abbr"}, while red
text indicates components removed in the revised
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

Changes and tests are encapsulated in the revised
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, and do **not**
affect the `BoM (Bill of Materials)`{.interpreted-text role="abbr"}
currently used in production. That is, until the
`changes are applied <plm/eco/apply-changes>`{.interpreted-text
role="ref"}.

::: {.example}
View the summary of the differences between the current and revised
keyboard `BoMs (Bills of Materials)`{.interpreted-text role="abbr"} in
the `BoM Changes`{.interpreted-text role="guilabel"} tab of the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}.

{.align-center}
:::

Change operations
-----------------

To modify the operations in a
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, click the
`Revision`{.interpreted-text role="guilabel"} smart button on an
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} to
access the archived, new version of the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

In the new `BoM (Bill of Materials)`{.interpreted-text role="abbr"}
version, switch to the `Operations`{.interpreted-text role="guilabel"}
tab to view and edit `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} operations. To make changes, select each operation, which
opens the corresponding `Open:
Operations`{.interpreted-text role="guilabel"} pop-up window.

::: {.note}
::: {.title}
Note
:::

The `Operations`{.interpreted-text role="guilabel"} tab is *not*
available by default. To enable it, navigate to
`Manufacturing app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and check the `Work
Orders`{.interpreted-text role="guilabel"} box.
:::

Make changes to any of the fields in the
`Open: Operations`{.interpreted-text role="guilabel"} pop-up window,
then click `Save`{.interpreted-text role="guilabel"} once completed.

Create new operations by clicking the `Add a line`{.interpreted-text
role="guilabel"} button, and remove new operations by clicking the
`Archive Operation`{.interpreted-text role="guilabel"} button.

### Compare changes

Once the changes are complete, navigate back to the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}, by
clicking [ECO00X]{.title-ref} in the breadcrumbs located in the top-left
corner.

On the `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}
form, a new `Operation Changes`{.interpreted-text role="guilabel"} tab
displays the differences between the current production
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} and the new
version.

Blue text indicates new operations added to the revised
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} that do not yet
exist in the production `BoM (Bill of Materials)`{.interpreted-text
role="abbr"}. Black text represents updates shared by both
`BoMs (Bills of Materials)`{.interpreted-text role="abbr"}, while red
text indicates operations removed in the revised
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

Modifications to the `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} in an `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"} will **not** affect the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} used in
production. That is, until the
`changes are applied <plm/eco/apply-changes>`{.interpreted-text
role="ref"}.

In the `Operation Changes`{.interpreted-text role="guilabel"} tab, each
row of details, beneath the columns in the table, reflect the following
information:

-   `Operation`{.interpreted-text role="guilabel"}: Name of the
    operation that was modified.
-   `Step`{.interpreted-text role="guilabel"}: specifies the quality
    control point, visible when the operation includes detailed
    instructions.

::: {.note}
::: {.title}
Note
:::

To check for instructions, click the operation line item in the
`Operations`{.interpreted-text role="guilabel"} tab of a
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}. Then, in the
`Open: Operations`{.interpreted-text role="guilabel"} pop-up window,
look for the `Instructions`{.interpreted-text role="guilabel"} smart
button displayed at the top.
:::

::: {.example}
The [Assembly]{.title-ref} `Operation`{.interpreted-text
role="guilabel"} includes [10]{.title-ref} detailed
`Instructions`{.interpreted-text role="guilabel"} to complete it.

![Show \*Instructions\* smart button to check whether an operation has additional
instructions.](engineering_change_orders/instructions-smart-button.png){.align-center}
:::

-   `Step Type`{.interpreted-text role="guilabel"} details the type of
    quality control for further instructions in the operation.
-   `Type`{.interpreted-text role="guilabel"} corresponds with the
    colored text to specify how the revised
    `BoM (Bill of Materials)`{.interpreted-text role="abbr"} differs
    from the production `BoM (Bill of Materials)`{.interpreted-text
    role="abbr"}. Operation change types can be `Add`{.interpreted-text
    role="guilabel"}, `Remove`{.interpreted-text role="guilabel"}, or
    `Update`{.interpreted-text role="guilabel"}.
-   `Work Center`{.interpreted-text role="guilabel"} specifies the work
    center at which the operation is performed.
-   `Manual Duration Change`{.interpreted-text role="guilabel"} refers
    to the change in the `Default Duration`{.interpreted-text
    role="guilabel"} field in the `Open: Operations`{.interpreted-text
    role="guilabel"} pop-up window, which specifies the expected time
    for completing the operation.

::: {.example}
The `Operation Changes`{.interpreted-text role="guilabel"} tab compares
the production `BoM (Bill of Materials)`{.interpreted-text role="abbr"}
with the revised `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} in the `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"}.

In the revised `BoM (Bill of Materials)`{.interpreted-text role="abbr"},
a new [Assembly]{.title-ref} `Operation`{.interpreted-text
role="guilabel"} at the `Work Center`{.interpreted-text role="guilabel"}
[Assembly Line 1]{.title-ref} is added. In addition, the expected
duration of the operation is [20.00]{.title-ref} minutes, as specified
by the `Manual Duration Change`{.interpreted-text role="guilabel"}.

To supplement the [Assembly]{.title-ref} operation, two quality control
point instructions are added:

1.  The first is the `Step`{.interpreted-text role="guilabel"}
    [QCP00039]{.title-ref}, a `Step Type`{.interpreted-text
    role="guilabel"} to `Register
    Production`{.interpreted-text role="guilabel"} of components.
2.  The second `Step`{.interpreted-text role="guilabel"} is
    [QCP00034]{.title-ref}, an [Instructions]{.title-ref}
    `Step Type`{.interpreted-text role="guilabel"} that provides
    additional assembly details.

{.align-center}
:::

Apply changes {#plm/eco/apply-changes}
-------------

After verifying the changes, move the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} to a
`verification stage <plm/eco/stage-config>`{.interpreted-text
role="ref"}, which are stages that require approval before the revised
changes can be applied to the production
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

Once the approvers accept the changes, the
`Apply Changes`{.interpreted-text role="guilabel"} button becomes
available. Click this button, and the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} is
automatically moved to a closing stage. The changes are applied, which
archives the original production
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, and the
revised `BoM (Bill of Materials)`{.interpreted-text role="abbr"} becomes
the new production `BoM (Bill of Materials)`{.interpreted-text
role="abbr"}.

### Verify changes

To ensure the changes are live, from the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} where
the `Apply Changes`{.interpreted-text role="guilabel"} button was just
pressed, return to the revised
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} by clicking the
`Revision`{.interpreted-text role="guilabel"} smart button.

On the revised `BoM (Bill of Materials)`{.interpreted-text role="abbr"},
the large red `Archived`{.interpreted-text role="guilabel"} flag is
removed.

To further verify the changes, check the production
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} by going to
`Manufacturing
app --> Products --> Products`{.interpreted-text role="menuselection"}
and select the product.

Then, on the product form, click the
`Bill of Materials`{.interpreted-text role="guilabel"} smart button, and
select the `BoM (Bill of Materials)`{.interpreted-text role="abbr"} from
the list. In the `Miscellaneous`{.interpreted-text role="guilabel"} tab
of the `BoM (Bill of Materials)`{.interpreted-text role="abbr"}, the
`Version`{.interpreted-text role="guilabel"} field is updated to match
the version number shown on the `Revision`{.interpreted-text
role="guilabel"} smart button of the latest
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}.

::: {.example}
After applying the changes of the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} for the
`keyboard <plm/eco/example-keyboard>`{.interpreted-text role="ref"},
view the version of the current keyboard
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} in the
`Miscellaneous`{.interpreted-text role="guilabel"} tab. Here, the
`Version`{.interpreted-text role="guilabel"} number has been updated to
[2]{.title-ref}, matching the [V2]{.title-ref} that appears in the
`Revision`{.interpreted-text role="guilabel"} smart button of the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}.

{.align-center}
:::

Create ECO from tablet view {#plm/eco/tablet-view}
---------------------------

Operators can directly suggest clearer operation instructions, while
performing manufacturing orders (MOs) in the *Manufacturing* app.

To create `ECOs (Engineering Change Orders)`{.interpreted-text
role="abbr"} in this manner, begin by navigating to
`Manufacturing app -->
Operations --> Manufacturing Orders`{.interpreted-text
role="menuselection"}. Then, select the desired
`MO (Manufacturing Order)`{.interpreted-text role="abbr"} and switch to
the `Work Orders`{.interpreted-text role="guilabel"} tab. Then, click
the `📱 (mobile phone)`{.interpreted-text role="guilabel"} icon for the
desired work order to open the *tablet view* of the operation.

::: {.important}
::: {.title}
Important
:::

The `📱 (mobile phone)`{.interpreted-text role="guilabel"} icon is
**only** available for `MOs (Manufacturing
Orders)`{.interpreted-text role="abbr"} with a
`Confirmed`{.interpreted-text role="guilabel"} or
`In Progress`{.interpreted-text role="guilabel"} status.
:::

{.align-center}

Next, add an instructional step, by clicking the
`☰ (three horizontal lines)`{.interpreted-text role="guilabel"} icon in
the tablet view of an operation. Doing so opens the
`Menu`{.interpreted-text role="guilabel"} of action items for a `MO
(Manufacturing Order)`{.interpreted-text role="abbr"}. Then, click the
`Add a step`{.interpreted-text role="guilabel"} button.

{.align-center}

Clicking the button reveals an `Add a step`{.interpreted-text
role="guilabel"} pop-up window, where the proposed changes are
submitted.

In the `Title`{.interpreted-text role="guilabel"} field, enter a short
step description. Next, in the `Instruction`{.interpreted-text
role="guilabel"} text field, type the instructions of the step in
greater detail. Optionally, add an image to the
`Document`{.interpreted-text role="guilabel"} field. Once completed,
finish by clicking the `Propose Change`{.interpreted-text
role="guilabel"} button.

::: {.example}
To propose an additional check for broken components, enter the details
in the `Add a
Step`{.interpreted-text role="guilabel"} pop-up window. Doing so creates
an instructional quality control point that will be reviewed in the
following section.

{.align-center}
:::

Based on the inputs from the `Add a Step`{.interpreted-text
role="guilabel"} pop-up window, an
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} is
created with the following information:

1.  `Description`{.interpreted-text role="guilabel"} is the name of the
    operation, followed by the `MO (Manufacturing
    Order)`{.interpreted-text role="abbr"} number for reference.
2.  The `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}
    `Type`{.interpreted-text role="guilabel"} is automatically assigned
    to [BOM Changes]{.title-ref}.
3.  `Product`{.interpreted-text role="guilabel"} and
    `Bill of Materials`{.interpreted-text role="guilabel"} fields are
    automatically populated, based on the
    `BoM (Bill of Materials)`{.interpreted-text role="abbr"} used in the
    `MO (Manufacturing Order)`{.interpreted-text role="abbr"}.
4.  `Responsible`{.interpreted-text role="guilabel"} is the operator who
    submitted the feedback.

### View ECO

To review the proposed changes, navigate to the
`PLM app --> Overview`{.interpreted-text role="menuselection"}. In the
[BOM Updates]{.title-ref}
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} type
card, the `X Engineering Changes`{.interpreted-text role="guilabel"}
button represents the amount of operational changes created from the
tablet view.

Click on the `X Engineering Changes`{.interpreted-text role="guilabel"}
button to open the kanban view of the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} type. To
view the suggestion, select an
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} in the
[New]{.title-ref} stage.

On the `ECO (Engineering Change Order)`{.interpreted-text role="abbr"},
view a summary of the proposed changes in the
`Operation Changes`{.interpreted-text role="guilabel"} tab. Click the
`Revision`{.interpreted-text role="guilabel"} smart button to navigate
to the revised `BoM (Bill of Materials)`{.interpreted-text role="abbr"}
and look into the proposed changes in greater detail.

::: {.example}
An operator suggested another check for broken components by adding a
step from the tablet view, while performing the [Assemble
switches]{.title-ref} operation for the
`MO (Manufacturing Order)`{.interpreted-text role="abbr"}
[WH/MO/00010]{.title-ref} for the product, [Keyboard]{.title-ref}.

Then, this created `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"} can be viewed by navigating to the [BOM
Changes]{.title-ref} ECO type found in
`PLM app --> Overview`{.interpreted-text role="menuselection"}. By
default, `ECOs (Engineering Change Orders)`{.interpreted-text
role="abbr"} created from tablet view are set to spawn in the
[New]{.title-ref} stage.

The `Responsible`{.interpreted-text role="guilabel"} field is assigned
to the operator who made the suggestion, allowing the employee revising
the `BoM (Bill of Materials)`{.interpreted-text role="abbr"} to seek
further clarification from the person who proposed the changes.

{.align-center}
:::

On the revised `BoM (Bill of Materials)`{.interpreted-text role="abbr"},
switch to the `Operations`{.interpreted-text role="guilabel"} tab, and
select the `☰ (three
horizontal lines)`{.interpreted-text role="guilabel"} icon. Doing so
opens a list of `Steps`{.interpreted-text role="guilabel"} to perform
the operation, with the newest instruction titled [New Step
Suggestion:]{.title-ref}, followed by the user-entered title. Click the
line item to view the suggested changes.

{.align-center}

On the
`quality control point <quality/quality_management/quality-control-points>`{.interpreted-text
role="ref"} form, ensure the following form fields are accurately filled
out to give detailed instructions for operators:

-   `Title`{.interpreted-text role="guilabel"}: rename to give a concise
    description of the new instruction.
-   `Control per`{.interpreted-text role="guilabel"}: using the
    drop-down menu, determine whether this instruction applies broadly
    for the `Product`{.interpreted-text role="guilabel"}, specifically
    for this `Operation`{.interpreted-text role="guilabel"} *only*, or a
    particular `Quantity`{.interpreted-text role="guilabel"} of the
    product.
-   `Type`{.interpreted-text role="guilabel"}: categorizes the control
    point type. From the drop-down menu, select
    `Instructions`{.interpreted-text role="guilabel"} to detail an
    instruction for the worker. To receive input from the workers,
    select the `Take a Picture`{.interpreted-text role="guilabel"},
    `Register Consumed Materials`{.interpreted-text role="guilabel"},
    `Print Label`{.interpreted-text role="guilabel"}, or other
    `quality check options
    <quality/quality_management/quality-control-points>`{.interpreted-text
    role="ref"}.

::: {.seealso}
`Configure quality control points <quality/quality_management/quality-control-points>`{.interpreted-text
role="ref"}
:::

Once the quality control point is configured, return to the
`Steps`{.interpreted-text role="guilabel"} list using the breadcrumbs.
Finally, drag the last quality control line item to its intended order
of instructions.

::: {.example}
Drag and reorder the [Check for broken switches]{.title-ref}
instruction, by clicking and dragging its \"6 dots\" icon to move it
from the bottom to the second position.

{.align-center}
:::
