# File: /content/odoo_doc17.0/fr/content/applications/hr/time_off/allocations.md

Allocations
===========

Once `time off types <time_off/time-off-types>`{.interpreted-text
role="ref"} and `accrual plans
<time_off/accrual-plans>`{.interpreted-text role="ref"} have been
configured, the next step is to *allocate*, or give, time off to
employees.

The *Allocations* page of the **Time Off** app is **only** visible to
users who have either *Time Off Officer* or *Administrator* access
rights for the **Time Off** application. For more information on access
rights, refer to the
`access rights <../../general/users/access_rights/>`{.interpreted-text
role="doc"} documentation.

Allocate time off
-----------------

To create a new allocation, navigate to `Time Off app --> Management -->
Allocations`{.interpreted-text role="menuselection"}.

This presents a list of all current allocations, including their
respective statuses.

Click `New`{.interpreted-text role="guilabel"} to allocate time off, and
a blank allocation form appears.

After entering a name for the allocation on the first blank field of the
form, enter the following information:

-   `Time Off Type`{.interpreted-text role="guilabel"}: Using the
    drop-down menu, select the type of time off that is being allocated
    to the employees.

-   `Allocation Type`{.interpreted-text role="guilabel"}: Select either
    `Regular Allocation`{.interpreted-text role="guilabel"} or `Accrual
    Allocation`{.interpreted-text role="guilabel"}. If the allocation is
    **not** based on an `accrual plan
    <time_off/accrual-plans>`{.interpreted-text role="ref"}, select
    `Regular Allocation`{.interpreted-text role="guilabel"}.

-   `Accrual Plan`{.interpreted-text role="guilabel"}: If
    `Accrual Allocation`{.interpreted-text role="guilabel"} is selected
    for the `Allocation Type`{.interpreted-text role="guilabel"}, the
    `Accrual Plan`{.interpreted-text role="guilabel"} field appears.
    Using the drop-down menu, select the accrual plan with which the
    allocation is associated. An accrual plan **must** be selected for
    an `Accrual Allocation`{.interpreted-text role="guilabel"}.

