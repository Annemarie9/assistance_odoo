# File: /content/odoo_doc17.0/fr/content/applications/marketing/surveys/questions.md

Create questions
================

In Odoo *Surveys*, crafting and tailoring survey questions is crucial
for `creating and
customizing surveys <../surveys/create>`{.interpreted-text role="doc"}.

Fortunately, Odoo provides numerous ways to configure tailored questions
for any kind of survey.

To access a list of *all* the questions that have been created in the
database, navigate to
`Surveys app --> Questions & Answers --> Questions`{.interpreted-text
role="menuselection"}. There, users can view and modify any question
from any survey.

However, there is only one place in the Odoo *Surveys* application where
survey questions can be created. To do that, navigate to a survey form,
by going to `Surveys app --> New`{.interpreted-text
role="menuselection"}, or by selecting any pre-existing survey from the
`Surveys`{.interpreted-text role="guilabel"} page (`Surveys app
--> Surveys`{.interpreted-text role="menuselection"}).

Questions tab
-------------

On a survey form, users can view, access, add, and/or delete questions
(and sections) in the `Questions`{.interpreted-text role="guilabel"}
tab.

By default, two columns are present in the `Questions`{.interpreted-text
role="guilabel"} tab: `Title`{.interpreted-text role="guilabel"} (i.e.
the question) and `Question Type`{.interpreted-text role="guilabel"}.

If the `Randomized per Section`{.interpreted-text role="guilabel"}
option is enabled in the `Options`{.interpreted-text role="guilabel"}
tab of the survey form, a column titled,
`# Questions Randomly Picked`{.interpreted-text role="guilabel"} appears
in the `Questions`{.interpreted-text role="guilabel"} tab.

To reveal the `Mandatory Answer`{.interpreted-text role="guilabel"}
column on the `Questions`{.interpreted-text role="guilabel"} tab, which
indicates if questions require a mandatory answer or not, click the
`(optional columns)`{.interpreted-text role="guilabel"} icon located to
the far-right of the column titles.

{.align-center}

### Create sections

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
question(s) in the survey, in order to populate the section with
specific questions that fit the theme of the section.

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

Create questions
----------------

To create questions for the survey, click
`Add a question`{.interpreted-text role="guilabel"} in the
`Questions`{.interpreted-text role="guilabel"} tab.

Clicking `Add a question`{.interpreted-text role="guilabel"} opens the
`Create Sections and Questions`{.interpreted-text role="guilabel"}
pop-up window, in which a survey question can be created.

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

When all desired configurations are complete click either
`Save & Close`{.interpreted-text role="guilabel"} to save the question
and return to the survey form, or `Save & New`{.interpreted-text
role="guilabel"} to save the question and create a new one right away in
a fresh `Create Sections and Questions`{.interpreted-text
role="guilabel"} pop-up window.

Click `Discard`{.interpreted-text role="guilabel"} to discard the
question entirely.

### Create Sections and Questions pop-up window

{.align-center}

In the `Create Sections and Questions`{.interpreted-text
role="guilabel"} pop-up window, start by typing the question into the
`Question`{.interpreted-text role="guilabel"} field, located at the top
of the pop-up window.

Then, choose the desired `Question Type`{.interpreted-text
role="guilabel"}. A preview of each `Question Type`{.interpreted-text
role="guilabel"} is to the right of the
`Question Type`{.interpreted-text role="guilabel"} field, when a
`Question Type`{.interpreted-text role="guilabel"} is selected.

Choose from the following `Question Types`{.interpreted-text
role="guilabel"}:

-   `Multiple choice: only one answer`{.interpreted-text
    role="guilabel"}: a multiple choice question, where only one answer
    is permitted.
-   `Multiple choice: multiple answers allowed`{.interpreted-text
    role="guilabel"}: a multiple choice question, where more than answer
    is permitted.
-   `Multiple Lines Text Box`{.interpreted-text role="guilabel"}: an
    open-ended question, where participants can type in a multiple line
    response.
-   `Single Line Text Box`{.interpreted-text role="guilabel"}: an
    open-ended question, where participants can type in a single line
    response.
