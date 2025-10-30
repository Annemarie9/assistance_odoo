# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/plm/manage_changes/version_control.md

Version control
===============

Use Odoo\'s *Product Lifecycle Management (PLM)* to manage previous
versions of bills of materials (BoMs). Store former assembly
instructions, component details, and past product design files while
keeping the past details out of the production
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

Easily revert to previous `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} versions, when needed. Additionally, use *PLM* to trace
which `BoM (Bill of Materials)`{.interpreted-text role="abbr"} version
was active on specific dates for recalls or customer complaints.

Every `BoM (Bill of Materials)`{.interpreted-text role="abbr"} version
is stored in an *engineering change order* (ECO) for organized testing
and improvements without disrupting normal manufacturing operations.

::: {.seealso}
`Engineering change order <plm/eco>`{.interpreted-text role="ref"}
:::

Current BoM version
-------------------

To see the current version of the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} used in
production, go to `PLM app --> Master
Data --> Bill of Materials`{.interpreted-text role="menuselection"}, and
select the desired `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} from the list. Then, switch to the
`Miscellaneous`{.interpreted-text role="guilabel"} tab, where the
currently live `Version`{.interpreted-text role="guilabel"} of the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} is displayed.

::: {.note}
::: {.title}
Note
:::

`BoMs (Bills of Materials)`{.interpreted-text role="abbr"} can also be
accessed from `Manufacturing app --> Products --> Bill of
Materials`{.interpreted-text role="menuselection"}.
:::

{.align-center}

Version history
---------------

To manage all former, current, and future versions of a
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, begin by
navigating to
`Manufacturing app --> Products --> Bills of Materials`{.interpreted-text
role="menuselection"} and click the desired
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

From the `BoM (Bill of Materials)`{.interpreted-text role="abbr"} page,
click the `ECO`{.interpreted-text role="guilabel"} smart button, and
switch to list view by selecting the
`≣ (four horizontal lines)`{.interpreted-text role="guilabel"} icon on
the top right corner.

::: {.note}
::: {.title}
Note
:::

The `ECO`{.interpreted-text role="guilabel"} smart button is visible on
the `BoM (Bill of Materials)`{.interpreted-text role="abbr"} **only** if
the *PLM* app is installed.
:::

{.align-center}

In the list of `ECOs (Engineering Change Orders)`{.interpreted-text
role="abbr"} for the product, navigate to the search bar at the top, and
click the `▼ (down arrow)`{.interpreted-text role="guilabel"} icon on
the right to access a drop-down menu of `Filters`{.interpreted-text
role="guilabel"}.

Next, filter by `Done`{.interpreted-text role="guilabel"}
`ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} to
view: the revision history of the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, the
`Responsible`{.interpreted-text role="guilabel"} user who applied the
change, and the `Effective Date`{.interpreted-text role="guilabel"} of
the `BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

Click each `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"} to view the past components, operations, and design files
associated with the `BoM (Bill of Materials)`{.interpreted-text
role="abbr"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If the `Effective Date`{.interpreted-text role="guilabel"} field is
empty, the `Effective`{.interpreted-text role="guilabel"} date of the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} is
automatically set to `As soon as possible`{.interpreted-text
role="guilabel"} and no dates are recorded in the revision history of
the `BoM (Bill of Materials)`{.interpreted-text role="abbr"}.

{.align-center}
:::

::: {.tip}
::: {.title}
Tip
:::

A workaround for checking when the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} went live is by
navigating to the chatter, and hovering over the time the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} was
moved to the `closing stage <plm/eco/stage-config>`{.interpreted-text
role="ref"}.
:::

Design files
------------

Attach computer-aided design (CAD) files, PDFs, images, or other design
material to the `BoM (Bill of Materials)`{.interpreted-text role="abbr"}
itself.

To do so, navigate to
`PLM app --> Master Data --> Bill of Materials`{.interpreted-text
role="menuselection"}, and select the desired
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}. On the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, navigate to
the *chatter*, and click the `📎 (paperclip)`{.interpreted-text
role="guilabel"} icon.

The files associated with the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} are displayed
in the `Files`{.interpreted-text role="guilabel"} section. To add more
design files, select the `Attach files`{.interpreted-text
role="guilabel"} button.

{.align-center}

### Manage design files in an ECO

Add, modify, and remove files in an
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}. Once
the `ECO (Engineering Change Order)`{.interpreted-text role="abbr"} is
approved and applied, the new files are automatically linked to the
production `BoM (Bill of Materials)`{.interpreted-text role="abbr"}.
Archived files are removed from the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, but are still
accessible in the `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"}.

