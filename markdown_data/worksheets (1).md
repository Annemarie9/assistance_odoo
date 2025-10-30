# File: /content/odoo_doc17.0/fr/content/applications/services/field_service/worksheets.md

Worksheets
==========

**Worksheets** help your field service workers perform and report their
on-site tasks. They can feature various information, such as
instructions, to-do lists, etc. You can also format your worksheet using
checkboxes, bullet points, blank fields to fill in, HTML, and add files,
images, links, and more.

It is common for businesses to have their workers perform the same type
of field service repeatedly. Making custom **worksheet templates**
eliminates the need to recreate the same worksheet each time you plan a
similar field service task.

Configuration
-------------

To use worksheets in Field Service, go to
`Field Service --> Configuration -->
Settings`{.interpreted-text role="menuselection"}, enable the
`Worksheets`{.interpreted-text role="guilabel"} feature, and click
`Save`{.interpreted-text role="guilabel"}.

::: {.warning}
::: {.title}
Warning
:::

Worksheet templates are designed using **Studio**. Enabling the
`Worksheets`{.interpreted-text role="guilabel"} feature automatically
installs the **Studio** app, which may impact your price plan.
:::

### Create a worksheet template

To create your **worksheet templates**, go to
`Field Service --> Configuration -->
Worksheet Templates`{.interpreted-text role="menuselection"}. Click
`New`{.interpreted-text role="guilabel"} and give your worksheet
template a name. Manually save, then click
`Design Template`{.interpreted-text role="guilabel"} to open **Studio**
and customize your worksheet template.

In Studio, drag and drop the desired fields from the left column into
your worksheet on the right. To rearrange the fields on the worksheet,
drag and drop them in the desired order. Click a field to customize its
`properties <studio/fields/properties>`{.interpreted-text role="ref"}.

When your worksheet template is complete, click
`Close`{.interpreted-text role="guilabel"} in the top right corner of
the page to leave **Studio**.

::: {.seealso}
`Fields and widgets in Studio <../../studio/fields>`{.interpreted-text
role="doc"}
:::

Add a worksheet template to a field service task
------------------------------------------------

Go to your field service task, select a
`Worksheet Template`{.interpreted-text role="guilabel"}, and click
`Save`{.interpreted-text role="guilabel"}.

By default, the `Default Worksheet`{.interpreted-text role="guilabel"}
template is selected. To define another default worksheet template,
click the `➔`{.interpreted-text role="guilabel"}
(`Internal link`{.interpreted-text role="guilabel"}) icon that appears
when you hover your mouse over the `Project`{.interpreted-text
role="guilabel"} field on the task form.



Then, in the `Settings`{.interpreted-text role="guilabel"} tab, scroll
down to the `Field service`{.interpreted-text role="guilabel"} section
and select the `Worksheet Template`{.interpreted-text role="guilabel"}
you want to set up as default.

Use worksheets on site
----------------------

To complete the worksheet on site, access the task and click the
`Worksheet`{.interpreted-text role="guilabel"} smart button.

::: {.note}
::: {.title}
Note
:::

\- As soon as you save a worksheet, the label of the
`Worksheet`{.interpreted-text role="guilabel"} smart button on the task
changes to `Worksheet Complete`{.interpreted-text role="guilabel"}
instead, even if some fields are left blank. - Any field defined as
`Required`{.interpreted-text role="guilabel"} has to be filled for a
worksheet to be saved.
:::
