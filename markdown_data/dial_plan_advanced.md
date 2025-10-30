# File: /content/odoo_doc17.0/fr/content/applications/productivity/voip/axivox/dial_plan_advanced.md

Advanced dial plans
===================

Typically, companies have a lot of incoming calls every day, but many do
not want their teams to answer calls 24 hours a day, 7 days a week.

By using Axivox advanced dial plan features, the process can be
automated, and routing can be set up for all scenarios. This way,
customers are never left waiting, or frustrated, because they cannot get
in touch with anyone.

By utilizing the advanced elements in dial plans, companies can automate
call routing for certain days or times, like company holidays. Companies
can also allow callers to enter extensions themselves, and get
transferred automatically using a digital receptionist. This way, an
administrative team does **not** have to be available around the clock.

There is even the option to route callers, depending on where they are
calling from in the world, thus maximizing efficiency.

::: {.important}
::: {.title}
Important
:::

For more information on basic dial plans, and how to add elements, visit
`dial_plan_basics`{.interpreted-text role="doc"}.
:::

::: {.warning}
::: {.title}
Warning
:::

Using a browser add-on for spelling may hinder the use of the visual
editor in dial plans. Do **not** use a translator with the Axivox
management console.
:::

Advanced elements
-----------------

In Axivox dial plans (as described in
`dial_plan_basics`{.interpreted-text role="doc"}), there are two
advanced elements that can be used.

-   `Record`{.interpreted-text role="guilabel"}: recording feature is
    enabled (requires plan change, enabled in Axivox settings).
-   `Caller ID`{.interpreted-text role="guilabel"}: replace the caller
    ID by the called number or free text.

