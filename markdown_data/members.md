show-content

:   

Members
=======

The *Members* application is where all operations related to memberships
can be configured and managed. The *Members* app integrates with the
*Sales* and *Accounting* applications to sell and invoice memberships
directly to customers.

Membership products
-------------------

To create a new membership product, navigate to
`Members app --> Configuration -->
Membership Products`{.interpreted-text role="menuselection"}, and click
`New`{.interpreted-text role="guilabel"} to open a blank product record.

Complete the blank form with the necessary information, including the
`Membership
Duration`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Membership products require a start and end date, as they are used to
determine `membership
status <sales/membership-status>`{.interpreted-text role="ref"}.
Membership products can be sold *before* their active start date.
:::

{.align-center}

Membership products can be added to a sales order, and invoiced as
regular products or subscriptions.

Activate a membership
---------------------

To activate a membership from the *Contacts* application, navigate to
`Contacts app`{.interpreted-text role="menuselection"}, and click on a
contact to open that specific contact\'s detail form.

From the resulting contact form, open the `Membership`{.interpreted-text
role="guilabel"} tab, and click `Buy
Membership`{.interpreted-text role="guilabel"}.

On the `Join Membership`{.interpreted-text role="guilabel"} pop-up
window that appears, select a `Membership`{.interpreted-text
role="guilabel"} from the drop-down menu. Then, configure a
`Member Price`{.interpreted-text role="guilabel"}.

Click `Invoice Membership`{.interpreted-text role="guilabel"} when both
fields are filled in. Doing so reveals a
`Membership Invoices`{.interpreted-text role="guilabel"} page, wherein
invoices can be confirmed and completed.

Alternatively, to offer a free membership, tick the
`Free Member`{.interpreted-text role="guilabel"} checkbox, in the
`Membership`{.interpreted-text role="guilabel"} tab of a contact form.

Membership status {#sales/membership-status}
-----------------

The `Current Membership Status`{.interpreted-text role="guilabel"} is
listed on the `Membership`{.interpreted-text role="guilabel"} tab of
each contact record:

-   `Non Member`{.interpreted-text role="guilabel"}: a partner who has
    **not** applied for membership.
-   `Cancelled Member`{.interpreted-text role="guilabel"}: a member who
    has cancelled their membership.
-   `Old Member`{.interpreted-text role="guilabel"}: a member whose
    membership end date has passed.
-   `Waiting Member`{.interpreted-text role="guilabel"}: a member who
    has applied for membership, but whose invoice has not yet been
    created.
-   `Invoiced Member`{.interpreted-text role="guilabel"}: a member whose
    invoice has been created, but has not been paid.
-   `Paid Member`{.interpreted-text role="guilabel"}: a member who has
    paid the membership fee.

Publish members directory
-------------------------

To publish a list of active members on the website, the *Online Members
Directory* application must first be
`installed <general/install>`{.interpreted-text role="ref"}. After
installing the module, add the [/members]{.title-ref} page to the
website\'s menu by
`editing the website menu <../websites/website/pages/menus>`{.interpreted-text
role="doc"}.

{.align-center}

### Publish individual members

Return to `CRM app --> Sales --> Customers`{.interpreted-text
role="menuselection"}, and click the Kanban card for a member. From the
resulting customer form that appears, click the
`Go to Website`{.interpreted-text role="guilabel"} smart button at the
top of the page to open the member\'s webpage.

Click the `fa-pencil`{.interpreted-text role="icon"}
`Edit`{.interpreted-text role="guilabel"} button to reveal a sidebar of
editing tools. After making any necessary changes to the page, click
`Save`{.interpreted-text role="guilabel"}. At the top of the page, slide
the `Unpublished`{.interpreted-text role="guilabel"} toggle to the
active, `Published`{.interpreted-text role="guilabel"} position.

Repeat these steps for all desired members.

::: {.toctree titlesonly=""}
members/members\_analysis
:::
