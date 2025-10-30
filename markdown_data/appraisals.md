# File: /content/odoo_doc17.0/fr/content/applications/hr/appraisals.md

show-content

:   

Appraisals
==========

In Odoo, the *Appraisals* application can be used to evaluate employee
performance on a recurring basis. Managers can evaluate the performance
of their employees, and also allow employees to do a self-assessment of
their own. Appraisals are customizable, and can be set for any kind of
schedule desired.

Appraisals give employees valuable feedback, including actionable goals
to work toward, and measurable skills to improve upon. Additionally,
appraisals may form the basis for raises, promotions, and other
benefits.

Regular appraisals are good for both the employees and the company,
since they can accurately measure performance based on company goals,
and show employees where they need to improve.

Configuration
-------------

The `Configuration`{.interpreted-text role="guilabel"} menu in the
*Appraisals* application is where the settings can be configured,
feedback templates can be edited, frequencies can be set, evaluation
scales can be managed, data for 360 feedback can be stored, and goal
tags can be viewed/created.

### Settings

To access the *Settings* menu, navigate to
`Appraisals application --> Configuration
--> Settings`{.interpreted-text role="menuselection"}.

#### Feedback templates

Feedback templates are form outlines used during an employee appraisal.
Any edits made to a template are, ultimately, reflected in the
appraisals sent to employees.

There are two default templates pre-configured in Odoo *Appraisals*: one
for employee feedback, and one for manager feedback. Each contains
several sections, along with questions, and brief explanations for how
to respond to the questions.

The `Employee Feedback Template`{.interpreted-text role="guilabel"} has
the following sections: `My work`{.interpreted-text role="guilabel"},
`My future`{.interpreted-text role="guilabel"}, and
`My feelings`{.interpreted-text role="guilabel"}.

The `Manager Feedback Template`{.interpreted-text role="guilabel"} has
the following sections: `Feedback`{.interpreted-text role="guilabel"},
`Evaluation`{.interpreted-text role="guilabel"}, and
`Improvements`{.interpreted-text role="guilabel"}.

Any desired changes to the default feedback templates can be made by
making changes directly in each template.

#### Appraisals

The `Appraisals`{.interpreted-text role="guilabel"} section of the
settings menu determines the frequency that appraisals are performed,
and if it is possible to request additional feedback.

{.align-center}

##### Appraisals plans {#appraisals/appraisal-plan}

By default, appraisals are pre-configured to be automatically created
six months after an employee is hired, with a second appraisal exactly
six months after that.

Once those two initial appraisals have been completed in the employee\'s
first year, following appraisals are only created once a year (every
twelve months).

To modify this schedule, change the number of months in the blank fields
under the `Appraisals Plans`{.interpreted-text role="guilabel"} section.

::: {.important}
::: {.title}
Important
:::

If the `Appraisals Plans`{.interpreted-text role="guilabel"} section is
modified, **all** empty `Next Appraisal
Dates`{.interpreted-text role="guilabel"} are modified for **all**
employees.
:::

##### 360 feedback

The `360 Feedback`{.interpreted-text role="guilabel"} option can be
enabled to allow managers to request feedback from other employees using
a different survey form, at any time, independent of the appraisal
schedule.

Typically, managers ask for feedback from other people who work with an
employee they manage. This includes the employee\'s various managers,
peers, and direct reports.

To view the `360 Feedback`{.interpreted-text role="guilabel"} survey,
click the `→ Internal link`{.interpreted-text role="guilabel"} icon at
the end of the `Default Template`{.interpreted-text role="guilabel"}
field. The `360 Feedback`{.interpreted-text role="guilabel"} survey
loads, and any desired changes to the survey can be made.

For more information on how to edit a survey, refer to the
`../marketing/surveys/create`{.interpreted-text role="doc"} document.

::: {.important}
::: {.title}
Important
:::

The `360 Feedback`{.interpreted-text role="guilabel"} form is a
pre-configured survey within the *Surveys* application. In order to use
the `360 Feedback`{.interpreted-text role="guilabel"} option, including
the ability to edit the survey, the *Surveys* application **must** be
installed.
:::

### Evaluation scale

