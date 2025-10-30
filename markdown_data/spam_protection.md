# File: /content/odoo_doc17.0/fr/content/applications/websites/website/configuration/spam_protection.md

Forms spam protection
=====================

`Cloudflare Turnstile <cloudflare-turnstile>`{.interpreted-text
role="ref"} and
`Google reCAPTCHA v3 <google-recaptcha>`{.interpreted-text role="ref"}
protect website forms against spam and abuse. They attempt to
distinguish between human and bot submissions using non-interactive
challenges based on telemetry and visitor behavior.

::: {.important}
::: {.title}
Important
:::

We recommend using **Cloudflare Turnstile** as reCAPTCHA v3 may not be
compliant with local data protection regulations.
:::

::: {.note}
::: {.title}
Note
:::

All pages using the `Form`{.interpreted-text role="guilabel"},
`Newsletter Block`{.interpreted-text role="guilabel"},
`Newsletter Popup`{.interpreted-text role="guilabel"} snippets, and the
eCommerce `Extra Step During Checkout`{.interpreted-text
role="guilabel"} form are protected by both tools.
:::

::: {.seealso}
\- [Cloudflare Turnstile\'s
documentation](https://developers.cloudflare.com/turnstile/) -
[Google\'s reCAPTCHA v3
guide](https://developers.google.com/recaptcha/docs/v3)
:::

Cloudflare Turnstile configuration {#cloudflare-turnstile}
----------------------------------

### On Cloudflare

-    a Cloudflare account
    or use an existing one and [log
    in](https://dash.cloudflare.com/login).
-   On the dashboard navigation sidebar, click
    `Turnstile`{.interpreted-text role="guilabel"}.
-   On the `Turnstile Sites`{.interpreted-text role="guilabel"} page,
    click `Add Site`{.interpreted-text role="guilabel"}.
-   Add a `Site name`{.interpreted-text role="guilabel"} to identify it
    easily.
-   Enter or select the website\'s `Domain`{.interpreted-text
    role="guilabel"} (e.g., *example.com* or *subdomain.example.com*).
-   Select a `Widget Mode`{.interpreted-text role="guilabel"}:
    -   The `Managed`{.interpreted-text role="guilabel"} mode is
        **recommended**, as visitors can be prompted to check a box
        confirming they are human if deemed necessary by Turnstile.

        

    -   For the `Non-interactive`{.interpreted-text role="guilabel"} and
        `Invisible`{.interpreted-text role="guilabel"} modes, visitors
        are never prompted to interact. In
        `Non-interactive`{.interpreted-text role="guilabel"} mode, a
        loading widget can be displayed to warn visitors that Turnstile
        protects the form; however, the widget is not supported by Odoo.

        ::: {.note}
        ::: {.title}
        Note
        :::

        If the Turnstile check fails, visitors are not able to submit
        the form, and the following error message is displayed:

        
        :::
-   Click `Create`{.interpreted-text role="guilabel"}.



The generated keys are then displayed. Leave the page open for
convenience, as copying the keys in Odoo is required next.

### On Odoo

-   From the database dashboard, click `Settings`{.interpreted-text
    role="guilabel"}. Under `Integrations`{.interpreted-text
    role="guilabel"}, enable `Cloudflare Turnstile`{.interpreted-text
    role="guilabel"} and click `Save`{.interpreted-text
    role="guilabel"}.
-   Open the Cloudflare Turnstile page, copy the
    `Site Key`{.interpreted-text role="guilabel"}, and paste it into the
    `CF Site Key`{.interpreted-text role="guilabel"} field in Odoo.
-   Open the Cloudflare Turnstile page, copy the
    `Secret Key`{.interpreted-text role="guilabel"}, and paste it into
    the `CF Secret Key`{.interpreted-text role="guilabel"} field in
    Odoo.
-   Click `Save`{.interpreted-text role="guilabel"}.

::: {.tip}
::: {.title}
Tip
:::

Navigate to Turnstile on your Cloudflare account to view the solve rates
and access more settings.
:::

reCAPTCHA v3 configuration {#google-recaptcha}
--------------------------

::: {.warning}
::: {.title}
Warning
:::

reCAPTCHA v3 may not be compliant with local data protection
regulations.
:::

### On Google

Open [the reCAPTCHA website registration
page](https://www.google.com/recaptcha/admin/create). Log in or create a
Google account if necessary.

On the website registration page:

-   Give the website a `Label`{.interpreted-text role="guilabel"}.
-   Leave the `reCAPTCHA type`{.interpreted-text role="guilabel"} on
    `Score based (v3)`{.interpreted-text role="guilabel"}.
-   Enter one or more `Domains`{.interpreted-text role="guilabel"}
    (e.g., *example.com* or *subdomain.example.com*).
-   Under `Google Cloud Platform`{.interpreted-text role="guilabel"}, a
    project is automatically selected if one was already created with
    the logged-in Google account. If not, one is automatically created.
    Click `Google Cloud Platform`{.interpreted-text role="guilabel"} to
    select a project yourself or rename the automatically created
    project.
-   Agree to the terms of service.
-   Click `Submit`{.interpreted-text role="guilabel"}.



A new page with the generated keys is then displayed. Leave it open for
convenience, as copying the keys to Odoo is required next.

### On Odoo

-   From the database dashboard, click `Settings`{.interpreted-text
    role="guilabel"}. Under `Integrations`{.interpreted-text
    role="guilabel"}, enable `reCAPTCHA`{.interpreted-text
    role="guilabel"} if needed.

    ::: {.warning}
    ::: {.title}
    Warning
    :::

    Do not disable the `reCAPTCHA`{.interpreted-text role="guilabel"}
    feature or uninstall the `Google reCAPTCHA
    integration`{.interpreted-text role="guilabel"} module, as many
    other modules would also be removed.
    :::

-   Open the Google reCAPTCHA page, copy the
    `Site key`{.interpreted-text role="guilabel"}, and paste it into the
    `Site Key`{.interpreted-text role="guilabel"} field in Odoo.

-   Open the Google reCAPTCHA page, copy the
    `Secret key`{.interpreted-text role="guilabel"}, and paste it into
    the `Secret Key`{.interpreted-text role="guilabel"} field in Odoo.

-   Change the default `Minimum score`{.interpreted-text
    role="guilabel"} ([0.70]{.title-ref}) if necessary, using a value
    between [1.00]{.title-ref} and [0.00]{.title-ref}. The higher the
    threshold is, the more difficult it is to pass the reCAPTCHA, and
    vice versa. Out of the 11 levels, only the following four score
    levels are available by default: [0.1]{.title-ref},
    [0.3]{.title-ref}, [0.7]{.title-ref} and [0.9]{.title-ref}.

-   Click `Save`{.interpreted-text role="guilabel"}.

::: {.seealso}
[Interpret reCAPTCHA scores - Google
documentation](https://cloud.google.com/recaptcha/docs/interpret-assessment-website#interpret_scores)
:::

You can notify visitors that reCAPTCHA protects a form. To do so, open
the website editor and navigate to the form. Then, click somewhere on
the form, and on the right sidebar\'s `Customize`{.interpreted-text
role="guilabel"} tab, toggle `Show reCAPTCHA Policy`{.interpreted-text
role="guilabel"} found under the `Form`{.interpreted-text
role="guilabel"} section.



::: {.note}
::: {.title}
Note
:::

If the reCAPTCHA check fails, the following error message is displayed:


:::

::: {.tip}
::: {.title}
Tip
:::

Analytics and additional settings are available on [Google\'s reCAPTCHA
administration page](https://www.google.com/recaptcha/admin/). For
example, you can receive email alerts if Google detects suspicious
traffic on your website or view the percentage of suspicious requests,
which could help you determine the right minimum score.
:::
