# File: /content/odoo_doc17.0/fr/content/applications/marketing/surveys/live_session.md

Live Session surveys
====================

With the Odoo *Surveys* application, users can enhance in-person
demonstrations and presentations with the *Live Session* feature.

*Live Session* surveys function the same way as a normal survey, but
with a host or moderator, who presents the questions to participants,
reveals their responses in real-time, and controls the tempo of the
survey.

In *Live Session* surveys, participants access the survey experience via
a custom URL, and sign in with an optional access code. When the survey
has begun, the host presents one question at a time.

Then, the audience of participants submit their answer, either via their
computer or mobile device, and once the responses have been gathered,
the host reveals all the participant\'s responses, in real time, with
each answer\'s results displayed as a bar graph.

{.align-center}

Create Live Session survey
--------------------------

To create a *Live Session* survey, begin by opening the *Surveys*
application. From the `Surveys`{.interpreted-text role="guilabel"}
dashboard, click the `New`{.interpreted-text role="guilabel"} button to
reveal a blank survey form.

Any of the survey type options (`Survey`{.interpreted-text
role="guilabel"}, `Live Session`{.interpreted-text role="guilabel"},
`Assessment`{.interpreted-text role="guilabel"}, or
`Custom`{.interpreted-text role="guilabel"}), presented as radio buttons
at the top of the survey, can be used to create a *Live Session*.

However, selecting the `Live Session`{.interpreted-text role="guilabel"}
survey type radio button streamlines the process because Odoo
auto-selects the optimal settings and options for a *Live Session*
survey when that option is selected.

::: {.important}
::: {.title}
Important
:::

If the `Is a Certification`{.interpreted-text role="guilabel"} option is
enabled in the `Options`{.interpreted-text role="guilabel"} tab, the
survey **cannot** be used as a *Live Session* survey.
:::

With the desired survey radio button option selected, proceed to
`create a survey
<../surveys/create>`{.interpreted-text role="doc"} with
`questions and sections <../surveys/questions>`{.interpreted-text
role="doc"}.

While creating questions for the *Live Session* survey, open the
`Options`{.interpreted-text role="guilabel"} tab on the
`Create Sections and Questions`{.interpreted-text role="guilabel"}
pop-up form, in order to reveal the `Live
Sessions`{.interpreted-text role="guilabel"} section, which only has one
available feature: `Question Time Limit`{.interpreted-text
role="guilabel"}.

When the `Question Time Limit`{.interpreted-text role="guilabel"} option
is enabled, a new field appears beside it, wherein the user **must**
enter the desired amount of time (in seconds) the participant gets to
answer the question.

{.align-center}

### Options tab

After the questions have been created for the *Live Session* survey,
open the `Options`{.interpreted-text role="guilabel"} tab of the survey
form to further configure the survey.

The `Options`{.interpreted-text role="guilabel"} tab is organized into
four sections: `Questions`{.interpreted-text role="guilabel"}, `Time
& Scoring`{.interpreted-text role="guilabel"},
`Participants`{.interpreted-text role="guilabel"}, and
`Live Session`{.interpreted-text role="guilabel"}.

#### Questions section

Regardless of the option selected for the `Pagination`{.interpreted-text
role="guilabel"} field, the *Live Session* survey *only* shows
`One page per question`{.interpreted-text role="guilabel"}, and will
default to that option when the `Create Live Session`{.interpreted-text
role="guilabel"} button is clicked, and a *Live Session* survey
officially begins.

::: {.note}
::: {.title}
Note
:::

The `One page per question`{.interpreted-text role="guilabel"} option in
the `Pagination`{.interpreted-text role="guilabel"} field is selected by
default, and no other options appear in the
`Questions`{.interpreted-text role="guilabel"} section, when the
`Live Session`{.interpreted-text role="guilabel"} survey type radio
button is selected.
:::

The `Display Progress as`{.interpreted-text role="guilabel"} and
`Question Selection`{.interpreted-text role="guilabel"} options are
still viable and active options for *Live Session* surveys, if desired,
but they are **not** required.

