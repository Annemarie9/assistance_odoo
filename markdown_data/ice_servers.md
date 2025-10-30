# File: /content/odoo_doc17.0/fr/content/applications/productivity/discuss/ice_servers.md

Configure ICE servers with Twilio
=================================

Odoo Discuss uses WebRTC API and peer-to-peer connections for voice and
video calls. If one of the call attendees is behind a symmetric NAT, you
need to configure an ICE server to establish a connection to the call
attendee. To set up an ICE server, first, create a Twilio account for
video calls, and then, connect that Twilio account to Odoo.

Create a Twilio account
-----------------------

First, go to  and click
`Sign up`{.interpreted-text role="guilabel"} to create a new Twilio
account. Next, enter your name and email address, create a password, and
accept Twilio\'s terms of service. Then, click
`Start your free trial`{.interpreted-text role="guilabel"}. Verify your
email address with Twilio, as per their instructions.

Next, enter your phone number into Twilio. Then, Twilio will send you an
SMS text message containing a verification code. Enter the verification
code into Twilio to verify your phone number.

After that, Twilio redirects to a welcome page. Use the following list
to answer Twilio\'s questions:

-   For `Which Twilio product are you here to use?`{.interpreted-text
    role="guilabel"}, select `Video`{.interpreted-text role="guilabel"}.
-   For `What do you plan to build with Twilio?`{.interpreted-text
    role="guilabel"}, select `Other`{.interpreted-text role="guilabel"}.
-   For `How do you want to build with Twilio?`{.interpreted-text
    role="guilabel"}, select `With no code at all`{.interpreted-text
    role="guilabel"}.
-   For `What is your goal today?`{.interpreted-text role="guilabel"},
    select `3rd party integrations`{.interpreted-text role="guilabel"}.

{.align-center}

If necessary, change the billing country. Finally, click
`Get Started with Twilio`{.interpreted-text role="guilabel"}.

Locate the Twilio Account SID and Auth Token
--------------------------------------------

To locate the Account SID and Auth Token, go to the Twilio account
dashboard. Then, click `Develop`{.interpreted-text role="guilabel"} on
the sidebar. In the `Account Info`{.interpreted-text role="guilabel"}
section, locate the `Account SID`{.interpreted-text role="guilabel"} and
the `Auth Token`{.interpreted-text role="guilabel"}. Both of these are
needed to connect Twilio to Odoo.

{.align-center}

Connect Twilio to Odoo
----------------------

Open the Odoo database and go to
`Settings --> General Settings --> Discuss`{.interpreted-text
role="menuselection"}. Check the box next to
`Use Twilio ICE servers`{.interpreted-text role="guilabel"} and enter
the Twilio account\'s `Account SID`{.interpreted-text role="guilabel"}
and `Auth Token`{.interpreted-text role="guilabel"}. Finally, click
`Save`{.interpreted-text role="guilabel"} to apply these changes.

{.align-center}

Define a list of custom ICE servers
-----------------------------------

This step is not required for the Twilio configuration. However, if
Twilio is not configured or is not working at any given moment, Odoo
will fall back on the custom ICE servers list. The user must define the
list of custom ICE servers.

In `Settings --> General Settings --> Discuss`{.interpreted-text
role="menuselection"}, click the `ICE Servers`{.interpreted-text
role="guilabel"} button under `Custom ICE server list`{.interpreted-text
role="guilabel"}.

{.align-center}

Odoo will redirect to the `ICE servers`{.interpreted-text
role="guilabel"} page. Here you can define your own list of ICE servers.

{.align-center}

::: {.note}
::: {.title}
Note
:::

For on-premise instances of Odoo, the package
[python3-gevent]{.title-ref} is necessary for the Discuss module to run
calls/video calls on Ubuntu (Linux) servers.
:::