To manage the design files in the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}, begin
by navigating to `PLM app --> Changes`{.interpreted-text
role="menuselection"} and choose the desired
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}. Next,
open the `Attachments`{.interpreted-text role="guilabel"} page by
clicking the `Documents`{.interpreted-text role="guilabel"} smart
button.

Hover over each attachment to reveal the
`︙ (three vertical dots)`{.interpreted-text role="guilabel"} icon. From
there, choose whether to `Edit`{.interpreted-text role="guilabel"},
`Remove`{.interpreted-text role="guilabel"}, or
`Download`{.interpreted-text role="guilabel"} the file. Any changes made
to these files are contained within the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}, and
will only apply to the production
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} once the
`changes are applied <plm/eco/apply-changes>`{.interpreted-text
role="ref"}.

::: {.example}
In the [Create 60% keyboard]{.title-ref}
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}, the
design files are from the original [100% keyboard]{.title-ref}
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}. To replace the
keyboard PDF, begin by selecting the `Documents`{.interpreted-text
role="guilabel"} smart button.

{.align-center}

On the `Attachments`{.interpreted-text role="guilabel"} page, hover over
the [100% keyboard manual.pdf]{.title-ref} design file, and click the
`︙ (three vertical dots)`{.interpreted-text role="guilabel"} icon.
Then, click the `Remove`{.interpreted-text role="guilabel"} option to
archive the file.

Next, on the same `Attachments`{.interpreted-text role="guilabel"} page,
click the `Upload`{.interpreted-text role="guilabel"} button to upload
the new design file, named [60% keyboard manual]{.title-ref}.

![View of \*Attachments\* page from the \*Documents\* smart button. Displays one archived and
one newly added attachment.](version_control/attachments.png){.align-center}
:::

::: {.note}
::: {.title}
Note
:::

Archived files are **not** permanently deleted --- they can still be
accessed in the previous
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}, or as
an archived file in the latest
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}, where
the archival occurred.
:::

Apply rebase
------------

Odoo simplifies merge conflict resolution for concurrent
`ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} on the
same product.

Conflicts can occur when the production
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} is updated
while other `ECOs (Engineering Change Orders)`{.interpreted-text
role="abbr"} are modifying the previous version. Differences between the
new and previous production
`BoMs (Bills of Materials)`{.interpreted-text role="abbr"} are displayed
in the `Previous Eco Bom Changes`{.interpreted-text role="guilabel"}
tab, visible only in this scenario.

To resolve conflicts and retain
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} changes,
click the `Apply Rebase`{.interpreted-text role="guilabel"} button.

::: {.example}
Two `ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"},
[ECO0011]{.title-ref} and [ECO0012]{.title-ref}, are created when the
current `BoM (Bill of Materials)`{.interpreted-text role="abbr"} version
is [5]{.title-ref}. In [ECO0011]{.title-ref}, a new component, [Space
stabilizer]{.title-ref}, is added, and the changes are applied. This
means the current `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} version has become [6]{.title-ref}.

{.align-center}

This means [ECO0012]{.title-ref} is modifying an outdated
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}. As shown in
the `Previous Eco Bom
Changes`{.interpreted-text role="guilabel"} tab, the
`BoM (Bill of Materials)`{.interpreted-text role="abbr"} is missing the
[Space stabilizer]{.title-ref}.

To ensure the changes applied by [ECO0011]{.title-ref} are kept when the
changes occur in [ECO0012]{.title-ref}, click the
`Apply Rebase`{.interpreted-text role="guilabel"} button to apply the
previous `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}
changes, without affecting the changes already made to
[ECO0012]{.title-ref}.

{.align-center}
:::
