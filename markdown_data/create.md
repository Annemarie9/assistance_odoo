# File: /content/odoo_doc17.0/fr/content/applications/marketing/surveys/create.md

Create surveys
==============

To create a survey in the Odoo *Surveys* application, navigate to
`Surveys app -->
New`{.interpreted-text role="menuselection"} to reveal a blank survey
form.

::: {.note}
::: {.title}
Note
:::

The `New`{.interpreted-text role="guilabel"} button is **not** present
on the *Surveys* dashboard if in the *Activities* view.
:::

Survey form
-----------

{.align-center}

At the top of the survey form are four radio buttons, each representing
a survey style. The radio button options are:

-   `Survey`{.interpreted-text role="guilabel"}
-   `Live Session`{.interpreted-text role="guilabel"}
-   `Assessment`{.interpreted-text role="guilabel"}
-   `Custom`{.interpreted-text role="guilabel"} (selected by default)

These options are here to streamline the survey-making process, by
providing users with automated settings and options that are ideally
specific to those types of surveys. Each of those survey type options
comes equipped with its own specific selection of options.

The `Custom`{.interpreted-text role="guilabel"} option, selected by
default, offers all the options from every potential survey type
(located in the `Options`{.interpreted-text role="guilabel"} tab).

Beneath those radio survey type options is a blank field in which a name
for the survey **must** be entered.

Below the survey name field, is the `Responsible`{.interpreted-text
role="guilabel"} field. Choose a user from the drop-down menu to be in
charge of the survey. By default, the user who initially created the
survey is selected as the default `Responsible`{.interpreted-text
role="guilabel"}.

To the right of those fields, and above the tabs, is the option to add a
background image, represented by a `📷 (camera)`{.interpreted-text
role="guilabel"} icon. When clicked, the option to upload an image
becomes available. This image would be used as the background image for
the entire survey. This is **not** a required option.

Below those fields and options are four tabs:
`Questions`{.interpreted-text role="guilabel"},
`Options`{.interpreted-text role="guilabel"},
`Description`{.interpreted-text role="guilabel"}, and
`End Message`{.interpreted-text role="guilabel"}.

### Questions tab

View, access, add, and/or delete questions and sections to the survey in
the `Questions`{.interpreted-text role="guilabel"} tab.

By default, two columns are present in the `Questions`{.interpreted-text
role="guilabel"} tab: `Title`{.interpreted-text role="guilabel"} (i.e.
the question) and `Question Type`{.interpreted-text role="guilabel"}.

If the `Randomized per Section`{.interpreted-text role="guilabel"}
option is enabled in the `Options`{.interpreted-text role="guilabel"}
tab of the survey form, a column titled,
`# Questions Randomly Picked`{.interpreted-text role="guilabel"} appears
in the `Questions`{.interpreted-text role="guilabel"} tab.

Indicate whether questions require a mandatory answer by clicking the
`(optional columns)`{.interpreted-text role="guilabel"} icon to the
far-right of the column titles. Then, select
`Mandatory Answer`{.interpreted-text role="guilabel"} from the drop-down
menu to reveal the `Mandatory Answer`{.interpreted-text role="guilabel"}
column in the `Questions`{.interpreted-text role="guilabel"} tab.

{.align-center}

#### Add a question

To add a question to a survey, click `Add a question`{.interpreted-text
role="guilabel"} in the `Questions`{.interpreted-text role="guilabel"}
tab, and proceed to fill out the
`Create Sections and Questions`{.interpreted-text role="guilabel"}
pop-up window that appears.

To learn how to create and customize questions, refer to the
`create questions <questions>`{.interpreted-text role="doc"}
documentation.

::: {.important}
::: {.title}
Important
:::

There **must** be a survey title entered in order for the
`Create Sections and
Questions`{.interpreted-text role="guilabel"} pop-up window to appear.
If no title is entered for the survey, an error pop-up message appears
in the upper-right corner, instructing the user to enter a survey title.
:::

#### Add a section

A *section* divides the survey into organized parts, in order to
visually group similar questions together. To make a section, click
`Add a section`{.interpreted-text role="guilabel"} at the bottom of the
`Questions`{.interpreted-text role="guilabel"} tab, proceed to type in a
desired name for the section, then either press
`Enter`{.interpreted-text role="kbd"} or click away.

The section line appears in dark gray in the
`Questions`{.interpreted-text role="guilabel"} tab.

