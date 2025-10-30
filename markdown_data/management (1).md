# File: /content/odoo_doc17.0/fr/content/applications/hr/time_off/management.md

Management
==========

::: {#time_off/approvals}
Time off and allocation requests undergo an approval process before
being granted. Requests either need one or two approvals, if any,
depending on how the specific type of time off is configured. All these
configurations can be found under the *Management* section of the *Time
Off* application.
:::

Only people who can approve allocation and time off requests have the
`Management`{.interpreted-text role="guilabel"} section visible in the
*Time Off* application.

Manage time off {#time_off/manage-time-off}
---------------

To view time off requests that need approval, navigate to
`Time Off app -->
Management --> Time Off`{.interpreted-text role="menuselection"}. Doing
so reveals the `All Time Off`{.interpreted-text role="guilabel"} page.

The only time off requests that are visible on this page belong to
employees the user either has `Time Off Officer`{.interpreted-text
role="guilabel"} or `Administrator`{.interpreted-text role="guilabel"}
access rights for in the *Time Off* application.

The default filter on the `All Time Off`{.interpreted-text
role="guilabel"} page is [Waiting For Me]{.title-ref}.

This filter only presents time off requests that need to be approved for
current employees on the user\'s team, with a status of either
`To Approve`{.interpreted-text role="guilabel"} or
`Second Approval`{.interpreted-text role="guilabel"}.

On the left side of the `All Time Off`{.interpreted-text
role="guilabel"} page, there are various grouping options that can be
used to narrow down the presented time off requests, located beneath the
`Status`{.interpreted-text role="guilabel"} and
`Department`{.interpreted-text role="guilabel"} headings.

Since only time off requests that need to be approved are shown, the
only `Status`{.interpreted-text role="guilabel"} options are
`All`{.interpreted-text role="guilabel"}, `To Approve`{.interpreted-text
role="guilabel"}, and `Second Approval`{.interpreted-text
role="guilabel"}.

The various departments the user is a member of, and manages employees
under, also appear on the left side of the page, under
`Departments`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

If there are no requests that fall under one of the status options or
departments, that status or department is **not** visible on the
left-side menu.
:::

To only display time off requests for specific departments, click on the
`Department`{.interpreted-text role="guilabel"} on the left-hand side of
the page. Only requests within the selected department are then
presented.

The status column displays the status of each request, with the status
highlighted in a specific color.

The `To Approve`{.interpreted-text role="guilabel"} and
`Second Approval`{.interpreted-text role="guilabel"} requests are
highlighted in yellow, and are the only ones that appear in the list by
default.

If the [Waiting For Me]{.title-ref} filter is removed, all statuses
appear.

`Approved`{.interpreted-text role="guilabel"} requests are highlighted
in green, `To Submit`{.interpreted-text role="guilabel"} (drafts)
requests are highlighted in blue, and the `Refused`{.interpreted-text
role="guilabel"} requests are highlighted in gray.

To approve a time off request, click the
`fa-thumbs-up`{.interpreted-text role="icon"}
`Approve`{.interpreted-text role="guilabel"} button at the end of the
line.

To validate a time off request that has already been approved, and is
waiting on a second approval, click the `fa-check`{.interpreted-text
role="icon"} `Validate`{.interpreted-text role="guilabel"} button at the
end of the line.

To refuse a request, click the `fa-times`{.interpreted-text role="icon"}
`Refuse`{.interpreted-text role="guilabel"} button at the far end of the
line.

{.align-center}

For more details, click anywhere on the time off request line (except
for the `fa-thumbs-up`{.interpreted-text role="icon"}
`Approve`{.interpreted-text role="guilabel"},
`fa-check`{.interpreted-text role="icon"} `Validate`{.interpreted-text
role="guilabel"} icon, and `fa-times`{.interpreted-text role="icon"}
`Refuse`{.interpreted-text role="guilabel"} buttons). Doing so loads
that specific time off request form. Depending on the rights of the
user, changes can be made.

To modify the request, make any desired changes to the form. All changes
are automatically saved.

It is also possible to approve, validate, or refuse the request from
this form. Click the `Approve`{.interpreted-text role="guilabel"} button
to approve, the `Validate`{.interpreted-text role="guilabel"} button to
validate, or the `Refuse`{.interpreted-text role="guilabel"} button to
refuse the request.

Manage allocations {#time_off/manage-allocations}
------------------

To view allocations that need approval, navigate to
`Time Off app --> Management -->
Allocations`{.interpreted-text role="menuselection"}. Doing so reveals
the `Allocations`{.interpreted-text role="guilabel"} page.

The user is only presented with allocations for employees they have
either `Time Off
Officer`{.interpreted-text role="guilabel"} or
`Administrator`{.interpreted-text role="guilabel"} access rights for in
the *Time Off* application.

The default filters configured on the `Allocations`{.interpreted-text
role="guilabel"} page are `My Team`{.interpreted-text role="guilabel"}
and `Active Employee`{.interpreted-text role="guilabel"}. These default
filters *only* present employees on the user\'s team (who they manage)
and active employees. Inactive records are not shown.

The left side of the `Allocations`{.interpreted-text role="guilabel"}
page has various grouping options to narrow down the presented
allocation requests.

The `Status`{.interpreted-text role="guilabel"} options are:
`All`{.interpreted-text role="guilabel"}, `To Approve`{.interpreted-text
role="guilabel"}, `Refused`{.interpreted-text role="guilabel"}, and
`Approved`{.interpreted-text role="guilabel"}. Click on a specific
`Status`{.interpreted-text role="guilabel"} to view only requests with
that specific status.

To view all allocation requests, regardless of status, click
`All`{.interpreted-text role="guilabel"} under the
`Status`{.interpreted-text role="guilabel"} heading.

It is also possible to display allocation requests by department. Click
on the desired `Department`{.interpreted-text role="guilabel"} on the
left side of the `Allocations`{.interpreted-text role="guilabel"} page,
to only present allocations for that specific department.

::: {.note}
::: {.title}
Note
:::

The groupings on the left side **only** present allocation requests that
fall under the default filters of `My Team`{.interpreted-text
role="guilabel"} and `Active Employee`{.interpreted-text
role="guilabel"}, if those default filters are not removed from the
`Search...`{.interpreted-text role="guilabel"} bar. Only the statuses
for allocation requests that fall under those filters are presented on
the left side.

For example, if there are no requests with a status of
`To Submit`{.interpreted-text role="guilabel"}, that status option does
not appear in the left-hand side of the `Allocations`{.interpreted-text
role="guilabel"} page.

All departments for the user\'s employees appear in the list. If there
are no allocation requests that fall under that department matching the
preconfigured filters, the list is blank.

It is always possible to remove any of the preconfigured filters, by
clicking the `fa-times`{.interpreted-text role="icon"}
`(remove)`{.interpreted-text role="guilabel"} icon on the specific
filter to remove it.
:::

The status column displays the status of each request, with the status
highlighted in a specific color.

The `To Approve`{.interpreted-text role="guilabel"} requests are
highlighted in yellow, `Approved`{.interpreted-text role="guilabel"}
requests are highlighted in green, and the `Refused`{.interpreted-text
role="guilabel"} requests are highlighted in gray.

To approve an allocation request, click the `fa-check`{.interpreted-text
role="icon"} `Validate`{.interpreted-text role="guilabel"} button at the
end of the line. To refuse a request, click the
`fa-times`{.interpreted-text role="icon"} `Refuse`{.interpreted-text
role="guilabel"} button.

{.align-center}

If more details are needed, click anywhere on the allocation request
line (except for the `fa-check`{.interpreted-text role="icon"}
`Validate`{.interpreted-text role="guilabel"} or
`fa-times`{.interpreted-text role="icon"} `Refuse`{.interpreted-text
role="guilabel"} buttons) to view the specific request in detail, via
the allocation request form.

Depending on the rights of the user, changes can be made to the
allocation request form that appears. To modify the request, make any
desired changes to the form. All changes are automatically saved.

It is also possible to approve or refuse the request from this form.
Click the `Validate`{.interpreted-text role="guilabel"} button to
approve, or the `Refuse`{.interpreted-text role="guilabel"} button to
refuse the request.
