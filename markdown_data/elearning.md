# File: /content/odoo_doc17.0/fr/content/applications/websites/elearning.md

eLearning
=========

The **eLearning** app allows you to easily upload content, define
learning objectives, manage attendees, assess students\' progress, and
even set up rewards. Engaging participants in a meaningful learning
experience enhances their attentiveness and fosters heightened
productivity.

::: {.important}
::: {.title}
Important
:::

You can manage your eLearning content on the **front end** or the **back
end**. The **front end** allows you to create content quickly from your
website, while the **back end** provides additional options and allows
collaboration. This documentation focuses on using the back end to
create your content.
:::

::: {.seealso}

:::

Courses {#elearning/courses}
-------

To get an overview of all courses, go to
`eLearning --> Courses --> Courses`{.interpreted-text
role="menuselection"}.

Click on a course card to edit the course on the back end. Click
`View course`{.interpreted-text role="guilabel"} to access the course on
the front end.

### Course creation {#elearning/course-creation}

Click `New`{.interpreted-text role="guilabel"} to create a new course.
In the form that opens, add a `Course Title`{.interpreted-text
role="guilabel"} and one or more `Tags`{.interpreted-text
role="guilabel"} to categorize the course and `allow users
to filter courses based on their tags <elearning/course-groups>`{.interpreted-text
role="ref"}. To add an image to illustrate the course, hover your mouse
on the camera placeholder image and click on
`fa-pencil`{.interpreted-text role="icon"} `(Edit)`{.interpreted-text
role="guilabel"}.

Four tabs allow you to edit your course further:
`Content <elearning/content>`{.interpreted-text role="ref"},
`Description <elearning/description>`{.interpreted-text role="ref"},
`Options <elearning/options>`{.interpreted-text role="ref"}, and
`Karma <elearning/karma>`{.interpreted-text role="ref"}.



#### Content tab {#elearning/content}

This tab allows you to manage the course content. Click
`Add Section`{.interpreted-text role="guilabel"} to divide the course
into different sections. Click `Add Content`{.interpreted-text
role="guilabel"} to create `content items
<elearning/content-creation>`{.interpreted-text role="ref"}. Click
`Add Certification`{.interpreted-text role="guilabel"} to assess the
attendees\' level of understanding, certify their skills, and motivate
them. **Certification** is part of the
`Surveys <../marketing/surveys/create>`{.interpreted-text role="doc"}
app.

#### Description tab {#elearning/description}

You can add a short description or information related to the course in
the `Description`{.interpreted-text role="guilabel"} tab. It appears
under the course title on your website.



#### Options tab {#elearning/options}

In the `Options`{.interpreted-text role="guilabel"} tab, different
configurations are available:
`Course <elearning/options-course>`{.interpreted-text role="ref"},
`Communication <elearning/options-communication>`{.interpreted-text
role="ref"},
`Access rights <elearning/options-access-rights>`{.interpreted-text
role="ref"}, and `Display
<elearning/options-display>`{.interpreted-text role="ref"}.



##### Course {#elearning/options-course}

Assign a `Responsible`{.interpreted-text role="guilabel"} user for the
course. If you have multiple websites, use the
`Website`{.interpreted-text role="guilabel"} field to display the course
only on the selected website.

##### Communication {#elearning/options-communication}

-   `Allow Reviews`{.interpreted-text role="guilabel"}: Enable this
    option to allow attendees to like, comment on, and submit reviews
    for the course content.
-   `Forum`{.interpreted-text role="guilabel"}: Add a dedicated forum to
    the course (only shown if the `Forum`{.interpreted-text
    role="guilabel"} feature is enabled in the
    `eLearning settings <elearning/settings>`{.interpreted-text
    role="ref"}).
-   `New Content Notification`{.interpreted-text role="guilabel"}:
    Select an email template to send emails to attendees when you upload
    new content items. Click on `oi-arrow-right`{.interpreted-text
    role="icon"} `Internal link`{.interpreted-text role="guilabel"} to
    access the email template editor.
-   `Completion Notification`{.interpreted-text role="guilabel"}: Select
    an email template to send emails to attendees once they reach the
    end of the course. Click on `oi-arrow-right`{.interpreted-text
    role="icon"} `Internal link`{.interpreted-text role="guilabel"} to
    access the email template editor.

::: {.note}
::: {.title}
Note
:::

If the `Mailing`{.interpreted-text role="guilabel"} feature is enabled
in the `eLearning settings
<elearning/settings>`{.interpreted-text role="ref"}, a
`Contact Attendees`{.interpreted-text role="guilabel"} button at the top
left of the course form allows you to send mass mailings to people
enrolled in the course.
:::

##### Access rights {#elearning/options-access-rights}

-   `Prerequisites`{.interpreted-text role="guilabel"}: Set one or more
    other courses that users are advised to complete before accessing
    the course.

-   `Prerequisite Of`{.interpreted-text role="guilabel"}: If the course
    has been defined as a prerequisite for one or more courses, this
    read-only field displays the course name(s).

-   `Show course to`{.interpreted-text role="guilabel"}: Define who can
    access the course and its content. Select
    `Everyone`{.interpreted-text role="guilabel"},
    `Signed In`{.interpreted-text role="guilabel"}, or
    `Course Attendees`{.interpreted-text role="guilabel"}.

-   `Enroll Policy`{.interpreted-text role="guilabel"}: Define how
    people enroll in the course. Select:

    > -   `Open`{.interpreted-text role="guilabel"}: to make the course
    >     available to anyone.
    >
    > -   `On Invitation`{.interpreted-text role="guilabel"}: to
    >     restrict enrollment to invited attendees only. If enabled,
    >     provide an `Enroll Message`{.interpreted-text role="guilabel"}
    >     explaining the enrollment process. This message is displayed
    >     on your website beneath the course title. To send invite to
    >     attendees, click `Invite`{.interpreted-text role="guilabel"}
    >     and either`Copy`{.interpreted-text role="guilabel"} the link
    >     or toggle `Send by Email`{.interpreted-text role="guilabel"}
    >     to send the invitation via email.
    >
    > -   `On Payment`{.interpreted-text role="guilabel"}: to restrict
    >     enrollment to users who purchase the course. If enabled,
    >     select the `Product`{.interpreted-text role="guilabel"} to be
    >     used. This option requires the
    >     `Paid Courses`{.interpreted-text role="guilabel"} feature to
    >     be enabled in the
    >     `eLearning settings <elearning/settings>`{.interpreted-text
    >     role="ref"}.
    >
    >     > ::: {.note}
    >     > ::: {.title}
    >     > Note
    >     > :::
    >     >
    >     > Only products set up with `Course`{.interpreted-text
    >     > role="guilabel"} as their `Product Type`{.interpreted-text
    >     > role="guilabel"} are available for selection.
    >     > :::

##### Display {#elearning/options-display}

-   `Training`{.interpreted-text role="guilabel"}: The course content
    appears as a training program, and the courses must be taken in the
    proposed order.
-   `Documentation`{.interpreted-text role="guilabel"}: The content is
    available in any order. Use the `Featured
    Content`{.interpreted-text role="guilabel"} field to define which
    content items are promoted on the course homepage.

#### Karma tab {#elearning/karma}

This tab is about gamification to make eLearning fun and interactive.

In the `Rewards`{.interpreted-text role="guilabel"} section, choose how
many karma points you want to grant attendees when they
`Review`{.interpreted-text role="guilabel"} or
`Finish`{.interpreted-text role="guilabel"} a course.

In the `Access Rights`{.interpreted-text role="guilabel"} section,
define the karma points needed to `Add Review`{.interpreted-text
role="guilabel"}, `Add Comment`{.interpreted-text role="guilabel"}, or
`Vote`{.interpreted-text role="guilabel"} on the course.

### Course groups {#elearning/course-groups}

**Course Groups** allow users to filter the
`All Courses`{.interpreted-text role="guilabel"} dashboard on your
website and find the course that meets their interests, needs, level,
etc.

To manage them, go to
`eLearning --> Configuration --> Course Groups`{.interpreted-text
role="menuselection"}. Click `New`{.interpreted-text role="guilabel"} to
create a new course group. Add the `Course Group Name`{.interpreted-text
role="guilabel"}, enable `Menu Entry`{.interpreted-text role="guilabel"}
to allow users to search by course group on the website, and add tags in
the `Tag Name`{.interpreted-text role="guilabel"} column. For each tag,
you can select a corresponding color.

### Settings {#elearning/settings}

The following options are available in the eLearning settings. Go to
`eLearning -->
Configuration --> Settings`{.interpreted-text role="menuselection"},
then enable the desired feature:

-   `Certifications`{.interpreted-text role="guilabel"}: Assess
    attendees\' knowledge and provide official certification of their
    skills.
-   `Paid Courses`{.interpreted-text role="guilabel"}: Sell course
    access directly through your website and track revenue.
-   `Mailing`{.interpreted-text role="guilabel"}: Send mass mailings to
    keep all attendees informed and up to date.
-   `Forum`{.interpreted-text role="guilabel"}: Build a community space
    where attendees can ask questions and help each other.

Content {#elearning/content-creation}
-------

To manage course content, go to
`eLearning --> Courses --> Contents`{.interpreted-text
role="menuselection"}. Click `New`{.interpreted-text role="guilabel"} to
create a content item. Add the `Content Title`{.interpreted-text
role="guilabel"} and any desired
`Tags <elearning/content-tags>`{.interpreted-text role="ref"}, then fill
in the required information in the different tabs.



::: {.tip}
::: {.title}
Tip
:::

You can also create new content from within a course. Go to
`eLearning --> Courses
--> Courses`{.interpreted-text role="menuselection"}, click the relevant
course card, then click `Add content`{.interpreted-text role="guilabel"}
at the bottom of the `Content`{.interpreted-text role="guilabel"} tab.
:::

### Document tab {#elearning/content-document}

For each content type, provide the following information:

-   `Course`{.interpreted-text role="guilabel"}: Select the course to
    which the content item belongs.
-   `Content Type`{.interpreted-text role="guilabel"}: Select the
    relevant `content type <elearning/content-type>`{.interpreted-text
    role="ref"} and provide the required information.
-   `Responsible`{.interpreted-text role="guilabel"}: Select the user
    responsible for the content item. By default, this is the user who
    creates the course, but another user can be selected.
-   `Duration`{.interpreted-text role="guilabel"}: Enter the time
    required to complete the lesson.
-   `Allow Preview`{.interpreted-text role="guilabel"}: Enable this if
    the content should be accessible to anyone.

::: {.note}
::: {.title}
Note
:::

If the `Content Type <elearning/content-type>`{.interpreted-text
role="ref"} is `Document`{.interpreted-text role="guilabel"}, enabling
`Allow Download`{.interpreted-text role="guilabel"} allows users to
download the content.
:::

Two read-only fields provide data about how often the content item is
viewed:

-   `# of Public Views`{.interpreted-text role="guilabel"}: displays the
    number of views from non-enrolled participants.
-   `# Total Views`{.interpreted-text role="guilabel"}: displays the
    total number of views (non-enrolled and enrolled participants).



#### Content types {#elearning/content-type}

You can add the following content types:

-   `Image`{.interpreted-text role="guilabel"}: To upload an image,
    select `Upload from Device`{.interpreted-text role="guilabel"},
    click `Upload your file`{.interpreted-text role="guilabel"}, then
    select the relevant file. Supported formats include JPG, JPEG, PNG,
    SVG, GIF, and WEBP. The maximum file size is 25MB.

    Alternatively, to add an image saved on Google Drive, select
    `Retrieve from Google
    Drive`{.interpreted-text role="guilabel"}, then add the Google Drive
    link to the image.

-   `Article`{.interpreted-text role="guilabel"}: Articles are website
    pages that are customized using the website builder on your
    website\'s front end.

    With the `Course`{.interpreted-text role="guilabel"} selected, click
    the `Go to Website`{.interpreted-text role="guilabel"} smart button,
    then, at the top-right of the screen, click
    `fa-pencil`{.interpreted-text role="icon"}
    `(Edit)`{.interpreted-text role="guilabel"}. Write the article\'s
    content and
    `customize the page using the website builder </applications/websites/website/web_design>`{.interpreted-text
    role="doc"}.

-   `Document`{.interpreted-text role="guilabel"}: To upload a document,
    select `Upload from Device`{.interpreted-text role="guilabel"},
    click `Upload your file`{.interpreted-text role="guilabel"}, then
    select the relevant file. Only PDF documents can be uploaded.

    Alternatively, to add a Google Slides presentation, Google Doc
    document, or Google Sheets spreadsheet, click
    `Retrieve from Google Drive`{.interpreted-text role="guilabel"} and
    add the Google Drive link to the file.

-   `Video`{.interpreted-text role="guilabel"}: Add the YouTube, Google
    Drive, or Vimeo link to the video.

-   `Quiz`{.interpreted-text role="guilabel"}: Open the
    `Quiz tab <elearning/content-quiz>`{.interpreted-text role="ref"} to
    create a quiz.

### Description tab {#elearning/content-description}

Add a description for the content. This text is displayed in the
`About`{.interpreted-text role="guilabel"} section of the content item
on your website.

### Additional Resources tab {#elearning/content-additional-resources}

Click `Add a line`{.interpreted-text role="guilabel"} to add a link or a
file that supports your participants\' learning. The resource appears in
the course content on your website.



### Quiz tab {#elearning/content-quiz}

From this tab, you can create a quiz to assess your students at the end
of the course.

The `Points Rewards`{.interpreted-text role="guilabel"} section allows
you to assign karma points based on how many attempts are needed to
answer correctly. To create a question, click
`Add a line`{.interpreted-text role="guilabel"}, enter the
`Question Name`{.interpreted-text role="guilabel"}, and add possible
answers. Mark the correct answer(s) by selecting
`Is correct answer`{.interpreted-text role="guilabel"}. You can also use
the `Comment`{.interpreted-text role="guilabel"} field to provide
additional information when an answer is selected.

### Content Tags {#elearning/content-tags}

**Content Tags** are visible on the `Contents`{.interpreted-text
role="guilabel"} dashboard of a course on your website, and can help
users identify the kind of content a particular lesson contains, e.g.,
theory, or exercises.

To manage content tags, go to
`eLearning --> Configuration --> Content Tags`{.interpreted-text
role="menuselection"}. Click `New`{.interpreted-text role="guilabel"} to
create a new tag.

Publish courses and content {#elearning/publish-content}
---------------------------

Courses and content items must be published from the front end to be
available to your audience. To access the front end, click the
`Go to Website`{.interpreted-text role="guilabel"} smart button at the
top of the course form or an individual content form.

A course and its content items are published separately:

-   To publish a course, access the main course page, then toggle the
    switch in the upper-right corner from
    `Unpublished`{.interpreted-text role="guilabel"} to
    `Published`{.interpreted-text role="guilabel"}.
-   To publish individual content items, click on an item to open it,
    then toggle the switch from `Unpublished`{.interpreted-text
    role="guilabel"} to `Published`{.interpreted-text role="guilabel"}.



::: {.tip}
::: {.title}
Tip
:::

When publishing a new course, publish the individual content items
before publishing the course itself. Published content is only available
to your audience once the course it is part of is published.
:::

To unpublish a course or an individual content item, open the course or
item, then toggle the switch from `Published`{.interpreted-text
role="guilabel"} to `Unpublished`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

Unpublishing a course renders the course *and* its content unavailable
to your audience.
:::
