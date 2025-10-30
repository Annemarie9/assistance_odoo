# File: /content/odoo_doc17.0/fr/content/applications/services/helpdesk/overview/help_center.md

Help Center
===========

Odoo *Helpdesk* integrates with the *Forum*, *eLearning*, and
*Knowledge* apps to create the *Help Center*. The *Help Center* is a
centralized location where teams and customers can search for and share
detailed information about products and services.

{.align-center}

Configuration
-------------

To activate any *Help Center* features (*Forums*, *eLearning*, or
*Knowledge*) on a *Helpdesk* team, go to
`Helpdesk app --> Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"} and select a team, or create a
`new one <../../helpdesk>`{.interpreted-text role="doc"}. Verify the
`Visibility`{.interpreted-text role="guilabel"} of the team is set to
`Invited portal users and all internal users (public)`{.interpreted-text
role="guilabel"} in the `Visibility &
Assignment`{.interpreted-text role="guilabel"} section.

Additionally, the `Website Form`{.interpreted-text role="guilabel"}
option on the *Helpdesk* team page **must** be enabled to activate any
of the *Help Center* features. When one or more of the *Help Center*
features is enabled, the `Website Form`{.interpreted-text
role="guilabel"} is automatically enabled, as well.

::: {.danger}
::: {.title}
Danger
:::

Since all of the *Help Center* features require integration with other
applications, enabling any of them may result in the installation of
additional modules or applications.

Installing a new application on a *One-App-Free* database will trigger a
15-day trial. At the end of the trial, if a paid subscription has
**not** been added to the database, it will no longer be active or
accessible.
:::

::: {.seealso}
`Helpdesk Overview <../../helpdesk>`{.interpreted-text role="doc"}
:::

Knowledge
---------

Odoo\'s *Knowledge* application is a collaborative library, where users
can store, edit, and share information. The *Knowledge* app is
accessible throughout the database by clicking on the
`Knowledge (bookmark)`{.interpreted-text role="guilabel"} icon.

{.align-center}

### Enable Knowledge on a Helpdesk team

To enable the *Knowledge* feature on a *Helpdesk* team, go to
`Helpdesk app -->
Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"} and select a team, or create a
`new one <../../helpdesk>`{.interpreted-text role="doc"}.

When a team has been selected or created, Odoo displays that team\'s
detail form.

On the team\'s detail form, scroll down to the
`Help Center`{.interpreted-text role="guilabel"} section. Then, click
the box next to `Knowledge`{.interpreted-text role="guilabel"} to
activate the *Knowledge* feature. When clicked, a new field labeled,
`Article`{.interpreted-text role="guilabel"} appears.

Clicking the `Article`{.interpreted-text role="guilabel"} field reveals
a drop-down menu. At first, there is only one option in the drop-down
menu titled `Help`{.interpreted-text role="guilabel"}, which Odoo
provides by default. Select `Help`{.interpreted-text role="guilabel"}
from the drop-down menu to choose this article.

::: {.tip}
::: {.title}
Tip
:::

To create a new article, go to the `Knowledge app`{.interpreted-text
role="menuselection"}, then hover the cursor next to the
`Workspace`{.interpreted-text role="guilabel"} section heading, located
in the left sidebar. Moving the cursor there reveals a hidden
`➕ (plus sign)`{.interpreted-text role="guilabel"} icon.

Click the `➕ (plus sign)`{.interpreted-text role="guilabel"} icon to
create a new article in the `Workspace`{.interpreted-text
role="guilabel"}. In the upper-right corner of the page, click the
`Share`{.interpreted-text role="guilabel"} button, and slide the
`Share to Web`{.interpreted-text role="guilabel"} toggle switch until it
reads `Article Published`{.interpreted-text role="guilabel"}. It can
then be added to a *Helpdesk* team.
:::

Once an article has been created and assigned to a *Helpdesk* team,
content can be added and organized through the *Knowledge* app.

::: {.seealso}
`Editing Knowledge articles <../../../productivity/knowledge/articles_editing>`{.interpreted-text
role="doc"}
:::