-   `Numerical Value`{.interpreted-text role="guilabel"}: a number-based
    question, where participants must enter a number as a response.
-   `Date`{.interpreted-text role="guilabel"}: a date-based question,
    where participants must enter a date (year-month-day) as a response.
-   `Datetime`{.interpreted-text role="guilabel"}: a date-based
    question, where participants must enter a date *and* time
    (year-month-day, hour-minute-second) as a response.
-   `Matrix`{.interpreted-text role="guilabel"}: a multiple-choice,
    multiple question, in a table/chart layout, where participants are
    presented with different questions on each row, and different answer
    options on each column.

::: {.note}
::: {.title}
Note
:::

Different features appear in the `Answers`{.interpreted-text
role="guilabel"} and `Options`{.interpreted-text role="guilabel"} tabs,
depending on the chosen `Question Type`{.interpreted-text
role="guilabel"}.

However, the `Description`{.interpreted-text role="guilabel"} tab
**always** remains the same, regardless of the question type chosen.
:::

Once a `Question Type`{.interpreted-text role="guilabel"} has been
selected, there are three possible tabs where information can be
customized for the question. These include the
`Answers`{.interpreted-text role="guilabel"} tab (if applicable for the
chosen `Question Type`{.interpreted-text role="guilabel"}), the
`Description`{.interpreted-text role="guilabel"} tab, and the
`Options`{.interpreted-text role="guilabel"} tab.

Each tab offers a variety of different features, depending on what
`Question Type`{.interpreted-text role="guilabel"} was chosen.

#### Answers tab

The `Answers`{.interpreted-text role="guilabel"} tab **only** appears if
the selected `Question Type`{.interpreted-text role="guilabel"} provides
answer options to the participant.

However, if a custom response is required to answer the selected
`Question Type`{.interpreted-text role="guilabel"}, like a
`Multiple Lines Text Box`{.interpreted-text role="guilabel"}, for
example. Or, if the answer to the `Question Type`{.interpreted-text
role="guilabel"} is a number, date, or datetime, the
`Answers`{.interpreted-text role="guilabel"} tab disappears completely.

If the `Single Line Text Box`{.interpreted-text role="guilabel"} is
selected as the `Question Type`{.interpreted-text role="guilabel"}, the
`Answers`{.interpreted-text role="guilabel"} tab remains, although it
only provides two checkbox options: `Input
must be an email`{.interpreted-text role="guilabel"} and
`Save as user nickname`{.interpreted-text role="guilabel"}.

{.align-center}

If the `Input must be an email`{.interpreted-text role="guilabel"}
option is enabled, a new field, `Save as user
email`{.interpreted-text role="guilabel"} appears. If that box is
ticked, Odoo saves the participant\'s answer to that specific question
as their email address.

If the `Save as user nickname`{.interpreted-text role="guilabel"} option
is enabled, Odoo saves the participant\'s answer as its nickname.

For all other applicable `Question Type`{.interpreted-text
role="guilabel"} options that provide answer options to the participant,
the `Answers`{.interpreted-text role="guilabel"} tab appears the same.

{.align-center}

From here, users can add answer options by clicking
`Add a line`{.interpreted-text role="guilabel"}, and typing in the
various answer options for that question. Then, either press
`Enter`{.interpreted-text role="kbd"} to lock in that answer option and
immediately add another one. Or, click away to simply lock in that
answer option.

The entered answer options appear in the `Choices`{.interpreted-text
role="guilabel"} column of the `Answers`{.interpreted-text
role="guilabel"} tab.

If any *Scoring* option is enabled in the `Options`{.interpreted-text
role="guilabel"} tab of the survey form, the `Correct`{.interpreted-text
role="guilabel"} and `Score`{.interpreted-text role="guilabel"} columns
appear to the right of the `Choices`{.interpreted-text role="guilabel"}
column.

