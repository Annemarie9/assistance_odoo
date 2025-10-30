# File: /content/odoo_doc17.0/fr/content/applications/marketing/social_marketing.md

show-content

:   

Social Marketing
================

Odoo\'s *Social Marketing* application helps content marketers create
and schedule posts, manage various social media accounts, analyze
content effectiveness, and engage directly with social media followers
in one, centralized location.

::: {.seealso}
\- 
:::

::: {.cards}
::: {.card target="social_marketing/social_posts"}
Social posts

Discover everything there is to know about how to create and customize
social media posts using Odoo.
:::

::: {.card target="social_marketing/social_campaigns"}
Social campaigns

Learn about all the different campaign and marketing tools this
application has to offer.
:::
:::

Social media accounts
---------------------

In order to create social posts and analyze content with Odoo *Social
Marketing*, social media accounts **must** be added as a *stream* on the
application\'s main dashboard.

::: {.note}
::: {.title}
Note
:::

Be aware that personal profiles **cannot** be added as a stream. The
main use of Odoo *Social Marketing* is to manage and analyze business
accounts on social media platforms.
:::

::: {.warning}
::: {.title}
Warning
:::

Odoo *Social Marketing* has some limitations in regards to social media
accounts. For example, Odoo **cannot** handle a large quantity of
various pages (e.g. \~40 pages) under the same company. The same
limitations are present in a multi-company environment because of how
the API is constructed.
:::

::: {.warning}
::: {.title}
Warning
:::

In multi-company environments, if every company doesn\'t activate a page
at once, it will result in a permission error.

For example, if Company 1 is the only company selected from the main
Odoo dashboard, and activates *Facebook Page 1* and *Facebook Page 2*,
then those pages will be accesible on the *Social Marketing* dashboard.

However, if on that same database, the user adds Company 2 from the
company drop-down menu in the header, and attempts to add those same
streams, it results in a permission error.

{.align-center}
:::

Social media streams
--------------------

To add a social media business account as a stream, navigate to
`Social Marketing
app`{.interpreted-text role="menuselection"} and select the
`Add A Stream`{.interpreted-text role="guilabel"} button located in the
upper-left corner. Doing so reveals an `Add a Stream`{.interpreted-text
role="guilabel"} pop-up window.

{.align-center}

In the `Add a Stream`{.interpreted-text role="guilabel"} pop-up window,
choose to `Link a new account`{.interpreted-text role="guilabel"} for a
business from any of the following popular social media platforms:
`Facebook`{.interpreted-text role="guilabel"},
`Instagram`{.interpreted-text role="guilabel"},
`LinkedIn`{.interpreted-text role="guilabel"},
`Twitter`{.interpreted-text role="guilabel"}, and
`YouTube`{.interpreted-text role="guilabel"}.

After clicking the desired social media outlet from the
`Add a Stream`{.interpreted-text role="guilabel"} pop-up window, Odoo
navigates directly to that specific social media outlet\'s authorization
page, where permission must be granted, in order for Odoo to add that
particular social media account as a stream to the *Social Marketing*
application.

{.align-center}

Once permission is granted, Odoo navigates back to the
`Feed`{.interpreted-text role="guilabel"} on the main
`Social Marketing`{.interpreted-text role="guilabel"} dashboard, and a
new column, with that account\'s posts, is added. Accounts/streams can
be added at any time.

::: {.important}
::: {.title}
Important
:::

A `Facebook`{.interpreted-text role="guilabel"} page can be added as
long as the `Facebook`{.interpreted-text role="guilabel"} account that
grants permission is the administrator for the page. It should also be
noted that different pages can be added for different streams.
:::

::: {.note}
::: {.title}
Note
:::

`Instagram`{.interpreted-text role="guilabel"} accounts are added
through a `Facebook`{.interpreted-text role="guilabel"} login because it
uses the same API. This means, an `Instagram`{.interpreted-text
role="guilabel"} account needs to be linked to a
`Facebook`{.interpreted-text role="guilabel"} account in order for it to
show up as a stream in Odoo.
:::

Social media page
-----------------

Another way to quickly link social media accounts to Odoo *Social
Marketing* can be done on the `Social Media`{.interpreted-text
role="guilabel"} page. To access the `Social Media`{.interpreted-text
role="guilabel"} page, navigate to
`Social Marketing app --> Configuration --> Social Media`{.interpreted-text
role="menuselection"}.

On the `Social Media`{.interpreted-text role="guilabel"} page there is a
collection of all social media options, each complete with a
`Link account`{.interpreted-text role="guilabel"} button:
`Facebook`{.interpreted-text role="guilabel"},
`Instagram`{.interpreted-text role="guilabel"},
`LinkedIn`{.interpreted-text role="guilabel"},
`Twitter`{.interpreted-text role="guilabel"},
`YouTube`{.interpreted-text role="guilabel"}, and
`Push Notifications`{.interpreted-text role="guilabel"}.

{.align-center}

Social accounts page
--------------------

To see a list of all social accounts and websites linked to the
database, go to
`Social Marketing app --> Configuration --> Social Accounts`{.interpreted-text
role="menuselection"}. This `Social
Accounts`{.interpreted-text role="guilabel"} display the
`Name`{.interpreted-text role="guilabel"}, the
`Handle/Short Name`{.interpreted-text role="guilabel"}, the `Social
Media`{.interpreted-text role="guilabel"} platform, who it was
`Created by`{.interpreted-text role="guilabel"}, and the
`Company`{.interpreted-text role="guilabel"} to which it is associated.

{.align-center}

To edit/modify any of the social accounts on this page, simply select
the desired account from the list on this page, and proceed to make any
adjustments necessary.

Social streams page
-------------------

To view a separate page with all the social media streams that have been
added to the main *Social Marketing* dashboard, navigate to
`Social Marketing app --> Configuration --> Social
Streams`{.interpreted-text role="menuselection"}.

{.align-center}

Here, the social stream information is organized in a list with the
`Social Media`{.interpreted-text role="guilabel"}, the
`Title`{.interpreted-text role="guilabel"} of the stream, the
`Type`{.interpreted-text role="guilabel"} of the stream (e.g.
`Posts`{.interpreted-text role="guilabel"}, `Keyword`{.interpreted-text
role="guilabel"}, etc.), who it was `Created by`{.interpreted-text
role="guilabel"}, and the `Company`{.interpreted-text role="guilabel"}
to which it is associated.

To modify any stream\'s information, simply click the desired stream
from the list, and proceed to make any necessary adjustments.

Visitors
--------

To see a complete overview of all the people who have visited the
website(s) connected to the database, navigate to
`Social Marketing app --> Visitors`{.interpreted-text
role="menuselection"}.

{.align-center}

Here, Odoo provides a detailed layout of all the visitors\' pertinent
information in a default kanban view. If visitors already have contact
information in the database, the option to send them an
`Email`{.interpreted-text role="guilabel"} and/or an
`SMS`{.interpreted-text role="guilabel"} is available.

This same visitor data can also be viewed as a list or a graph. Those
view options are located in the upper-right corner of the
`Visitors`{.interpreted-text role="guilabel"} page.

::: {.toctree}
social\_marketing/social\_posts social\_marketing/social\_campaigns
:::
