# File: /content/odoo_doc17.0/fr/content/applications/hr/referrals.md

show-content

:   

Referrals
=========

Odoo\'s *Referrals* application is a centralized place where all
information regarding referrals is housed - from points earned,
coworkers hired, and rewards selected. Users can recommend people they
know for job positions, and then earn referral points as those people
progress through the recruitment pipeline. Once enough referral points
are earned, they can be exchanged for prizes. The *Referrals*
application integrates with the *Employees*, *Recruitment*, and
*Website* applications, all of which must be installed in order for the
*Referrals* application to function.

The only configurations needed for the *Referrals* application *after*
it has been installed, are related to the
`rewards <referrals/rewards>`{.interpreted-text role="doc"}; everything
else is pre-configured when Odoo *Referrals* is installed.

Users with either `Referral User`{.interpreted-text role="guilabel"},
`Officer`{.interpreted-text role="guilabel"}, or
`Administrator`{.interpreted-text role="guilabel"} access rights for the
*Recruitment* application have access to the *Referrals* application.
Only users with `Administrator`{.interpreted-text role="guilabel"}
access rights for the *Recruitment* application have access to the
`reporting <referrals/reporting>`{.interpreted-text role="doc"} and
configurations menus. For more information on users and access rights,
refer to these documents: `../general/users`{.interpreted-text
role="doc"} and `../general/users/access_rights`{.interpreted-text
role="doc"}.

