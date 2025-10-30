# File: /content/odoo_doc17.0/fr/content/applications/services/field_service/planning_itinerary.md

Planning an itinerary
=====================

By default, **Odoo Field Service** shows a static map where all task
locations for the day are pinned. To make it more useful for the field
service workers, it is possible to display an itinerary on the map using
MapBox. To do so, enable the **Map Routes** feature as follows:

1.  Create or sign in to a MapBox account using the following link:
    <https://www.mapbox.com/>.
2.  [Create a
    token](https://docs.mapbox.com/help/getting-started/access-tokens/#adding-url-restrictions-to-access-tokens).
3.  Go to the [Access tokens page on
    Mapbox](https://account.mapbox.com/access-tokens/) and copy your
    token.
4.  In Odoo, go to the `Settings`{.interpreted-text role="guilabel"} app
    and scroll down to the `Integrations`{.interpreted-text
    role="guilabel"} section. Paste your Mapbox access token in the
    `Token`{.interpreted-text role="guilabel"} field under
    `Map Routes`{.interpreted-text role="guilabel"}, and click
    `Save`{.interpreted-text role="guilabel"}.

Displaying your itinerary on a map
----------------------------------

::: {.important}
::: {.title}
Important
:::

For a field service task to be featured on the map, a **valid address**
must be provided for the customer.
:::

To display your tasks on a map, go to
`Field Service --> My Tasks --> Map`{.interpreted-text
role="menuselection"}. To create your itinerary, Odoo sorts out your
field service tasks based on their `Planned Date`{.interpreted-text
role="guilabel"} to show the way from one location to the next.

To open your itinerary on the Google Maps website or app, click
`View in Google Maps`{.interpreted-text role="guilabel"}. Google Maps
includes your current location as a starting point for your itinerary.

::: {.tip}
::: {.title}
Tip
:::

\- By default, the map shows today's tasks. Remove the
`Today`{.interpreted-text role="guilabel"} filter in the search bar to
display all tasks. Your tasks are then sorted by date in the left
column. - Click your task in the left column or the map pin to display
the task\'s details. From there, you can `Open`{.interpreted-text
role="guilabel"} the task or click `Navigate to`{.interpreted-text
role="guilabel"} to get an itinerary from your current location to this
specific task\'s location.
:::
