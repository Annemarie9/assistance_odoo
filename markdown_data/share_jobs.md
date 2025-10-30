# File: /content/odoo_doc17.0/fr/content/applications/hr/referrals/share_jobs.md

Share job positions
===================

In Odoo *Referrals*, users can earn referral points by sharing job
positions with potential applicants. Job positions can be shared in
several ways, through the `View Jobs
<referrals/view-jobs>`{.interpreted-text role="ref"} button and the
`Email A Friend <referrals/email-jobs>`{.interpreted-text role="ref"}
button, located at the bottom of the *Referrals* app dashboard.

::: {.note}
::: {.title}
Note
:::

Sharing jobs can **only** occur after onboarding slides have been viewed
or skipped.
:::

View Jobs {#referrals/view-jobs}
---------

To see all job positions that are actively recruiting candidates, click
the `View Jobs`{.interpreted-text role="guilabel"} button on the main
*Referrals* dashboard. This presents all job positions, with each
individual job presented with its own card.

![The \'View Jobs\' screen, displaying all current open job positions. All information is
displayed on the card.](share_jobs/jobs.png){.align-center}

Each job position card contains the following information:

-   The title of the job position. This information is taken from the
    *Job Position* field of the job form.
-   The number of `Open Positions`{.interpreted-text role="guilabel"}
    being recruited. This information is taken from the *Expected New
    Employees* field of the *Recruitment* tab of the job form.
-   The points a user earns when an applicant applies for the position.
-   The job description detailing the job position. This information is
    taken from the *Job Position* tab of the job form.

To see all the details for a job position, click the
`More Info`{.interpreted-text role="guilabel"} button on the specific
card. This opens the job position webpage in a new browser tab. This is
what an applicant sees before applying for a position.

::: {.note}
::: {.title}
Note
:::

Only published job positions are visible in the *Referrals* app. To
check which job positions are published or not, refer to the
`../recruitment/new_job`{.interpreted-text role="doc"} documentation.
:::

Refer friends
-------------

To share a job position with someone, click the
`Refer Friend`{.interpreted-text role="guilabel"} button on the specific
job position card. A pre-configured
`Send Job Offer by Mail`{.interpreted-text role="guilabel"} pop-up
window appears. Enter the recipient\'s email address in the
`Email`{.interpreted-text role="guilabel"} field.

The `Subject`{.interpreted-text role="guilabel"} and
`Body`{.interpreted-text role="guilabel"} are populated using a default
template. The `Subject`{.interpreted-text role="guilabel"} [Job for
you]{.title-ref} is present, by default, but can be modified, if
desired.

The specific title of the job position populates the *Job Position*
placeholder in the email body. The [See Job Offer]{.title-ref} text in
the email body is an individualized tracking link to the specific job
position listed on the website.

When the prospective employee receives the email, the link sends them to
the job position page, where they can apply for the position, and the
person who referred them is tracked in the *Referrals* application.

If desired, add any text or closing salutation to the email body. When
all edits have been made, click `Send Mail`{.interpreted-text
role="guilabel"} to send the email, or click `Cancel`{.interpreted-text
role="guilabel"} to close the pop-up window.

{.align-center}

Share a job
-----------

Other than sending an email, job positions can be shared, via social
media platforms, and by tracking links to the job position. At the
bottom of each job position card are four icons, and corresponding
tracking links, that can be used to share the job position, keeping
track of applicants in the *Referrals* application.

{.align-center}

### Link

To share the job position with a customized tracking link, click the
`Share Now`{.interpreted-text role="guilabel"} button with the
`fa-chain`{.interpreted-text role="icon"} `(link)`{.interpreted-text
role="guilabel"} icon above it. A `Link to Share`{.interpreted-text
role="guilabel"} pop-up window appears with the tracking link. Click
`Copy`{.interpreted-text role="guilabel"} to copy the link. After the
link is copied, click the `Close`{.interpreted-text role="guilabel"}
button to close the pop-up window. Next, share the link with the
prospective employee.

### Facebook

To share the job position using Facebook, click the
`Share Now`{.interpreted-text role="guilabel"} button with the
`fa-facebook`{.interpreted-text role="icon"}
`(Facebook)`{.interpreted-text role="guilabel"} icon above it.

If the user is already logged into Facebook, when the the
`Share Now`{.interpreted-text role="guilabel"} button is clicked, a
`Share on Facebook`{.interpreted-text role="guilabel"} page loads in a
new tab, with the link populated in the main body of the new post in a
pop-up window. If the user is *not* already logged in, a log-in screen
loads, instead, prompting the user to log-in to Facebook first.

Type in any additional information to add to the post, then share the
job position using the available options in Facebook.

### X (formerly Twitter)

A job position can also be shared on X. Click the
`Share Now`{.interpreted-text role="guilabel"} button with the
`(X)`{.interpreted-text role="guilabel"} icon above it.

If the user is already signed-in to X, when the
`Share Now`{.interpreted-text role="guilabel"} button is clicked, an X
page loads in a new tab with a pre-populated message ready to post, in a
draft pop-up window. If the user is *not* already signed-in, a sign-in
screen loads instead, prompting the user to first sign-in to X.

The default message is:

[Amazing job offer for (Job Position)! Check it live: (link to Job
Position)]{.title-ref}

Type in any additional information, or make any edits to the message,
then share using the available options in X.

### LinkedIn

To share a job position on LinkedIn, click the
`Share Now`{.interpreted-text role="guilabel"} button with the
`fa-linkedin`{.interpreted-text role="icon"}
`(LinkedIn)`{.interpreted-text role="guilabel"} icon above it.

If the user is already logged into LinkedIn, when the
`Share Now`{.interpreted-text role="guilabel"} button is clicked, a new
tab loads in LinkedIn, with a link to the job position at the top. If
the user is *not* already logged in, a log-in screen loads instead,
prompting the user to log-in to LinkedIn first.

The job position can be shared either in a public post, or in a private
message to an individual (or group of individuals).

Type in any additional information, or make any edits to the message or
post, then share using the available options in LinkedIn.

### Email a friend {#referrals/email-jobs}

Another way to share job opportunities is to share the entire current
list of open job positions, instead of one job position at a time. To do
this, navigate to the `Referrals`{.interpreted-text
role="menuselection"} main dashboard. Click the
`Email a friend`{.interpreted-text role="guilabel"} button at the bottom
of the screen. A `Send Job Offer by Mail`{.interpreted-text
role="guilabel"} pop-up window appears.

Enter the email address in the `Email`{.interpreted-text
role="guilabel"} field. The email can be sent to multiple recipients by
separating each email address with a comma followed by a single space.
The `Subject`{.interpreted-text role="guilabel"} is pre-configured with
`Job for you`{.interpreted-text role="guilabel"}, but can be edited.

The email `Body`{.interpreted-text role="guilabel"} is also populated
with pre-configured text. The text that appears is:

[Hello,]{.title-ref}

[There are some amazing job offers in my company! Have a look, they can
be interesting for you:]{.title-ref}

[See Job Offers]{.title-ref}

The `See Job Offers`{.interpreted-text role="guilabel"} text is a
tracking link to a complete list of all job positions currently being
recruited for. Add any additional text and make any edits to the message
body, if necessary. Then, click `Send Mail`{.interpreted-text
role="guilabel"} to send the email. This sends the message, and closes
the window.