Then, drag-and-drop desired questions beneath a section, or
drag-and-drop a section title on top of (i.e. *before*) the desired
question(s) in the survey. Doing so populates the section with questions
that align with its theme.

If the `Randomized per Section`{.interpreted-text role="guilabel"}
option is enabled in the `Options`{.interpreted-text role="guilabel"}
tab of the survey form, the number [1]{.title-ref} appears, by default,
on the section line, beneath the `#
Questions Randomly Picked`{.interpreted-text role="guilabel"} column.

This indicates that [1]{.title-ref} question from that section will be
picked at random for each participant taking the survey, bypassing every
other, non-chosen question from that section. To change that number,
select that figure, and type in the desired number in its place. Then,
either press `Enter`{.interpreted-text role="kbd"}, or click away.

### Options tab

In the `Options`{.interpreted-text role="guilabel"} tab of the survey
form, there are many options to choose from, separated in four different
sections: `Questions`{.interpreted-text role="guilabel"},
`Time & Scoring`{.interpreted-text role="guilabel"},
`Participants`{.interpreted-text role="guilabel"}, and
`Live Session`{.interpreted-text role="guilabel"}.

The options available in this tab vary on the survey type chosen, via
the radio buttons at the top of the survey form:
`Survey`{.interpreted-text role="guilabel"},
`Live Session`{.interpreted-text role="guilabel"},
`Assessment`{.interpreted-text role="guilabel"}, or
`Custom`{.interpreted-text role="guilabel"}.

The `Custom`{.interpreted-text role="guilabel"} survey type showcases
all the possible options in the `Options`{.interpreted-text
role="guilabel"} tab. So, if any of the following options do **not**
appear in the `Options`{.interpreted-text role="guilabel"} tab, it is
likely because the selected survey type does not offer it.

#### Questions section

{.align-center}

The first field in the `Questions`{.interpreted-text role="guilabel"}
section revolves around the `Pagination`{.interpreted-text
role="guilabel"}, or overall layout, of the survey.

Choose between `One page per question`{.interpreted-text
role="guilabel"}, `One page per section`{.interpreted-text
role="guilabel"}, or `One page with all the questions`{.interpreted-text
role="guilabel"} in the `Pagination`{.interpreted-text role="guilabel"}
field.

::: {.note}
::: {.title}
Note
:::

If `One page with all the questions`{.interpreted-text role="guilabel"}
is selected, all the remaining options in the
`Questions`{.interpreted-text role="guilabel"} field, apart from
`Question Selection`{.interpreted-text role="guilabel"} is removed, as
they are no longer needed.
:::

Next, select one of the following options in the
`Display Progress as`{.interpreted-text role="guilabel"} field:

-   `Percentage left`{.interpreted-text role="guilabel"}: displays the
    percentage of the survey remaining to participants.
-   `Number`{.interpreted-text role="guilabel"}: display the number of
    questions answered along with the total number of questions to
    answer.

In the `Question Selection`{.interpreted-text role="guilabel"} field
choose to have the survey show `All questions`{.interpreted-text
role="guilabel"} or `Randomized per Section`{.interpreted-text
role="guilabel"}. If `Randomized per Section`{.interpreted-text
role="guilabel"} a new column appears in the
`Questions`{.interpreted-text role="guilabel"} tab, titled:
`# Questions Randomly Picked`{.interpreted-text role="guilabel"}.

In the `# Questions Randomly Picked`{.interpreted-text role="guilabel"}
column, designate how many questions, in that particular section, should
be chosen at random to the participant.

Lastly, there is the `Allow Roaming`{.interpreted-text role="guilabel"}
option. When enabled, participants are able to navigate back to previous
pages in the survey.

#### Time & Scoring section

{.align-center}

The first option in the `Time & Scoring`{.interpreted-text
role="guilabel"} section is the `Survey Time Limit`{.interpreted-text
role="guilabel"} option. If enabled, proceed to enter in an amount of
time (in `minutes`{.interpreted-text role="guilabel"}) to be set as the
time limit for the survey.

Next, in the `Scoring`{.interpreted-text role="guilabel"} section,
determine whether there should be: `No scoring`{.interpreted-text
role="guilabel"},
`Scoring with answers after each page`{.interpreted-text
role="guilabel"}, `Scoring with answers at the end`{.interpreted-text
role="guilabel"}, or `Scoring without answers`{.interpreted-text
role="guilabel"}.

