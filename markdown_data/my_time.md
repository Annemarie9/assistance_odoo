# File: /content/odoo_doc17.0/fr/content/applications/hr/time_off/my_time.md

My time
=======

The *My Time* menu of the *Time Off* application houses all the various
time off information for the signed-in user.

This includes the main *Time Off* dashboard, which displays an overview
of the various time off balances, as well as time-off requests and
allocations.

Dashboard {#time_off/dashboard}
---------

All users have access to the *Time Off* `Dashboard`{.interpreted-text
role="guilabel"}, which is the first page that appears when the *Time
Off* application is opened. The `Dashboard`{.interpreted-text
role="guilabel"} can also be accessed at any point in the application,
by navigating to
`Time Off app --> My Time --> Dashboard`{.interpreted-text
role="menuselection"}.

The current year is displayed, and the current day is highlighted in a
red circle.

To change the view, click on the `Year`{.interpreted-text
role="guilabel"} button to reveal a drop-down menu. Then, select either
`Day`{.interpreted-text role="guilabel"}, `Week`{.interpreted-text
role="guilabel"}, or `Month`{.interpreted-text role="guilabel"} to
present the calendar in that corresponding view.

::: {.note}
::: {.title}
Note
:::

To change the displayed dates, click the
`fa-arrow-left`{.interpreted-text role="icon"}
`(left arrow)`{.interpreted-text role="guilabel"} or
`fa-arrow-right`{.interpreted-text role="icon"}
`(right arrow)`{.interpreted-text role="guilabel"} icons to the left of
the `Year`{.interpreted-text role="guilabel"} button. The calendar view
adjusts in increments of the selected view.

For example, if `Year`{.interpreted-text role="guilabel"} is selected,
the arrows adjust the view by one year.

To reset the view, so it includes the current date, click the
`Today`{.interpreted-text role="guilabel"} button.
:::

Above the calendar view is a summary of the user\'s time off balances.
Every time off type that has been allocated appears in its own summary
box. Each summary lists the type of time off, the corresponding icon,
the current available balance (in hours or days), and an expiration date
(if applicable).

To view the full details of a time off balance, click the
`fa-question-circle-o`{.interpreted-text role="icon"}
`(question mark)`{.interpreted-text role="guilabel"} icon at the end of
the `(DAYS/HOURS) AVAILABLE`{.interpreted-text role="guilabel"} on the
time off summary. The complete details are presented in a popover
window, including the `Allocated`{.interpreted-text role="guilabel"}
time, `Accrual (Future)`{.interpreted-text role="guilabel"} time,
`Approved`{.interpreted-text role="guilabel"} time off scheduled,
`Planned`{.interpreted-text role="guilabel"} time off, and the currently
`Available`{.interpreted-text role="guilabel"} time off.

{.align-center}

A user can also select a future date to see an estimate of how much time
they should accrue by that point. On the right side of the time off
summary blocks, there is a `Balance at the
(date)`{.interpreted-text role="guilabel"} field. Click on the date, and
a calendar selector popover appears.

::: {.note}
::: {.title}
Note
:::

The `Balance at the (date)`{.interpreted-text role="guilabel"} field
**only** appears if the user is accruing time off through an
`accrual plan <time_off/accrual-plans>`{.interpreted-text role="ref"}.
:::

The current date is the default date selected. Navigate to the desired
date, and Odoo displays the time off balances the user should have on
that date. This takes into account all time off currently planned and
approved. To return to the current date, click the
`Today`{.interpreted-text role="guilabel"} button to the right of the
date field.

On the right side of the calendar, the various time off types are
displayed, each with their own corresponding color. The
`Legend`{.interpreted-text role="guilabel"} explains how the various
statuses for time off requests are presented.

Time off that has been validated appears in a solid color. Time off
requests that still are still in the `To Approve`{.interpreted-text
role="guilabel"} stage, appear with white stripes in the color.
`Refused`{.interpreted-text role="guilabel"} time off requests have a
line through the dates.

The color for each request corresponds to the specified color set with
the various time off types, listed in the section above the
`Legend`{.interpreted-text role="guilabel"}.

New time off requests can be made from the `Dashboard`{.interpreted-text
role="guilabel"}. Click the `New`{.interpreted-text role="guilabel"}
button in the upper-left corner, and a
`New Time Off <request_time_off>`{.interpreted-text role="doc"} pop-up
window appears.

New allocation requests can also be made from the
`Dashboard`{.interpreted-text role="guilabel"}. Click the `New
Allocation Request`{.interpreted-text role="guilabel"} button to request
more time off, and a `New Allocation
<time_off/request-allocation>`{.interpreted-text role="ref"} pop-up
window appears.

{.align-center}

My time off {#time_off/my-time-off}
-----------

To view a list of all the time off requests, navigate to
`Time Off app --> My Time
--> My Time Off`{.interpreted-text role="menuselection"}. Here, all time
off requests, both past and present, appear in a list view.

The list includes the following information for each request: the
`Time Off Type`{.interpreted-text role="guilabel"},
`Description`{.interpreted-text role="guilabel"},
`Start Date`{.interpreted-text role="guilabel"},
`End Date`{.interpreted-text role="guilabel"},
`Duration`{.interpreted-text role="guilabel"}, and
`Status`{.interpreted-text role="guilabel"}.

A new time off request can be made from this view. Click the
`New`{.interpreted-text role="guilabel"} button to
`request_time_off`{.interpreted-text role="doc"}.

My allocations {#time_off/my-allocations}
--------------

To view a list of all allocations, navigate to
`Time Off app --> My Time --> My
Allocations`{.interpreted-text role="menuselection"}. All allocations
and requested allocations appear in a list view.

The information presented on the `My Allocations`{.interpreted-text
role="guilabel"} page includes: `Time Off
Type`{.interpreted-text role="guilabel"},
`Description`{.interpreted-text role="guilabel"},
`Amount`{.interpreted-text role="guilabel"},
`Allocation Type`{.interpreted-text role="guilabel"}, and
`Status`{.interpreted-text role="guilabel"}.

A new allocation request can be made from this view, as well. Click the
`New`{.interpreted-text role="guilabel"} button to
`request an allocation <time_off/request-allocation>`{.interpreted-text
role="ref"}.