On each employee appraisal form, final rating options appear by default.
To view and edit these options, navigate to
`Appraisals application --> Configuration --> Evaluation Scale`{.interpreted-text
role="menuselection"}. This presents the ratings in a list view.

The pre-configured ratings are `Needs Improvement`{.interpreted-text
role="guilabel"}, `Meets Expectations`{.interpreted-text
role="guilabel"}, `Exceeds Expectations`{.interpreted-text
role="guilabel"}, and `Strongly Exceeds Expectations`{.interpreted-text
role="guilabel"}. To add another rating, click the
`New`{.interpreted-text role="guilabel"} button.

When the `New`{.interpreted-text role="guilabel"} button is clicked on
the `Evaluation Scale`{.interpreted-text role="guilabel"} page, a blank
line appears at the bottom of the list. Enter the name of the rating in
the field.

To rearrange the order of the ratings, click the
`(six small gray boxes)`{.interpreted-text role="guilabel"} icon to the
left of a rating, and drag the rating to the desired position on the
list.

{.align-center}

### 360 feedback

The `360 Feedback`{.interpreted-text role="guilabel"} section displays
information for all the surveys currently configured in the *Appraisals*
application. To view the surveys, and their statistics, navigate to
`Appraisals application --> Configuration --> 360 Feedback`{.interpreted-text
role="menuselection"}.

{.align-center}

Each appraisal (or survey) is presented in its own line on the
`360 Feedback`{.interpreted-text role="guilabel"} page, along with
various information related to that particular appraisal.

Each appraisal includes the following information:

-   `Survey Name`{.interpreted-text role="guilabel"}: the name of the
    specific survey.
-   `Responsible`{.interpreted-text role="guilabel"}: the employee
    responsible for the survey, including the month and year they were
    given that designation.
-   `Questions`{.interpreted-text role="guilabel"}: the number of
    questions in that particular survey.
-   `Average Duration`{.interpreted-text role="guilabel"}: the average
    time a user spends completing the survey.
-   `Registered`{.interpreted-text role="guilabel"}: the number of
    people who have been sent the survey.
-   `Completed`{.interpreted-text role="guilabel"}: the number of people
    who have completed the survey.

Each appraisal also has two buttons at the end of each line: a
`Test`{.interpreted-text role="guilabel"} button and a
`See Results`{.interpreted-text role="guilabel"} button.

To see what an appraisal looks like for the end user (i.e. an employee),
click the `Test`{.interpreted-text role="guilabel"} button, and the
appraisal loads in a new browser tab. The entire appraisal loads, and
can be clicked through without having to enter any answers.

To exit, close the tab. Or, click
`This is a Test Survey. → Edit Survey`{.interpreted-text
role="guilabel"} at the top of the page to be taken to the detail form
for that particular survey.

To view the results from everyone who completed an appraisal, click the
`See Results`{.interpreted-text role="guilabel"} button. This presents
all the answers for the survey in a new tab. Each question provides
information on how many people responded to a question, and how many
people skipped it. All answers for each question are visible.

To exit, close the tab. Or, click `→ Edit Survey`{.interpreted-text
role="guilabel"} at the top of the page to be taken to the detail form
for that particular survey.

In addition to viewing the responses from past appraisals and surveys,
new surveys can also be created from the
`360 Feedback`{.interpreted-text role="guilabel"} page. Simply click the
`New`{.interpreted-text role="guilabel"} button in the top-left of the
page to create a new survey.

For more information on how to create a survey, refer to the
`../marketing/surveys/create`{.interpreted-text role="doc"} document.

::: {.note}
::: {.title}
Note
:::

In previous versions of Odoo, this section was referred to as
`Surveys`{.interpreted-text role="guilabel"}.
:::

::: {.seealso}
\- `appraisals/new_appraisals`{.interpreted-text role="doc"} -
`appraisals/goals`{.interpreted-text role="doc"} -
`appraisals/appraisal_analysis`{.interpreted-text role="doc"} -
`appraisals/skills_evolution`{.interpreted-text role="doc"}
:::

::: {.toctree titlesonly=""}
appraisals/new\_appraisals appraisals/goals
appraisals/appraisal\_analysis appraisals/skills\_evolution
:::