If the `No scoring`{.interpreted-text role="guilabel"} option is
selected, no other options are available in this section. However, if
any *other* `Scoring`{.interpreted-text role="guilabel"} option is
selected, two additional fields appear:
`Required Score (%)`{.interpreted-text role="guilabel"} and
`Is a Certification`{.interpreted-text role="guilabel"}.

In the `Required Score (%)`{.interpreted-text role="guilabel"} field,
enter the minimum percentage participants **must** earn in order to pass
the survey. Scores below this threshold are considered fails. This
figure is also used to determine if a participant is \'certified\' or
not, if the `Is a Certification`{.interpreted-text role="guilabel"}
option is enabled.

If the `Is a Certification`{.interpreted-text role="guilabel"} option is
enabled, that makes the survey a *Certification*, which is represented
on the main *Surveys* app dashboard via a half-tropy image behind the
survey title, while in the default Kanban view. Or, via a full-trophy
icon, while in list view.

When the `Is a Certification`{.interpreted-text role="guilabel"} option
is enabled, three additional fields appear \-- one beside the option,
and two below.

In the field that appears beside the option, users can select (and
`Preview`{.interpreted-text role="guilabel"}) a certification template.

Beneath that, in the `Certified Email Template`{.interpreted-text
role="guilabel"} field, users can select a preconfigured email template,
or create one on-the-fly, to be sent to certified participants of the
survey upon completion.

Lastly, if the `Give Badge`{.interpreted-text role="guilabel"} field is
enabled, a preconfigured badge is then displayed on the contact page for
that certified survey participant.

#### Participants section

{.align-center}

The first available option in the `Participants`{.interpreted-text
role="guilabel"} section is the `Access Mode`{.interpreted-text
role="guilabel"} field. This is where users can determine who has access
to the survey. Users can select either:
`Anyone with the link`{.interpreted-text role="guilabel"} or
`Invited people only`{.interpreted-text role="guilabel"}.

Next, there is the option to `Require Login`{.interpreted-text
role="guilabel"}. Enabling this feature means users **must** login
before being able to take the survey, even if they have a valid token.

Lastly, in there is the `Limit Attempts`{.interpreted-text
role="guilabel"} field. If enabled, an additional field appears beside
it, in which users can determine how many times users can attempt this
survey.

#### Live Session section

{.align-center}

::: {.note}
::: {.title}
Note
:::

The `Live Session`{.interpreted-text role="guilabel"} section in the
`Options`{.interpreted-text role="guilabel"} tab of the survey form
**only** pertains to *Live Session* surveys.
:::

The first option in the `Live Session`{.interpreted-text
role="guilabel"} section is the `Session Code`{.interpreted-text
role="guilabel"} field. In this field, enter a custom code, consisting
of letters, numbers, and/or symbols, to be used by participants in order
to access the live session survey.

Next, is the `Session Link`{.interpreted-text role="guilabel"} field,
which **cannot** be customized, but it *can* be sent out to potential
participants.

::: {.note}
::: {.title}
Note
:::

If a `Session Code`{.interpreted-text role="guilabel"} has been entered,
the URL in the `Session Link`{.interpreted-text role="guilabel"} field
ends with that specific `Session Code`{.interpreted-text
role="guilabel"}.

If that complete `Session Link`{.interpreted-text role="guilabel"}
(ending in the custom `Session Code`{.interpreted-text role="guilabel"})
is used by participants to access the live session survey, that link
would *already* be entered for them. At that point, they\'d simply have
to wait until the host of the live session begins the survey, and then
they\'d be able to enter.

If the `Session Link`{.interpreted-text role="guilabel"} (ending in the
custom `Session Code`{.interpreted-text role="guilabel"}) is sent
**without** including the `Session Code`{.interpreted-text
role="guilabel"} ending, participants trying to access the live session,
via that link, will need to enter the custom
`Session Code`{.interpreted-text role="guilabel"} to gain access.

If the `Session Code`{.interpreted-text role="guilabel"} field is empty,
a slightly longer, more complicated URL populates the
`Session Link`{.interpreted-text role="guilabel"} field. When
participants attempt to access the live session via that link (without a
configured `Session Code`{.interpreted-text role="guilabel"}), all they
have to do is wait for the host of the live session to begin the survey,
and they\'d be able to participate.
:::

Lastly, in the `Live Session`{.interpreted-text role="guilabel"}
section, there is the option to `Reward quick
answers`{.interpreted-text role="guilabel"}. If that option is enabled,
participants who submit their answer quickly receive more points.