-   `Validity Period/Start Date`{.interpreted-text role="guilabel"}: If
    `Regular Allocation`{.interpreted-text role="guilabel"} is selected
    for the `Allocation Type`{.interpreted-text role="guilabel"}, this
    field is labeled `Validity Period`{.interpreted-text
    role="guilabel"}. If `Accrual Allocation`{.interpreted-text
    role="guilabel"} is selected for the
    `Allocation Type`{.interpreted-text role="guilabel"}, this field is
    labeled `Start Date`{.interpreted-text role="guilabel"}.

    The current date populates the first date field, by default. To
    select another date, click on the pre-populated date to reveal a
    popover calendar window. Navigate to the desired start date for the
    allocation, and click on the date to select it.

    If the allocation expires, select the expiration date in the next
    date field. If the time off does *not* expire, leave the second date
    field blank. `No Limit`{.interpreted-text role="guilabel"} appears
    in the field if no date is selected.

    If `Accrual Allocation`{.interpreted-text role="guilabel"} is
    selected for the `Allocation Type`{.interpreted-text
    role="guilabel"}, this second field is labeled
    `Run until`{.interpreted-text role="guilabel"}.

    ::: {.important}
    ::: {.title}
    Important
    :::

    If the `Start Date`{.interpreted-text role="guilabel"} entered is in
    the middle of a period of time, such as the middle of the month,
    Odoo applies the allocation to the beginning or end of the period,
    depending on the *Accrued Gain Time* entered on the
    `accrual plan <time_off/accrual-plans>`{.interpreted-text
    role="ref"} (either *At the start of the accrual period*, or *At the
    end of the accrual period*) instead of the specific date entered.

    For example, an allocation is created, and references an accrual
    plan that grants time *At the start of the accrual period*, monthly,
    on the first of the month.

    On the allocation form, the `Allocation Type`{.interpreted-text
    role="guilabel"} is set to `Accrual
    Allocation`{.interpreted-text role="guilabel"}, and the
    `Start Date`{.interpreted-text role="guilabel"} entered is
    [06/16/24]{.title-ref}.

    Odoo\'s **Time Off** app retroactively applies the allocation to the
    beginning of the time period entered in the
    `Start Date`{.interpreted-text role="guilabel"}.

    Therefore, this allocation accrues time from [06/01/24]{.title-ref},
    rather than [06/16/24]{.title-ref}.

    Additionally, if on the accrual form, the allocation references an
    accrual plan that grants time *\`At the end of the accrual period*,
    the allocation accrues time from [7/01/24]{.title-ref} rather than
    [6/18/24]{.title-ref}.
    :::

-   `Allocation`{.interpreted-text role="guilabel"}: Enter the amount of
    time that is being allocated to the employees. This field displays
    the time in either `Hours`{.interpreted-text role="guilabel"} or
    `Days`{.interpreted-text role="guilabel"}, depending on how the
    selected `Time Off Type <time_off/time-off-types>`{.interpreted-text
    role="ref"} is configured.

-   `Mode`{.interpreted-text role="guilabel"}: Using the drop-down menu,
    select how the allocation is assigned. This selection determines who
    receives the time off allocation. The options are
    `By Employee`{.interpreted-text role="guilabel"},
    `By Company`{.interpreted-text role="guilabel"},
    `By Department`{.interpreted-text role="guilabel"}, or
    `By Employee Tag`{.interpreted-text role="guilabel"}.

    Depending on what is selected for the `Mode`{.interpreted-text
    role="guilabel"}, the field beneath `Mode`{.interpreted-text
    role="guilabel"} is labeled either: `Employees`{.interpreted-text
    role="guilabel"}, `Company`{.interpreted-text role="guilabel"},
    `Department`{.interpreted-text role="guilabel"}, or
    `Employee Tag`{.interpreted-text role="guilabel"}.

    Using the drop-down menu, indicate the specific employees, company,
    department, or employee tags receiving this time off.

    Multiple selections can be made for either
    `Employees`{.interpreted-text role="guilabel"} or
    `Employee Tag`{.interpreted-text role="guilabel"}.

    Only one selection can be made for the `Company`{.interpreted-text
    role="guilabel"} or `Department`{.interpreted-text role="guilabel"}.

-   `Add a reason...`{.interpreted-text role="guilabel"}: If any
    description or note is necessary to explain the time off allocation,
    enter it in this field at the bottom of the form.

![A new allocation form with all the fields filled out for the annual two week vacation
granted to all employees.](allocations/new-allocation.png){.align-center}

Request allocation {#time_off/request-allocation}
------------------

If an employee has used all their time off, or will run out of time off,
they can request an allocation for additional time. Allocations can be
requested in one of two ways, either from the
`Dashboard <time_off/dashboard>`{.interpreted-text role="ref"} or the
`My Allocations <time_off/my-allocations>`{.interpreted-text role="ref"}
view.

To create a new allocation request, click either the
`New Allocation Request`{.interpreted-text role="guilabel"} button on
the main **Time Off** dashboard, or the `New`{.interpreted-text
role="guilabel"} button in the `My Allocations`{.interpreted-text
role="guilabel"} list view. Both buttons open a new allocation request
form.

::: {.note}
::: {.title}
Note
:::

Both options open a new allocation request form, but when requested from
the `Dashboard`{.interpreted-text role="guilabel"}, the form appears in
a pop-up window, and the *Validity Period* field does **not** appear.
When requested from the `My Allocations`{.interpreted-text
role="guilabel"} list view, the screen navigates to a new allocation
request page, instead of presenting a pop-up window.
:::

Enter the following information on the new allocation request form:

-   `Time Off Type`{.interpreted-text role="guilabel"}: Select the type
    of time off being requested for the allocation from the drop-down
    menu. After a selection is made, the title updates with the time off
    type.
-   `Validity Period`{.interpreted-text role="guilabel"}: By default,
    the current date populates this field, and it is **not** able to be
    modified. This field **only** appears when requesting an allocatoin
    from the `My Allocations`{.interpreted-text role="guilabel"} view
    (`Time Off --> My Time --> My Allocations`{.interpreted-text
    role="menuselection"}).
-   `Allocation`{.interpreted-text role="guilabel"}: Enter the amount of
    time being requested in this field. The format is presented in
    either `Days`{.interpreted-text role="guilabel"} or
    `Hours`{.interpreted-text role="guilabel"}, depending on how the
    `Time
    Off Type`{.interpreted-text role="guilabel"} is configured. Once
    this field is populated, the name of the allocation request is
    updated to include the amount of time being requested.
-   `Add a reason...`{.interpreted-text role="guilabel"}: Enter a
    description for the allocation request in this field. This should
    include any details that approvers may need to approve the request.

If the request was created from the `Dashboard`{.interpreted-text
role="guilabel"}, click the `Save & Close`{.interpreted-text
role="guilabel"} button on the `New Allocation`{.interpreted-text
role="guilabel"} pop-up window to save the information and submit the
request.

If the form was completed from the `My Allocations`{.interpreted-text
role="guilabel"} list view, the information is automatically saved as it
is entered. However, the form can be saved manually at any time by
clicking the `fa-cloud-upload`{.interpreted-text role="icon"}
`(cloud upload)`{.interpreted-text role="guilabel"} icon.

![An allocation request form filled out for an employee requesting an additional week of
sick time.](allocations/allocation-request.png){.align-center}