However, the `Allow Roaming`{.interpreted-text role="guilabel"} feature
is **not** available during *Live Session* surveys whatsoever, as the
host/moderator controls the survey, and participants have no control
over what question they see, or when they see it.

#### Time & Scoring section

The `Survey Time Limit`{.interpreted-text role="guilabel"} option is
**not** applicable for *Live Session* surveys. This option does not even
appear in the `Time & Scoring`{.interpreted-text role="guilabel"}
section of the `Options`{.interpreted-text role="guilabel"} tab if the
`Live Session`{.interpreted-text role="guilabel"} survey type radio
button option is selected.

::: {.note}
::: {.title}
Note
:::

While the `Survey Time Limit`{.interpreted-text role="guilabel"} option
is not applicable for *Live Session* surveys, each question *can* be
affixed with its own *Question Time Limit*, via the *Options* tab of the
question pop-up form. Those question-specific time limits *do* work with
*Live Session* surveys.
:::

If desired, any `Scoring`{.interpreted-text role="guilabel"} option, and
subsequent `Required Score (%)`{.interpreted-text role="guilabel"}
option are available to use with *Live Session* surveys.

However, if the `Is a Certification`{.interpreted-text role="guilabel"}
option is enabled, the survey **cannot** be used as a *Live Session*
survey. The `Is a Certification`{.interpreted-text role="guilabel"}
option does **not** appear in the `Time & Scoring`{.interpreted-text
role="guilabel"} section of the `Options`{.interpreted-text
role="guilabel"} tab if the `Live Session`{.interpreted-text
role="guilabel"} survey type radio button option is selected.

#### Participants section

The `Access Mode`{.interpreted-text role="guilabel"} field is set to the
`Anyone with the link`{.interpreted-text role="guilabel"} option when
the survey is used as a *Live Session*. The
`Anyone with the link`{.interpreted-text role="guilabel"} option
**cannot** be modified if the `Live Session`{.interpreted-text
role="guilabel"} survey type radio button option is selected.

The `Require Login`{.interpreted-text role="guilabel"} option is
available for *Live Session* surveys. However, if the
`Live Session`{.interpreted-text role="guilabel"} survey type radio
button option is selected, the usual `Limit
Attempts`{.interpreted-text role="guilabel"} field that appears when
`Require Login`{.interpreted-text role="guilabel"} is enabled does
**not** appear, as live session participants only get to attempt the
survey once, as the host leads them through it.

#### Live Session section

The `Session Code`{.interpreted-text role="guilabel"} field allows users
to create unique codes for participants to use, in order to gain access
to the *Live Session* survey. This code can consist of any combination
of letters, numbers, and/or symbols.

The `Session Code`{.interpreted-text role="guilabel"} field is **not**
required, however, it is encouraged because it adds a level of
exclusivity to the survey and, without a
`Session Code`{.interpreted-text role="guilabel"}, the URL that appears
in the following `Session Link`{.interpreted-text role="guilabel"} field
becomes far more complex.

::: {.important}
::: {.title}
Important
:::

If a `Session Code`{.interpreted-text role="guilabel"} is **not**
entered, participants can access the survey, via the
`Session Link`{.interpreted-text role="guilabel"} without needing a
host, and the fundamental elements of the *Live Session* are lost, as
the survey is then just a normal questionnaire, without any real-time
results.
:::

With a `Session Code`{.interpreted-text role="guilabel"}, the URL in the
non-modifiable `Session Link`{.interpreted-text role="guilabel"} field
is simplified, and ends with the `Session Code`{.interpreted-text
role="guilabel"}, preceded by [/s/]{.title-ref}.

::: {.example}
If [1212]{.title-ref} has been entered as the
`Session Code`{.interpreted-text role="guilabel"}, the URL in the
`Session
Link`{.interpreted-text role="guilabel"} field begins with the basic URL
of the database (e.g. [sample-database.odoo.com]{.title-ref}), followed
by: [/s/1212]{.title-ref}.

So, collectively, that sample `Session Link`{.interpreted-text
role="guilabel"} would be:
[sample-database.odoo.com/s/1212]{.title-ref}.
:::

::: {.tip}
::: {.title}
Tip
:::

