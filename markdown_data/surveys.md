# File: /content/odoo_doc17.0/fr/content/applications/marketing/surveys.md

show-content

:   

Surveys
=======

Companies gather valuable insights from customers and employees through
surveys, aiding informed decision-making.

With Odoo *Surveys*, users create various surveys, questionnaires,
certifications, assessments, and so much more. These can be used to
collect feedback, evaluate the success of a recent event, and measure
the satisfaction of customers and/or employees. This process yields
valuable insights into shifting market trends.

::: {.seealso}

:::

::: {.cards}
::: {.card target="surveys/create"}
Create surveys

Discover how to create surveys with Odoo.
:::

::: {.card target="surveys/scoring"}
Scoring surveys

Learn how to create and analyze survey scores with Odoo.
:::

::: {.card target="surveys/questions"}
Create questions

See how to create, configure, and customize all types of survey
questions with Odoo.
:::

::: {.card target="surveys/live_session"}
Live Session surveys

Find out everything there is to know about Odoo\'s unique Live Session
surveys.
:::

::: {.card target="surveys/analysis"}
Survey analysis

Explore the various ways to analyze surveys using Odoo\'s in-depth
reporting pages.
:::
:::

Dashboard
---------

Upon opening the *Surveys* application, Odoo presents the main dashboard
of the *Surveys* application, otherwise known as the
`Surveys`{.interpreted-text role="guilabel"} page.

{.align-center}

::: {.tip}
::: {.title}
Tip
:::

The *Surveys* dashboard can be accessed at any time throughout the
application by clicking `Surveys`{.interpreted-text
role="menuselection"} from the header menu.
:::

In the upper-left corner, there is a `New`{.interpreted-text
role="guilabel"} button. When clicked, Odoo presents a blank survey form
that can be used to create a survey.

On the dashboard, all the surveys that have been created in the database
are displayed in a default Kanban view.

From left-to-right, after the survey name, the user who is responsible
for it, and the month it was created, each line on the *Surveys*
dashboard shows the following:

-   Number of `Questions`{.interpreted-text role="guilabel"} in that
    particular survey

-   `Average Duration`{.interpreted-text role="guilabel"} of the survey
    (how long it typically takes a participant to complete)

-   Number of `Registered`{.interpreted-text role="guilabel"}
    participants for the survey

-   Number of times that particular survey has been
    `Completed`{.interpreted-text role="guilabel"}

-   Percentage and data bar showcasing how many people have
    `Passed`{.interpreted-text role="guilabel"} or become
    `Certified`{.interpreted-text role="guilabel"}

    ::: {.note}
    ::: {.title}
    Note
    :::

    The `Passed`{.interpreted-text role="guilabel"} percentage and bar
    **only** appears when a *Required Score* has been configured for
    that particular survey.

    The `Certified`{.interpreted-text role="guilabel"} percentage and
    bar **only** appears if that particular survey has the *Is a
    Certification* option enabled on the survey form.

    If neither `Passed`{.interpreted-text role="guilabel"} nor
    `Certified`{.interpreted-text role="guilabel"} appear on the line,
    that indicates the survey is without a *Required Score* and was not
    enabled with the *Is a Certification* option.
    :::

-   Number of `Courses`{.interpreted-text role="guilabel"} related to
    that survey, which **only** appears if more than one course has been
    created and attached to a single survey

::: {.note}
::: {.title}
Note
:::

A half-trophy background image behind the survey name indicates that the
survey is a *Certification*.
:::

To the far-right of those data points on the survey lines, located on
the *Surveys* application dashboard, are a collection of buttons.

Those buttons are as follows:

-   `Share`{.interpreted-text role="guilabel"}: click to reveal a
    `Share a Survey`{.interpreted-text role="guilabel"} pop-up form that
    can be used to invite potential participants to the survey -
    complete with a `Survey Link`{.interpreted-text role="guilabel"}
    that can be copied and sent to potential participants, and a
    `Send by Email`{.interpreted-text role="guilabel"} toggle switch.

    When the `Send by Email`{.interpreted-text role="guilabel"} toggle
    is active (green switch), additional fields appear, in which
    `Recipients`{.interpreted-text role="guilabel"},
    `Additional Emails`{.interpreted-text role="guilabel"}, and a
    `Subject`{.interpreted-text role="guilabel"} can be added to the
    email.

    Below that, a dynamic email template, complete with a
    `Start Certification`{.interpreted-text role="guilabel"} button
    appears, which can be modified, as well, if needed.

    `Attachments`{.interpreted-text role="guilabel"} can be added to the
    email, as well as an `Answer deadline`{.interpreted-text
    role="guilabel"} can be set, if needed.

    Once modifications are complete, click `Send`{.interpreted-text
    role="guilabel"} to send that email invite to all the email
    addresses/contacts listed in the `Recipients`{.interpreted-text
    role="guilabel"} field.

    {.align-center}

    ::: {.tip}
    ::: {.title}
    Tip
    :::

    The default `Mail Template`{.interpreted-text role="guilabel"} for
    survey invites can be edited by navigating to
    `Settings --> Technical --> Email Templates`{.interpreted-text
    role="menuselection"} and searching for [Survey:
    Invite]{.title-ref}.
    :::

    ::: {.note}
    ::: {.title}
    Note
    :::

    The `Send by Email`{.interpreted-text role="guilabel"} toggle switch
    is **not** present when the survey line has zero questions.

    The `Survey Link`{.interpreted-text role="guilabel"} only appears
    when the survey\'s *Access Mode* is set to *Anyone with the link*.

    The `Additional Emails`{.interpreted-text role="guilabel"} field
    only appears when the survey\'s *Require Login* field is **not**
    active.
    :::

