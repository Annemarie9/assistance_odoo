# File: /content/odoo_doc17.0/fr/content/applications/websites/forum.md

Forum
=====

**Odoo Forum** is a question-and-answer forum designed with providing
customer support in mind. Adding a forum to a website enables you to
build a community, encourage engagement, and share knowledge.

Create a forum {#forum/create}
--------------

To create or edit a forum, go to
`Website --> Configuration --> Forum: Forums`{.interpreted-text
role="menuselection"}. Click `New`{.interpreted-text role="guilabel"} or
select an existing forum and configure the following elements.

`Forum Name`{.interpreted-text role="guilabel"}: add the name of the
forum.

`Mode`{.interpreted-text role="guilabel"}: select
`Questions`{.interpreted-text role="guilabel"} to enable marking an
answer as best, meaning questions then appear as *solved*, or
`Discussions`{.interpreted-text role="guilabel"} if the feature is not
needed.

::: {.note}
::: {.title}
Note
:::

Regardless of the selected mode, only **one answer** per user is allowed
on a single post. Commenting multiple times is allowed, however.
:::

`Default Sort`{.interpreted-text role="guilabel"}: choose how questions
are sorted by default.

> -   `Newest`{.interpreted-text role="guilabel"}: by latest question
>     posting date
> -   `Last Updated`{.interpreted-text role="guilabel"}: by latest
>     posting activity date (answers and comments included)
> -   `Most Voted`{.interpreted-text role="guilabel"}: by highest vote
>     tally
> -   `Relevance`{.interpreted-text role="guilabel"}: by post relevancy
>     (determined by a formula)
> -   `Answered`{.interpreted-text role="guilabel"}: by likelihood to be
>     answered (determined by a formula)

::: {.note}
::: {.title}
Note
:::

Users have several sorting options (total replies, total views, last
activity) on the forum front end.
:::

`Privacy`{.interpreted-text role="guilabel"}: select
`Public`{.interpreted-text role="guilabel"} to let anyone view the
forum, `Signed In`{.interpreted-text role="guilabel"} to make it visible
only for signed-in users, or `Some users`{.interpreted-text
role="guilabel"} to make it visible only for a specific user access
group by selecting one `Authorized Group`{.interpreted-text
role="guilabel"}.

Next, configure the `karma gains <forum/karma-gains>`{.interpreted-text
role="ref"} and the `karma-related rights
<forum/karma-related-rights>`{.interpreted-text role="ref"}.

### Karma points {#forum/karma}

Karma points can be given to users based on different forum
interactions. They can be used to determine which forum functionalities
users can access, from being able to vote on posts to having moderator
rights. They are also used to set user
`ranks <forum/ranks>`{.interpreted-text role="ref"}.

::: {.important}
::: {.title}
Important
:::

\- A user\'s karma points are shared across all forums, courses, etc.,
of a single Odoo website. - eLearning users can earn karma points
through different `course interactions
<elearning/karma>`{.interpreted-text role="ref"} and by
`completing quizzes <elearning/content-quiz>`{.interpreted-text
role="ref"}.
:::

#### Karma gains {#forum/karma-gains}

Several forum interactions can give or remove karma points.

  Interaction                                                Description                                                                                                     Default karma gain
  ---------------------------------------------------------- --------------------------------------------------------------------------------------------------------------- --------------------
  `Asking a question`{.interpreted-text role="guilabel"}     You post a question.                                                                                            2
  `Question upvoted`{.interpreted-text role="guilabel"}      Another user votes for a question you posted.                                                                   5
  `Question downvoted`{.interpreted-text role="guilabel"}    Another user votes against a question you posted.                                                               -2
  `Answer upvoted`{.interpreted-text role="guilabel"}        Another user votes for an answer you posted.                                                                    10
  `Answer downvoted`{.interpreted-text role="guilabel"}      Another user votes against an answer you posted.                                                                -2
  `Accepting an answer`{.interpreted-text role="guilabel"}   You mark an answer posted by another user as best.                                                              2
  `Answer accepted`{.interpreted-text role="guilabel"}       Another user marks an answer you posted as best.                                                                15
  `Answer flagged`{.interpreted-text role="guilabel"}        A question or an answer you posted is `marked as offensive <forum/moderation>`{.interpreted-text role="ref"}.   -100

::: {.note}
::: {.title}
Note
:::

New users receive **three points** upon validating their email address.
:::

To modify the default values, go to
`Website --> Configuration --> Forum: Forums`{.interpreted-text
role="menuselection"}, select the forum, and go to the
`Karma Gains`{.interpreted-text role="guilabel"} tab. Select a value to
edit it.

If the value is positive (e.g., [5]{.title-ref}), the number of points
will be added to the user\'s tally each time the interaction happens on
the selected forum. Conversely, if the value is negative (e.g.,
[-5]{.title-ref}), the number of points will be deducted. Use
[0]{.title-ref} if an interaction should not impact a user\'s tally.

#### Karma-related rights {#forum/karma-related-rights}

To configure how many karma points are required to access the different
forum functionalities, go to
`Website --> Configuration --> Forum: Forums`{.interpreted-text
role="menuselection"}, select the forum, and go to the
`Karma Related Rights`{.interpreted-text role="guilabel"} tab. Select a
value to edit it.

::: {.warning}
::: {.title}
Warning
:::

Some functionalities, such as `Edit all posts`{.interpreted-text
role="guilabel"}, `Close all posts`{.interpreted-text role="guilabel"},
`Delete all posts`{.interpreted-text role="guilabel"},
`Moderate posts`{.interpreted-text role="guilabel"}, and
`Unlink all comments`{.interpreted-text role="guilabel"}, are rather
sensitive. Make sure to understand the consequences of giving *any* user
reaching the set karma requirements access to such functionalities.
:::

  Functionality                                                                         Description                                                                                                                                                                                       Default karma requirement
  ------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------
  `Ask questions`{.interpreted-text role="guilabel"}                                    Post questions.                                                                                                                                                                                   3
  `Answer questions`{.interpreted-text role="guilabel"}                                 Post answers to questions.                                                                                                                                                                        3
  `Upvote`{.interpreted-text role="guilabel"}                                           Vote for questions or answers.                                                                                                                                                                    5
  `Downvote`{.interpreted-text role="guilabel"}                                         Vote against questions or answers.                                                                                                                                                                50
  `Edit own posts`{.interpreted-text role="guilabel"}                                   Edit questions or answers you posted.                                                                                                                                                             1
  `Edit all posts`{.interpreted-text role="guilabel"}                                   Edit any question or answer.                                                                                                                                                                      300
  `Close own posts`{.interpreted-text role="guilabel"}                                  Close questions or answers you posted.                                                                                                                                                            100
  `Close all posts`{.interpreted-text role="guilabel"}                                  Close any question or answer.                                                                                                                                                                     500
  `Delete own posts`{.interpreted-text role="guilabel"}                                 Delete questions or answers you posted.                                                                                                                                                           500
  `Delete all posts`{.interpreted-text role="guilabel"}                                 Delete any question or answer.                                                                                                                                                                    1,000
  `Nofollow links`{.interpreted-text role="guilabel"}                                   If you are under the karma threshold, a *nofollow* attribute tells search engines to ignore links you post.                                                                                       500
  `Accept an answer on own questions`{.interpreted-text role="guilabel"}                Mark an answer as best on questions you posted.                                                                                                                                                   20
  `Accept an answer to all questions`{.interpreted-text role="guilabel"}                Mark an answer as best on any question.                                                                                                                                                           500
  `Editor Features: image and links`{.interpreted-text role="guilabel"}                 Add links and images to your posts.                                                                                                                                                               30
  `Comment own posts`{.interpreted-text role="guilabel"}                                Post comments under questions or answers you created.                                                                                                                                             1
  `Comment all posts`{.interpreted-text role="guilabel"}                                Post comments under any question or answer.                                                                                                                                                       1
  `Convert own answers to comments and vice versa`{.interpreted-text role="guilabel"}   Convert comments you posted as answers.                                                                                                                                                           50
  `Convert all answers to comments and vice versa`{.interpreted-text role="guilabel"}   Convert any comment as answer.                                                                                                                                                                    500
  `Unlink own comments`{.interpreted-text role="guilabel"}                              Delete comments you posted.                                                                                                                                                                       50
  `Unlink all comments`{.interpreted-text role="guilabel"}                              Delete any comment.                                                                                                                                                                               500
  `Ask questions without validation`{.interpreted-text role="guilabel"}                 Questions you post do not require to be `validated <forum/moderation>`{.interpreted-text role="ref"} first.                                                                                       100
  `Flag a post as offensive`{.interpreted-text role="guilabel"}                         Flag a question or answer as offensive.                                                                                                                                                           500
  `Moderate posts`{.interpreted-text role="guilabel"}                                   Access all `moderation tools <forum/moderation>`{.interpreted-text role="ref"}.                                                                                                                   1,000
  `Change question tags`{.interpreted-text role="guilabel"}                             Change posted questions\' `tags <forum/tags>`{.interpreted-text role="ref"} (if you have the right to edit them).                                                                                 75
  `Create new tags`{.interpreted-text role="guilabel"}                                  Create new `tags <forum/tags>`{.interpreted-text role="ref"} when posting questions.                                                                                                              30
  `Display detailed user biography`{.interpreted-text role="guilabel"}                  When a user hovers their mouse on your avatar or username, a popover box showcases your karma points, biography, and number of `badges <forum/badges>`{.interpreted-text role="ref"} per level.   750

::: {.tip}
::: {.title}
Tip
:::

Track all karma-related activity and add or remove karma manually by
`enabling developer
mode <developer-mode>`{.interpreted-text role="ref"} and going to
`Settings --> Gamification Tools --> Karma
Tracking`{.interpreted-text role="menuselection"}.
:::

### Gamification {#forum/gamification}

Ranks and badges can be used to encourage participation. Ranks are based
on the total `karma
points <forum/karma>`{.interpreted-text role="ref"}, while badges can be
granted manually or automatically by completing challenges.

#### Ranks {#forum/ranks}

To create new ranks or modify the default ones, go to
`Website --> Configuration -->
Forum: Ranks`{.interpreted-text role="menuselection"} and click
`New`{.interpreted-text role="guilabel"} or select an existing rank.

Add the `Rank Name`{.interpreted-text role="guilabel"}, the
`Required Karma`{.interpreted-text role="guilabel"} points to reach it,
its `Description`{.interpreted-text role="guilabel"}, a
`Motivational`{.interpreted-text role="guilabel"} message to encourage
users to reach it, and an image.



#### Badges {#forum/badges}

To create new badges or modify the default ones, go to
`Website --> Configuration -->
Forum: Badges`{.interpreted-text role="menuselection"} and click
`New`{.interpreted-text role="guilabel"} or select an existing badge.

Enter the badge name and description, add an image, and configure it.

##### Assign manually

If the badge should be granted manually, select which users can grant
them by selecting one of the following
`Allowance to Grant`{.interpreted-text role="guilabel"} options:

-   `Everyone`{.interpreted-text role="guilabel"}: all non-portal users
    (since badges are granted from the backend).
-   `A selected list of users`{.interpreted-text role="guilabel"}: users
    selected under `Authorized Users`{.interpreted-text
    role="guilabel"}.
-   `People having some badges`{.interpreted-text role="guilabel"}:
    users who have been granted the badges selected under
    `Required Badges`{.interpreted-text role="guilabel"}.

It is possible to restrict how many times per month each user can grant
the badge by enabling `Monthly Limited Sending`{.interpreted-text
role="guilabel"} and entering a `Limitation Number`{.interpreted-text
role="guilabel"}.

##### Assign automatically

If the badge should be granted **automatically** when certain conditions
are met, select `No one, assigned through challenges`{.interpreted-text
role="guilabel"} under `Allowance to Grant`{.interpreted-text
role="guilabel"}.

Next, determine how the badge should be granted by clicking
`Add`{.interpreted-text role="guilabel"} under the
`Rewards for challenges`{.interpreted-text role="guilabel"} section.
Select a challenge to add it or create one by clicking
`New`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

It is possible to give the badge a `Forum Badge Level`{.interpreted-text
role="guilabel"} (`Bronze`{.interpreted-text role="guilabel"},
`Silver`{.interpreted-text role="guilabel"}, `Gold`{.interpreted-text
role="guilabel"}) to give it more or less importance.
:::



### Tags {#forum/tags}

Users can use tags to filter forum posts.

To manage tags, go to
`Website --> Configuration --> Forum: Tags`{.interpreted-text
role="menuselection"}. Click `New`{.interpreted-text role="guilabel"} to
create a tag and select the related `Forum`{.interpreted-text
role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

\- Use the `Tags`{.interpreted-text role="guilabel"} section on the
forum\'s sidebar to filter all questions assigned to the selected tag.
Click `View all`{.interpreted-text role="guilabel"} to display all tags.
- New tags can be created when posting a new message, provided the user
has enough `karma
points <forum/karma-related-rights>`{.interpreted-text role="ref"}.
:::

Use a forum {#forum/use}
-----------

::: {.note}
::: {.title}
Note
:::

Access to many functionalities depends on a user\'s `karma points
<forum/karma-related-rights>`{.interpreted-text role="ref"}.
:::

### Post questions {#forum/post}

To create a new post, access the forum\'s front end, click
`New Post`{.interpreted-text role="guilabel"}, and fill in the
following:

-   `Title`{.interpreted-text role="guilabel"}: add the question or the
    topic of the post.
-   `Description`{.interpreted-text role="guilabel"}: add a description
    for the question.
-   `Tags`{.interpreted-text role="guilabel"}: add up to five
    `tags <forum/tags>`{.interpreted-text role="ref"}.

Click `Post Your Question`{.interpreted-text role="guilabel"}.

### Interact with posts {#forum/interact}

Different actions are possible on a post.

-   Mark a question as **favorite** by clicking the star button
    (`☆`{.interpreted-text role="guilabel"}).
-   Follow a post and get **notifications** (by email or within Odoo)
    when it is answered by clicking the bell button
    (`🔔`{.interpreted-text role="guilabel"}).
-   **Vote** *for* (up arrow `▲`{.interpreted-text role="guilabel"}) or
    *against* (down arrow `▼`{.interpreted-text role="guilabel"}) a
    question or answer.
-   Mark an answer as **best** by clicking the check mark button
    (`✔`{.interpreted-text role="guilabel"}). This option is only
    available if the `Forum Mode`{.interpreted-text role="guilabel"} is
    set to `Questions`{.interpreted-text role="guilabel"}.
-   `Answer`{.interpreted-text role="guilabel"} a question.
-   **Comment** on a question or answer by clicking the speech bubble
    button (`💬`{.interpreted-text role="guilabel"}).
-   **Share** a question on Facebook, Twitter, or LinkedIn by clicking
    the *share nodes* button.

Click the ellipsis button (`...`{.interpreted-text role="guilabel"}) to:

> -   `Edit`{.interpreted-text role="guilabel"} a question or answer.
> -   `Close`{.interpreted-text role="guilabel"} a question.
> -   `Delete`{.interpreted-text role="guilabel"} a question, answer, or
>     comment. It is possible to `Undelete`{.interpreted-text
>     role="guilabel"} questions afterward.
> -   `Flag`{.interpreted-text role="guilabel"} a question or answer as
>     offensive.
> -   `Convert`{.interpreted-text role="guilabel"} a comment into an
>     answer.
> -   `View`{.interpreted-text role="guilabel"} the related
>     `Helpdesk ticket <helpdesk/forum>`{.interpreted-text role="ref"},
>     if any.



::: {.note}
::: {.title}
Note
:::

By default, 150 karma points are required to view another user\'s
profile. This value can be configured when creating a new website.
:::

Moderate a forum {#forum/moderation}
----------------

On the forum\'s front end, the sidebar\'s
`Moderation tools`{.interpreted-text role="guilabel"} section gathers
the essential moderator functionalities.



`To Validate`{.interpreted-text role="guilabel"}: access all questions
and answers waiting for validation before being displayed to
non-moderator users.



::: {.note}
::: {.title}
Note
:::

A question is pending if a user does not have the required karma. The
user is not able to post questions or answers while awaiting validation.
Only one pending question per user is allowed per forum.
:::

`Flagged`{.interpreted-text role="guilabel"}: access all questions and
answers that have been flagged as offensive. Click
`Accept`{.interpreted-text role="guilabel"} to remove the offensive flag
or `Offensive`{.interpreted-text role="guilabel"} to confirm it, then
select a reason and click `Mark as offensive`{.interpreted-text
role="guilabel"}. The post is then hidden from users without moderation
rights, and 100 karma points are deducted from the offending user\'s
tally.



`Closed`{.interpreted-text role="guilabel"}: access all questions that
have been closed. It is possible to `Delete`{.interpreted-text
role="guilabel"} or `Reopen`{.interpreted-text role="guilabel"} them. To
close a question, open it, click the ellipsis button
(`...`{.interpreted-text role="guilabel"}), then
`Close`{.interpreted-text role="guilabel"}, select a
`Close Reason`{.interpreted-text role="guilabel"}, and click
`Close post`{.interpreted-text role="guilabel"}. The post is then hidden
from users without moderation rights.

::: {.note}
::: {.title}
Note
:::

When selecting `Spam or advertising`{.interpreted-text role="guilabel"}
or `Contains offensive or malicious
remarks`{.interpreted-text role="guilabel"} as the reason, 100 karma
points are deducted from the poster\'s tally.
:::

::: {.tip}
::: {.title}
Tip
:::

\- Create and edit close reasons by going to
`Website --> Configuration --> Forum:
Close Reasons`{.interpreted-text role="menuselection"}. Select
`Basic`{.interpreted-text role="guilabel"} as
`Reason Type`{.interpreted-text role="guilabel"} if the reason should be
used when closing a question, and `Offensive`{.interpreted-text
role="guilabel"} if it should be used for flagged posts. - Manage all
posts by going to
`Website  --> Configuration --> Forum: Forums`{.interpreted-text
role="menuselection"}, selecting the forum, and clicking the
`Posts`{.interpreted-text role="guilabel"} smart button. By clicking the
`Actions`{.interpreted-text role="guilabel"} button, it is possible to
`Export`{.interpreted-text role="guilabel"}, `Archive`{.interpreted-text
role="guilabel"}, `Unarchive`{.interpreted-text role="guilabel"}, or
`Delete`{.interpreted-text role="guilabel"} one or multiple posts.
:::
