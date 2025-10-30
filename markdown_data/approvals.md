# File: /content/odoo_doc17.0/fr/content/applications/inventory_and_mrp/plm/management/approvals.md

Approvals
=========

::: {#plm/approvals}
Notify stakeholders and managers automatically by assigning approvers to
stages of `engineering
change orders <plm/eco>`{.interpreted-text role="ref"} (ECOs) under
review. Changes can only be applied after the assigned approver accepts
them. Approvals ensure reviews by team members, which prevents mistakes
and premature actions.
:::

::: {.seealso}
`Stage configuration <plm/eco/stage-config>`{.interpreted-text
role="ref"}
:::

Add approver
------------

To add an approver, first go to the `PLM app`{.interpreted-text
role="menuselection"}, and click on the project card of an ECO type to
open the Gantt view of the
`ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"}.

On the `Engineering Change Orders`{.interpreted-text role="guilabel"}
page, hover over the intended stage, and select the
`⚙️ (gear)`{.interpreted-text role="guilabel"} icon. Then, click
`Edit`{.interpreted-text role="guilabel"} to open a pop-up window.

::: {.note}
::: {.title}
Note
:::

Approvers can be added to any stage, but it\'s strongly recommended to
assign them to the *verification* stage, which comes before the
*closing* stage, where
`ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} are
applied, and the `BoM (Bill of Materials)`{.interpreted-text
role="abbr"} version is updated.

See the documentation about
`stage types <plm/eco/stage-config>`{.interpreted-text role="ref"} for
more information.
:::

::: {#plm/approvals/approval-type}
In the `Edit`{.interpreted-text role="guilabel"} stage pop-up window,
click the `Add a line`{.interpreted-text role="guilabel"} button,
located under `Approvals`{.interpreted-text role="guilabel"}. Then, type
in the approver\'s position (or title) under `Role`{.interpreted-text
role="guilabel"} (e.g. [Engineering Manager]{.title-ref}, [Quality
Team]{.title-ref}, etc.), and select the relevant
`User`{.interpreted-text role="guilabel"} from the drop-down menu.
:::

Next, set the `Approval Type`{.interpreted-text role="guilabel"} to
`Is required to approve`{.interpreted-text role="guilabel"}, `Approves,
but the approval is optional`{.interpreted-text role="guilabel"}, or
`Comments only`{.interpreted-text role="guilabel"}.

::: {.example}
Assign the [CTO]{.title-ref}, \"Mitchell Admin,\" as a required approver
for `ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} in
the [Validated]{.title-ref} stage in the [New Product
Introduction]{.title-ref} ECO type.

Approvals from the quality and marketing teams are **not** required to
apply changes to the `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"} because their `Approval Type`{.interpreted-text
role="guilabel"} is set to `Approves, but the approval is
optional`{.interpreted-text role="guilabel"} and
`Comments only`{.interpreted-text role="guilabel"}, respectively.

{.align-center}
:::

Manage approvals
----------------

Approvers can easily track their to-do approvals by navigating to the
`PLM app`{.interpreted-text role="menuselection"}, and looking at the
card for an ECO type, which shows the count of open tasks assigned to
them.

Here\'s what each button on an ECO project card does:

1.  The `# Engineering Changes`{.interpreted-text role="guilabel"}
    button displays a count of in-progress
    `ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} of
    this ECO type. Clicking the button opens the Gantt view of the
    `Engineering Change Orders`{.interpreted-text role="guilabel"} page.

2.  `My Validations`{.interpreted-text role="guilabel"} displays a count
    of `ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"}
    the approver must accept or reject. Clicking on this button displays
    `ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"}
    pending approval or rejected (marked with the red
    `Blocked`{.interpreted-text role="guilabel"} state).

3.  The `All Validations`{.interpreted-text role="guilabel"} button
    shows the count of
    `ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"}
    awaiting approval or rejected by any approver. Clicking it reveals
    these pending `ECOs (Engineering Change Orders)`{.interpreted-text
    role="abbr"}.

4.  `To Apply`{.interpreted-text role="guilabel"} displays a count of
    `ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} to
    which the user needs to apply changes. Clicking on the button
    displays all the
    `ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"} to
    approve, and apply changes to, in the verification stage.

    `ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"}
    marked with the green `Done`{.interpreted-text role="guilabel"}
    stage have already been approved, and the user just needs to click
    on the `ECO (Engineering Change Order)`{.interpreted-text
    role="abbr"} to enter the form view, and click the
    `Apply Changes`{.interpreted-text role="guilabel"} button.

{.align-center}

### Approve ECOs

Navigate to an `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"} in a verification stage, while logged in as the assigned
approver, to see the `Approve`{.interpreted-text role="guilabel"},
`Reject`{.interpreted-text role="guilabel"}, and
`Apply Changes`{.interpreted-text role="guilabel"} buttons.

