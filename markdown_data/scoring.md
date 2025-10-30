# File: /content/odoo_doc17.0/fr/content/applications/marketing/surveys/scoring.md

Scoring surveys
===============

To measure a survey participant\'s performance, knowledge, or overall
satisfaction, Odoo ascribes points to survey answers. At the end of the
survey, these points are summed up, resulting in the participant\'s
final score.

To add points to questions, open the `Surveys`{.interpreted-text
role="guilabel"} application, choose the desired survey form, and then
click on the `Options`{.interpreted-text role="guilabel"} tab. Under the
:guilabel;\`Scoring\` section, choose between
`Scoring with answers at the end`{.interpreted-text role="guilabel"} or
`Scoring without answers at the
end`{.interpreted-text role="guilabel"}.

-   `Scoring with answers at the end`{.interpreted-text role="guilabel"}
    shows the survey participant their answers after completing the
    survey, and displays which questions they got right or wrong. On
    questions where there was an incorrect answer, the correct answer
    will be highlighted.
-   `Scoring without answers at the end`{.interpreted-text
    role="guilabel"} does not show the survey participant their answer
    choices after completing the survey, only their final score.

To indicate correct answers, click on the
`Questions tab`{.interpreted-text role="guilabel"} and choose a
question. In the question form, check the
`Is a correct answer`{.interpreted-text role="guilabel"} box for the
choice that is the correct answer and attach a score value.

Back on the `Options`{.interpreted-text role="guilabel"} tab of the
survey, set the `Success %`{.interpreted-text role="guilabel"}. The
percentage entered determines what percentage of correct answers is
needed to pass the survey.

Further on the `Options`{.interpreted-text role="guilabel"} tab of the
survey, survey administrators can also choose to make the survey a
certification. A certification indicates that the survey asks questions
to test the participants\' knowledge level on a subject.

When enabling the `Is a certification`{.interpreted-text
role="guilabel"} option, choose a `Certification email
template`{.interpreted-text role="guilabel"}. The certification will
automatically be emailed using this email template to users who pass the
survey with a final score that is greater than or equal to the set
`Success %`{.interpreted-text role="guilabel"}.

In the `Candidates`{.interpreted-text role="guilabel"} section,
participants can be required to log in to take the survey. If the
`Login Required`{.interpreted-text role="guilabel"} setting is enabled,
two new options appear: the `Attempts Limit`{.interpreted-text
role="guilabel"} checkbox, which limits the number of times a
participant can attempt the survey, and the option to
`Give Badge`{.interpreted-text role="guilabel"}, located beneath the
`Certification`{.interpreted-text role="guilabel"} options in the
`Scoring`{.interpreted-text role="guilabel"} section.

{.align-center}

Badges are displayed on the eLearning portion of a given user\'s portal,
and are a way to set milestones and reward participants for passing
surveys or gaining points. Besides the awardee, website visitors who
access the `Courses`{.interpreted-text role="guilabel"} page will also
be able to see the granted badges.

{.align-center}

::: {.seealso}
`questions`{.interpreted-text role="doc"}
:::