To mark an answer option as correct, tick the box beneath the
`Correct`{.interpreted-text role="guilabel"} column for the respective
question. If
`Multiple choice: multiple answers allowed`{.interpreted-text
role="guilabel"} is set as the `Question Type`{.interpreted-text
role="guilabel"}, multiple answers in the `Choices`{.interpreted-text
role="guilabel"} column can be marked as `Correct`{.interpreted-text
role="guilabel"}.

In the `Score`{.interpreted-text role="guilabel"} column, designate how
many points (if any) should be rewarded to the participant for entering
that specific answer. It is possible to enter a negative amount as the
`Score`{.interpreted-text role="guilabel"} to take points away for an
incorrect response.

The option to upload a corresponding image to accompany the answer
options is available on the question line, beneath the
`Image`{.interpreted-text role="guilabel"} column, by clicking
`Upload your file`{.interpreted-text role="guilabel"}, and uploading the
desired image.

To delete any answer option, click the
`🗑️ (trash can)`{.interpreted-text role="guilabel"} icon to the
far-right of the question line.

An exception to that is if the `Matrix`{.interpreted-text
role="guilabel"} option is selected as the `Question
Type`{.interpreted-text role="guilabel"}. If that\'s chosen, the
`Answers`{.interpreted-text role="guilabel"} tab remains, but below the
typical `Choices`{.interpreted-text role="guilabel"} section, there is a
`Rows`{.interpreted-text role="guilabel"} section. That\'s because the
`Matrix`{.interpreted-text role="guilabel"} option provides an answer
table for participants to fill out.

{.align-center}

#### Description tab

In the `Description`{.interpreted-text role="guilabel"} tab of the
`Create Sections and Questions`{.interpreted-text role="guilabel"}
pop-up window is used to provide any kind of guidelines, instructions,
or any other type of supplemental material deemed necessary to help
participants answer/understand the question.

Entering a description is **not** required.

#### Options tab

In the `Options`{.interpreted-text role="guilabel"} tab of the
`Create Sections and Questions`{.interpreted-text role="guilabel"}
pop-up window, there are four available sections:
`Answers`{.interpreted-text role="guilabel"},
`Constraints`{.interpreted-text role="guilabel"}, `Conditional
Display`{.interpreted-text role="guilabel"}, and
`Live Sessions`{.interpreted-text role="guilabel"}.

##### Answers section

::: {.note}
::: {.title}
Note
:::

Fields in the `Answers`{.interpreted-text role="guilabel"} section in
the `Options`{.interpreted-text role="guilabel"} tab of the `Create
Sections and Questions`{.interpreted-text role="guilabel"} pop-up window
vary, depending on the selected `Question Type`{.interpreted-text
role="guilabel"} and overall `Options`{.interpreted-text
role="guilabel"} configured on the survey form.
:::

###### Multiple Choice question types

If the selected `Question Type`{.interpreted-text role="guilabel"} is
either `Multiple choice: only one answer`{.interpreted-text
role="guilabel"} or
`Multiple choice: multiple answers allowed`{.interpreted-text
role="guilabel"}, there is a `Show Comments Field`{.interpreted-text
role="guilabel"} present in the `Answers`{.interpreted-text
role="guilabel"} section.

When enabled, two additional fields appear:
`Comment Message`{.interpreted-text role="guilabel"} and `Comment is an
answer`{.interpreted-text role="guilabel"}.

{.align-center}

In the `Comment Message`{.interpreted-text role="guilabel"} field, type
in a guiding message to help participants know what is expected of them
(e.g. [If other, please specify]{.title-ref}).

If the `Comment is an answer`{.interpreted-text role="guilabel"} option
is enabled, Odoo takes the participant\'s commented response as an
answer, and not just commentary on the question. This is best utilized
in surveys where there is no scoring option enabled.

###### Multiple Lines Text Box question type

If the selected `Question Type`{.interpreted-text role="guilabel"} is
`Multiple Lines Text Box`{.interpreted-text role="guilabel"}, a
`Placeholder`{.interpreted-text role="guilabel"} field appears in the
`Answers`{.interpreted-text role="guilabel"} section of the
`Options`{.interpreted-text role="guilabel"} tab.

{.align-center}

