# File: /content/odoo_doc17.0/fr/content/applications/websites/website/pages.md

show-content

:   

Pages
=====

Odoo allows you to create pages for your website and customize their
content and appearance to your needs.

::: {#website/page_type}
**Static** pages have stable content, such as the homepage. You can
manually create new ones, define their URLs, adapt their
`properties <website/page_properties>`{.interpreted-text role="ref"},
etc. **Dynamic** pages, on the other hand, are generated dynamically.
All pages generated automatically by Odoo, for example, when you install
an app or module (e.g., [/shop]{.title-ref} or [/blog]{.title-ref}) or
publish a new product or blog post, are dynamic pages and are therefore
managed differently.
:::

Page creation
-------------

Website pages can be created from the **frontend** and the **backend**.
To create a new website page, proceed as follows:

> 1.  -   Either open the **Website** app, click
>         `+ New`{.interpreted-text role="guilabel"} in the top-right
>         corner, then select `Page`{.interpreted-text role="guilabel"};
>     -   Or go to `Website --> Site --> Pages`{.interpreted-text
>         role="menuselection"} and click `New`{.interpreted-text
>         role="guilabel"}.
>
> 2.  Enter a `Page Title`{.interpreted-text role="guilabel"}; this
>     title is used in the menu and the page\'s URL.
>
> 3.  Click `Create`{.interpreted-text role="guilabel"}.
>
> 4.  Customize the page\'s content and appearance using the website
>     builder, then click `Save`{.interpreted-text role="guilabel"}.
>
> 5.  `Publish <website/un-publish-page>`{.interpreted-text role="ref"}
>     the page.

::: {.note}
::: {.title}
Note
:::

Disable `Add to menu`{.interpreted-text role="guilabel"} if the page
should not appear in the menu.
:::

Page management
---------------

### Publishing/unpublishing pages {#website/un-publish-page}

Pages need to be published to make them accessible to website visitors.
To publish or unpublish a page, access it and toggle the switch in the
upper-right corner from `Unpublished`{.interpreted-text role="guilabel"}
to `Published`{.interpreted-text role="guilabel"}, or vice versa.



::: {.note}
::: {.title}
Note
:::

It is also possible to:

-   publish/unpublish a page from the
    `page properties <website/page_properties>`{.interpreted-text
    role="ref"}, where you can define a publishing date and/or restrict
    the page\'s visibility if needed;
-   publish/unpublish several pages at once: go to
    `Website --> Site --> Pages`{.interpreted-text
    role="menuselection"}, select the pages, then click
    `Action`{.interpreted-text role="guilabel"} and select
    `Publish`{.interpreted-text role="guilabel"} or
    `Unpublish`{.interpreted-text role="guilabel"}.
:::

### Homepage

When you create a website, Odoo creates a dedicated
`Home`{.interpreted-text role="guilabel"} page by default, but you can
define any website page as your homepage. To do so, go to
`Website --> Configuration
--> Settings`{.interpreted-text role="menuselection"}, then, in the
`Website info`{.interpreted-text role="guilabel"} section, define the
URL of the desired page in the field `Homepage URL`{.interpreted-text
role="guilabel"} (e.g., [/shop]{.title-ref}).

Alternatively, you can define any
`static page <website/page_type>`{.interpreted-text role="ref"} as your
homepage by going to `Website --> Site --> Properties`{.interpreted-text
role="menuselection"}. Select the `Publish`{.interpreted-text
role="guilabel"} tab and enable `Use as Homepage`{.interpreted-text
role="guilabel"}.

### Page properties {#website/page_properties}

To modify a `static page's <website/page_type>`{.interpreted-text
role="ref"} properties, access the page you wish to modify, then go to
`Site --> Properties`{.interpreted-text role="menuselection"}.

The `Name`{.interpreted-text role="guilabel"} tab allows you to:

-   rename the page using the `Page Name`{.interpreted-text
    role="guilabel"} field;

-   modify the `Page URL`{.interpreted-text role="guilabel"}. In this
    case, you can redirect the old URL to the new one if needed. To do
    so, enable `Redirect Old URL`{.interpreted-text role="guilabel"},
    then select the `Type`{.interpreted-text role="guilabel"} of
    `redirection <website/URL-redirection>`{.interpreted-text
    role="ref"}:

    -   `301 Moved permanently`{.interpreted-text role="guilabel"}: to
        redirect the page permanently;
    -   `302 Moved temporarily`{.interpreted-text role="guilabel"}: to
        redirect the page temporarily.

    

You can further adapt the page\'s properties in the
`Publish`{.interpreted-text role="guilabel"} tab:

-   `Show in Top Menu`{.interpreted-text role="guilabel"}: Disable if
    you don\'t want the page to appear in the menu;
-   `Use as Homepage`{.interpreted-text role="guilabel"}: Enable if you
    want the page to be the homepage of your website;
-   `Indexed`{.interpreted-text role="guilabel"}: Disable if you don\'t
    want the page to be shown in search engine results;
-   `Published`{.interpreted-text role="guilabel"}: Enable to publish
    the page;
-   `Publishing Date`{.interpreted-text role="guilabel"}: To publish the
    page at a specific moment, select the date, click the clock icon to
    set the time, then click the green check mark to validate your
    selection.
-   `Visibility`{.interpreted-text role="guilabel"}: Select who can
    access the page:
    -   `All`{.interpreted-text role="guilabel"}
    -   `Signed In`{.interpreted-text role="guilabel"}
    -   `Restricted Group`{.interpreted-text role="guilabel"}: Select
        the `user access group(s)
        </applications/general/users/access_rights>`{.interpreted-text
        role="doc"} in the `Authorized group`{.interpreted-text
        role="guilabel"} field.
    -   `With Password`{.interpreted-text role="guilabel"}: Enter the
        password in the `Password`{.interpreted-text role="guilabel"}
        field.

::: {.tip}
::: {.title}
Tip
:::

*Some* of these properties can also be modified from
`Website --> Site --> Pages`{.interpreted-text role="menuselection"}.
:::

#### Duplicating pages

To duplicate a page, access the page, then go to
`Site --> Properties`{.interpreted-text role="menuselection"} and click
`Duplicate Page`{.interpreted-text role="guilabel"}. Enter a
`Page Name`{.interpreted-text role="guilabel"}, then click
`OK`{.interpreted-text role="guilabel"}. By default, the new page is
added after the duplicated page in the menu, but you can remove it from
the menu or change its position using the
`menu editor <pages/menus>`{.interpreted-text role="doc"}.

#### Deleting pages {#website/delete-page}

To delete a page, proceed as follows:

1.  Access the page, then go to `Site --> Properties`{.interpreted-text
    role="menuselection"} and click `Delete
    Page`{.interpreted-text role="guilabel"}.
2.  A pop-up window appears on the screen with all links referring to
    the page you want to delete, organized by category. To ensure
    website visitors don\'t land on a 404 error page, you must update
    all the links on your website referring to the page. To do so,
    expand a category, then click on a link to open it in a new window.
    Alternatively, you can set up a `redirection
    <website/URL-redirection>`{.interpreted-text role="ref"} for the
    deleted page.
3.  Once you have updated the links (or set up a
    `redirection <website/URL-redirection>`{.interpreted-text
    role="ref"}), select the `I am sure about this`{.interpreted-text
    role="guilabel"} check box, then click `OK`{.interpreted-text
    role="guilabel"}.

### URL redirect mapping {#website/URL-redirection}

URL redirect mapping consists in sending visitors and search engines to
a URL different from the one they initially requested. This technique is
used, for example, to prevent broken links when you
`delete a page <website/delete-page>`{.interpreted-text role="ref"},
`modify its URL <website/page_properties>`{.interpreted-text
role="ref"}, or migrate your site from another platform to an Odoo
`domain <configuration/domain_names>`{.interpreted-text role="doc"}. It
can also be used to improve `pages/seo`{.interpreted-text role="doc"}.

To access existing URL redirections and create new ones,
`activate the developer mode
</applications/general/developer_mode>`{.interpreted-text role="doc"}
and go to `Website --> Configuration -->
Redirects`{.interpreted-text role="menuselection"}.

::: {.note}
::: {.title}
Note
:::

\- A redirect record is added automatically every time you
`modify a page's URL
<website/page_properties>`{.interpreted-text role="ref"} and enable
`Redirect Old URL`{.interpreted-text role="guilabel"}. - You can set up
redirections for
`static and dynamic pages <website/page_type>`{.interpreted-text
role="ref"}.
:::

To create a new redirection, click the `New`{.interpreted-text
role="guilabel"} button, then fill in the fields:

-   `Name`{.interpreted-text role="guilabel"}: Enter a name to identify
    the redirect.

-   `Action`{.interpreted-text role="guilabel"}: Select the type of
    redirection:

    > -   `404 Not found`{.interpreted-text role="guilabel"}: visitors
    >     are redirected to a 404 error page when they try to access an
    >     unpublished or deleted page.
    > -   `301 Moved Permanently`{.interpreted-text role="guilabel"}:
    >     for permanent redirections of unpublished or deleted
    >     `static pages <website/page_type>`{.interpreted-text
    >     role="ref"}. The new URL is shown in search engine results,
    >     and the redirect is cached by browsers.
    > -   `302 Moved Temporarily`{.interpreted-text role="guilabel"}:
    >     for short-term redirections, for example, if you are
    >     redesigning or updating a page. The new URL is neither cached
    >     by browsers nor shown in search engine results.
    > -   `308 Redirect/Rewrite`{.interpreted-text role="guilabel"}: for
    >     permanent redirections of existing `dynamic pages
    >     <website/page_type>`{.interpreted-text role="ref"}. The URL is
    >     renamed; the new name is shown in search engine results and is
    >     cached by browsers. Use this redirect type to rename a dynamic
    >     page, for example, if you wish to rename [/shop]{.title-ref}
    >     into [/market]{.title-ref}.

-   `URL from`{.interpreted-text role="guilabel"}: Enter the URL to be
    redirected (e.g., [/about-the-company]{.title-ref}) or search for
    the desired `dynamic page <website/page_type>`{.interpreted-text
    role="ref"} and select it from the list.

-   `URL to`{.interpreted-text role="guilabel"}: For 301, 302, and 308
    redirects, enter the URL to be redirected to. If you want to
    redirect to an external URL, include the protocol (e.g.,
    [https://]{.title-ref}).

-   `Website`{.interpreted-text role="guilabel"}: Select a specific
    website.

-   `Sequence`{.interpreted-text role="guilabel"}: To define the order
    in which redirections are performed, e.g., in the case of redirect
    chains (i.e., a series of redirects where one URL is redirected to
    another one, which is itself further redirected to another URL).

Toggle the `Activate`{.interpreted-text role="guilabel"} switch to
deactivate the redirection.

::: {.important}
::: {.title}
Important
:::

404, 301, and 302 redirections are meant to migrate traffic from
`unpublished <website/un-publish-page>`{.interpreted-text role="ref"} or
`deleted <website/delete-page>`{.interpreted-text role="ref"} pages to
*new* pages, while the 308 redirect is used for *permanent* redirections
of *existing* pages.
:::

::: {.seealso}
\- [Google documentation on redirects and
search](https://developers.google.com/search/docs/crawling-indexing/301-redirects)
- `pages/seo`{.interpreted-text role="doc"}
:::

::: {.toctree titlesonly=""}
pages/menus pages/seo
:::