### Search articles from a Helpdesk ticket

When members of a *Helpdesk* team are trying to solve a ticket, they can
search through the content in the *Knowledge* app for more information
on the issue.

To search *Knowledge* articles, open a ticket --- either from the
*Helpdesk* app dashboard, or by going to
`Helpdesk app --> Tickets --> All Tickets`{.interpreted-text
role="menuselection"}, then select a ticket from the list.

When a ticket is selected, Odoo reveals that ticket\'s detail form.

Click the `Knowledge (bookmark)`{.interpreted-text role="guilabel"}
icon, located at the top-right of the page, to open a pop-up search
window.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

*Knowledge* articles can also be searched by pressing
`Ctrl + K`{.interpreted-text role="command"} to open the command
palette, then typing [?]{.title-ref}, followed by the name of the
desired article.
:::

When Odoo reveals the desired article, click it, or highlight the
`Article`{.interpreted-text role="guilabel"} title, and press
`Enter`{.interpreted-text role="command"}. This will open the article in
the `Knowledge`{.interpreted-text role="guilabel"} application.

To open the article in a new tab, press `Ctrl + Enter`{.interpreted-text
role="command"}.

::: {.tip}
::: {.title}
Tip
:::

If a more in-depth search is required, press `Alt + B`{.interpreted-text
role="command"}. That reveals a separate page, in which a more detailed
search can occur.
:::

#### Share an article to the Help Center

To make a *Knowledge* article available to customers and website
visitors, it **must** be published.

::: {.important}
::: {.title}
Important
:::

Even though the *Help* article has been enabled on a team, Odoo does
**not** share all the nested articles to the web. Individual articles
intended for customers **must** be published for them to be viewable on
the website.
:::

To publish an article, navigate to the desired article, by following the
above steps, and click the `Share`{.interpreted-text role="guilabel"}
icon in the upper-right corner. This reveals a menu. Slide the toggle
button labeled `Share to Web`{.interpreted-text role="guilabel"} to read
`Article Published`{.interpreted-text role="guilabel"}.

{.align-center}

### Solve tickets with a clipboard box

*Clipboard* boxes can be added to *Knowledge* articles to allow content
to be reused, copied, sent as messages, or added to the description on a
ticket. This allows teams to maintain consistency when answering
customer tickets, and minimize the amount of time spent on responding to
repeat questions.

#### Add clipboard boxes to articles

To create a clipboard box, go to
`Knowledge app --> Help`{.interpreted-text role="menuselection"}. Click
on an existing nested article or create a new one by clicking the
`➕ (plus sign)`{.interpreted-text role="guilabel"} icon next to *Help*.

Type [/]{.title-ref} to open the *powerbox*, and view a drop-down list
of `commands
<../../../productivity/knowledge/articles_editing>`{.interpreted-text
role="doc"}. Select or type [clipboard]{.title-ref}. A gray block is
then added to the page. Add any necessary content to this block.

{.align-center}

::: {.note}
::: {.title}
Note
:::

Clipboard boxes only display the `Use as description`{.interpreted-text
role="guilabel"} or `Send as Message`{.interpreted-text role="guilabel"}
options if they are accessed directly from the *Helpdesk*.
:::

#### Use clipboard boxes in tickets

Clipboard boxes can be used to respond directly to a *Helpdesk* ticket
as a message, or to add information to the ticket\'s description.

To use clipboard boxes in a *Helpdesk* ticket, first, open a ticket,
either from the `Helpdesk`{.interpreted-text role="guilabel"} dashboard
or by going to `Helpdesk app --> Tickets --> All
Tickets`{.interpreted-text role="menuselection"} and selecting a ticket
from the list.

Click on the `Knowledge (bookmark)`{.interpreted-text role="guilabel"}
icon in the top-right corner. This opens a search window. In this search
window, select, or search, for the desired article. Doing so reveals
that article page in the Odoo *Knowledge* application.

To use a clipboard box to respond to a ticket, click
`Send as message`{.interpreted-text role="guilabel"} in the upper-right
corner of the clipboard box, located in the body of the article.