Onboarding {#referrals/onboarding}
----------

When opening the *Referrals* application for the first time, a
pre-configured onboarding script appears. This is in the form of four
slides, each explaining the different parts of the *Referrals*
application. At the top of the dashboard, the following message is
displayed throughout all the onboarding slides:
`GATHER YOUR TEAM! Job Referral Program`{.interpreted-text
role="guilabel"}. Behind this main message is an image, and beneath it
some more explanatory text.

Each of the onboarding slides has a corresponding image and message that
is displayed. After reading each message, click the
`Next`{.interpreted-text role="guilabel"} button to advance to the next
slide.

The text that appears on each slide is as follows:

1.  `Oh no! Villains are lurking the city! Help us recruit a team of superheroes to save
    the day!`{.interpreted-text role="guilabel"}
2.  `Browse through open job positions, promote them on social media, or refer friends.`{.interpreted-text
    role="guilabel"}
3.  `Collect points and exchange them for awesome gifts in the shop.`{.interpreted-text
    role="guilabel"}
4.  `Compete against your colleagues to build the best justice league!`{.interpreted-text
    role="guilabel"}

::: {.note}
::: {.title}
Note
:::

The onboarding slides will appear every time the *Referrals* application
is opened, until all the slides have been viewed and the
`Start Now`{.interpreted-text role="guilabel"} button has been clicked.
If the onboarding is exited at any point, or if the
`Start Now`{.interpreted-text role="guilabel"} button has *not* been
clicked, the onboarding slides will begin again when the *Referrals*
application is opened. Once the `Start Now`{.interpreted-text
role="guilabel"} button has been clicked, the onboarding slides will not
be seen again, and the main dashboard will load when the *Referrals*
application is opened from that point on.
:::

At any point during onboarding, the `Skip`{.interpreted-text
role="guilabel"} button may be clicked. This exits the onboarding, and
the main *Referrals* dashboard loads. If `Skip`{.interpreted-text
role="guilabel"} is clicked, onboarding slides will not load anymore
when opening the *Referrals* application.

{.align-center}

::: {.note}
::: {.title}
Note
:::

If there are any candidates hired that the user had referred prior to
opening the Referrals app (meaning the onboarding slides have not
appeared before), when `Start Now`{.interpreted-text role="guilabel"} is
clicked at the end of onboarding, instead of going to the main
dashboard, a `hired
<referrals/hired>`{.interpreted-text role="ref"} screen appears instead.
:::

### Modifying onboarding slides

Onboarding slides can be modified if desired. Only users with
`Administrator`{.interpreted-text role="guilabel"} rights for the
*Recruitment* application can modify onboarding slides. To edit a slide,
navigate to
`Referrals app --> Configuration --> Onboarding.`{.interpreted-text
role="menuselection"} Each line displays the text for the individual
onboarding slide. To edit an onboarding slide, click on an individual
slide line to open the slide\'s onboarding form.

Make any changes to the message in the `Text`{.interpreted-text
role="guilabel"} field. A `Company`{.interpreted-text role="guilabel"}
may be selected, as well. However, if this field is populated, that
slide is *only* displayed for that particular company.

::: {.note}
::: {.title}
Note
:::

The `Company`{.interpreted-text role="guilabel"} field only appears when
in a multi-company database.
:::

The image can be modified, as well. Hover over the image thumbnail in
the top-right corner of the form. A `✏️ (pencil)`{.interpreted-text
role="guilabel"} icon and `🗑️ (garbage can)`{.interpreted-text
role="guilabel"} icon appear. Click the `✏️ (pencil)`{.interpreted-text
role="guilabel"} icon to change the image. A file navigator window
loads. Navigate to the desired image, select it, then click
`Open`{.interpreted-text role="guilabel"}. The new image appears in the
thumbnail. To delete an image, click the
`🗑️ (garbage can)`{.interpreted-text role="guilabel"} icon, then select
a new image using the `✏️ (pencil)`{.interpreted-text role="guilabel"}
icon.

{.align-center}

The sequence in which the slides appear can be changed from the
*Onboarding* dashboard. Click the
`(six small gray boxes)`{.interpreted-text role="guilabel"} icon to the
left of the the slide text, and drag the slide to the desired position.

{.align-center}

Hired referrals {#referrals/hired}
---------------

When a candidate that has been referred by a user is hired, the user
\"grows their superhero team\" and adds superhero avatars to their
Referrals dashboard.

After a referral has been hired, when the user next opens the Referrals
app, instead of the main dashboard, a hired page loads. The text
`(Referral Name) has been hired! Choose an avatar
for your new friend!`{.interpreted-text role="guilabel"} appears.

Below this message are five avatar thumbnails to choose from. If an
avatar has already been assigned to a referral, the thumbnail is grayed
out, and the name that the avatar has been chosen for appears beneath
the avatar. Click on an available avatar to select it.

If more than one referral was hired since opening the *Referrals*
application, after selecting the first avatar, the user is prompted to
select another avatar for the subsequent hired referral. Once all
avatars have been selected, the dashboard loads and all the avatars are
now visible. Mouse over each avatar and their name is displayed above
them.

![The hired screen. A selection of avatars are presented to chose from, with any already
chosen are greyed out.](referrals/avatars.png){.align-center}

### Modify friends

Friend avatars are able to be modified in the same manner that
`levels <referrals/levels>`{.interpreted-text role="ref"} are modified.
Only users with `Administrator`{.interpreted-text role="guilabel"}
rights for the *Recruitment* application can make modifications to
friends. The pre-configured friends can be seen and modified by
navigating to
`Referrals app --> Configuration --> Friends`{.interpreted-text
role="menuselection"}. Each friend avatar appears in the
`Dashboard Image`{.interpreted-text role="guilabel"} column, and the
corresponding name appears in the `Friend
Name`{.interpreted-text role="guilabel"} column. The default images are
a motley group of hero characters, ranging from robots to dogs.

To modify a friend\'s dashboard image, thumbnail, name, or position,
click on an individual friend to open the referral friend form. Click
`Edit`{.interpreted-text role="guilabel"} to make modifications. Type
the name in the `Friend Name`{.interpreted-text role="guilabel"} field.
The name is solely to differentiate the friends in the configuration
menu; the friend\'s name is not visible anywhere else in the *Referrals*
application.

The `Position`{.interpreted-text role="guilabel"} can be set to either
`Front`{.interpreted-text role="guilabel"} or `Back`{.interpreted-text
role="guilabel"}. This determines the position of the friend in relation
to the user\'s super hero avatar. Click the radio button next to the
desired selection, and the friend will appear either in front of or
behind the user\'s avatar when activated.

If desired, both the thumbnail `Image`{.interpreted-text
role="guilabel"} and the `Dashboard Image`{.interpreted-text
role="guilabel"} can be modified. Hover over the image being replaced to
reveal a `✏️ (pencil)`{.interpreted-text role="guilabel"} icon and
`🗑️ (garbage can)`{.interpreted-text role="guilabel"} icon. Click the
`✏️ (pencil)`{.interpreted-text role="guilabel"} icon, and a file
explorer window appears. Navigate to the desired image file, then click
`Open`{.interpreted-text role="guilabel"} to select it.

The referral friend form automatically saves, but can be saved manually
at any time by clicking the *Save manually* option, represented by a
`(cloud upload)`{.interpreted-text role="guilabel"} icon, located in the
top-left corner. To cancel any changes made, click the
`✖️ (Discard all changes)`{.interpreted-text role="guilabel"} icon to
delete any changes, and revert to the original content.

{.align-center}

::: {.warning}
::: {.title}
Warning
:::

It is not advised to edit the images. An image file must have a
transparent background in order for it to render properly. Only users
with knowledge about transparent images should attempt adjusting any
images in the *Referrals* application.

Once an image is changed and the friend is saved, it is **not possible**
to revert to the original image. To revert to the original image, the
*Referrals* application must be *uninstalled then reinstalled.*
:::

Levels {#referrals/levels}
------

The *Referrals* application has pre-configured levels that are reflected
in the user\'s avatar on the Referrals dashboard. As a user refers
potential employees and earns points, they can *level up*, much like in
a video game.

Levels have no functional impact on the performance of the application.
They are solely used for the purpose of adding achievement tiers for
participants to aim for, gamifying referrals for the user.

The user\'s current level is displayed at the top of the main
*Referrals* application dashboard, directly beneath their photo, in a
`Level: X`{.interpreted-text role="guilabel"} format. In addition, a
colored ring appears around the user\'s photo, indicating how many
points the user currently has, and how many additional points they need
to level up. The cyan colored portion of the ring represents points
earned, while the white colored portion represents the points still
needed before they can level up.

### Modify levels

Only users with `Administrator`{.interpreted-text role="guilabel"}
rights for the *Recruitment* application can modify levels. The
pre-configured levels can be seen and modified by navigating to
`Referrals app --> Configuration --> Levels`{.interpreted-text
role="menuselection"}. Each avatar appears in the
`Image`{.interpreted-text role="guilabel"} column, and the corresponding
level number appears in the `Level Name`{.interpreted-text
role="guilabel"} column. The default images are of Odoo superheroes, and
each level adds an additional element to their avatar, such as capes and
shields.

To modify a level\'s image, name, or points required to reach the level,
click on an individual level in the list to open the level form, then
make modifications.

Type in the name (or number) of the level in the
`Level Name`{.interpreted-text role="guilabel"} field. What is entered
is displayed beneath the user\'s photo on the main dashboard when they
reach that level. Enter the number of referral points needed to reach
that level in the `Requirements`{.interpreted-text role="guilabel"}
field. The points needed to level up are the total accumulated points
earned over the lifetime of the employee, not additional points from the
previous level that must be earned.

If desired, the `Image`{.interpreted-text role="guilabel"} can also be
modified. Hover over the image to reveal a
`✏️ (pencil)`{.interpreted-text role="guilabel"} icon and
`🗑️ (garbage can)`{.interpreted-text role="guilabel"} icon. Click the
`✏️
(pencil)`{.interpreted-text role="guilabel"} icon, and a file explorer
window appears. Navigate to the desired image file, then click
`Open`{.interpreted-text role="guilabel"} to select it.

The level form saves automatically, but can be saved manually at any
time by clicking the *save manually* option, represented by a
`(cloud upload)`{.interpreted-text role="guilabel"} icon, located in the
top-left corner. To cancel any changes made, click the
`✖️ (Discard all changes)`{.interpreted-text role="guilabel"} icon to
delete any changes, and revert to the original content.

{.align-center}

::: {.warning}
::: {.title}
Warning
:::

It is not advised to edit the images. An image file must have a
transparent background in order for it to render properly. Only users
with knowledge about transparent images should attempt adjusting any
images in the *Referrals* application.

Once an image is changed and the level is saved, it is **not possible**
to revert to the original image. To revert to the original image, the
*Referrals* application must be *uninstalled then reinstalled.*
:::

### Level up

Once enough points have been accumulated to level up, the circle around
the user\'s photo is completely filled in with a cyan color, a large
image stating `Level up!`{.interpreted-text role="guilabel"} appears
above the photo, and the phrase `Click to level up!`{.interpreted-text
role="guilabel"} appears beneath the user\'s photo and current level.

Click on either the `LEVEL UP!`{.interpreted-text role="guilabel"}
graphic, the user\'s photo, or the text `Click to
level up!`{.interpreted-text role="guilabel"} beneath the user\'s photo
to level up the user. The user\'s avatar changes to the current level,
and the ring around the photo is updated to indicate the current amount
of points.

Leveling up does not cost the user any points, the user simply needs to
earn the specified amount of points required.

![A \'Click to level up!\' appears beneath the user\'s image, and a large \'Level up!\' appears
above their image.](referrals/level-up.png){.align-center}

::: {.note}
::: {.title}
Note
:::

Once a user has reached the highest configured level, they will continue
to accrue points that can be redeemed for rewards, but they are no
longer able to level up. The ring around their photo remains solid cyan.
:::

::: {.seealso}
\- `referrals/share_jobs`{.interpreted-text role="doc"} -
`referrals/points`{.interpreted-text role="doc"} -
`referrals/rewards`{.interpreted-text role="doc"} -
`referrals/alerts`{.interpreted-text role="doc"} -
`referrals/reporting`{.interpreted-text role="doc"}
:::

::: {.toctree}
referrals/share\_jobs referrals/points referrals/rewards
referrals/alerts referrals/reporting
:::