To add one of these elements, navigate to the
`Dial plans`{.interpreted-text role="guilabel"} page, located in the
menu on the left side of the [Axivox management
console](https://manage.axivox.com).

Next, click on the `Visual Editor`{.interpreted-text role="guilabel"}
button to the right of the desired dial plan to edit it. Finally, open
the `New element`{.interpreted-text role="guilabel"} drop-down menu,
select the element, and click `Add`{.interpreted-text role="guilabel"}.

{.align-center}

For more information, visit `voip/axivox/dial_plans`{.interpreted-text
role="ref"}.

::: {.important}
::: {.title}
Important
:::

The `Record`{.interpreted-text role="guilabel"} element records calls
that are routed through this element, and requires an additional plan
change in Axivox.
:::

To enable recording on Axivox, navigate to `Settings`{.interpreted-text
role="guilabel"} in the [Axivox management
console](https://manage.axivox.com). Then, go to the
`Recording`{.interpreted-text role="guilabel"} drop-down menu, near the
bottom of the page. From there, select `Enabled`{.interpreted-text
role="guilabel"} from the drop-down menu to enable recording using the
`Record`{.interpreted-text role="guilabel"} element in a dial plan.

::: {.tip}
::: {.title}
Tip
:::

If the `Recording`{.interpreted-text role="guilabel"} drop-down menu is
unavailable and unable to change, then consult Axivox to enable the
feature.
:::

The `Caller ID`{.interpreted-text role="guilabel"} element allows for
the replacement of the caller ID downstream, after routing.

Upon adding the `Caller ID`{.interpreted-text role="guilabel"} element
to the dial plan, and double-clicking it to configure it, two options
appear.

The first is a `Free text`{.interpreted-text role="guilabel"} field,
where any text can be input to replace the caller ID. The second option
is `Replace the caller ID by the called number`{.interpreted-text
role="guilabel"}. This option replaces the caller\'s ID with the
`Incoming number`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

A company may want to use the `Caller ID`{.interpreted-text
role="guilabel"} element to replace the `Incoming
number`{.interpreted-text role="guilabel"}, so employees, or outside
transfers, cannot see the number, and information is kept private.
:::

Basic routing elements
----------------------

Basic routing elements in Axivox dial plans provide extension-based
routing. This can be done by adding either a *Menu* to numerically link
the dial-by-numbers to an action, or by using a *Digital Receptionist*
to automatically route or listen for an extension, based on a key input
from the caller.

The main difference between the two elements is that the *Digital
Receptionist* does **not** need to be pre-configured numerically with
actions. Instead, it acts as a virtual receptionist.

-   `Menu`{.interpreted-text role="guilabel"}: add a dial-by-number
    directory and configured downstream actions (not terminal). For
    example, a dial-by-numbers function could feature an element,
    wherein clicking \'2\' takes the caller to the element linked to
    \'2\' on the Menu element in the dial plan.
-   `Digital Receptionist`{.interpreted-text role="guilabel"}: attach a
    virtual dispatcher to listen for extensions.

To add one of these elements, navigate to the
`Dial plans`{.interpreted-text role="guilabel"} page, located in the
menu on the left side of the [Axivox management
console](https://manage.axivox.com). Next, click on the
`Visual Editor`{.interpreted-text role="guilabel"} button to the right
of the dial plan, to edit the dial plan. Then, open the
`New element`{.interpreted-text role="guilabel"} drop-down menu, select
the element, and click `Add`{.interpreted-text role="guilabel"}.

For more information, visit `voip/axivox/dial_plans`{.interpreted-text
role="ref"}.

### Digital receptionist scenario

The *Digital Receptionist* element is a listen-feature that accurately
routes callers through a dial plan, based on the extension they enter,
via the key pad.

Set a *Digital Receptionist* to eliminate the need of a team, or live
receptionist, to be on-call all the time. With that element in place,
calls now reach their destination, without a real person interjecting.

After adding the `Digital Receptionist`{.interpreted-text
role="guilabel"} element to a dial plan, connect the appropriate
endpoints, and double-click on the element to set the
`Timeout`{.interpreted-text role="guilabel"} on the
`receptionist`{.interpreted-text role="guilabel"} pop-up window that
appears.

The `Timeout`{.interpreted-text role="guilabel"} can be set in
[5]{.title-ref} second increments, from [5]{.title-ref} seconds to
[60]{.title-ref} seconds.

::: {.important}
::: {.title}
Important
:::

The `Digital Receptionist`{.interpreted-text role="guilabel"} element
**requires** a `Play a file`{.interpreted-text role="guilabel"} element
on either side of it, to explain what action to take, and when a wrong
extension is entered.
:::

::: {.example}
While customizing a dial plan in a `Dialplan Editor`{.interpreted-text
role="guilabel"} pop-up window, add a `Menu`{.interpreted-text
role="guilabel"} element, with a `Greeting message`{.interpreted-text
role="guilabel"} that might read, [Press star to dial an
extension]{.title-ref}.

Then, on the `Menu`{.interpreted-text role="guilabel"} element, for the
`* (star)`{.interpreted-text role="guilabel"} option, link a
`Play a file`{.interpreted-text role="guilabel"} element, that plays an
`Audio message`{.interpreted-text role="guilabel"} saying, \'Enter the
extension of the person you are trying to reach\'.

Following the first `Play a file`{.interpreted-text role="guilabel"}
element, add the `Digital Receptionist`{.interpreted-text
role="guilabel"} element, followed by another
`Play a file`{.interpreted-text role="guilabel"} element, which states,
\'That is not a valid extension\'.

This last element is in place to close the loop, should the caller not
enter a correct extension.

Finally, this last `Play a file`{.interpreted-text role="guilabel"}
element is looped back into the `Menu`{.interpreted-text
role="guilabel"} element.

{.align-center}
:::

::: {.important}
::: {.title}
Important
:::

Dial plan elements can be configured by double-clicking them, and
selecting different features of the Axivox console to them.

For example, an `Audio message`{.interpreted-text role="guilabel"} needs
to be made, and then selected in a `Play a file`{.interpreted-text
role="guilabel"} or `Menu`{.interpreted-text role="guilabel"} element.

For more information, see this documentation
`voip/axivox/audio_messages`{.interpreted-text role="ref"}.
:::

Advanced routing elements
-------------------------

Advanced routing elements route calls automatically as they are received
into the incoming number(s). This can be configured using geo-location,
whitelisting, or time-based variables. Calls pass through a filter prior
to their final destination, and are routed, based on the set
variable(s).

The following are advanced routing elements:

-   `Dispatcher`{.interpreted-text role="guilabel"}: create a call
    filter to route traffic, based on the geo-location of the caller ID.
-   `Access List`{.interpreted-text role="guilabel"}: create a tailored
    access list, with VIP customer preference.
-   `Time Condition`{.interpreted-text role="guilabel"}: create time
    conditions to route incoming traffic around holidays, or other
    sensitive time-frames.

::: {.tip}
::: {.title}
Tip
:::

Whitelisting is a technical term used to create a list of allowed
numbers. Conversely, blacklisting is used to create a list of denied
numbers.
:::

To add one of these elements, navigate to the
`Dial plans`{.interpreted-text role="guilabel"} page, located in the
menu on the left side of the [Axivox management
console](https://manage.axivox.com). Next, click on the
`Visual Editor`{.interpreted-text role="guilabel"} button to the right
of the dial plan, to edit the dial plan. Then, open the
`New element`{.interpreted-text role="guilabel"} drop-down menu, select
the element, and click `Add`{.interpreted-text role="guilabel"}. For
more information, visit `voip/axivox/dial_plans`{.interpreted-text
role="ref"}.

### Dispatcher scenario

A *Dispatcher* element is a dial plan feature that directs calls, based
on region or geo-location. In most cases, the
`Dispatcher`{.interpreted-text role="guilabel"} element in a dial plan
is linked to the `Start`{.interpreted-text role="guilabel"} element, in
order to filter or screen calls as they come into an incoming number.

Double-click the `Dispatcher`{.interpreted-text role="guilabel"} element
in the `Dialplan Editor`{.interpreted-text role="guilabel"} pop-up
window to configure it.

This element checks numbers (routed through this element), according to
regular expressions. To add a regular expression, click
`Add a line`{.interpreted-text role="guilabel"} on the bottom of the
`Dispatcher`{.interpreted-text role="guilabel"} pop-up window.

Then, under `Name`{.interpreted-text role="guilabel"}, enter a
recognizable name to identify this expression. This is the name that
appears in the `Dispatcher`{.interpreted-text role="guilabel"} element
on the dial plan showcased in the `Dialplan Editor`{.interpreted-text
role="guilabel"} pop-up window.

In the `Regular expression`{.interpreted-text role="guilabel"} field,
enter the country code, or area code, which Axivox should route for
incoming calls. This is especially helpful when a company would like to
filter their customers to certain queues, or users based on the
customer\'s geo-location.

To specify all numbers behind a certain country code, or area code,
include [d+]{.title-ref} after the country code, or country code + area
code.

{.align-center}

::: {.example}
\- \`02\\d+\`: validates the numbers starting with [02]{.title-ref} -
\`00\\d+\`: validates all numbers beginning with [00]{.title-ref} -
[0052d+]{.title-ref} validates all numbers beginning with
[0052]{.title-ref} (Mexico country code) - \`001716\\d+\`: validates all
numbers beginning with [001716]{.title-ref} (USA country code + Western
New York area code)
:::

::: {.tip}
::: {.title}
Tip
:::

A regular expression (shortened to \"regex\" or \"regexp\"), sometimes
referred to as a \"rational expression,\" is a sequence of characters
that specifies a match pattern in text. In other words, a match is made
within the given range of numbers.
:::

When the desired configurations are complete on the
`Dispatcher`{.interpreted-text role="guilabel"} pop-up window, be sure
to click `Save`{.interpreted-text role="guilabel"}.

Upon doing so, the `Dispatcher`{.interpreted-text role="guilabel"}
element appears with different routes available to configure, based on
the `Regular Expressions`{.interpreted-text role="guilabel"} that were
set.

Attach these routes to any `New element`{.interpreted-text
role="guilabel"} in the `Dialplan Editor`{.interpreted-text
role="guilabel"} pop-up window.

By default, there is an `Unknown`{.interpreted-text role="guilabel"}
path that appears on the `Dispatcher`{.interpreted-text role="guilabel"}
element after setting at least one
`Regular Expression`{.interpreted-text role="guilabel"}.

Calls follow this route/path when their number does not match any
`Regular Expression`{.interpreted-text role="guilabel"} set on the
`Dispatcher`{.interpreted-text role="guilabel"} element.

{.align-center}

### Time condition scenario

When a `Time Condition`{.interpreted-text role="guilabel"} element is
added to a dial plan, it has a simple `True`{.interpreted-text
role="guilabel"} and `False`{.interpreted-text role="guilabel"} routing.

After adding the `Time Condition`{.interpreted-text role="guilabel"}
element to a dial plan, double-click it to configure the variables.
`Hour/Minute`{.interpreted-text role="guilabel"},
`Days of the week`{.interpreted-text role="guilabel"},
`Day of the month`{.interpreted-text role="guilabel"}, and
`Month`{.interpreted-text role="guilabel"} can all be configured.

If the time which the caller contacts the incoming number matches the
set time conditions, then the `True`{.interpreted-text role="guilabel"}
path is followed, otherwise the `False`{.interpreted-text
role="guilabel"} path is followed.

::: {.example}
For a company that is closed yearly for the American Independence Day
holiday (July 4th) the following time conditions should be set:

-   `Hour/Minute`{.interpreted-text role="guilabel"} - [0:0 to
    23:59]{.title-ref}
-   `Day of the week`{.interpreted-text role="guilabel"} - [All to
    All]{.title-ref}
-   `Day of the month`{.interpreted-text role="guilabel"} - [From 4 to
    4]{.title-ref}
-   `Month`{.interpreted-text role="guilabel"} - [July]{.title-ref}
:::

The `Time Condition`{.interpreted-text role="guilabel"} element is
especially useful for holidays, weekends, and to set working hours. When
a caller reaches a destination where they can be helped, either with a
real person or voicemail, this reduces wasted time and hangups.

{.align-center}

::: {.important}
::: {.title}
Important
:::

To set the `Timezone`{.interpreted-text role="guilabel"} that the
`Time Condition`{.interpreted-text role="guilabel"} operates under,
navigate to , and
click `Settings`{.interpreted-text role="guilabel"} in the menu on the
left. Then, set the `Timezone`{.interpreted-text role="guilabel"} using
the second field from the bottom, by clicking the drop-down menu.
:::

### Access list scenario

An *Access List* element in a dial plan allows for the routing of
certain numbers, and disallows (denies) other numbers.

After adding an `Access List`{.interpreted-text role="guilabel"} element
to a dial plan, it can be configured by double-clicking on the element
directly in the `Dialplan Editor`{.interpreted-text role="guilabel"}
pop-up window.

Two fields appear where regular expressions can based in the
`Allow`{.interpreted-text role="guilabel"} and `Deny`{.interpreted-text
role="guilabel"} fields of the `Access List`{.interpreted-text
role="guilabel"} pop-up window.

::: {.example}
For a very important customer, their number can be set in the
`Allow`{.interpreted-text role="guilabel"} field, and these callers can
be sent directly to management.
:::

::: {.tip}
::: {.title}
Tip
:::

A regular expression (shortened to \"regex\" or \"regexp\"), sometimes
also referred to as a \"rational expression,\" is a sequence of
characters that specifies a match pattern in text.
:::

{.align-center}

::: {.example}
\- \`2\\d\\d\`: validates numbers from [200 to 299]{.title-ref} -
\`02\\d\*[: validates all numbers beginning with \`02]{.title-ref} -
\`0017165551212\`: validates the number ([0017165551212]{.title-ref})
:::

After setting the `Allow`{.interpreted-text role="guilabel"} and
`Deny`{.interpreted-text role="guilabel"} fields with regular
expressions or numbers, click `Save`{.interpreted-text role="guilabel"}
on the `Access List`{.interpreted-text role="guilabel"} pop-up window.

Then, on the `Access list`{.interpreted-text role="guilabel"} element in
the dial plan, three paths (or routes) are available to link to further
actions.

Unknown calls can be routed through the regular menu flow by adding a
`Menu`{.interpreted-text role="guilabel"} element, and connecting it to
the `Unknown`{.interpreted-text role="guilabel"} path.
`Refused`{.interpreted-text role="guilabel"} calls can be routed to the
`Hang up`{.interpreted-text role="guilabel"} element. Lastly,
`Authorized`{.interpreted-text role="guilabel"} callers can be sent to a
specific extension or queue.

{.align-center}

Switches
--------

A *Switch* element in Axivox is a simple activated/deactivated route
action.

These can be activated or chosen quickly, allowing for quick routing
changes, without altering the dial plan.

Alternate routes can be configured, so that in a moments notice, they
can be switched to. This could be for new availability, or to adjust
traffic flow for any number of reasons.

Axivox allows for a simple on/off switch, and a multi-switch, which can
have several paths to choose from.

-   `Switch`{.interpreted-text role="guilabel"}: a manual on/off control
    that can divert traffic, based on whether it is opened (on) or
    closed (off).
-   `Multi-Switch`{.interpreted-text role="guilabel"}: a mechanism to
    create paths, and turn them on and off, to divert incoming calls.

### Basic switch

A `Switch`{.interpreted-text role="guilabel"} can be set in the [Axivox
management console](https://manage.axivox.com) by navigating to
`Switches`{.interpreted-text role="guilabel"} in the left menu. To
create a new switch click `Add a
switch`{.interpreted-text role="guilabel"} from the
`Switches`{.interpreted-text role="guilabel"} dashboard, configure a
`Name`{.interpreted-text role="guilabel"} for it, and click
`Save`{.interpreted-text role="guilabel"}.

Then, toggle the desired switch to either `On`{.interpreted-text
role="guilabel"} or `Off`{.interpreted-text role="guilabel"}, from the
`State`{.interpreted-text role="guilabel"} column on the
`Switches`{.interpreted-text role="guilabel"} dashboard.

This `On`{.interpreted-text role="guilabel"} / `Off`{.interpreted-text
role="guilabel"} state automatically routes traffic in a dial plan, in
which this switch is set.

The traffic travels to the `Active`{.interpreted-text role="guilabel"}
route when `On`{.interpreted-text role="guilabel"} is toggled in the
switch. The call traffic travels to the `Inactive`{.interpreted-text
role="guilabel"} route when `Off`{.interpreted-text role="guilabel"} is
toggled in the switch.

Changes can be made on the fly, just be sure to click
`Apply changes`{.interpreted-text role="guilabel"} to implement the
them.

#### Add a switch to dial plan

To add a `Switch`{.interpreted-text role="guilabel"} to a dial plan,
navigate to , and
click on `Dial plans`{.interpreted-text role="guilabel"} in the left
menu. Then, click `Visual Editor`{.interpreted-text role="guilabel"}
next to the desired dial plan to open the
`Dialplan Editor`{.interpreted-text role="guilabel"} pop-up window.

Then, from the `New element`{.interpreted-text role="guilabel"}
drop-down menu, select `Switch`{.interpreted-text role="guilabel"}, and
then click `Add`{.interpreted-text role="guilabel"}. Double-click on the
element to further configure the `Switch`{.interpreted-text
role="guilabel"} element.

{.align-center}

### Multi-switch

A *Multi-Switch* element in Axivox is a switch where multiple paths can
be configured, and switched between.

To configure and set a `Multi-Switch`{.interpreted-text role="guilabel"}
element, navigate to [Axivox management
console](https://manage.axivox.com). Then, click on the
`Switches`{.interpreted-text role="guilabel"} menu item in the left
menu.

Toggle to the `Multi-switch`{.interpreted-text role="guilabel"} tab to
create, or set, a pre-configured `Multi-Switch`{.interpreted-text
role="guilabel"} element.

To create a new `Multi-Switch`{.interpreted-text role="guilabel"}, click
`Create new`{.interpreted-text role="guilabel"}. Then, enter a
`Name`{.interpreted-text role="guilabel"} for the element, and then
enter the `Available choice`{.interpreted-text role="guilabel"}. Enter
one `Available choice`{.interpreted-text role="guilabel"} per line. Do
**not** duplicate any entries.

Remember to click `Save`{.interpreted-text role="guilabel"} when done.

To select the `State`{.interpreted-text role="guilabel"} of the
`Multi-Switch`{.interpreted-text role="guilabel"}, click the drop-down
menu next to the `Multi-Switch`{.interpreted-text role="guilabel"} name,
under the `Multi-switch`{.interpreted-text role="guilabel"} tab on the
`Switches`{.interpreted-text role="guilabel"} dashboard.

The `State`{.interpreted-text role="guilabel"} chosen is the route that
is followed in the dial plan. The `State`{.interpreted-text
role="guilabel"} can be edited on the fly, just be sure to click
`Apply changes`{.interpreted-text role="guilabel"}.

#### Add a multi-switch to dial plan

To add a `Multi-Switch`{.interpreted-text role="guilabel"} element to a
dial plan, navigate to [Axivox management
console](https://manage.axivox.com), and click
`Dial plans`{.interpreted-text role="guilabel"} in the left menu.

Then, select or create a dial plan. Next, click
`Visual Editor`{.interpreted-text role="guilabel"} on the desired dial
plan.

On the `Dialplan Editor`{.interpreted-text role="guilabel"} pop-up
window that appears, click on the `New element`{.interpreted-text
role="guilabel"} drop-down menu, and select
`Multi-Switch`{.interpreted-text role="guilabel"}. Then, click
`Add`{.interpreted-text role="guilabel"}. Double-click on the element to
further configure the `Switch`{.interpreted-text role="guilabel"}
element.

{.align-center}
