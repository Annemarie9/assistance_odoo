# File: /content/odoo_doc17.0/fr/content/applications/websites/website/configuration/multi_website.md

Multiple websites
=================

Odoo allows you to create multiple websites from the same database. This
can be useful, for example, if you have multiple brands operating under
your organization, or to create separate websites for different
products/services, or different audiences. In these cases, having
different websites can help avoid confusion and make it easier to tailor
your digital outreach strategies and reach your target audience.

Each website can be designed and configured independently with its own
`domain name
<domain_names>`{.interpreted-text role="doc"},
`theme <../web_design/themes>`{.interpreted-text role="doc"},
`pages <../pages>`{.interpreted-text role="doc"}, `menus
<../pages/menus>`{.interpreted-text role="doc"},
`languages <translate>`{.interpreted-text role="doc"}, `products
<../../ecommerce/products>`{.interpreted-text role="doc"}, assigned
sales team, etc. They can also
`share content and pages <multi-website/website_content>`{.interpreted-text
role="ref"}.

::: {.tip}
::: {.title}
Tip
:::

Duplicate content (i.e., pages and content shared between multiple
websites) can have a negative impact on `../pages/seo`{.interpreted-text
role="doc"}.
:::

Website creation
----------------

To create a new website, proceed as follows:

1.  Go to `Website --> Configuration --> Settings`{.interpreted-text
    role="menuselection"}.

2.  Click `+ New Website`{.interpreted-text role="guilabel"}.

    

3.  Specify the `Website Name`{.interpreted-text role="guilabel"} and
    `Website domain`{.interpreted-text role="guilabel"}. Each website
    must be published under its own
    `domain <domain_names>`{.interpreted-text role="doc"}.

4.  Adapt the `Company name`{.interpreted-text role="guilabel"},
    `Languages`{.interpreted-text role="guilabel"} and
    `Default language`{.interpreted-text role="guilabel"} if needed.

5.  Click the `Create`{.interpreted-text role="guilabel"} button.

You can then start building your new website.

::: {.note}
::: {.title}
Note
:::

By default, all website-related apps that you have installed (e.g.
**eCommerce**, **Forum**, **Blog**, etc.) and their related website
pages are also available on the new website. You can remove them by
amending the website\'s menu.
:::

Switching websites
------------------

To switch from one website to another, click the menu next to the
`+New`{.interpreted-text role="guilabel"} button in the top right corner
and select the website you want to switch to.



::: {.note}
::: {.title}
Note
:::

When you switch websites, you are redirected to the homepage of the
other website.
:::

Website-specific configuration
------------------------------

Most website settings are website-specific, which means they can be
enabled/disabled per website. To adapt the settings for a website, go to
`Website --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Select the desired website in the field
`Settings of Website`{.interpreted-text role="guilabel"} at the top of
the `Settings`{.interpreted-text role="guilabel"} page, in the
**yellow** banner. Then, adapt the options for that specific website.

::: {.note}
::: {.title}
Note
:::

\- Websites are created with the default settings; the settings are not
copied from one website to the other. - In a
`multi-company environment </applications/general/companies>`{.interpreted-text
role="doc"}, each website can be linked to a specific company in your
database so that only company-related data (e.g., products, jobs,
events, etc.) is displayed on the website. To display company-specific
data, set the desired company in the `Company`{.interpreted-text
role="guilabel"} field.
:::

### Content availability {#multi-website/website_content}

By default, pages, products, events, etc. created from the frontend
(using the `+New`{.interpreted-text role="guilabel"} button) are only
available on the website from which it was created. Records created from
the backend, however, are made available on all websites by default. The
content\'s availability can be changed in the backend, in the
`Website`{.interpreted-text role="guilabel"} field. For example, for
products, go to `eCommerce --> Products`{.interpreted-text
role="menuselection"}, then select the product and go to the
`Sales`{.interpreted-text role="guilabel"} tab. For forums, go to
`Configuration --> Forums`{.interpreted-text role="menuselection"}, then
select the forum.



::: {#website_field}
Records and features can be made available:
:::

-   On all websites: leave the `Website`{.interpreted-text
    role="guilabel"} field empty;
-   Only on one website: set the `Website`{.interpreted-text
    role="guilabel"} field accordingly;
-   On some websites: in this case, you should duplicate the item and
    set the `Website`{.interpreted-text role="guilabel"} field.

#### Website pages

To modify the website on which a page is to be published, proceed as
follows:

1.  Go to `Website --> Site --> Pages`{.interpreted-text
    role="menuselection"}.

2.  Open the search panel and select the website on which the page is
    currently published.

    

3.  Tick the check box next to the page(s) you want to change.

4.  Click the `Website`{.interpreted-text role="guilabel"} field and
    select the website, or empty it to publish the page on all websites.

::: {.note}
::: {.title}
Note
:::

Each website must have its own homepage; you may not use the same
homepage for several websites.
:::

eCommerce features
------------------

eCommerce features such as products, eCommerce categories, pricelists,
discounts, payment providers, etc. can be restricted to
`a specific website <website_field>`{.interpreted-text role="ref"}.

### Customer accounts

You can `allow your customers to use the same account
<../../ecommerce/customer_accounts>`{.interpreted-text role="doc"} on
all of your websites by enabling the `Shared
Customer Accounts`{.interpreted-text role="guilabel"} check box in the
website settings.

### Pricing

Products can be priced differently based on the website using
`pricelists
<ecommerce/pricelists>`{.interpreted-text role="ref"}. The following
configuration is required:

1.  Go to `Website --> Configuration --> Settings`{.interpreted-text
    role="menuselection"}.
2.  Scroll down to the `Shop - Products`{.interpreted-text
    role="guilabel"} section and select the
    `Pricelists`{.interpreted-text role="guilabel"} option
    `Multiple prices per product`{.interpreted-text role="guilabel"}.
3.  Click `Pricelists`{.interpreted-text role="guilabel"} to define new
    pricelists or edit existing ones.
4.  Select the pricelist or click `New`{.interpreted-text
    role="guilabel"} to create a new one, then select the
    `Configuration`{.interpreted-text role="guilabel"} tab and set the
    `Website`{.interpreted-text role="guilabel"} field.

Reporting
---------

### Analytics

Each website has its own
`analytics <analytics/plausible>`{.interpreted-text role="ref"}. To
switch between websites, click the buttons in the upper right corner.



### Other reporting data

Other reporting data such as eCommerce dashboard data, online sales
analyses and visitors can be grouped by website if necessary. Open the
search panel and select `Group by --> Website`{.interpreted-text
role="guilabel"}.
