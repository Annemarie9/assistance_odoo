# File: /content/odoo_doc17.0/fr/content/applications/productivity/whatsapp.md

WhatsApp
========

**WhatsApp** is an instant messaging and voice-over-IP app that allows
users to send messages, make calls, and share content. Businesses can
use [WhatsApp
Business](https://developers.facebook.com/products/whatsapp/) to
communicate with their customers by text, send documents and provide
support.

::: {.warning}
::: {.title}
Warning
:::

WhatsApp is an Odoo Enterprise-only application that does not work in
Odoo Community edition. To sign up for Odoo Enterprise edition, click
here: .
:::

::: {.seealso}
For more information on migrating from Odoo Community version to Odoo
Enterprise version see this documentation:
`/administration/on_premise/community_to_enterprise`{.interpreted-text
role="doc"}.
:::

With the **Odoo WhatsApp** app, a company can connect a WhatsApp
Business Account (WABA) to an Odoo database, which allows for the
following:

-   Receive and reply to WhatsApp messages directly from an Odoo
    database
-   Create new templates with dynamic placeholders/variables
-   Send pre-approved templates that use dynamic variables, such as:
    -   Quotations from the Sales app
    -   Receipts and invoices from the Point of Sale app
    -   Tickets from the Events app

::: {.seealso}
\- [Meta Business: create message templates for the WhatsApp Business
account](https://www.facebook.com/business/help/2055875911147364). -
[Meta Business: connect a phone number to the WhatsApp Business
account](https://www.facebook.com/business/help/456220311516626). -
[Meta Business: change the WhatsApp Business display
name](https://www.facebook.com/business/help/378834799515077).
:::

WhatsApp is a messaging service operated by Meta, which is the parent
company of Facebook. WhatsApp is commonly used as a communication tool
in many countries and by many businesses. This documentation will cover
the integration of a WhatsApp Business Account with Odoo. The company\'s
Meta account is configured in Odoo via an
`API (Application Programming Interface)`{.interpreted-text role="abbr"}
connection.

The WhatsApp connector supports two flows: company initiated, and
customer initiated. A company can initiate a discussion by sending a
template to one or more people. Once the template is sent, the recipient
can answer in order to trigger a discussion between the sender and the
receiver (a *Discuss* chat window will pop up if the customer answers
within 15 days).

If the discussion is initiated by the client (e.g. by sending to the
company\'s public WhatsApp number), then Odoo will open a group chat
with all operators responsible for this WhatsApp channel.

::: {.tip}
::: {.title}
Tip
:::

It is recommended to set up multiple WhatsApp accounts for different
departments. For example, the help desk team and sales teams can chat on
different channels.
:::

WhatsApp configuration in a Meta
--------------------------------

A WhatsApp integration with Odoo uses a standard
`API (Application Programming Interface)`{.interpreted-text role="abbr"}
connection, and is configured on Meta in the following steps:

1.  Create a Meta business account
2.  Create a Meta developer account
3.  Setup an *app* and WhatsApp *product* on Meta\'s developer console
4.  Test the API connection.

Once connected, messages are then sent and received through Odoo\'s
*Discuss* application using the WhatsApp
`API (Application Programming Interface)`{.interpreted-text
role="abbr"}.

### Meta business account setup

To create a Business account with Meta (owner of Facebook) navigate to:
.
Begin by clicking `Create account`{.interpreted-text role="guilabel"}
and then enter the business name, the administrator\'s name, and a work
email address. Then click `Next`{.interpreted-text role="guilabel"}, and
a pop-up window will appear prompting to confirm the email address.
After confirming, click `Done`{.interpreted-text role="guilabel"} to
close the window.

Next, follow the instructions in the email sent by Facebook to confirm
the creation of the business account and to complete the setup process.

::: {.seealso}
[Set up a Meta business
account](https://www.facebook.com/business/help/1710077379203657?id=180505742745347).
:::

::: {.important}
::: {.title}
Important
:::

If the business account is linked to a personal Facebook account then
the administrator must toggle between the personal account to the
business account for the remainder of the configuration.

To toggle to the business account navigate to the [Facebook Developer
Console](https://developers.facebook.com) and click on the *account
name* in the upper right corner. Under the
`Business Accounts`{.interpreted-text role="guilabel"} heading, click on
the desired business that the WhatsApp configuration should take place
in. This will be the account for which Odoo will send and receive
WhatsApp messages.

{.align-center}
:::

::: {.important}
::: {.title}
Important
:::

In order to create a Meta business account, the user must already have a
personal Facebook account that has existed for a minimum of one hour
prior to setting up the Facebook Business account. Trying to create the
business account prior to this time will result in an error.
:::

### App creation

On the  dashboard,
sign in with the Meta developer account. If no account is configured
yet, link a Facebook account to create a Meta developer account.

::: {.note}
::: {.title}
Note
:::

A Facebook *developer* account is different than a Facebook *business*
account. While developer accounts are made up of personal Facebook
accounts, business accounts are **not** as they represent a business and
manage all of the business\'s assets in Meta, such as apps.
:::

::: {.seealso}
[Set up the WhatsApp Business
Platform](https://www.facebookblueprint.com/student/collection/409587/path/360218).
:::

Click on `My Apps`{.interpreted-text role="guilabel"} in the top right
corner after successfully signing in to the Meta developer account. This
will redirect the administrator to all the apps the developer has
configured in this specific developer account. Click on
`Create App`{.interpreted-text role="guilabel"} to begin the process of
configuring a new Meta application.

### App type

On the `Create an app`{.interpreted-text role="menuselection"} page,
select `Other`{.interpreted-text role="guilabel"} under the section
labeled, `Looking for something else?`{.interpreted-text
role="guilabel"}, and then click `Next`{.interpreted-text
role="guilabel"} to be directed to another page in order to select the
app type. Then, click on the first option listed under the
`Select an app type`{.interpreted-text role="guilabel"} label, titled
`Business`{.interpreted-text role="guilabel"}. This selection allows for
the creation and management of the WhatsApp
`API (Application Programming Interface)`{.interpreted-text
role="abbr"}.

Now, click `Next`{.interpreted-text role="guilabel"} to configure the
app, as desired. When the app *type* has been configured, the
administrator will move onto the app *details* section.

### App details

On the `Details`{.interpreted-text role="guilabel"} section of the
`Create an app`{.interpreted-text role="guilabel"} process, enter
[Odoo]{.title-ref} in the field under the
`Add an app name`{.interpreted-text role="guilabel"} label.

::: {.note}
::: {.title}
Note
:::

The app name can be changed at a later time in the settings, if
necessary.
:::

::: {.warning}
::: {.title}
Warning
:::

Trademarks and branded elements may not be used in this text section.
These include the Meta group of companies. Do not include the word:
[WhatsApp]{.title-ref} or the system will flag this in error.
:::

Next, enter the developer email address in the field under the
`App contact email`{.interpreted-text role="guilabel"} label.

Lastly, set the `Business Account - Optional`{.interpreted-text
role="guilabel"} field to the Meta business account profile, using the
drop-down menu. To finish, click `Create app`{.interpreted-text
role="guilabel"}. This action will create the app and prompts the *Meta
Platform Terms* and *Developer Policies* agreements.

To accept the agreements, enter the Facebook password for security
purposes, and click `Submit`{.interpreted-text role="guilabel"} to
finalize the app creation. The browser will then direct to the `Meta
for Developers`{.interpreted-text role="guilabel"} dashboard.

::: {.note}
::: {.title}
Note
:::

If the Meta business account is prohibited from advertising, claiming an
app won\'t be allowed. To resolve this issue navigate to
<https://business.facebook.com/business> for assistance.

For more information, see [Meta\'s documentation on advertising
restrictions](https://www.facebook.com/business/help/975570072950669).
:::

### Add a WhatsApp product to the app

Now that the basic structure of the app has been created, a product will
need to be added to the app. Begin by accessing the Meta app dashboard
by navigating to <https://developers.facebook.com/apps>, and clicking on
the app that is being configured.

On the next page: since WhatsApp will be used, click
`Set up`{.interpreted-text role="guilabel"} next to the box containing
WhatsApp, located towards the bottom of the page.

::: {.seealso}
[Meta\'s WhatsApp developer
documentation](https://developers.facebook.com/docs/whatsapp/).
:::

The page then directs to the configuration page for the
`WhatsApp Business Platform API`{.interpreted-text role="guilabel"}. Use
the drop-down menu to select the Meta business to be configured for the
`Select a Meta
Business Account`{.interpreted-text role="guilabel"} option, and then
click `Continue`{.interpreted-text role="guilabel"} to confirm the
selection.

::: {.note}
::: {.title}
Note
:::

When `Continue`{.interpreted-text role="guilabel"} is clicked, the
administrator agrees to Meta\'s terms and conditions as linked on the
`Meta App Dashboard`{.interpreted-text role="guilabel"}.
:::

::: {.note}
::: {.title}
Note
:::

Once the WhatsApp product is added to the app, Meta will provide a
WhatsApp test phone number with 5 test messages.
:::

### Start using the WhatsApp API

After finishing the previous WhatsApp product wizard, and clicking
`Continue`{.interpreted-text role="guilabel"}, the browser should have
directed to the WhatsApp `Quickstart`{.interpreted-text role="guilabel"}
page; this `Quickstart`{.interpreted-text role="guilabel"} page is where
to begin configuring the WhatsApp API by adding a phone number and then
sending an initial test message.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If the browser isn\'t on the `Quickstart`{.interpreted-text
role="guilabel"} page for WhatsApp, navigate to
<https://developers.facebook.com/apps> and click on the app that is
being configured, (the app name is [Odoo]{.title-ref} if the
instructions above were followed).

Then, in the menu on the left-hand side of the page, click the
`v (menu toggle)`{.interpreted-text role="guilabel"} icon next to the
`WhatsApp`{.interpreted-text role="guilabel"} section heading. A small
menu will open, containing the following options:

-   `Quickstart`{.interpreted-text role="guilabel"}
-   `API Setup`{.interpreted-text role="guilabel"}
-   `Configuration`{.interpreted-text role="guilabel"}

Click the `Quickstart`{.interpreted-text role="guilabel"} option, and
then click `Start using the API`{.interpreted-text role="guilabel"}.
:::

#### API Setup

After clicking on `Start using the API`{.interpreted-text
role="guilabel"}, the page navigates to the
`API Setup`{.interpreted-text role="guilabel"}. Now that the test number
has been created, a test message can be sent to confirm that WhatsApp is
working properly. To begin, navigate to the section on the page labeled
`Send and receive
messages`{.interpreted-text role="guilabel"} and click the drop-down
menu next to `To`{.interpreted-text role="guilabel"}, under
`Step 1 Select phone
numbers`{.interpreted-text role="guilabel"}.

Now, select the only option available:
`Manage phone number list`{.interpreted-text role="guilabel"}. Follow
the steps and add up to five numbers to send the free test messages to.
After entering the appropriate country code and phone number, click on
`Next`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

Adding a phone number to send to in this step will allow for a
successful test to be sent by the terminal. This is critical to ensure
the WhatsApp `API (Application Programming Interface)`{.interpreted-text
role="abbr"} is working.
:::

A verification code from WhatsApp Business is then sent to the phone
number, which needs to be input on the next screen to verify ownership
of the number. Enter the verification code and click
`Next`{.interpreted-text role="guilabel"} to verify the number.

#### Send a test message via terminal

Next, send a test message via the terminal. Under the section labeled
`Step 2 Send
messages with the API`{.interpreted-text role="guilabel"}, click
`Send Message`{.interpreted-text role="guilabel"}. A test message will
then be sent to the phone number that was set in the previous section.

Upon successfully receiving the message to the number, move onto the
next section to produce and configure webhooks.

WhatsApp configuration in Odoo {#productivity/whatsapp/webhooks}
------------------------------

The next steps configured in this section are all within the Odoo
database. A few different values for a token, phone number, and account
IDs all need to be configured in Odoo; these values are necessary in
order to create a `Callback URL`{.interpreted-text role="guilabel"} and
`Webhook Verify Token`{.interpreted-text role="guilabel"}, which are
then used to configure the webhooks (in order to receive messages back
into the database).

In Odoo, navigate to
`WhatsApp app --> Configuration --> WhatsApp Business Accounts`{.interpreted-text
role="menuselection"}. Then click `New`{.interpreted-text
role="guilabel"} to configure the WhatsApp business account in Odoo.

In another browser tab, navigate to
`https://developers.facebook.com --> My Apps -->
WhatsApp --> API Configuration`{.interpreted-text role="menuselection"},
and then copy the following values from the Meta developer console into
the corresponding fields in Odoo:

  Name         Meta Console                                                        Odoo Interface
  ------------ ------------------------------------------------------------------- ------------------------------------------------------
  Phone        `Phone number ID`{.interpreted-text role="guilabel"}                `Phone Number ID`{.interpreted-text role="guilabel"}
  Token        `Temporary access token`{.interpreted-text role="guilabel"}         `Access Token`{.interpreted-text role="guilabel"}
  App ID       `App ID`{.interpreted-text role="guilabel"}                         `App ID`{.interpreted-text role="guilabel"}
  Account ID   `WhatsApp Business Account ID`{.interpreted-text role="guilabel"}   `Account ID`{.interpreted-text role="guilabel"}

To retrieve the `App Secret`{.interpreted-text role="guilabel"},
navigate to the Meta developer console,
<https://developers.facebook.com/apps> and select the app that Odoo is
being configured in. Then in the left-side menu, under
`App settings`{.interpreted-text role="guilabel"}, select
`Basic`{.interpreted-text role="guilabel"}.

Next, click `Show`{.interpreted-text role="guilabel"} next to the field
`App secret`{.interpreted-text role="guilabel"}, and enter the account
password to verify ownership. Copy the `App secret`{.interpreted-text
role="guilabel"} and then paste that copied value into the
`App Secret`{.interpreted-text role="guilabel"} field on the Odoo
`WhatsApp Business Account`{.interpreted-text role="guilabel"}
configuration dashboard.

To complete the setup of the WhatsApp business account in Odoo, click
`Test Connection`{.interpreted-text role="guilabel"}. A successful
message in green will populate in the upper-right corner of the
dashboard if the configuration is set correctly.

### Configuring webhooks

To configure the webhooks for WhatsApp in Odoo, navigate to
<https://developers.facebook.com/apps> and select the app that Odoo is
being configured in. Next under the `WhatsApp`{.interpreted-text
role="guilabel"} menu heading on the left side of the screen, click on
the `API Setup`{.interpreted-text role="guilabel"} menu item. Finally go
to the section marked `Step 3: Configure
webhooks to receive messages`{.interpreted-text role="guilabel"} and
click on `Configure webhooks`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Another way to configure *Webhooks* is to navigate to
<https://developers.facebook.com/apps> and select the app that Odoo is
being configured in. Then select `Webhooks`{.interpreted-text
role="guilabel"} in the left hand menu.

{.align-center}
:::

On the `Webhook configuration`{.interpreted-text role="menuselection"}
page, click on `Edit`{.interpreted-text role="guilabel"}, where both the
`Callback URL`{.interpreted-text role="guilabel"} and
`Webhook Verify Token`{.interpreted-text role="guilabel"} values from
the Odoo will be added.

::: {.note}
::: {.title}
Note
:::

Both the `Callback URL`{.interpreted-text role="guilabel"} and
`Webhook Verify Token`{.interpreted-text role="guilabel"} values were
automatically populated after clicking on
`Test Connection`{.interpreted-text role="guilabel"} in the previous
step.
:::

In a separate browser window, retrieve the necessary values in Odoo by
navigating to
`WhatsApp app --> Configuration --> WhatsApp Business Accounts`{.interpreted-text
role="menuselection"} and select the account that is being configured.
Locate the values under the section labeled `Receiving
Messages`{.interpreted-text role="guilabel"}.

Copy and paste the `Callback URL`{.interpreted-text role="guilabel"}
from Odoo into the `Callback URL`{.interpreted-text role="guilabel"}
field in Meta. Similarly, copy and paste the
`Webhook Verify Token`{.interpreted-text role="guilabel"} into the
`Verify
Token`{.interpreted-text role="guilabel"} field on the Meta developer
console, as well.

Finally, click `Verify and save`{.interpreted-text role="guilabel"} to
record the values in the Meta developer console.

#### Webhook fields

Now input individual webhook fields into Meta\'s developer console,
under the `Webhook
fields`{.interpreted-text role="guilabel"} section. Click
`Manage`{.interpreted-text role="guilabel"} and when the pop-up window
appears, check the boxes in the `Subscribe`{.interpreted-text
role="guilabel"} column for the following *field names*:

-   account\_update
-   message\_template\_quality\_update
-   message\_template\_status\_update
-   messages
-   template\_category\_update

After making the selections, click `Done`{.interpreted-text
role="guilabel"}.

The finished `Webhooks`{.interpreted-text role="guilabel"} configuration
will appear like this in the Meta developer console:

{.align-center}

::: {.important}
::: {.title}
Important
:::

The `Webhook fields`{.interpreted-text role="guilabel"} will only appear
once the subscription is confirmed using the
`Callback URL`{.interpreted-text role="guilabel"} and
`Webhook Verify Token`{.interpreted-text role="guilabel"}.
:::

::: {.seealso}
[Meta\'s WhatsApp documentation on setting
webhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/set-up-webhooks).
:::

#### Add phone number

To configure the phone number to use for WhatsApp in Odoo, navigate back
to the Meta developer console (<https://developers.facebook.com/apps>)
and again select the app that Odoo is being configured in. Under the
`WhatsApp`{.interpreted-text role="guilabel"} menu heading on the left
side of the screen, click on the `API Setup`{.interpreted-text
role="guilabel"} menu item. From there, go to the section marked:
`Step 5: Add a
phone number`{.interpreted-text role="guilabel"}, and click on
`Add phone number`{.interpreted-text role="guilabel"}.

In the fields, enter a `Business name`{.interpreted-text
role="guilabel"} as well as a `Business website or profile
page`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

The `Business website or profile page`{.interpreted-text
role="guilabel"} field can be a social media page\'s `URL
(Uniform Resource Locator)`{.interpreted-text role="abbr"}.
:::

Complete filling out the business information by next selecting the
country that the company does business in from the drop-down menu in the
`Country`{.interpreted-text role="guilabel"} section. Add an address if
desired, however, this information is optional. After adding the
location, click `Next`{.interpreted-text role="guilabel"} to continue.

The following page contains information for the
`WhatsApp Business profile`{.interpreted-text role="guilabel"}. Complete
the following sections, accordingly:

-   `WhatsApp Business Profile Display Name`{.interpreted-text
    role="guilabel"}
-   `Timezone`{.interpreted-text role="guilabel"}
-   `Category`{.interpreted-text role="guilabel"}
-   `Business description`{.interpreted-text role="guilabel"} (optional)

Once these sections are complete, click `Next`{.interpreted-text
role="guilabel"}. The page refreshes and then prompts the administrator
to `Add a phone number for WhatsApp`{.interpreted-text role="guilabel"}
in the respective field. Here, enter the phone number to configure in
WhatsApp.

::: {.seealso}
[Migrate an Existing WhatsApp Number to a Business Account
\<https://developers.facebook.com/docs/whatsapp/cloud-api/get-started/migrate-existing-whatsapp-
number-to-a-business-account\>]().
:::

Next, choose a verification method for the phone number. Select either
`Text message`{.interpreted-text role="guilabel"} or
`Phone call`{.interpreted-text role="guilabel"}, and then click
`Next`{.interpreted-text role="guilabel"} proceed.

The phone number entered will receive either a text or a phone call by
WhatsApp with a code, depending on the verification method chosen. Enter
that verification code into the `Verification code`{.interpreted-text
role="guilabel"} field and click `Next`{.interpreted-text
role="guilabel"} to finish.

::: {.warning}
::: {.title}
Warning
:::

If a payment method hasn\'t been added this will be necessary to
proceed. [Visit Meta\'s documentation on how to add a payment method in
Meta\'s Business
Manager](https://www.facebook.com/business/help/915454841921082?id=180505742745347).
This is part of Meta\'s fraud detection system, in order to ensure that
the account/company are real a payment method is required to proceed.
:::

::: {.seealso}
[Meta for Developers: Add a Phone
Number](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started/add-a-phone-number).
:::

#### Permanent token {#productivity/whatsapp/token}

After configuration and testing are complete, a permanent token should
be created to replace the `Temporary token`{.interpreted-text
role="guilabel"}.

::: {.seealso}
[Meta for Developers: System User Access Tokens
\<https://developers.facebook.com/docs/whatsapp/business-management-api/get-started\#system-user-
access-tokens\>]().
:::

Begin by navigating to <https://business.facebook.com/> and then go to
`Business
settings --> User --> System Users`{.interpreted-text
role="menuselection"}. Select an existing system user or create a new
system user by clicking on `Add`{.interpreted-text role="guilabel"}.

Assets now must be added to the system user and then a permanent token
can be generated.

Click on `Add assets`{.interpreted-text role="guilabel"}, and when the
pop-up window appears select `Apps`{.interpreted-text role="guilabel"}
under the `Select asset type`{.interpreted-text role="guilabel"}. Then,
select the Odoo app and toggle the permissions to *On* under the
`Full control`{.interpreted-text role="guilabel"} option. Set this new
permission setting by clicking `Save Changes`{.interpreted-text
role="guilabel"}, to which a confirmation window will appear,
acknowledging the addition of the asset to the system user. Finish by
clicking `Done`{.interpreted-text role="guilabel"}.

Next, the permanent token will be generated. Click on
`Generate new token`{.interpreted-text role="guilabel"}, and a pop-up
window will appear asking which app this token should be generated for.
Select the `App`{.interpreted-text role="guilabel"} that this token is
for. Then determine the expiration date of either
`60 days`{.interpreted-text role="guilabel"} or
`Never`{.interpreted-text role="guilabel"}.

Finally, when Meta asks which permissions should the system user allow,
add all of the following permissions:

-   WhatsApp\_business\_messaging
-   WhatsApp\_business\_management

When permissions are set, click `Generate token`{.interpreted-text
role="guilabel"}. Copy the token value that populates on the screen that
follows.

With that token value, update the `Access Token`{.interpreted-text
role="guilabel"} field in the WhatsApp business account in Odoo by
navigating to `WhatsApp app --> Configuration --> WhatsApp Business
Accounts`{.interpreted-text role="menuselection"}.

Go live with the Meta app
-------------------------

Finally, to launch the app, the Meta app must be set to
`Live`{.interpreted-text role="guilabel"} in the Meta developer console.
Navigate to <https://developers.facebook.com/apps> and click on the app
that is being configured. In the top menu, toggle the
`App Mode`{.interpreted-text role="guilabel"} field from
`Development`{.interpreted-text role="guilabel"} to
`Live`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

If the app status is not set to *live*, then the database will only be
able to contact the test numbers specified in the developer console.
:::

::: {.warning}
::: {.title}
Warning
:::

A privacy policy URL must be set in order for the app to be set to live.
Go to the Meta developer console, <https://developers.facebook.com/apps>
and select the app that Odoo is being configured in. Then, using the
menu on the left side of the screen, go to `App
Settings --> Basic`{.interpreted-text role="menuselection"}. Then, enter
the privacy policy hyperlink address under the
`Privacy Policy URL`{.interpreted-text role="guilabel"} field of the
form. Click `Save changes`{.interpreted-text role="guilabel"} to apply
the privacy policy to the app.
:::

Once the app has gone live in the Meta developer console, a confirmation
email is sent to the administrator.

WhatsApp templates {#productivity/whatsapp/templates}
------------------

WhatsApp templates are saved messages that are used repeatedly to send
messages from the database. They allow users to send quality
communications, without having to compose the same text repeatedly.

Creating different templates that are tailored to specific situations
lets users choose the right message for the right audience. This
increases the quality of the message and the overall engagement rate
with the customer.

WhatsApp templates can be created on both the Odoo and Meta consoles.
The following process will overview the process for creating templates
in Odoo and then afterward in Meta.

::: {.important}
::: {.title}
Important
:::

WhatsApp has an approval process that must be completed before the
template can be used. `productivity/whatsapp/approval`{.interpreted-text
role="ref"}.
:::

### Creating templates in Odoo {#WhatsApp/templates}

To access and create WhatsApp templates, begin by navigating to the
`WhatsApp app -->
Templates`{.interpreted-text role="menuselection"} dashboard.

At the bottom of an individual template\'s form, there are three tabs:
`Body`{.interpreted-text role="guilabel"}, `Buttons`{.interpreted-text
role="guilabel"}, and `Variables`{.interpreted-text role="guilabel"};
these three tabs combined create the WhatsApp template.

The text is entered into the `Body`{.interpreted-text role="guilabel"}
tab, and dynamic content that is called out in the
`Body`{.interpreted-text role="guilabel"} tab is specified in the
`Variables`{.interpreted-text role="guilabel"} tab. Every piece of
dynamic content (e.g., placeholders) in the message (body) is
specifically called out and specified in the
`Variables`{.interpreted-text role="guilabel"} tab.

Templates are prefabricated layouts that allow users to send
professional looking messages to customers. These templates are capable
of containing dynamic data that will populate in the end message using
variables that are set in the template configuration. For example,
messages can contain the end user\'s name, call out specific products,
or reference a sales order, to name a few convenient and impactful
variables.

To create a WhatsApp template, go to the
`WhatsApp app --> Templates`{.interpreted-text role="menuselection"}
dashboard and click `New`{.interpreted-text role="guilabel"}. On the
form, enter a `Name`{.interpreted-text role="guilabel"} for the
template, and select a `Language`{.interpreted-text role="guilabel"}.

::: {.important}
::: {.title}
Important
:::

In order to complete this next task, administrator access rights are
needed to edit the `Applies to`{.interpreted-text role="guilabel"}
field. See this `access rights documentation
<../general/users/access_rights>`{.interpreted-text role="doc"} for more
information.
:::

In the `Account`{.interpreted-text role="guilabel"} drop-down menu,
select the *WhatsApp business account* in Odoo that this template should
link to. Next, under the `Applies to`{.interpreted-text role="guilabel"}
field select the *model* the server action will apply to for this
template.

::: {.tip}
::: {.title}
Tip
:::

These models can also be accessed in
`developer mode <developer-mode>`{.interpreted-text role="ref"}. On a
contact form (or similar relevant form in Odoo), navigate to the model
that will be referenced, and hover over any field name. A box of backend
information will reveal itself with the specific Odoo
`Model`{.interpreted-text role="guilabel"} name in the backend. Search
(using the front-end name) for this model in the
`Applies to`{.interpreted-text role="guilabel"} drop-down menu in the
WhatsApp template.
:::

::: {.warning}
::: {.title}
Warning
:::

Often when changing the model or `Applies to`{.interpreted-text
role="guilabel"} field, the `Phone Field`{.interpreted-text
role="guilabel"} may produce an error The
`Phone Field`{.interpreted-text role="guilabel"} should always be set to
the [Phone]{.title-ref} or [Mobile]{.title-ref} model.
:::

To search available fields, type in the front-end name in the
`Search...`{.interpreted-text role="guilabel"} box. This will find a
result from all of the available fields for the model
(`Applies to`{.interpreted-text role="guilabel"}) that the template is
created for.

::: {.note}
::: {.title}
Note
:::

In order to find specific fields, multiple levels may need to be
navigated in the search results box. Use the
`> (right chevron)`{.interpreted-text role="guilabel"} and
`⬅️ (left arrow)`{.interpreted-text role="guilabel"} icons to navigate
between the menu levels.
:::

{.align-center}

Change the `Category`{.interpreted-text role="guilabel"} to fit either a
`Marketing`{.interpreted-text role="guilabel"},
`Utility`{.interpreted-text role="guilabel"}, or
`Authentication`{.interpreted-text role="guilabel"} category. In most
instances the first two options will be used, unless the user would like
to send a password reset or something security related. Set to
`Marketing`{.interpreted-text role="guilabel"} should there be anything
promotional being sent and set to `Utility`{.interpreted-text
role="guilabel"} should there be general transactional messages being
sent (i.e., sales order, event ticket, etc).

::: {.important}
::: {.title}
Important
:::

Specifying an incorrect category can cause a flag/rejected status from
Meta during the approval process.
:::

Add any `Users`{.interpreted-text role="guilabel"} that are allowed to
use this template. In the right-side column, a
`Header type`{.interpreted-text role="guilabel"} can be configured along
with a `Header message`{.interpreted-text role="guilabel"}, as well.

The available `Header types`{.interpreted-text role="guilabel"} are as
follows:

-   Text
-   Image
-   Video
-   Document
-   Location (variables need to be set)

Navigate to the `Body`{.interpreted-text role="guilabel"} tab to
configure the main message of the template.

When all the necessary changes are made to the template, click on the
`Submit for
approval`{.interpreted-text role="guilabel"} button in the upper-left
corner. This will cause the status of the template to change to
`Pending`{.interpreted-text role="guilabel"}.

The status will remain in `Pending`{.interpreted-text role="guilabel"}
until a decision has been made by Meta, whereby a confirmation email
will then be sent indicating that the template has been approved (or
rejected). The templates will then need to be synced from the Odoo
database.

See this section for more information on
`syncing templates <productivity/whatsapp/sync>`{.interpreted-text
role="ref"}.

::: {.tip}
::: {.title}
Tip
:::

There are pre-configured demo data templates available in Odoo to use or
modify. These templates can be used as-is or modified to suit a specific
business need.

To use these templates, navigate to
`WhatsApp app --> Templates`{.interpreted-text role="menuselection"} and
select a pre-configured template. Click
`Submit for Approval`{.interpreted-text role="guilabel"} to start the
approval process. An email will be sent to the administrator of the Meta
account when the template has been approved.
:::

#### Buttons

Buttons can be added into the message from the
`Buttons`{.interpreted-text role="guilabel"} tab. Enter the
`Type`{.interpreted-text role="guilabel"} (either
`Visit Website`{.interpreted-text role="guilabel"},
`Call Number`{.interpreted-text role="guilabel"}, or
`Quick Reply`{.interpreted-text role="guilabel"}), and then specify the
`Button Text`{.interpreted-text role="guilabel"},
`Call Number`{.interpreted-text role="guilabel"} or
`Website URL`{.interpreted-text role="guilabel"} (including
`Url Type`{.interpreted-text role="guilabel"}), depending on the
`Type`{.interpreted-text role="guilabel"} of button.

::: {.note}
::: {.title}
Note
:::

Buttons can also be added on the Meta business console. See Meta\'s
WhatsApp template dashboard by navigating to
<https://business.facebook.com/wa/manage/home>. Then go to
`Account tools --> Message templates`{.interpreted-text
role="menuselection"}.
:::

#### Using placeholders and variables

Dynamic variables reference certain fields within the Odoo database to
produce unique data in the WhatsApp message when using a template.
Dynamic variables are encoded to display fields from within the
database, referencing fields from within a model.

::: {.example}
Many companies like to customize their WhatsApp messages with a
personalized piece of customer information to grab attention. This can
be accomplished in Odoo by referencing a field within a model by setting
a dynamic variable. For example, a customer\'s name can be referenced in
the email from the `Customer`{.interpreted-text role="guilabel"} field
on the `Sales Order`{.interpreted-text role="guilabel"} model.
:::

{.align-center}

Dynamic variables can be added in to the `Body`{.interpreted-text
role="guilabel"} by adding `placeholders`{.interpreted-text
role="guilabel"} in the *text*. To add a placeholder in the *message
body* enter the following text [{{1}}]{.title-ref}. For the second
placeholder enter [{{2}}]{.title-ref} and increase incrementally as more
placeholders are added to the text.

::: {.example}
*The following is the text from payment receipt template body:*

Dear {{1}},

| Here is your invoice *{{2}}* from *{{3}}* for a total of *{{4}}{{5}}*.
| To review your invoice or pay online: {{6}}

Thank you
:::

::: {.seealso}
`productivity/whatsapp/templates`{.interpreted-text role="ref"}.
:::

These placeholders must be configured on the
`Variables`{.interpreted-text role="guilabel"} tab of the template
before submitting for approval from Meta. To edit the dynamic variables
on a template, first change the `Type`{.interpreted-text
role="guilabel"} to `Field of Model`{.interpreted-text role="guilabel"}.
This allows Odoo to reference a field within a model to produce unique
data in the message being sent.

Next, edit the `Field`{.interpreted-text role="guilabel"} of the dynamic
variables. The `Applies to`{.interpreted-text role="guilabel"} field in
the template should be edited prior to ensure the correct model and
field are referenced.

To search the available fields, type in the front-end name of the field
in the search box. This will find a result from all of the available
fields for the model (`Applies to`{.interpreted-text role="guilabel"})
that the template is created for. There may be multiple levels that need
to be configured.

::: {.example}
The following is an example of the variables set for the above
placeholders in the payment receipt noted above:

  Name           Sample Value     Type             Field
  -------------- ---------------- ---------------- ----------------------------------
  body - {{1}}   Azure Interior   Field of Model   [Partner]{.title-ref}
  body - {{2}}   INV/2022/00001   Field of Model   [Number]{.title-ref}
  body - {{3}}   My Company       Field of Model   [Company]{.title-ref}
  body - {{4}}   \$               Field of Model   [Currency \> Symbol]{.title-ref}
  body - {{5}}   4000             Field of Model   [Amount]{.title-ref}
  body - {{6}}   https://..       Portal link      
:::

::: {.example}
For example, in the `Body`{.interpreted-text role="guilabel"} tab, if
the following is typed, \"Hello {{1}},\", then [{{1}}]{.title-ref} must
be set in the `Variables`{.interpreted-text role="guilabel"} tab. For
this specific case, the message should greet the customer by name, so
the [{{1}}]{.title-ref} should be configured to populate the
[{{1}}]{.title-ref} `Field`{.interpreted-text role="guilabel"} with the
`Customer`{.interpreted-text role="guilabel"} name.
:::

::: {.warning}
::: {.title}
Warning
:::

Customizing WhatsApp templates is out of the scope of Odoo Support.
:::

#### Meta template approval {#productivity/whatsapp/approval}

After updating the dynamic variables on the template, the template needs
to be submitted to Meta for approval again. Click
`Submit for Approval`{.interpreted-text role="guilabel"} to start the
approval process. An email will be sent to the administrator of the Meta
account when the template has been approved.

Following the approval from Meta, sync the templates again in the Odoo
database. See this documentation:
`productivity/whatsapp/sync`{.interpreted-text role="ref"}.

::: {.tip}
::: {.title}
Tip
:::

To see the status to Meta\'s WhatsApp template dashboard by navigating
to <https://business.facebook.com/wa/manage/home>. Then go to
`Account tools -->
Message templates`{.interpreted-text role="menuselection"}.
:::

#### Syncing templates {#productivity/whatsapp/sync}

Templates must be synced on the Odoo database once they are approved by
the Meta team. To do so, begin by navigating to
`WhatsApp app --> Configuration --> WhatsApp Business
Accounts`{.interpreted-text role="menuselection"} and select the
configuration that should be synced. Under the section marked
`Sending messages`{.interpreted-text role="menuselection"}, towards the
bottom, click on `Sync Templates`{.interpreted-text role="guilabel"}.
Meta will update the templates that are approved so that they can be
utilized with various apps in the database.

![Syncing Meta WhatsApp templates to the Odoo database, with the \'Sync Templates\'
highlighted.](whatsapp/sync-template.png){.align-center}

A successful message in green appears in the upper-right corner with the
number of templates updated.

::: {.tip}
::: {.title}
Tip
:::

Templates can also be synced individually from the template itself.
Navigate to the `WhatsApp app --> Templates`{.interpreted-text
role="menuselection"} dashboard and select the template to sync. Then,
click on the `Sync Template`{.interpreted-text role="guilabel"} button
located in the top menu of the template\'s form.
:::

### Creating templates in Meta

First, navigate to [Meta\'s WhatsApp template
dashboard](https://business.facebook.com/wa/manage/home), and then go to
`Account tools -->
Message templates`{.interpreted-text role="menuselection"}.

{.align-center}

To create a WhatsApp template, click on the blue
`Create template`{.interpreted-text role="guilabel"} button, and then
select the `Category`{.interpreted-text role="guilabel"}. The options
listed include: `Marketing`{.interpreted-text role="guilabel"},
`Utility`{.interpreted-text role="guilabel"}, and
`Authentication`{.interpreted-text role="guilabel"}. In most instances
the first two options will be used, unless the user would like to send a
password reset or something security related.

Enter the `Name`{.interpreted-text role="guilabel"} of the template and
then select the `Language`{.interpreted-text role="guilabel"} for the
template.

::: {.note}
::: {.title}
Note
:::

Multiple languages can be selected by typing the language name(s) and
selecting the other languages as needed.
:::

![Template configuration options listed, with Marketing, Utility, Name and Language
highlighted.](whatsapp/template-config.png){.align-center}

After making the appropriate selections, click on
`Continue`{.interpreted-text role="guilabel"} in the upper-right corner.
The page redirects to the `Edit template`{.interpreted-text
role="guilabel"} page. Here the `Header`{.interpreted-text
role="guilabel"}, `Body`{.interpreted-text role="guilabel"},
`Footer`{.interpreted-text role="guilabel"} and
`Buttons`{.interpreted-text role="guilabel"} are configured. To the
right of the template is a preview of what the template will look like
in production.

{.align-center}

When all the necessary changes are made to the template, click on the
`Submit`{.interpreted-text role="guilabel"} button in the upper-right
corner. A confirmation window appears to confirm the language--- click
`Confirm`{.interpreted-text role="guilabel"} to approve and then another
window appears stating that the template will be submitted to Meta for
review and approval.

The `Status`{.interpreted-text role="guilabel"} of the template will
remain in `In review`{.interpreted-text role="guilabel"} until a
decision has been made by Meta. Once an email confirmation is received
approving the template, the templates will need to be synced from within
the Odoo database.

::: {.seealso}
For more information on configuring templates on the Meta developer
console visit [Meta\'s WhatsApp template
documentation](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/).
:::

Notifications
-------------

Notifications in WhatsApp are handled similar to a message conversation
in Odoo. A pop-up window appears with the received conversation from the
customer. By default, notifications are set in the WhatsApp business
account configuration in Odoo.

Notification settings can be adjusted by navigating to `WhatsApp app -->
Configuration --> WhatsApp Business Accounts`{.interpreted-text
role="menuselection"}. From there, select the account and scroll down to
the `Control`{.interpreted-text role="menuselection"} section where
notifications are handled. Under the `Notify users`{.interpreted-text
role="guilabel"} heading, type in the field which user(s) should be
notified for this particular WhatsApp channel.

::: {.note}
::: {.title}
Note
:::

Once a conversation is initiated between a user and a customer,
notifications to all the users specified in the WhatsApp business
account configuration won\'t occur. Only notifications to the user(s) in
the conversation will occur. Should the user not respond within 15 days,
the customer\'s reply after the 15 days will populate once again to all
the users specified in the WhatsApp configuration.
:::

Adding users to chat
--------------------

Users can be added to a WhatsApp chat by expanding the WhatsApp pop-up
window. WhatsApp conversations are located in the *Discuss* app. Click
on the `👤+ (add user)`{.interpreted-text role="guilabel"} icon next to
it, and a window appears to invite users to the conversation.

{.align-center}

WhatsApp API FAQ
----------------

### Verification

As of February 1, 2023, if the Meta app requires advanced level access
to permissions, a complete business verification may need to be
completed. This includes submitting office business documents to Meta.
[See this
documentation](https://developers.facebook.com/docs/development/release/business-verification).

::: {.seealso}
[Meta\'s WhatsApp access verification
documentation](https://developers.facebook.com/docs/development/release/access-verification/).
:::

### Template errors

Editing templates can cause tracebacks and errors unless the exact
process is followed above, here:
(`productivity/whatsapp/templates`{.interpreted-text role="ref"}).

#### Duplicate validation error

When syncing the templates there may be an instance when there are
multiple templates with the same name on Meta\'s business manager and in
Odoo. This causes a duplicate validation error. To correct this issue,
rename the duplicate template name on Odoo and sync the templates once
again by following the steps here:
`productivity/whatsapp/sync`{.interpreted-text role="ref"}.

{.align-center}

### Token errors

#### User error

Should the temporary token not be replaced with a permanent token a user
error will populate in Odoo when testing the connection after sending
fails. To correct this issues see
`productivity/whatsapp/token`{.interpreted-text role="ref"}.

{.align-center}

#### System user error 100

Should the system user be an `Employee`{.interpreted-text
role="guilabel"} when setting up the permanent token, a user error 100
will populate.

To correct this error, create an `Admin`{.interpreted-text
role="guilabel"} system user, following the process outlined here:
`productivity/whatsapp/token`{.interpreted-text role="ref"}.

{.align-center}
