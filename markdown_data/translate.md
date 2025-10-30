# File: /content/odoo_doc17.0/fr/content/applications/websites/website/configuration/translate.md

Translations
============

Your website is displayed in the language that matches your visitor's
browser. If the browser's language has not been installed and added to
your website, the content is shown in the
`default language <translate/default-language>`{.interpreted-text
role="ref"}. When additional languages are installed, users can choose
their preferred language using the
`language selector <translate/language-selector>`{.interpreted-text
role="ref"}.

The `Translate <translate/translate>`{.interpreted-text role="ref"}
feature on your website allows automatic translation of standard terms
and provides a tool for manual content translation.

Install languages
-----------------

To allow translation of your website, you must first
`install <../../../general/users/language>`{.interpreted-text
role="doc"} the required languages and add them to your website. To do
so, go to `Website -->
Configuration --> Settings`{.interpreted-text role="menuselection"} and
click `fa-arrow-right`{.interpreted-text role="icon"}
`Install languages`{.interpreted-text role="guilabel"} in the
`Website Info`{.interpreted-text role="guilabel"} section. In the dialog
box that opens, select the `Languages`{.interpreted-text
role="guilabel"} you want from the dropdown menu, tick the required
`Websites to translate`{.interpreted-text role="guilabel"}, and click
`Add`{.interpreted-text role="guilabel"}.

To edit your website\'s languages, go to
`Website -–> Configuration -–> Settings`{.interpreted-text
role="menuselection"} and add/remove the required languages in/from the
`Languages`{.interpreted-text role="guilabel"} field in the
`Website info`{.interpreted-text role="guilabel"} section.

::: {.tip}
::: {.title}
Tip
:::

Alternatively, once the languages have been installed, you can add them
from the `language
selector <translate/language-selector>`{.interpreted-text role="ref"}.
You might then need to refresh your page to see the new language.
:::

### Default language {#translate/default-language}

When multiple languages are available on your website, you can set a
default language to be used if the visitor's browser language is not
available. To do so, go to `Website –->
Configuration -–> Settings`{.interpreted-text role="menuselection"}, and
select a language in the `Default`{.interpreted-text role="guilabel"}
field.

::: {.note}
::: {.title}
Note
:::

This field is only visible if multiple languages have been installed and
added to your website.
:::

Language selector {#translate/language-selector}
-----------------

Your website's visitors can switch languages using the language
selector, available by default in the `Copyright`{.interpreted-text
role="guilabel"} section at the bottom of the page. To edit the language
selector menu:

1.  Go to your website and click `Edit`{.interpreted-text
    role="guilabel"};

2.  Click the language selector available in the
    `Copyright`{.interpreted-text role="guilabel"} block and go to the
    `Copyright`{.interpreted-text role="guilabel"} section of the
    website builder;

3.  Set the `Language Selector`{.interpreted-text role="guilabel"} field
    to either `Dropdown`{.interpreted-text role="guilabel"} or
    `Inline`{.interpreted-text role="guilabel"}. Click
    `None`{.interpreted-text role="guilabel"} if you do not want to
    display the `Language selector`{.interpreted-text role="guilabel"};

    > 

4.  Click `Save`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

You can also add the `Language Selector`{.interpreted-text
role="guilabel"} to the `Header`{.interpreted-text role="guilabel"} of
your page. To do so, click the `Header`{.interpreted-text
role="guilabel"} block and go to the `Navbar`{.interpreted-text
role="guilabel"} section to edit the
`Language Selector`{.interpreted-text role="guilabel"}.
:::

Translate your website {#translate/translate}
----------------------

Select your desired language from the language selector to see your
content in another language. Then, click the
`Translate`{.interpreted-text role="guilabel"} button in the top-right
corner to manually activate the translation mode so that you can
translate what has not been translated automatically by Odoo.

Translated text strings are highlighted in green; text strings that were
not translated automatically are highlighted in yellow.



In this mode, you can only translate text. To change the page\'s
structure, you must edit the master page, i.e., the page in the original
language of the database. Any changes made to the master page are
automatically applied to all translated versions.

To replace the original text with the translation, click the block, edit
its contents, and `Save`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

When a website supports multiple languages, the core URL structure
remains consistent across languages, while specific elements like
product names or categories are translated. For example,
[https://www.mywebsite.com/shop/product/my-product-1]{.title-ref} is the
English version of a product page, while
[https://www.mywebsite.com/fr/shop/product/mon-produit-1]{.title-ref} is
the French version of the same page. The structure (/shop/product/)
stays unchanged, but the translated elements (e.g., product name) adapt
to the selected language.
:::

::: {.tip}
::: {.title}
Tip
:::

Once the desired language is installed, you can translate some items
from the backend (e.g., the product\'s name in the product form). To do
so, click the language code (e.g., `EN`{.interpreted-text
role="guilabel"}) next to the text you want to translate and add the
translation.
:::

### Content visibility by language

You can hide content (such as images or videos, for example) depending
on the language. To do so:

1.  Click `Edit`{.interpreted-text role="guilabel"} and select an
    element of your website;
2.  Go to the `Text - Image`{.interpreted-text role="guilabel"} section
    and `Visibility`{.interpreted-text role="guilabel"};
3.  Click `No condition`{.interpreted-text role="guilabel"} and select
    `Conditionally`{.interpreted-text role="guilabel"} instead;
4.  Go to `Languages`{.interpreted-text role="guilabel"} to configure
    the condition(s) to apply by selecting
    `Visible for`{.interpreted-text role="guilabel"} or
    `Hidden for`{.interpreted-text role="guilabel"}, and click
    `Choose a record`{.interpreted-text role="guilabel"} to decide which
    languages are impacted.