If a user sends out the `Session Link`{.interpreted-text
role="guilabel"} URL in its complete form - `Session
Code`{.interpreted-text role="guilabel"} and all - participants would
*not* need to enter in a code, as it would already be entered for them.
That complete link places the participant in a virtual waiting room,
where they simply need to wait for the host to officially start the
*Live Session* survey.

If a user sends out the `Session Link`{.interpreted-text
role="guilabel"} URL - *except* for the `Session Code`{.interpreted-text
role="guilabel"} at the end (i.e. the entire URL *through*
[\.../s/]{.title-ref}) - participants would be taken to a page, wherein
they would need to enter the specific `Session Code`{.interpreted-text
role="guilabel"} in order to access the *Live Session*.
:::

If any `Scoring`{.interpreted-text role="guilabel"} option has been
enabled, the opportunity to `Reward quick
answers`{.interpreted-text role="guilabel"} is also available with *Live
Session* surveys.

Start Live Session surveys
--------------------------

Once all the questions and configurations are complete, users can click
the `Create Live
Session`{.interpreted-text role="guilabel"} button at the top of the
survey form. Doing so opens a new browser tab to the *Session Manager*.

When the `Create Live Session`{.interpreted-text role="guilabel"} button
has been clicked, and the *Live Session* has begun, a new
`Open Session Manager`{.interpreted-text role="guilabel"} button appears
on the survey form, which opens a new browser tab to the *Session
Manager*. If the *Live Session* has already begun, that button leads the
user to the question or section the *Live Session* is currently on.

Additionally, a `Close Live Session`{.interpreted-text role="guilabel"}
button appears on the survey form. When that button is clicked, the
*Live Session* survey closes.

The *Session Manager* is controlled by the host/moderator of the *Live
Session* survey, and is typically shown on a projection or screen, so
the participants can collectively view the questions and real-time
responses, as the host/moderator guides them through the *Live Session*.

::: {.note}
::: {.title}
Note
:::

The participant can see and answer the questions from their computer or
mobile device, but the results and real-time responses can **only** be
seen on the *Session Manager*.
:::

Initially, the *Session Manager* shows the title of the *Live Session*
survey, the link needed to access it, and a
`Waiting for attendees...`{.interpreted-text role="guilabel"} counter,
which populates as participants enter the *Live Session* survey.

Once the desired amount of participants have entered the *Live Session*
survey, the host/moderator can click the `Start`{.interpreted-text
role="guilabel"} button on the right side of the *Session Manager*
window to begin the *Live Session*.

::: {.note}
::: {.title}
Note
:::

If the survey begins with a section title on the survey form, that
section title appears in the *Session Manager*, and the participant\'s
view of the survey informs them to [Pay attention to the host screen
until the next question]{.title-ref}. This message appears whenever a
section title appears during a *Live Session*.
:::

When the first question appears on the survey, the *Session Manager*
shows the question above an empty bar graph, showing the potential
answer options on the x-axis. The participants see the question and
selectable answer options on their computer or mobile device.

As participants submit their answers, a progress bar, in the upper-left
corner of the *Session Manager*, fills in. This is how *Live Session*
hosts/moderators know when every participant has submitted their
responses.

Then, when the desired amount of participants have submitted their
responses, the host/moderator clicks the
`Show Results`{.interpreted-text role="guilabel"} button on the right
side of the *Session Manager* to reveal the collective real-time
responses on the bar graph.

Once the host/moderator feels like the participants have had enough time
to view the real-time results, via the populated bar graph, they can
click the `Show Correct Answer(s)`{.interpreted-text role="guilabel"}
button on the right side of the *Session Manager* window. Doing so
highlights the correct response, if one has been designated, in green.
All incorrect responses are highlighted in red.

When the host/moderator feels the participants have had enough time to
take in the correct and incorrect responses, via the bar graph on the
*Session Manager*, they can click the `Next`{.interpreted-text
role="guilabel"} button to move on to the next portion of the survey.

Repeat this process until the survey is complete.

::: {.seealso}
\- `create`{.interpreted-text role="doc"} -
`questions`{.interpreted-text role="doc"} - `scoring`{.interpreted-text
role="doc"}
:::