Doing so opens a `Compose Email`{.interpreted-text role="guilabel"}
pop-up window. In this window, select the recipients, make any necessary
additions or edits to the clipboard content, then click
`Send`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

To use a clipboard box to add information to a ticket\'s description,
click `Use as
description`{.interpreted-text role="guilabel"} in the upper-right
corner of the clipboard box, located in the body of the article. Doing
so does **not** replace the existing text in a ticket\'s description.
The content from the clipboard box is added as additional text.
:::

Community Forum {#helpdesk/forum}
---------------

A *Community Forum* provides a space for customers to answer each
other\'s questions and share information. By integrating a forum with a
*Helpdesk* team, tickets submitted by customers can be converted to
posts and shared.

### Enable forums on a Helpdesk team

To enable `Community Forums`{.interpreted-text role="guilabel"} on a
*Helpdesk* team, start by navigating to
`Helpdesk app --> Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"} and select a team, or create a
`new one <../../helpdesk>`{.interpreted-text role="doc"}.

Selecting or creating a team reveals that team\'s detail form. Scroll
down to the `Help
Center`{.interpreted-text role="guilabel"} section of features, and
enable `Community Forum`{.interpreted-text role="guilabel"}, by checking
the box beside it.

When activated, a new field labeled `Forums`{.interpreted-text
role="guilabel"} appears beneath.

Click the empty `Forums`{.interpreted-text role="guilabel"} field to
reveal a drop-down menu. By default, there is only one option to begin
with, labeled `Help`{.interpreted-text role="guilabel"}. That is the
option Odoo automatically created when the
`Community Forums`{.interpreted-text role="guilabel"} feature was
enabled. Select `Help`{.interpreted-text role="guilabel"} from the
drop-down menu to enable that forum.

To create a new forum, type a name into the blank
`Forums`{.interpreted-text role="guilabel"} field, then click the
`Create and Edit`{.interpreted-text role="guilabel"} option. Multiple
forums can be selected in this field.

::: {.seealso}
`Forum documentation <../../../websites/forum>`{.interpreted-text
role="doc"}
:::

### Create a forum post from a Helpdesk ticket

When a *Helpdesk* team has a *Forum* enabled, tickets submitted to that
team can be converted to forum posts.

To do that, select a ticket, either from a team\'s pipeline or from
`Tickets --> All
Tickets`{.interpreted-text role="menuselection"} in the
`Helpdesk`{.interpreted-text role="guilabel"} application.

At the top of the ticket detail form, click the
`Share on Forum`{.interpreted-text role="guilabel"} button.

{.align-center}

When clicked, a pop-up window appears. Here, the
`Forum`{.interpreted-text role="guilabel"} post and
`Title`{.interpreted-text role="guilabel"} can be edited to correct any
typos, or modified to remove any proprietary or client information.

`Tags`{.interpreted-text role="guilabel"} can also be added to help
organize the post in the forum, making it easier for users to locate
during a search. When all adjustments have been made, click `Create and
View Post`{.interpreted-text role="guilabel"}.

eLearning
---------

Odoo *eLearning* courses offer customers additional training and content
in the form of videos, presentations, and certifications/quizzes.
Providing additional training enables customers to work through issues
and find solutions on their own. They can also develop a deeper
understanding of the services and products they are using.

### Enable eLearning courses on a Helpdesk team

To enable *eLearning* courses on a *Helpdesk* team, go to
`Helpdesk app -->
Configuration --> Helpdesk Teams`{.interpreted-text
role="menuselection"} and select a team, or create a
`new one <../../helpdesk>`{.interpreted-text role="doc"}.

On the team\'s settings page, scroll to the
`Help Center`{.interpreted-text role="guilabel"} section, and check the
box next to `eLearning`{.interpreted-text role="guilabel"}. A new field
appears below, labeled `Courses`{.interpreted-text role="guilabel"}.

Click the empty field next to `Courses`{.interpreted-text
role="guilabel"} beneath the `eLearning`{.interpreted-text
role="guilabel"} feature to reveal a drop-down menu. Select an available
course from the drop-down menu, or type a title into the field, and
click `Create and edit`{.interpreted-text role="guilabel"} to create a
new course from this page. Multiple courses can be assigned to a single
team.

### Create an eLearning course

A new *eLearning* course can be created from the
`Helpdesk`{.interpreted-text role="guilabel"} team\'s settings page, as
in the step above, or from the *eLearning* app.

To create a course directly through the *eLearning* application,
navigate to `eLearning --> New`{.interpreted-text role="menuselection"}.
This reveals a blank course template that can be customized and modified
as needed.

On the course template page, add a `Course Title`{.interpreted-text
role="guilabel"}, and below that, `Tags`{.interpreted-text
role="guilabel"}.

Click on the `Options`{.interpreted-text role="guilabel"} tab.

Under `Access Rights`{.interpreted-text role="guilabel"}, select which
users are able to view and enroll in the course.

The `Show Course To`{.interpreted-text role="guilabel"} field defines
who can access the courses. The `Enroll
Policy`{.interpreted-text role="guilabel"} field specifies how they can
register for the course.

Under `Display`{.interpreted-text role="guilabel"}, choose the preferred
course `Type`{.interpreted-text role="guilabel"}.

#### Add content to an eLearning course

To add content to a course, click the `Content`{.interpreted-text
role="guilabel"} tab and select `Add Content`{.interpreted-text
role="guilabel"}. Choose the `Content Type`{.interpreted-text
role="guilabel"} from the drop-down menu and upload the file, or paste
the link, where instructed. Click `Save`{.interpreted-text
role="guilabel"} when finished. Click `Add Section`{.interpreted-text
role="guilabel"} to organize the course in sections.

{.align-center}

::: {.note}
::: {.title}
Note
:::

In order to add a certification to a course, go to
`eLearning --> Configuration
--> Settings`{.interpreted-text role="menuselection"}, check the box
labeled `Certifications`{.interpreted-text role="guilabel"}, and
`Save`{.interpreted-text role="guilabel"} to activate the setting.
:::

::: {.seealso}

:::

### Publish an eLearning course

To allow customers to enroll in a course, both the course and the
contents **must** be published.

::: {.tip}
::: {.title}
Tip
:::

If the course is published, but the contents of the course are **not**
published, customers can enroll in the course on the website, but they
are **not** able to view any of the course content. Knowing this, it may
be beneficial to publish the course first, if the course contents are
intended to be released over time, such as classes with a weekly
schedule.
:::

To make the entire course available at once, each piece of course
content must be published first, then the course can be published.

To publish a course, choose a course from the *eLearning* dashboard. On
the course template page, click the `Go to Website`{.interpreted-text
role="guilabel"} smart button.

This will reveal the front end of the course\'s web page. At the top of
the course web page, move the `Unpublished`{.interpreted-text
role="guilabel"} toggle switch to `Published`{.interpreted-text
role="guilabel"}.

#### Publish eLearning course contents from the back-end

To publish *eLearning* course content from the back-end, choose a course
from the *eLearning* dashboard. On the course template page, click the
`Published Contents`{.interpreted-text role="guilabel"} smart button.

Doing so reveals a separate page displaying all the published content
related to that course. Remove the default `Published`{.interpreted-text
role="guilabel"} filter from the search bar in the upper-right corner,
to reveal all the content related to the course - even the non-published
content.

Click the `≣ (bars)`{.interpreted-text role="guilabel"} icon in the
upper-right corner, directly beneath the search bar to switch to list
view.

While in list view, there is a checkbox on the far-left of the screen,
above the listed courses, to the left of the `Title`{.interpreted-text
role="guilabel"} column title. When that checkbox is clicked, all the
course contents are selected at once.

With all the course content selected, click any of the boxes in the
`Is Published`{.interpreted-text role="guilabel"} column. This reveals a
pop-up window, asking for confirmation that all selected records are
intended to be published. Click `Confirm`{.interpreted-text
role="guilabel"} to automatically publish all course content.

{.align-center}
