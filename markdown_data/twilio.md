# File: /content/odoo_doc17.0/fr/content/applications/marketing/sms_marketing/twilio.md

SMS via Twilio
==============

What is Twilio
--------------

Twilio is a third-party provider that enables you to send SMS messages
to your clients. Odoo provides an easy way to use this service within
your Odoo apps.

### Why would I need it?

Although Odoo already comes with an out-of-the-box (IAP) solution for
SMS messages, it might not work in some countries with stricter legal
requirements. Currently, Odoo registers itself when possible to avoid
extra setup for its customers, however in some countries that is not
enough and the client itself must do it. This can be done through
Twilio.

Setup your Twilio account
-------------------------

By creating a Twilio account, you will be able to create a virtual phone
number from which you will be able to send SMS messages. These cost
credits that are to be bought on Twilio, not Odoo.

1.  Go to 
2.  Sign up and create a Twilio account
3.  Within your Twilio account, you can create multiple accounts (e.g.
    one for testing, one for each sub-company, etc.)
4.  Create a new account
    1.  Enter the name, and select `Twilio`{.interpreted-text
        role="guilabel"} for the type
    2.  Select your `Billing Country`{.interpreted-text role="guilabel"}
        and click `Create new account`{.interpreted-text
        role="guilabel"}
    3.  Select the different options that match your needs
        -   For the `Twilio product`{.interpreted-text role="guilabel"},
            select `SMS`{.interpreted-text role="guilabel"}
        -   For `How to build with Twilio`{.interpreted-text
            role="guilabel"}, select
            `With no code at all`{.interpreted-text role="guilabel"}
        -   For your `goal`{.interpreted-text role="guilabel"}, select
            `3rd party integrations`{.interpreted-text role="guilabel"}
    4.  Click on `Get Started with Twilio`{.interpreted-text
        role="guilabel"}
5.  You account is now created, and you should arrive on your
    `Dashboard`{.interpreted-text role="guilabel"}
6.  Go to `Phone Numbers --> Manage --> Buy a number`{.interpreted-text
    role="menuselection"}
7.  Buy a number (it is a paying service, but you should have received
    some credits to start with)
8.  Go back to bottom of the `Dashboard`{.interpreted-text
    role="guilabel"} page
9.  Copy the `Account SID`{.interpreted-text role="guilabel"} and
    `Auth Token`{.interpreted-text role="guilabel"}

::: {.important}
::: {.title}
Important
:::

In case of a testing account, you will only be able to send SMS to
phones that you have verified within [Twilio\'s
console](https://console.twilio.com).
:::

::: {.note}
::: {.title}
Note
:::

Sending SMS to some countries (such as the US or Canada) might require a
registration. This can only be done by you, and not by Odoo. Please
check out .
:::

Setup Odoo to use Twilio
------------------------

1.  `Install <general/install>`{.interpreted-text role="ref"} the
    `Twilio SMS`{.interpreted-text role="guilabel"} module
    ([sms\_twilio]{.title-ref})
2.  In Odoo, go to
    `Settings --> General Settings --> Contacts --> Send SMS`{.interpreted-text
    role="menuselection"}, select `Twilio`{.interpreted-text
    role="guilabel"} in the list of options, and save your change.
3.  Go back to that option, and click
    `Manage Twilio Connection`{.interpreted-text role="guilabel"}
4.  Paste the copied credentials accordingly
5.  Click on `Reload numbers`{.interpreted-text role="guilabel"}
6.  Your newly bought phone number should appear in the list
7.  You can use the testing section to send an SMS

You can have multiple numbers (for instance once per country, or one per
campaign), in that case, you can reorder the numbers. By default, when
sending an SMS to a client, Odoo will select the number whose country is
the same as the client. If none matches, Odoo will use the first number
available from the list respecting the order you have chosen.
