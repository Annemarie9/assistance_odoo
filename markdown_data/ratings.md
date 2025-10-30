# File: /content/odoo_doc17.0/fr/content/applications/websites/livechat/ratings.md

Ratings
=======

At the end of a *Live Chat* conversation, customers have the opportunity
to rate the quality of support they received from the live chat
*operator*. Customers provide ratings as soon as they close the
conversation. This allows operators to receive immediate feedback on
their performance. It also allows customers the chance to share any
final comments before leaving the chat window.

Rate live chat conversations
----------------------------

Customers end a *live chat* conversation by clicking the
`X`{.interpreted-text role="guilabel"} in the upper right-hand corner of
the chat window. They are then prompted to select an icon that reflects
their level of satisfaction. The icons represent the following ratings:

> -   **Satisfied** - *green smiling face*
> -   **Okay** - *yellow neutral face*
> -   **Dissatisfied** - *red frowning face*

{.align-center}

::: {.note}
::: {.title}
Note
:::

When customers end a conversation, a field marked
`Receive a copy of this conversation`{.interpreted-text role="guilabel"}
appears under the *ratings* icons. Customers can enter their email
either before or after they submit a rating.
:::

If the customer selects `Satisfied (smile)`{.interpreted-text
role="guilabel"} icon, they are presented with a thank you message and a
`Close Conversation`{.interpreted-text role="guilabel"} link.

{.align-center}

If the customer selects either `Okay (neutral)`{.interpreted-text
role="guilabel"} icon or `Dissatisfied (frown)`{.interpreted-text
role="guilabel"} icon, a text box will appear. Customers can add
comments in this text box to explain why they chose this rating. This
message will be sent to the live chat operator, along with the rating
icon.

{.align-center}

Publish customer ratings
------------------------

To publish a channel\'s ratings on the website, first navigate to a live
chat channel\'s record by going to the `Live Chat`{.interpreted-text
role="menuselection"} app and clicking on the kanban card for that team.
Then click on the `Go to Website`{.interpreted-text role="guilabel"}
smart button. This will open the `Live Chat Channel
Statistics`{.interpreted-text role="guilabel"} page.

In the upper right corner of the page, click the red
`Unpublished`{.interpreted-text role="guilabel"} slider. The slider
changes from `Unpublished`{.interpreted-text role="guilabel"} to
`Published`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.note}
::: {.title}
Note
:::

The customer notes that are submitted with the rating will *not* be
published on the website. These are kept internal. Only a statistical
overview of the operators\' performance for the *channel* appears on the
website.
:::

### Add ratings page to site

Once the rating page has been published, it has to be manually added to
the website. To do this, go to the main Odoo dashboard and open the
*Website* application. `Website app--> Site
--> Content --> Pages`{.interpreted-text role="menuselection"}, then
click `New`{.interpreted-text role="guilabel"}.

This will open a `New Page`{.interpreted-text role="guilabel"} pop-up
window. In the `Page Title`{.interpreted-text role="guilabel"} field,
enter [livechat]{.title-ref}. This acts as the URL for the published
webpage.

::: {.important}
::: {.title}
Important
:::

The URL *must* be named [livechat]{.title-ref} in order for the database
to recognize and connect the ratings page. After the page has been
published, the page title can be changed later under the
`Menu Editor`{.interpreted-text role="guilabel"}.
:::

Click `Create`{.interpreted-text role="guilabel"}, and the newly created
webpage will open. The `Webpage Editor`{.interpreted-text
role="guilabel"} appears in the right panel.

The page lists the names of the `Live Chat Channels`{.interpreted-text
role="guilabel"} whose ratings pages have been published. On the left
side of the channel name is a speech bubble icon, which users can click
on to go to the ratings\' page for the respective channel.

{.align-center}

Make any desired changes or additions to this page, then click
`Save`{.interpreted-text role="guilabel"} in the top right of the
webpage editor. The website editor side panel closes, and the webpage
remains on the screen.

To publish the [livechat]{.title-ref} webpage, return to the list of
webpages by navigating to `Site --> Content --> Pages`{.interpreted-text
role="menuselection"}. Click the checkbox to the left of
[livechat]{.title-ref} in the list of pages to select the page and
highlight the line. Then, click the checkbox under the column labeled
`Is Published`{.interpreted-text role="guilabel"}. The field with the
checkbox is highlighted in white. Click the checkbox a second time to
activate the `Is Published`{.interpreted-text role="guilabel"} box. The
webpage is now published.

{.align-center}

Once the page has been added to the site, ratings are set to be
published by default. However, individual ratings can be manually
selected to be hidden from the public. The rating will still be included
in internal reports, and can still be viewed by internal teams. However,
public website visitors and portal users will not have access.

See
`Hide individual ratings <livechat/overview/hide-ratings>`{.interpreted-text
role="ref"} for more information.

Customer ratings report
-----------------------

The `Customer Ratings`{.interpreted-text role="guilabel"} report
(`Live Chat --> Report --> Customer Ratings`{.interpreted-text
role="menuselection"}) displays an overview of the ratings received on
individual support tickets, as well as any additional comments submitted
with the rating.

{.align-center}

The report defaults to a kanban view, with each rating represented by a
different card. To switch to a different view, click on one of the icons
in the upper-right corner of the screen. The report is available in
*list* view, *pivot* view, and *graph* view.

Click on an individual rating to see additional details about the
conversation, and the rating.

### Hide individual ratings {#livechat/overview/hide-ratings}

Ratings are set to be published by default. However, individual ratings
can be manually selected to be hidden from the public. The rating will
still be included in internal reports, and can still be viewed by
internal teams. However, public website visitors and portal users will
not have access.

To hide a rating, go to
`Live Chat app --> Reports --> Customer Ratings`{.interpreted-text
role="menuselection"}. Click on the kanban card for the rating to be
hidden. On the individual rating\'s detail page, check the box labeled
`Visible Internally Only`{.interpreted-text role="guilabel"}.

{.align-center}

::: {.seealso}
\- `/applications/websites/livechat`{.interpreted-text role="doc"} -
`responses`{.interpreted-text role="doc"} -
`/applications/websites/website`{.interpreted-text role="doc"}
:::