-   `Test`{.interpreted-text role="guilabel"}: click to take a test
    version of the survey in a new tab, from the point-of-view of a
    survey participant, in order to check for any errors or
    inconsistencies.

-   `See results`{.interpreted-text role="guilabel"}: click to reveal a
    new tab showcasing detailed metrics and graphical representations of
    all survey participants, questions, and responses for deeper
    analysis.

-   `Start Live Session`{.interpreted-text role="guilabel"}: click to
    initiate a *Live session* survey, and reveal a session manager
    window in a new tab. This button is **not** present for surveys that
    have enabled the *Is a Certification* option on the survey form.

-   `End Live Session`{.interpreted-text role="guilabel"}: click to end
    a *Live session* survey that has been officially started. This
    button option **only** appears on survey lines that have previously
    initiated a live session.

Above the buttons that are located to the far-right of the survey lines,
a `⋮ (three
dots)`{.interpreted-text role="guilabel"} icon appears when the cursor
hovers over that particular line. When the `⋮ (three
dots)`{.interpreted-text role="guilabel"} icon is clicked, a drop-down
menu with some configuration-related options appear:

The options are:

-   `Edit Survey`{.interpreted-text role="guilabel"}: when clicked, Odoo
    reveals the survey form for that particular survey, which can then
    be modified in a number of different ways.
-   `Share`{.interpreted-text role="guilabel"}: when clicked, Odoo
    reveals the `Share a Survey`{.interpreted-text role="guilabel"}
    pop-up form that can be used to invite potential participants to the
    survey.
-   `Delete`{.interpreted-text role="guilabel"}: when clicked, Odoo
    presents a pop-up window, wherein the user **must** confirm they
    want to delete the survey entirely, which they can do by clicking
    the `Delete`{.interpreted-text role="guilabel"} button at the bottom
    of the pop-up window.
-   `Color`{.interpreted-text role="guilabel"}: users can opt to choose
    a color to add to the survey line on the dashboard for added
    organizational purposes, if needed.

{.align-center}

Beneath the buttons that are located to the far-right of the survey
lines, there is an *Activities* button, represented by a
`🕘 (clock)`{.interpreted-text role="guilabel"} icon. When clicked, a
mini pop-up window appears, from which activities related to that
particular survey can be scheduled and customized.

{.align-center}

### List view

The *Surveys* dashboard is shown in the Kanban view, by default, but
there is also a list view option available in the upper-right corner,
represented by a `≣ (bars)`{.interpreted-text role="guilabel"} icon.

When the `≣ (bars)`{.interpreted-text role="guilabel"} icon is clicked,
the survey related data is displayed in a list view.

{.align-center}

The columns shown on the *Surveys* app dashboard, while in list view,
are as follows:

-   `Survey Title`{.interpreted-text role="guilabel"}
-   `Responsible`{.interpreted-text role="guilabel"}
-   `Average Duration`{.interpreted-text role="guilabel"}
-   `Registered`{.interpreted-text role="guilabel"}
-   `Success Ratio (%)`{.interpreted-text role="guilabel"}
-   `Avg Score (%)`{.interpreted-text role="guilabel"}

::: {.tip}
::: {.title}
Tip
:::

Additional columns can be added to the *Surveys* application dashboard,
while in list view, by clicking the *additional options* drop-down menu,
located to the far-right of the column titles, represented by a
`(slider with two dots)`{.interpreted-text role="guilabel"} icon.
:::

### Activities view

To have the *Surveys* application dashboard display nothing but the
activities associated to the surveys in the database, click the
`🕘 (clock)`{.interpreted-text role="guilabel"} icon to the far-right of
the other view options, located in the upper-right corner.

{.align-center}

Doing so reveals a table with rows and columns. The rows show the
different surveys in the database, and the columns depict the various
activity types.

::: {.note}
::: {.title}
Note
:::

A new survey cannot be created in this view, as it is solely for the
purpose of creating and viewing scheduled activities.
:::

Create surveys
--------------

Learn about all the different options and configurations that can be
utilized when creating a survey in Odoo.

::: {.seealso}
`surveys/create`{.interpreted-text role="doc"}
:::

Scoring surveys
---------------

Discover how to measure a survey participant\'s performance, or overall
satisfaction, with Odoo\'s detailed (and fully customizable) survey
scoring options.

::: {.seealso}
`surveys/scoring`{.interpreted-text role="doc"}
:::

Create questions
----------------

With Odoo *Surveys*, there are many question types and options to choose
from, providing the ability to create any kind of unique survey,
questionnarire, and/or certification.

::: {.seealso}
`surveys/questions`{.interpreted-text role="doc"}
:::

Live Session surveys
--------------------

The *Live Session* survey option available in Odoo can enhance in-person
demonstrations and presentations, where participants\' real-time
responses can be used to dictate where the conversation goes next.

::: {.seealso}
`surveys/live_session`{.interpreted-text role="doc"}
:::

Survey analysis
---------------

Once the surveys start to come in, it is time to analyze the responses
from your participants. Fortuantely, the in-depth reporting pages and
options available in Odoo *Surveys* provide countless ways to examine
everything related to surveys, and their submitted responses.

::: {.seealso}
`surveys/analysis`{.interpreted-text role="doc"}
:::

::: {.toctree titlesonly=""}
surveys/create surveys/scoring surveys/questions surveys/live\_session
surveys/analysis
:::