::: {.seealso}
`live_session`{.interpreted-text role="doc"}
:::

### Description tab

In this non-required tab, users can enter a custom description about the
survey, along with any explanations or guidance that a survey
participant may need in order to properly participate (and complete) the
survey.

### End Message tab

In this non-required tab, users can enter a custom message that
participants see upon completing the survey.

Survey form buttons
-------------------

Once the survey has been configured properly, and questions have been
added, the user can utilize any of the available buttons in the
upper-left corner of the survey form.

{.align-center}

Those buttons are the following:

-   `Share`{.interpreted-text role="guilabel"}: click to reveal a
    `Share a Survey`{.interpreted-text role="guilabel"} pop-up form that
    can be used to invite potential participants to the survey ---
    complete with a `Survey Link`{.interpreted-text role="guilabel"}
    that can be copied and sent to potential participants, and a
    `Send by Email`{.interpreted-text role="guilabel"} toggle switch.

    {.align-center}

    When the `Send by Email`{.interpreted-text role="guilabel"} toggle
    is in the \'on\' position, indicated by a green switch, additional
    fields appear, in which `Recipients`{.interpreted-text
    role="guilabel"} and a `Subject`{.interpreted-text role="guilabel"}
    can be added to the email. Below that, a dynamic email template,
    complete with a `Start
    Certification`{.interpreted-text role="guilabel"} button appears,
    which can also be modified.

    {.align-center}

    Once modifications are complete, click `Send`{.interpreted-text
    role="guilabel"} to send that email invite to all the email
    addresses/contacts listed in the `Recipients`{.interpreted-text
    role="guilabel"} field.

-   `See results`{.interpreted-text role="guilabel"}: this button
    **only** appears if there has been at least one participant who has
    completed the survey. Clicking `See results`{.interpreted-text
    role="guilabel"} reveals a separate tab containing a visual analysis
    of the survey questions and responses. For more information, check
    out the `scoring surveys <scoring>`{.interpreted-text role="doc"}
    documentation.

-   `Create Live Session`{.interpreted-text role="guilabel"}: clicking
    this button opens the *Session Manager* in a separate tab. It also
    allows participants to access the live session, but the actual
    survey does **not** begin until the user hosting the live session
    survey clicks the `Start`{.interpreted-text role="guilabel"} button
    on the *Session Manager* window.

    Additionally, when `Create Live Session`{.interpreted-text
    role="guilabel"} has been clicked, and the *Session Manager* tab has
    been opened, the `Create Live Session`{.interpreted-text
    role="guilabel"} button on the survey form is replaced with two new
    buttons: `Open Session Manager`{.interpreted-text role="guilabel"}
    and `Close Live Session`{.interpreted-text role="guilabel"}.

    Clicking `Open Session Manager`{.interpreted-text role="guilabel"}
    opens another separate tab to the *Session Manager*, and clicking
    `Close Live Session`{.interpreted-text role="guilabel"} closes, and
    subsequently ends, the live session.

-   `Test`{.interpreted-text role="guilabel"}: clicking this button
    opens a new tab to a test version of the survey, in order for the
    user to check for errors or inconsistencies, from the point-of-view
    of a participant. Users can tell if they are in a test version of
    the survey if there is a blue banner at the top of the screen,
    reading: [This is a Test Survey \--\> Edit Survey]{.title-ref}.

    If the link in the blue banner is clicked, Odoo returns the user to
    the survey form.

-   `Print`{.interpreted-text role="guilabel"}: clicking this button
    opens a new tab to a printable version of the survey that the user
    can proceed to print for their records.

-   `Close`{.interpreted-text role="guilabel"}: clicking this button
    closes the survey (i.e. archives it), which is represented by a red
    `Archived`{.interpreted-text role="guilabel"} banner across the
    top-right corner of the survey form.

    When this button is clicked, and the survey is closed, a single
    button appears in the upper-right corner of the survey form, titled:
    `Reopen`{.interpreted-text role="guilabel"}. When
    `Reopen`{.interpreted-text role="guilabel"} is clicked the survey is
    reopened (i.e. unarchived), and the `Archived`{.interpreted-text
    role="guilabel"} banner is removed from the survey form.

::: {.seealso}
\- `questions`{.interpreted-text role="doc"} -
`scoring`{.interpreted-text role="doc"}
:::
