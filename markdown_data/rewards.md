# File: /content/odoo_doc17.0/fr/content/applications/hr/referrals/rewards.md

Rewards
=======

After employees have successfully earned referral points, they can
exchange their points by purchasing rewards in Odoo\'s *Referrals*
application. Rewards **must** be `created and
configured <referrals/create>`{.interpreted-text role="ref"} before
employees can `redeem points for rewards
<referrals/redeem>`{.interpreted-text role="ref"}.

Create rewards {#referrals/create}
--------------

Rewards are the only configurations needed when setting up the
*Referrals* application.

Only users with `Administrator`{.interpreted-text role="guilabel"}
rights for the *Recruitment* application can create or modify rewards.

To add rewards, navigate to
`Referrals app --> Configuration --> Rewards`{.interpreted-text
role="menuselection"}. Click `New`{.interpreted-text role="guilabel"},
and a reward form loads. Enter the following information on the form:

-   `Product Name`{.interpreted-text role="guilabel"}: enter the name as
    it should appear for the reward. This field is required.

-   `Cost`{.interpreted-text role="guilabel"}: enter the amount of
    points required to redeem the reward.

-   `Company`{.interpreted-text role="guilabel"}: using the drop-down
    menu, select the company the reward is configured for. If a reward
    is available for multiple companies, each company **must** configure
    a reward for their specific company. This field **only** appears if
    in a multi-company environment; if this field appears, it is
    required.

    ::: {.example}
    A corporation with three different companies offers a gift card as a
    reward. In the database, there are three separate rewards listed for
    a gift card, one for each of the three companies.
    :::

-   `Gift Responsible`{.interpreted-text role="guilabel"}: using the
    drop-down menu, select the person responsible for procuring and
    delivering the reward to the recipient. This person is alerted when
    the reward is bought in the *Referrals* application, so they know
    when to deliver the reward to the recipient.

-   `Photo`{.interpreted-text role="guilabel"}: add a photo of the
    reward, which appears on the rewards page. Hover over the image box
    in the top-right corner (a square with a camera and plus sign inside
    it), and a `fa-pencil`{.interpreted-text role="icon"}
    `(pencil)`{.interpreted-text role="guilabel"} icon appears. Click
    the `fa-pencil`{.interpreted-text role="icon"}
    `(pencil)`{.interpreted-text role="guilabel"} icon to select and add
    a photo to the reward form. Once a photo is added, hovering over the
    image reveals two icons instead of one: a
    `fa-pencil`{.interpreted-text role="icon"}
    `(pencil)`{.interpreted-text role="guilabel"} icon and a
    `fa-trash-o`{.interpreted-text role="icon"}
    `(trash can)`{.interpreted-text role="guilabel"} icon. Click the
    `fa-trash-o`{.interpreted-text role="icon"}
    `(trash can)`{.interpreted-text role="guilabel"} icon to delete the
    currently selected image.

-   `Description`{.interpreted-text role="guilabel"} tab: type in the
    description for the reward. This is visible on the reward card,
    beneath the title. This field is required.

{.align-center}

::: {.important}
::: {.title}
Important
:::

It is advised to enter a `Cost`{.interpreted-text role="guilabel"} and
add a `Photo`{.interpreted-text role="guilabel"}. If a cost is not
entered, the default cost is listed as zero, which would list the reward
as free in the reward shop. If a photo is not selected, a placeholder
icon is displayed on the rewards page.
:::

Redeem rewards {#referrals/redeem}
--------------

In order to redeem a reward, points must be earned. These points can
then be used to purchase a reward.

To purchase a reward, click the `Rewards`{.interpreted-text
role="guilabel"} button on the main `Referrals`{.interpreted-text
role="guilabel"} dashboard. All the configured rewards are listed in
individual reward cards.

The required point amount needed to purchase a reward is listed in the
top-right corner of the card.

If the user has enough points to purchase a reward, a
`fa-shopping-basket`{.interpreted-text role="icon"}
`Buy`{.interpreted-text role="guilabel"} button appears at the bottom of
the reward card. If they do not have enough points for a reward, the
reward card displays
`You need another (x) points to buy this`{.interpreted-text
role="guilabel"}, instead of a `fa-shopping-basket`{.interpreted-text
role="icon"} `Buy`{.interpreted-text role="guilabel"} button.

Click the `fa-shopping-basket`{.interpreted-text role="icon"}
`Buy`{.interpreted-text role="guilabel"} button on a reward to purchase
it. A `Confirmation`{.interpreted-text role="guilabel"} pop-up window
appears, asking if the user is sure they want to purchase the reward.
Click `OK`{.interpreted-text role="guilabel"} to purchase the item, or
`Cancel`{.interpreted-text role="guilabel"} to close the window, and
cancel the purchase.

After `OK`{.interpreted-text role="guilabel"} is clicked, the pop-up
window closes, and the points used to purchase the reward are subtracted
from the user\'s available points. The rewards presented are now updated
to reflect the user\'s current available points.

![Buy button appears below a mug and backpack reward, while the bicycle reward states how
many more reward points are needed to redeem.](rewards/redeem-rewards.png){.align-center}
