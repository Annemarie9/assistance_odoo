# File: /content/odoo_doc17.0/fr/content/applications/marketing/events/event_booths.md

Event booths
============

The Odoo *Events* application provides users with the ability to create
event booths, sell their availability, and manage their reservations.

Configuration
-------------

In order to create, sell, and manage booths for events, the *Booth
Management* feature must be activated.

To do that, navigate to
`Events app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, and tick the `Booth Management`{.interpreted-text
role="guilabel"} checkbox. Then, click `Save`{.interpreted-text
role="guilabel"}.

{.align-center}

::: {.important}
::: {.title}
Important
:::

When the `Booth Management`{.interpreted-text role="guilabel"} setting
is activated, a new `Product Type
<../../inventory_and_mrp/inventory/product_management/configure/type>`{.interpreted-text
role="doc"} becomes available on all product forms: *Event Booth*.

This is important because every created booth **must** be assigned a
*Booth Category* on their respective booth form, and every booth
category **must** have an *Event Booth* product assigned to it.
:::

Booth categories
----------------

With the *Booth Management* setting activated in the *Events* app, the
*Booth Categories* option appears in the
`Configuration`{.interpreted-text role="guilabel"} menu.

To access the `Booth Category`{.interpreted-text role="guilabel"}
dashboard, go to `Events app -->
Configuration --> Booth Categories`{.interpreted-text
role="menuselection"}, which reveals a list of all created booth
categories.

{.align-center}

On the `Booth Category`{.interpreted-text role="guilabel"} page, the
following information for each booth category is listed:

-   `Name`{.interpreted-text role="guilabel"}: the name of the booth
    category.
-   `Create Sponsor`{.interpreted-text role="guilabel"}: if checked,
    booking this booth category creates a sponsor for the user.
-   `Product`{.interpreted-text role="guilabel"}: the *Event Booth*
    product associated with that specific booth category.
-   `Price`{.interpreted-text role="guilabel"}: the price of a booth in
    that booth category.

When the `oi-settings-adjust`{.interpreted-text role="icon"}
`(settings)`{.interpreted-text role="guilabel"} icon, located to the
far-right of the column titles, is clicked, a drop-down menu of
additional column options appears. From the resulting drop-down menu,
tick the checkbox beside `Sponsor Level`{.interpreted-text
role="guilabel"} and/or `Sponsor Type`{.interpreted-text
role="guilabel"} to reveal those columns on the
`Booth Category`{.interpreted-text role="guilabel"} page.

To edit an existing booth category, select it from the list, and proceed
to make any desired modifications from the event category form.

### Create booth category

To create a booth category from the `Booth Category`{.interpreted-text
role="guilabel"} page, click the `New`{.interpreted-text
role="guilabel"} button in the upper-left corner to reveal a blank booth
category form.

{.align-center}

Start by entering a name for the booth category in the top
`Booth Category`{.interpreted-text role="guilabel"} field. This is a
**requried** field.

To add a corresponding image to the booth category (e.g. a sample photo
of how the booth looks), click the `fa-pencil`{.interpreted-text
role="icon"} `(pencil)`{.interpreted-text role="guilabel"} icon that
appears when the cursor hovers over the camera placeholder in the
upper-right corner of the booth category form. When clicked, proceed to
upload the desired image to the booth category form, if needed.

In the `Booth Details`{.interpreted-text role="guilabel"} section, users
**must** assign a `Product`{.interpreted-text role="guilabel"} to the
category, and it **must** have *Event Booth* set as the *Product Type*
on the product form.

And, regardless of the listed price on the *Event Booth* product chosen,
the user can input a custom `Price`{.interpreted-text role="guilabel"}
to be applied for this booth category in the field below.

In the `Sponsorship`{.interpreted-text role="guilabel"} section, there
is a `Create Sponsor`{.interpreted-text role="guilabel"} checkbox
option. With that checkbox ticked, whenever a booth belonging to this
category is booked, the user is created as an official *Sponsor* of the
event.

When the `Create Sponsor`{.interpreted-text role="guilabel"} checkbox is
ticked, two additional fields appear beneath it:
`Sponsor Level`{.interpreted-text role="guilabel"} and
`Sponsor Type`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

`Sponsor Level`{.interpreted-text role="guilabel"} and
`Sponsor Type`{.interpreted-text role="guilabel"} are purely to
distinguish different distinctions of sponsors. For example, if a
sponsor has been attached to a company for multiple years, they would be
granted a higher level (e.g. *Gold* level), which provides them with
immediate credability and status. Whereas, conversely, a relatively new
sponsor would be granted a lower level (e.g. *Bronze* level), which
coincides with its own credability and status.
:::

Select a desired level of sponsorship from the
`Sponsor Level`{.interpreted-text role="guilabel"} drop-down field.

::: {.tip}
::: {.title}
Tip
:::

To modify any existing `Sponsor Level`{.interpreted-text
role="guilabel"}, select it from the drop-down field, then click the
`fa-arrow-right`{.interpreted-text role="icon"}
`(right arrow)`{.interpreted-text role="guilabel"} that appears at the
end of the line. Doing so opens a separate page, wherein the
`Sponsor Level`{.interpreted-text role="guilabel"} name and
`Ribbon Style`{.interpreted-text role="guilabel"} can be changed, if
necessary.
:::

Users can also create a new `Sponsor Level`{.interpreted-text
role="guilabel"}, by typing in the name of the new level, and clicking
`Create and edit...`{.interpreted-text role="guilabel"} from the
resulting drop-down menu.

::: {.note}
::: {.title}
Note
:::

Clicking `Create`{.interpreted-text role="guilabel"} from the resulting
drop-down menu in this instance creates the sponsor level, but doesn\'t
immediately prompt the user to further configure it, via a
`Create Sponsor Level`{.interpreted-text role="guilabel"} pop-up window.
:::

Doing so reveals a `Create Sponsor Level`{.interpreted-text
role="guilabel"} pop-up window.

{.align-center}

From this pop-up window, confirm the newly-created
`Sponsor Level`{.interpreted-text role="guilabel"}, and decide what kind
of `Ribbon Style`{.interpreted-text role="guilabel"} should be applied,
if any. The `Ribbon Style`{.interpreted-text role="guilabel"} options
available in that drop-down field are: `No Ribbon`{.interpreted-text
role="guilabel"}, `Gold`{.interpreted-text role="guilabel"},
`Silver`{.interpreted-text role="guilabel"}, and
`Bronze`{.interpreted-text role="guilabel"}.

If one is selected, that `Ribbon Style`{.interpreted-text
role="guilabel"} appears with the sponsor\'s name on the event website.

On the booth category form, beneath those sections
(`Booth Details`{.interpreted-text role="guilabel"} and
`Sponsorship`{.interpreted-text role="guilabel"}), there is the
`Description`{.interpreted-text role="guilabel"} tab. In this tab,
proceed to enter any vital information related to the booth category
that would be important for any potential booth-buyer to know about
(e.g., the square footage, any amenities, size of display screen, etc.).

Add booth to an event
---------------------

In order to add a booth to an event, navigate to an existing event form,
via `Events
app --> Events`{.interpreted-text role="menuselection"}, and select the
desired event from the `Events`{.interpreted-text role="guilabel"}
dashboard. Or, click `New`{.interpreted-text role="guilabel"} to open a
blank event form.

From the event form, to access the *Booths* for that specific event,
click the `Booths`{.interpreted-text role="guilabel"} smart button at
the top of the page.

The `Booths`{.interpreted-text role="guilabel"} page is displayed in a
Kanban view, by default, with two different stages:
`Available`{.interpreted-text role="guilabel"} and
`Unavailable`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

The `Booths`{.interpreted-text role="guilabel"} page of an event is also
viewable in a `oi-view-list`{.interpreted-text role="icon"}
`List`{.interpreted-text role="guilabel"} view,
`fa-area-chart`{.interpreted-text role="icon"} `Graph`{.interpreted-text
role="guilabel"} view, and `oi-view-pivot`{.interpreted-text
role="icon"} `Pivot`{.interpreted-text role="guilabel"} view. All of
which are accessible, via their icons, in the upper-right corner of the
`Booths`{.interpreted-text role="guilabel"} page.
:::

The booths present in the `Available`{.interpreted-text role="guilabel"}
stage are still available for people to purchase for the event. The
booths present in the `Unavailable`{.interpreted-text role="guilabel"}
stage have already been purchased, and are no longer available.

To modify any existing booth, simply click the desired booth from the
`Booths`{.interpreted-text role="guilabel"} page, and proceed to make
any necessary changes from the booth form. Or, create a new one, by
clicking the `New`{.interpreted-text role="guilabel"} button in the
upper-left corner to reveal a blank booth form.

### Booth form

The booth form in Odoo *Events* lets users customize and configure event
booths in a number of different ways.

{.align-center}

Start by typing in a `Name`{.interpreted-text role="guilabel"} for the
booth. This is a **required** field.

Then, apply a `Booth Category`{.interpreted-text role="guilabel"} to the
booth. This is a **required** field.

::: {.tip}
::: {.title}
Tip
:::

A new `Booth Category`{.interpreted-text role="guilabel"} can be created
from this field, by typing in the name of the new category, and clicking
`Create and edit...`{.interpreted-text role="guilabel"} from the
resulting drop-down menu. Doing so reveals a
`Create Booth Category`{.interpreted-text role="guilabel"} pop-up
window, with all the standard fields found on a common booth category
form.

Simply clicking `Create`{.interpreted-text role="guilabel"} from the
resulting drop-down menu creates the category, but does not reveal the
`Create Booth Category`{.interpreted-text role="guilabel"} pop-up
window. The category would have to be modified later, via the *Booth
Categories* page (`Events app --> Configuration
--> Booth Categories`{.interpreted-text role="menuselection"}).
:::

Upon selecting a pre-existing `Booth Category`{.interpreted-text
role="guilabel"}, two additional, non-modifiable fields appear:
`Product`{.interpreted-text role="guilabel"} and
`Price`{.interpreted-text role="guilabel"}. Both fields represent their
respective selections for that specific booth category.

When a person purchases a booth rental through the event website, the
subsequent renter-related fields on the form auto-populate, based on the
information provided by the purchaser during the online transaction. The
booth also automatically changes its status from *Available* to
*Unavailable*.

However, if the rental of a booth is conducted in any other way (e.g.,
in person, via sales order, etc.), the `Renter`{.interpreted-text
role="guilabel"}, `Renter Name`{.interpreted-text role="guilabel"},
`Renter Email`{.interpreted-text role="guilabel"}, and
`Renter Phone`{.interpreted-text role="guilabel"} fields can be entered
in manually.

The status of the booth (`Available`{.interpreted-text role="guilabel"}
or `Unavailable`{.interpreted-text role="guilabel"}) can also be changed
manually, either by clicking the appropriate status from the status bar
present on the booth form, or by dragging-and-dropping the desired booth
into the appropriate stage, via the *Booths* page Kanban view.

Sell event booths
-----------------

With event booths configured on the event form, via the event-specific
*Booths* pages, Odoo presents them on the event website, via the *Get A
Booth* event subheader link.

To access the *Get A Booth* page on the event website, open the
`Events app`{.interpreted-text role="menuselection"}, and select the
desired event from the `Events`{.interpreted-text role="guilabel"}
dashboard. From the event form, click the
`Go to Website`{.interpreted-text role="guilabel"} smart button to be
taken to the Odoo-built event website.

If the event subheader menu (with the `Get A Booth`{.interpreted-text
role="guilabel"} option) is *not* showing up on the event website, there
are two ways to make it appear.

While on the event website, enter the edit mode by clicking the
`Edit`{.interpreted-text role="guilabel"} button in the upper-right
corner. Then, click into the `Customize`{.interpreted-text
role="guilabel"} tab of the resulting sidebar of web design tools.

In the `Customize`{.interpreted-text role="guilabel"} tab, click the
toggle switch for `Sub-Menu (Specific)`{.interpreted-text
role="guilabel"}, and click `Save`{.interpreted-text role="guilabel"}.
Doing so reveals the event subheader menu with various options.

Alternatively, enter
`Debug mode <../../general/developer_mode>`{.interpreted-text
role="doc"}, and open the specific event form in the the *Events*
application.

On the event form, with *Debug mode* on, an array of subheader menu
options appears. Tick the checkbox for
`Website Submenu`{.interpreted-text role="guilabel"}, in order for the
submenu to appear on the event website. Doing so also ticks every other
submenu-related checkbox automatically.

At this point, proceed to choose which options to keep on the event
subheader menu. In this case, make sure the
`Booth Register`{.interpreted-text role="guilabel"} checkbox is ticked.

From there, click the `Get A Booth`{.interpreted-text role="guilabel"}
event subheader menu option. Doing so reveals the
`Get A Booth`{.interpreted-text role="guilabel"} page, showcasing all
the configured event booths that were created on the event form.

{.align-center}

From here, the visitor can select their desired booth option, then
`Location`{.interpreted-text role="guilabel"}. Next, they would click
the `Book my Booth(s)`{.interpreted-text role="guilabel"} button,
located at the bottom of the `Get A
Booth`{.interpreted-text role="guilabel"} page.

Doing so reveals a `Contact Details`{.interpreted-text role="guilabel"}
page, wherein they fill out either *Contact Details* or *Sponsor
Details*, depending on how the booth was configured on the event form.
The fields present on this form vary, depending on whether its meant for
a basic contact or an event sponsor.

::: {.note}
::: {.title}
Note
:::

If the selected booth has the *Create Sponsor* checkbox ticked, this
page reads as *Sponsor Details*.
:::

The information provided on this details page is used to auto-populate
the renter-related information on the booth form on the event form in
the *Events* application.

Once the necessary information has been entered, the visitor then clicks
the `Go to
Payment`{.interpreted-text role="guilabel"} at the bottom of the page,
and proceeds to complete the typical checkout process.

Upon a successful payment confirmation, that selected booth
automatically moves to the *Unavailable* stage on the event-specific
*Booths* page in the *Events* application (accessible via the *Booths*
smart button on the event form).

Also, the provided *Sponsor* information (if applicable) and *Sales
Order* information are accessible from the specific event form, via
their respective smart buttons that appear at the top of the form.

::: {.note}
::: {.title}
Note
:::

Click the *Sponsors* smart button to modify any information about the
sponsor, if necessary.
:::

::: {.seealso}
\- `create_events`{.interpreted-text role="doc"} -
`sell_tickets`{.interpreted-text role="doc"}
:::
