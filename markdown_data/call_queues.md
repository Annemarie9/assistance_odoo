# File: /content/odoo_doc17.0/fr/content/applications/productivity/voip/axivox/call_queues.md

Call queues
===========

A call queue is a system that organizes and routes incoming calls. When
customers call a business, and all of the agents are busy, the call
queue lines up the callers in sequential order, based on the time they
called in.

The callers then wait on hold to be connected to the next available call
center agent.

Implementing a call queue system reduces stress for employees, and helps
build brand trust with customers. Many companies use call queues to set
expectations with customers, and to distribute the workload equally
amongst employees.

This document covers the process required to configure call queues (with
advanced settings), as well as how to log into a call queue from the
Odoo database.

::: {.seealso}
`voip/axivox/music_on_hold`{.interpreted-text role="ref"}
:::

Add a queue
-----------

To add a call queue in Axivox, navigate to the [Axivox management
console](https://manage.axivox.com). In the left menu, click
`Queues`{.interpreted-text role="guilabel"}. Next, click
`Add a queue`{.interpreted-text role="guilabel"}. Doing so reveals a
blank `New queue`{.interpreted-text role="guilabel"} form with various
fields to fill out.

### Name

Once the `New queue`{.interpreted-text role="guilabel"} page appears,
enter the `Name`{.interpreted-text role="guilabel"} of the queue.

### Internal extension

Choose an `Internal extension`{.interpreted-text role="guilabel"} for
the queue. This is a number to be dialed by users of the database to
reach the login prompt for the queue.

### Strategy

Next, is the `Strategy`{.interpreted-text role="guilabel"} field. This
field determines the call routing of received calls into this queue.

The following choices are available in the `Strategy`{.interpreted-text
role="guilabel"} drop-down menu:

-   `Call all available agents`{.interpreted-text role="guilabel"}
-   `Calls the agent who has received the call for the longest time`{.interpreted-text
    role="guilabel"}
-   `Calls the agent who has received the least call`{.interpreted-text
    role="guilabel"}
-   `Call a random agent`{.interpreted-text role="guilabel"}
-   `Call agents one after the other`{.interpreted-text role="guilabel"}
-   `Call agents one after the other starting with the first in the list`{.interpreted-text
    role="guilabel"}

Choose a strategy that best meets the company\'s needs for customers in
the queue.

### Maximum waiting time in seconds

In the `Maximum waiting time in seconds`{.interpreted-text
role="guilabel"} field, determine the longest time a customer waits in
the queue before going to a voicemail, or wherever else they are
directed to in a dial plan. Enter a time in seconds.

### Maximum duration of ringing at an agent

In the `Maximum duration of ringing at an agent`{.interpreted-text
role="guilabel"} field, determine the longest time an individual
agent\'s line rings before moving on to another agent, or moving to the
next step in the dial plan. Enter a time in seconds.

::: {.seealso}
For more information on dial plans, visit:

-   `dial_plan_basics`{.interpreted-text role="doc"}
-   `dial_plan_advanced`{.interpreted-text role="doc"}
:::

### Adding agents

The final two fields on the `New queue`{.interpreted-text
role="guilabel"} form revolve around adding agents. Adding
`Static agents`{.interpreted-text role="guilabel"} and
`Dynamic agents`{.interpreted-text role="guilabel"} are two
pre-configured methods for adding agents onto the call queue during the
configuration.

#### Static agents {#voip/axivox/static-agents}

When `Static agents`{.interpreted-text role="guilabel"} are added, these
agents are automatically added to the queue without the need to log in
to receive calls.

#### Dynamic agents {#voip/axivox/dynamic-agents}

When `Dynamic agents`{.interpreted-text role="guilabel"} are added,
these agents have the ability to log into this queue. They are **not**
logged-in automatically, and **must** log in to receive calls.

Be sure to `Save`{.interpreted-text role="guilabel"} the changes, and
click `Apply changes`{.interpreted-text role="guilabel"} in the
upper-right corner to implement the change in production.

Agent connection
----------------

There are three ways call agents can connect to an Axivox call queue:

1.  Dynamic agents connect automatically.
2.  Manager logs in specific agent(s), via the [Axivox management
    console](https://manage.axivox.com).
3.  Agent connects to the queue in Odoo, via the *VoIP* widget.

::: {.seealso}
See the documentation on setting
`voip/axivox/dynamic-agents`{.interpreted-text role="ref"} in the
.
:::

### Connect via Axivox queue

After the initial configuration of the call queue is completed, with the
changes saved and implemented, a manager can log into the [Axivox
management console](https://manage.axivox.com) and connect dynamic
agents to the queue manually.

To connect an agent, click `Queues`{.interpreted-text role="guilabel"},
located in the left-hand column. Doing so reveals the
`Queues`{.interpreted-text role="guilabel"} dashboard, with a few
different columns listed:

-   `Name`{.interpreted-text role="guilabel"}: name of the queue.
-   `Extension`{.interpreted-text role="guilabel"}: number of the
    extension to be dialed to reach the queue.
-   `Agent Connection`{.interpreted-text role="guilabel"}: number to
    dial to log into the queue.
-   `Agent disconnection`{.interpreted-text role="guilabel"}: number to
    dial to log out of the queue.
-   `Connected Agents`{.interpreted-text role="guilabel"}: name of agent
    connected to the queue.

The following buttons are also available on the
`Queues`{.interpreted-text role="guilabel"} dashboard:

-   `Connect an agent`{.interpreted-text role="guilabel"}: manually
    connect an agent to the queue.
-   `Report`{.interpreted-text role="guilabel"}: run a report on the
    queue.
-   `Delete`{.interpreted-text role="guilabel"}: delete the queue.
-   `Edit`{.interpreted-text role="guilabel"}: make changes to the
    settings of the queue.

When agents are connected to the queue, or are live with a customer,
they are displayed under the `Connected Agents`{.interpreted-text
role="guilabel"} column.

If they are static agents, they **always** show up as connected.

Connect an agent by clicking the orange button labeled,
`Connect an agent`{.interpreted-text role="guilabel"}. Then, select the
desired agent\'s name from the drop-down menu, and click
`Connect`{.interpreted-text role="guilabel"}.

![Call queue with connected agents column highlighted and connect an agent and report buttons
highlighted.](call_queues/call-queue.png){.align-center}

::: {.seealso}
For more information on static and dynamic agents, see this
documentation:

-   `voip/axivox/static-agents`{.interpreted-text role="ref"}
-   `voip/axivox/dynamic-agents`{.interpreted-text role="ref"}
:::

#### Report

Click `Report`{.interpreted-text role="guilabel"} to check on the
reporting for a particular queue, in order to see who connected when,
and what phone calls came in and out of the queue. This information is
showcased on a separate `Queue report`{.interpreted-text
role="guilabel"} page, when the green `Report`{.interpreted-text
role="guilabel"} button is clicked.

Reports can be customized by date in the `Period`{.interpreted-text
role="guilabel"} field, and specified in the `From`{.interpreted-text
role="guilabel"} and `to`{.interpreted-text role="guilabel"} fields. The
information can be organized by `Event
type`{.interpreted-text role="guilabel"}, and
`Call ID`{.interpreted-text role="guilabel"}.

When the custom configurations have been entered, click
`Apply`{.interpreted-text role="guilabel"}.

Each report can be exported to a
`CSV (comma separated value)`{.interpreted-text role="abbr"} file for
further use and analysis, via the `Export to CSV`{.interpreted-text
role="guilabel"} button.

When the `Event type`{.interpreted-text role="guilabel"} field is
clicked, a drop-down menu appears with the following options:

-   `The caller quit`{.interpreted-text role="guilabel"}
-   `An agent is connecting`{.interpreted-text role="guilabel"}
-   `An agent is disconnecting`{.interpreted-text role="guilabel"}
-   `The call was terminated (agent hangs up)`{.interpreted-text
    role="guilabel"}
-   `The call was terminated (caller hangs up)`{.interpreted-text
    role="guilabel"}
-   `The caller is connected to an agent.`{.interpreted-text
    role="guilabel"}
-   `Someone is entering the queue`{.interpreted-text role="guilabel"}
-   `The caller exits the queue (no agent is connected)`{.interpreted-text
    role="guilabel"}
-   `The caller exits the queue (timeout)`{.interpreted-text
    role="guilabel"}
-   `No one is answering`{.interpreted-text role="guilabel"}
-   `No one is answering, the caller hangs up`{.interpreted-text
    role="guilabel"}
-   `Transfer`{.interpreted-text role="guilabel"}
-   `Blind Transfer`{.interpreted-text role="guilabel"}

{.align-center}

There is no limit to how many options can be selected from the
`Event type`{.interpreted-text role="guilabel"} drop-down menu.

Clicking `Check all`{.interpreted-text role="guilabel"} selects all the
available options from the drop-down menu, and clicking
`Uncheck all`{.interpreted-text role="guilabel"} removes all selections
from the drop-down menu.

To select an individual `Event type`{.interpreted-text role="guilabel"},
click on the desired option in the drop-down menu.

{.align-center}

### Connect to queue on Odoo

Dynamic agents can connect manually to the Axivox call queue from the
Odoo *VoIP* widget, once the *VoIP* app is configured for the individual
user in Odoo.

::: {.seealso}
`axivox_config`{.interpreted-text role="doc"}
:::

To access the Odoo *VoIP* widget, click the
`☎️ (phone)`{.interpreted-text role="guilabel"} icon in the upper-right
corner of the screen, from any window within Odoo.

::: {.seealso}
For more information on the Odoo *VoIP* widget, see this documentation:
`../voip_widget`{.interpreted-text role="doc"}
:::

For an agent to connect to the call queue, simply dial the
`Agent connection`{.interpreted-text role="guilabel"} number, and press
the green call button `📞 (phone)`{.interpreted-text role="guilabel"}
icon in the *VoIP* widget. Then, the agent hears a short, two-second
message indicating the agent is logged in. The call automatically ends
(disconnects).

To view the connected agents in a call queue, navigate to the [Axivox
management console](https://manage.axivox.com), and click
`Queues`{.interpreted-text role="guilabel"}, located in the left-hand
column.

Then, click the green `Refresh`{.interpreted-text role="guilabel"}
button at the top of the `Connected agents`{.interpreted-text
role="guilabel"} column. Any agent (static or dynamic) that is connected
to the queue currently, appears in the column next to the queue they are
logged into.

To log out of the queue, open the Odoo *VoIP* widget, dial the
`Agent disconnection`{.interpreted-text role="guilabel"} number, and
press the green call button `📞 (phone)`{.interpreted-text
role="guilabel"} icon. The agent is disconnected from the queue after a
short, two-second message.

To manually log a dynamic agent out of a call queue, navigate to the
, and click
`Queues`{.interpreted-text role="guilabel"}, located in the left-hand
column. Then, click the green `Refresh`{.interpreted-text
role="guilabel"} button at the top of the
`Connected agents`{.interpreted-text role="guilabel"} column.

To disconnect an agent manually, click the red
`Disconnect`{.interpreted-text role="guilabel"} button, and they are
immediately disconnected. This can be helpful in situations where agents
forget to log out at the end of the day.
