# File: /content/odoo_doc17.0/fr/content/applications/productivity/voip/axivox/dial_plan_basics.md

Dial plan basics
================

When someone calls a business, they might need to get in contact with
customer support, a sales team, or even a person\'s direct line. The
caller might also be in search of some information about the business,
such as store hours. Or, they might want to leave a voicemail, so
someone from the company can call them back. With dial plans in Axivox,
a company can manage how incoming calls like this are handled.

Using proper call architecture through a dial plan, callers get directed
to the right people, or to the right information, in a quick, efficient
manner.

This document covers the basic configuration of dial plans in Axivox.

::: {.seealso}
For more information on advanced dial plans, visit
`dial_plan_advanced`{.interpreted-text role="doc"}.
:::

::: {.important}
::: {.title}
Important
:::

Using a browser add-on for spelling may hinder the use of the visual
editor in dial plans. Do not use a translator with the Axivox management
console.
:::

Dial plans {#voip/axivox/dial_plans}
----------

Access dial plans by navigating to [Axivox management
console](https://manage.axivox.com), and clicking on
`Dial plans`{.interpreted-text role="guilabel"} from the menu on the
left.

To add a new dial plan from the `Dial plan`{.interpreted-text
role="guilabel"} page, click the green button labeled,
`Add a new dial plan`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Axivox has no limit to the number of dial plans that can be created.
These can be added, and improved upon, at any time. This allows for
sandboxes to be created with many different configurations.
:::

{.align-center}

To edit an existing dial plan, choose one of the following options to
the right of the saved dial plan:

1.  `Delete`{.interpreted-text role="guilabel"}: this action deletes the
    attached dial plan.
2.  `Edit`{.interpreted-text role="guilabel"}: this action allows the
    user to edit the dial plan.
3.  `Visual Editor`{.interpreted-text role="guilabel"}: this action
    opens a visual editor window, where the dial plan architecture can
    be viewed and edited.
4.  `Duplicate`{.interpreted-text role="guilabel"}: this action
    duplicates the dial plan, and puts it at the bottom of the list,
    with an extension of one number (+1) larger than the original
    extension.

### Dialplan editor (visual editor)

When the `Visual Editor`{.interpreted-text role="guilabel"} button is
clicked for a dial plan on the `Dial plan`{.interpreted-text
role="guilabel"} page, a pop-up `Dialplan Editor`{.interpreted-text
role="guilabel"} window appears.

This pop-up window is the primary place where the architecture, or
structure, of the dial plan is configured. In this window, a
`GUI (graphical user interface)`{.interpreted-text role="abbr"} appears,
where various dial plan elements can be configured and linked together.

![Visual editor for an example dial plan, with the new element, Add, and Save buttons
highlighted.](dial_plan_basics/dial-plan-visual.png){.align-center}

::: {.important}
::: {.title}
Important
:::

New dial plans come blank with `New element`{.interpreted-text
role="guilabel"} options for the user to `Add`{.interpreted-text
role="guilabel"} and `Save`{.interpreted-text role="guilabel"}.

The method for saving in the `Dialplan Editor`{.interpreted-text
role="guilabel"} is different from saving any other edits in the Axivox
management console because the `Save`{.interpreted-text role="guilabel"}
button **must** be pressed before closing the
`Visual editor`{.interpreted-text role="menuselection"}.

Then, before these changes can take place on the Axivox platform, the
user **must** click `Apply changes`{.interpreted-text role="guilabel"}
in the upper-right corner of the `Dial plan`{.interpreted-text
role="guilabel"} page.
:::

From the `Dialplan Editor`{.interpreted-text role="guilabel"} pop-up
window, users can add a new element to the dial plan. To do that, open
the `New element`{.interpreted-text role="guilabel"} drop-down menu, and
select the desired element. Then, click `Add`{.interpreted-text
role="guilabel"}.

Doing so adds that element to the visual editor display of the dial plan
being modified. This element can be moved where desired amongst the
other elements present in the dial plan.

Connect elements in the dial plan by clicking and dragging outward from
the `(open
circle)`{.interpreted-text role="guilabel"} icon on the right side of
the element. Doing so reveals an `(arrow)`{.interpreted-text
role="guilabel"} icon. Proceed to drag this `(arrow)`{.interpreted-text
role="guilabel"} icon to the desired element in the dial plan that it is
meant to connect with.

Connect the `(arrow)`{.interpreted-text role="guilabel"} icon to the
circle on the left side of the desired element.

Calls displayed in the dial plan flow from left-to-right in the element.

In order to further configure a `New element`{.interpreted-text
role="guilabel"}, double-click on the element inside the dial plan, to
reveal a subsequent pop-up window, wherein additional customizations can
be entered.

Each element has a different configuration pop-up window that appears
when double-clicked.

::: {.important}
::: {.title}
Important
:::

All elements **must** have a final destination in the dial plan in order
to close a loop. This can be accomplished by implementing the
`Hang up`{.interpreted-text role="guilabel"} element, or looping the
element back to a `Menu`{.interpreted-text role="guilabel"} element or
`Digital Receptionist`{.interpreted-text role="guilabel"} element
elsewhere in the dial plan.

![Dial plan, shown with highlight looping open end back to the beginning of the menu
element.](dial_plan_basics/loop-back.png){.align-center}
:::

Once all desired dial plan elements and configurations are complete,
remember to click `Save`{.interpreted-text role="guilabel"} before
exiting the `Dialplan Editor`{.interpreted-text role="guilabel"} pop-up
window. Then, click `Apply changes`{.interpreted-text role="guilabel"}
on the `Dial plans`{.interpreted-text role="guilabel"} page to ensure
they are implemented into Axivox production.

### Dial plan elements

The following elements are available in the
`New element`{.interpreted-text role="guilabel"} drop-down menu, while
designing a dial plan in the `Dialplan Editor`{.interpreted-text
role="guilabel"} pop-up window.

#### Basic elements

These are the basic elements that are used in simple dial plans in
Axivox:

-   `Call`{.interpreted-text role="guilabel"}: call an extension or
    queue.
-   `Play a file`{.interpreted-text role="guilabel"}: play an audio file
    or voice greeting.
-   `Voicemail`{.interpreted-text role="guilabel"}: forward to a
    voicemail (terminal).
-   `Hang up`{.interpreted-text role="guilabel"}: hang up the call
    (terminal).
-   `Queue`{.interpreted-text role="guilabel"}: attach a call queue with
    a group of users to answer a call.
-   `Conference`{.interpreted-text role="guilabel"}: add a conference
    room for a caller to connect to.

#### Basic routing elements

Routing elements change or route the path of a caller, these are some
basic routing elements used in Axivox:

-   `Menu`{.interpreted-text role="guilabel"}: add a dial-by-number
    directory and configure downstream actions (not terminal).
-   `Switch`{.interpreted-text role="guilabel"}: attach a manual on/off
    control that can divert traffic based on whether it is opened (On)
    or closed (Off).
-   `Digital Receptionist`{.interpreted-text role="guilabel"}: attach a
    virtual dispatcher to listen for extensions to connect to.

#### Advanced routing elements

These are the more advanced elements that route calls in Axivox:

-   `Dispatcher`{.interpreted-text role="guilabel"}: create a call
    filter to route traffic based on the geo-location of the caller ID.
-   `Access List`{.interpreted-text role="guilabel"}: create a tailored
    access list with VIP customer preference.
-   `Time Condition`{.interpreted-text role="guilabel"}: create time
    conditions to route incoming traffic around holidays, or other
    sensitive time-frames.
-   `Multi-Switch`{.interpreted-text role="guilabel"}: a mechanism to
    create paths, and turn them on and off, to divert incoming calls.

#### Advanced elements

The following are more advanced elements (not routing) in Axivox:

-   `Record`{.interpreted-text role="guilabel"}: recording feature is
    enabled (requires plan change, enabled in Axivox settings).
-   `Caller ID`{.interpreted-text role="guilabel"}: replace the caller
    ID by the called number or free text.

::: {.important}
::: {.title}
Important
:::

Dial plan elements can be configured by double-clicking them, and
linking different aspects of the Axivox console to them.
:::

Attach to incoming number
-------------------------

To attach an existing dial plan to an incoming number, go to [Axivox
management console](https://manage.axivox.com) , and click on
`Incoming numbers`{.interpreted-text role="guilabel"}.

Next, click `Edit`{.interpreted-text role="guilabel"} next to the number
to which the dial plan should be attached.

Doing so reveals a separate page wherein that number\'s dial plan can be
modified. To do that, select `Dial plan`{.interpreted-text
role="guilabel"} from the
`Destination type for voice call`{.interpreted-text role="guilabel"}
field drop-down menu. Then, choose the desired dial plan from the
`Dial plan`{.interpreted-text role="guilabel"} field that appears.

With that in place, that means when that specific number calls in, the
configured dial plan is activated, and runs through the prompts to
properly route the caller.

Finally, `Save`{.interpreted-text role="guilabel"} the changes, and
click `Apply changes`{.interpreted-text role="guilabel"} in the
upper-right corner.

### Basic dial plan scenario

The following showcases a basic dial plan scenario for call routing,
where additional elements can be added to expand the setup. This basic
dial plan scenario includes the following linked elements
`Start --> Play a file --> Menu --> (Hang-up, Calls, Queues, Conferences) -->
(Voicemail, Hang-up)`{.interpreted-text role="menuselection"}.

{.align-center}

::: {.seealso}
This setup does **not** include any basic or advanced call routing. For
more information on call routing, reference this documentation:
`dial_plan_advanced`{.interpreted-text role="doc"}.
:::