In the `Placeholder`{.interpreted-text role="guilabel"} field, enter a
guiding direction to help participants know what they should write in
the `Multiple Lines Text Box`{.interpreted-text role="guilabel"}
presented to them.

###### Single Line Text Box, Numerical Value, Date, Datetime question types

If the selected `Question Type`{.interpreted-text role="guilabel"} is
`Single Line Text Box`{.interpreted-text role="guilabel"}, `Numerical
Value`{.interpreted-text role="guilabel"}, `Date`{.interpreted-text
role="guilabel"}, or `Datetime`{.interpreted-text role="guilabel"}, two
options appear in the `Answers`{.interpreted-text role="guilabel"}
section of the `Options`{.interpreted-text role="guilabel"} tab:
`Validate Entry`{.interpreted-text role="guilabel"} and
`Placeholder`{.interpreted-text role="guilabel"}.

If the `Validate Entry`{.interpreted-text role="guilabel"} option is
enabled, two additional fields appear beneath:
`Min/Max Limits`{.interpreted-text role="guilabel"} and
`Validation Error`{.interpreted-text role="guilabel"}.

{.align-center}

In the `Min/Max Limits`{.interpreted-text role="guilabel"} field,
designate the minimum and maximum allowed quantities for that specific
question.

In the `Validation Error`{.interpreted-text role="guilabel"} field,
enter a custom message that Odoo displays when an answer is not valid.

In the `Placeholder`{.interpreted-text role="guilabel"} field, enter a
guiding direction to help participants know what they should write in
the `Multiple Lines Text Box`{.interpreted-text role="guilabel"}
presented to them.

##### Constraints section

The `Constraints`{.interpreted-text role="guilabel"} section in the
`Options`{.interpreted-text role="guilabel"} tab is the same, regardless
of the selected `Question Type`{.interpreted-text role="guilabel"}.

{.align-center}

In the `Constraints`{.interpreted-text role="guilabel"} section, there
is one option available: `Mandatory Answer`{.interpreted-text
role="guilabel"}.

When `Mandatory Answer`{.interpreted-text role="guilabel"} is enabled,
that means that specific question requires an answer from the
participant before they can move on. Also, when
`Mandatory Answer`{.interpreted-text role="guilabel"} is enabled, that
reveals an additional field: `Error Message`{.interpreted-text
role="guilabel"}.

In the `Error Message`{.interpreted-text role="guilabel"} field, enter a
custom error message prompting the participant to provide an answer for
this question.

##### Conditional Display section

`Conditional Display`{.interpreted-text role="guilabel"} means the
question is **only** displayed if a specified conditional answer(s)
(i.e. `Triggering Answers`{.interpreted-text role="guilabel"}) has been
selected in a previous question(s).

::: {.note}
::: {.title}
Note
:::

The `Conditional Display`{.interpreted-text role="guilabel"} section of
the `Options`{.interpreted-text role="guilabel"} tab is **not**
available when questions are randomly picked.
:::

There is only one field in the `Conditional Display`{.interpreted-text
role="guilabel"} section: `Triggering
Answers`{.interpreted-text role="guilabel"}.

{.align-center}

In the `Triggering Answers`{.interpreted-text role="guilabel"} field,
select specific responses from previous questions that would trigger
this question. More than one answer can be selected. Leave the field
empty if the question should always be displayed.

##### Live Sessions section

The option in the `Live Sessions`{.interpreted-text role="guilabel"}
section of the `Options`{.interpreted-text role="guilabel"} tab are
**only** supported by *Live Session* surveys.

There is only one option available in the
`Live Sessions`{.interpreted-text role="guilabel"} section: `Question
Time Limit`{.interpreted-text role="guilabel"}.

{.align-center}

When the `Question Time Limit`{.interpreted-text role="guilabel"} option
is enabled, designate how much time (in `seconds`{.interpreted-text
role="guilabel"}) participants have to answer the question during a
*Live Session* survey.

::: {.note}
::: {.title}
Note
:::

Survey text colors are directly linked to the colors used for the
`website theme
<../../websites/website/web_design/themes>`{.interpreted-text
role="doc"}.
:::
