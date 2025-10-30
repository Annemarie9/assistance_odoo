Create opportunities from web contact forms
===========================================

Adding a contact form to a website makes it easy to convert visitors
into leads and opportunities. After a visitor submits their information,
an opportunity can be created automatically, and assigned to a
designated sales team and salesperson.

Customize contact forms {#crm/customize-contact-form}
-----------------------

By default, the *Contact Us* page on an Odoo website displays a
preconfigured contact form. This form can be customized, as needed, to
suit the needs of a specific sales team.

Navigate to `Website app --> Contact Us`{.interpreted-text
role="menuselection"}, then click `Edit`{.interpreted-text
role="guilabel"} in the top-right of the screen to open the web editor.
Click on the form building block in the body of the webpage to open the
form configuration settings on the right sidebar. The following options
are available to customize the contact form from the
`From`{.interpreted-text role="guilabel"} section of the right sidebar:

{.align-center}

-   `Action`{.interpreted-text role="guilabel"}: the default action for
    a contact form is `Send an Email`{.interpreted-text
    role="guilabel"}. Select `Create an Opportunity`{.interpreted-text
    role="guilabel"} from the drop-down list to capture the information
    in the *CRM* app.
-   `Sales Team`{.interpreted-text role="guilabel"}: choose a sales team
    from the drop-down menu that the opportunities from this form should
    be assigned to. This field **only** appears if the
    `Action`{.interpreted-text role="guilabel"} field is set to
    `Create an Opportunity`{.interpreted-text role="guilabel"}.
-   `Salesperson`{.interpreted-text role="guilabel"}: if the
    opportunities should be assigned to a specific salesperson, select
    them from the drop-down menu. If no selection is made in this field,
    the opportunities are assigned based on the team\'s existing rules.
-   `Marked Fields`{.interpreted-text role="guilabel"}: use this field
    to alter how the form handles marked fields. The default option is
    to treat marked fields as `Required`{.interpreted-text
    role="guilabel"}, which is the recommended setting.
-   `Mark Text`{.interpreted-text role="guilabel"}: choose how
    `Marked Fields`{.interpreted-text role="guilabel"} should be
    identified. The default character is an asterisk ([\*]{.title-ref}).
-   `Labels Width`{.interpreted-text role="guilabel"}: use this field to
    alter the pixel width of the labels, if desired.
-   `On Success`{.interpreted-text role="guilabel"}: select how the
    webpage reacts after a customer successfully submits a form.
    `Nothing`{.interpreted-text role="guilabel"} keeps the customer on
    the same screen, with the addition of a confirmation message that
    the form was submitted successfully. `Redirect`{.interpreted-text
    role="guilabel"} sends the customer to a new webpage, based on the
    address provided in the `URL`{.interpreted-text role="guilabel"}
    field below. `Show Message`{.interpreted-text role="guilabel"}
    replaces the form with a preconfigured message that informs the
    customer someone should respond to them as soon as possible.
-   `URL`{.interpreted-text role="guilabel"}: if
    `Redirect`{.interpreted-text role="guilabel"} is selected in the
    `On Success`{.interpreted-text role="guilabel"} field, enter the URL
    for the webpage, where customers should be directed after
    successfully submitting a form.
-   `Visibility`{.interpreted-text role="guilabel"}: use the drop-down
    menu to add any visibility conditions for this field, if desired.

::: {.important}
::: {.title}
Important
:::

If *leads* are activated in *CRM* settings, selecting
`Create an Opportunity`{.interpreted-text role="guilabel"} generates a
lead instead. To activate leads, navigate to
`CRM app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, and tick the
`Leads`{.interpreted-text role="guilabel"} checkbox. Then, click
`Save`{.interpreted-text role="guilabel"}.
:::

### Customize contact form fields

In addition to the settings for the form, the settings for each field
can be customized, as well. With the web editor menu still open, click
into a field to open the `Field`{.interpreted-text role="guilabel"}
configuration settings section on the sidebar. The following options are
available to customize a field:

-   `Type`{.interpreted-text role="guilabel"}: choose a custom field
    option or an existing field type.
-   `Input Type`{.interpreted-text role="guilabel"}: determine the type
    of information customers should input. Available options are
    `Text`{.interpreted-text role="guilabel"}, `Email`{.interpreted-text
    role="guilabel"}, `Telephone`{.interpreted-text role="guilabel"}, or
    `Url`{.interpreted-text role="guilabel"}. The selection made in this
    field limits the format that customers can use when entering
    information.
-   `Label`{.interpreted-text role="guilabel"}: enter the name for the
    field.
-   `Position`{.interpreted-text role="guilabel"}: choose the way the
    label is aligned with the rest of the form. The label can be hidden,
    above the field, to the left of the field, or right adjusted and
    closer to the field.
-   `Description`{.interpreted-text role="guilabel"}: slide the toggle
    to add a description for the field, which can provide additional
    instructions to customers. Click under the field on the form to add
    the description.
-   `Placeholder`{.interpreted-text role="guilabel"}: enter an example
    to help users know how to input information where formatting is
    important, such as a phone number or email address.
-   `Default Value`{.interpreted-text role="guilabel"}: enter a value to
    include in the form, by default, if the customer does not provide
    information in the field. *It is not recommended to include a
    default value for required fields*.
-   `Required`{.interpreted-text role="guilabel"}: slide the toggle to
    mark this field as required if it **must** be filled in for every
    submission.
-   `Visibility`{.interpreted-text role="guilabel"}: select when this
    field should be visible. Use the button on the left to choose
    whether to show or hide this field on a desktop users. Use the
    button on the right to choose whether to show or hide this field to
    mobile users.
-   `Animation`{.interpreted-text role="guilabel"}: select if this field
    should have any animation.

{.align-center}

View opportunities
------------------

After a customer submits a contact form, and an opportunity is created,
it is assigned based on the
`form settings <crm/customize-contact-form>`{.interpreted-text
role="ref"}. To view opportunities, navigate to
`CRM app --> Sales --> My Pipeline`{.interpreted-text
role="menuselection"}.

::: {.note}
::: {.title}
Note
:::

If leads are activated on the database, contact form submissions are
generated as leads, not opportunities. To activate leads, navigate to
`CRM app --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, and tick the
`Leads`{.interpreted-text role="guilabel"} checkbox. Then, click
`Save`{.interpreted-text role="guilabel"}.

Navigate to `CRM app --> Leads`{.interpreted-text role="menuselection"}
to view the newly-created leads.
:::

On the `My Pipeline`{.interpreted-text role="guilabel"} dashboard, click
on an opportunity card in the Kanban view to open the opportunity
record. The information submitted by the customer is visible on the
opportunity record.

::: {.note}
::: {.title}
Note
:::

As the contact form fields are customizable, the fields on the
opportunity record, where the form information is stored, varies
accordingly.

If the preconfigured contact form is used, the *Subject* field is added
to the `Title`{.interpreted-text role="guilabel"} field, and the content
in the `Notes`{.interpreted-text role="guilabel"} field, which is
labeled as `Your
Question`{.interpreted-text role="guilabel"}, is added to the
`Internal Notes`{.interpreted-text role="guilabel"} tab.
:::

::: {.seealso}
\- `../pipeline/manage_sales_teams`{.interpreted-text role="doc"} -
`convert`{.interpreted-text role="doc"} -
`../track_leads/lead_scoring`{.interpreted-text role="doc"} -
`Website forms <website/dynamic_content/form>`{.interpreted-text
role="ref"}
:::
