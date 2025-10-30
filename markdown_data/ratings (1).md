# File: /content/odoo_doc17.0/fr/content/applications/services/helpdesk/overview/ratings.md

Customer ratings
================

Asking customers to rate the support they received from a *Helpdesk*
team provides an opportunity to gauge team performance and track
customer satisfaction. Ratings can be published on the portal, providing
customers with a general overview of the team\'s performance.

Enable customer ratings on Helpdesk teams {#helpdesk/enable-ratings}
-----------------------------------------

To enable *customer ratings* on a helpdesk team, navigate to
`Helpdesk app -->
Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"}. Select a team from the list and click on it to
open the settings page. Scroll to the `Performance`{.interpreted-text
role="guilabel"} section, and tick the
`Customer Ratings`{.interpreted-text role="guilabel"} checkbox.

![Overview of the settings page of a helpdesk team emphasizing the rating on ticket feature
in Odoo Helpdesk.](ratings/ratings-enable.png){.align-center}

Set a ratings request email template on a stage
-----------------------------------------------

To automatically request ratings from customers once their tickets have
closed, an email template should be added to the appropriate stage.

After the `Customer Ratings`{.interpreted-text role="guilabel"}
`setting has been enabled <helpdesk/enable-ratings>`{.interpreted-text
role="ref"} on the team\'s settings page, click the
`Set an Email Template on Stages`{.interpreted-text role="guilabel"}
link. Select a stage from the list, or click `New`{.interpreted-text
role="guilabel"} to create a new stage.

::: {.important}
::: {.title}
Important
:::

Customers should only be asked to rate tickets once an issue has been
resolved and their ticket is *closed*. Therefore, a *ratings request*
email should **only** be added to a stage that is folded in the Kanban,
as tickets in a *folded stage* are considered closed.
:::

On the stage\'s settings page, select the template, [Helpdesk: Ticket
Rating Request]{.title-ref} in the `Email Template`{.interpreted-text
role="guilabel"} field. This template has been preconfigured with
ratings customers can use to provide feedback. To view the template,
click the arrow button to the right of the field.

After the template is added to the stage, it automatically sends a
message when a ticket is moved to that stage. Customers are then asked
to rate the support they received with colored icons.

> -   *Green smiling face* - Satisfied
> -   *Yellow neutral face* - Okay
> -   *Red frowning face* - Dissatisfied

After selecting a rating, customers are taken to a webpage where they
can provide specific written feedback to support their rating. The
rating is then submitted, and the rating, as well as any additional
comments, are added to the chatter on the ticket.

::: {.tip}
::: {.title}
Tip
:::

Customer ratings can also be viewed through the
`Customer Ratings`{.interpreted-text role="guilabel"} report. To view
this report, go to
`Helpdesk app --> Reporting --> Customer Ratings`{.interpreted-text
role="menuselection"}.
:::

::: {.seealso}
`../../../general/companies/email_template`{.interpreted-text
role="doc"}
:::

Publish ratings on the customer portal
--------------------------------------

After enabling the `Customer Ratings`{.interpreted-text role="guilabel"}
setting, an option to publish ratings on the team\'s website appears.
Enabling this setting provides portal users with an overview of the
ratings the team has received over the last thirty days. Specific
written feedback will not be included; only statistics of the team\'s
performance will be visible.

::: {.important}
::: {.title}
Important
:::

To display ratings on the customer portal, a team **must** have their
visibility setting set to
`Invited portal users and all internal users (public)`{.interpreted-text
role="guilabel"}. To enable this setting, navigate to
`Helpdesk app --> Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"}. Select a team from the list and click on it to
open the settings page. Scroll to the `Visibility &
Assignment`{.interpreted-text role="guilabel"} section, and tick the
`Invited portal users and all internal users
(public)`{.interpreted-text role="guilabel"} checkbox.
:::

Next, to publish the ratings, go to
`Helpdesk app--> Configuration --> Helpdesk
Teams`{.interpreted-text role="menuselection"} and select a team. Scroll
to `Performance`{.interpreted-text role="guilabel"} and tick the
checkbox for
`Publish this team's ratings on your website`{.interpreted-text
role="guilabel"}.

To view the ratings for a team, a customer will log into the portal and
navigate to one of their tickets. After clicking on the team name in the
`Managed By`{.interpreted-text role="guilabel"} field, they will be
directed to a page with the team\'s ratings over the past thirty days.

{.align-center}

::: {.seealso}
`Portal access <../../../general/users/portal>`{.interpreted-text
role="doc"}
:::

### Manually hide individual ratings

Individual ratings can be manually hidden from the portal. This allows
for specific ratings to be kept out of the performance metrics shared
with customers.

To make a rating visible only to internal users, navigate to the page
for a rating. This can be done in one of the following ways:

> -   Go to
>     `Helpdesk app --> Reporting --> Customer Ratings`{.interpreted-text
>     role="menuselection"} and click on one of the Kanban cards for an
>     individual rating.
> -   Navigate to
>     `Helpdesk app--> Tickets --> All Tickets`{.interpreted-text
>     role="menuselection"} and remove the `Open`{.interpreted-text
>     role="guilabel"} filter from the search bar. Then filter by
>     `Satisfied`{.interpreted-text role="guilabel"},
>     `Okay`{.interpreted-text role="guilabel"} and/or
>     `Dissatisfied`{.interpreted-text role="guilabel"}. Select a ticket
>     from the results. Click the `Rating`{.interpreted-text
>     role="guilabel"} smart button.

Once on the rating details page, check the
`Visible Internally Only`{.interpreted-text role="guilabel"} box.

{.align-center}

::: {.seealso}
\- `../advanced/close_tickets`{.interpreted-text role="doc"} -
`reports`{.interpreted-text role="doc"}
:::