To approve the `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"}, and apply the changes onto the production
`BoM (Bill of Materials)`{.interpreted-text role="abbr"}, click
`Approve`{.interpreted-text role="guilabel"}, and then
`Apply Changes`{.interpreted-text role="guilabel"}.

Note that the `Apply Changes`{.interpreted-text role="guilabel"} button
will **not** work unless the `Approve`{.interpreted-text
role="guilabel"} button was clicked first. Additionally, the chatter
logs the history of the clicked buttons.

::: {.warning}
::: {.title}
Warning
:::

When the `Approval Type`{.interpreted-text role="guilabel"} is **not**
set to `Is required to approve`{.interpreted-text role="guilabel"},
approval from the associated user is not needed before applying changes
with the `Apply Changes`{.interpreted-text role="guilabel"} button.
Thus, the `Apply Changes`{.interpreted-text role="guilabel"} button
**will work** without requiring the `Approve`{.interpreted-text
role="guilabel"} button to be clicked first.
:::

### Automated activities

When an `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}
is moved to a verification stage, a planned activity is automatically
created for assigned approvers to review the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}.
Approvers receive a notification in their activities inbox, accessible
through the `🕘 (clock)`{.interpreted-text role="guilabel"} icon at the
top of the page.

In the to-do task list, the
`Engineering Change Order (ECO)`{.interpreted-text role="guilabel"}
notification displays the number of activities marked
`Late`{.interpreted-text role="guilabel"}, `Today`{.interpreted-text
role="guilabel"}, and `Future`{.interpreted-text role="guilabel"}.
Clicking on each of these buttons shows a filtered Gantt view of the
respective `ECOs (Engineering Change Orders)`{.interpreted-text
role="abbr"}.

::: {.example}
Scheduled activities are shown as a number on the
`🕘 (clock)`{.interpreted-text role="guilabel"} icon, with
[5]{.title-ref} `ECOs (Engineering Change Orders)`{.interpreted-text
role="abbr"} pending approval `Today`{.interpreted-text
role="guilabel"}. Currently, there are [0]{.title-ref}
`Late`{.interpreted-text role="guilabel"} or `Future`{.interpreted-text
role="guilabel"} `ECOs (Engineering Change Orders)`{.interpreted-text
role="abbr"}.

{.align-center}
:::

By clicking a pending `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"}, a *planned activity* for `ECO Approval`{.interpreted-text
role="guilabel"} is recorded in the chatter. Click on the
`i (Info)`{.interpreted-text role="guilabel"} icon to view additional
information, including the approval\'s `Created`{.interpreted-text
role="guilabel"} date, the approver `Assigned to`{.interpreted-text
role="guilabel"} it, and the due date.

{.align-center}

#### Follow-up activities

When `ECOs (Engineering Change Orders)`{.interpreted-text role="abbr"}
are rejected, tasks need to be assigned to project members for required
modifications before `ECO (Engineering Change Order)`{.interpreted-text
role="abbr"} approval. To create tasks with deadlines, navigate to the
rejected `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}
form, and go to the chatter.

Select the `Mark Done`{.interpreted-text role="guilabel"} button in the
`Planned Activities`{.interpreted-text role="guilabel"} section of the
chatter to close the activity, and open a pop-up window for creating
tasks.

![Show \*Mark Done\* window to show \*Done & Schedule Next\*, \*Done\*, and \*Discard\* buttons to
close the planned activity.](approvals/mark-as-done.png){.align-center}

In the `Mark Done`{.interpreted-text role="guilabel"} window, click
`Done & Schedule Next`{.interpreted-text role="guilabel"} to open a new
`Schedule an Activity`{.interpreted-text role="guilabel"} window. Next,
set the `Assigned to`{.interpreted-text role="guilabel"} team member and
the `Due Date`{.interpreted-text role="guilabel"} for completing the
changes. Provide task details in the `Summary`{.interpreted-text
role="guilabel"} field and the text box. Click the
`Schedule`{.interpreted-text role="guilabel"} button to close the
window.

After closing the window, on the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} form,
move the `ECO (Engineering Change Order)`{.interpreted-text role="abbr"}
back one stage. Doing so ensures that when the team member completes the
changes, and returns the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"} to the
verification stage, a new `ECO Approval`{.interpreted-text
role="guilabel"} task is created for the approver.

::: {.example}
The approver creates an activity for the `Responsible`{.interpreted-text
role="guilabel"} of the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}, [Laurie
Poiret]{.title-ref}, that details the changes required for the approver
to `Accept`{.interpreted-text role="guilabel"} the
`ECO (Engineering Change Order)`{.interpreted-text role="abbr"}.
Clicking the `Schedule`{.interpreted-text role="guilabel"} button
creates a planned activity for Laurie due on [08/15/2023]{.title-ref}.

{.align-center}
:::
