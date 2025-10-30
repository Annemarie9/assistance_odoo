# File: /content/odoo_doc17.0/fr/content/applications/services/project/tasks/task_creation.md

Task creation
=============

Tasks in Odoo Project can be created manually or automatically,
including from emails or website forms.

Manual task creation
--------------------

Open the Project app and choose the desired project. Create a new task
by doing one of the following:

> -   Clicking the `fa-plus`{.interpreted-text role="icon"}
>     (`plus`{.interpreted-text role="guilabel"}) button in the upper
>     left corner. This creates a new task in the first stage of your
>     Kanban view.
> -   Pressing the `fa-plus`{.interpreted-text role="icon"}
>     (`plus`{.interpreted-text role="guilabel"}) button next to the
>     Kanban stage name. This creates a new task in this Kanban stage.

Fill in the `Task Title`{.interpreted-text role="guilabel"} and add one
or more `Assignees`{.interpreted-text role="guilabel"}, then click
`Add`{.interpreted-text role="guilabel"}.

### Task configuration {#task_creation/task-configuration}

Click the task to open it. The task form includes the following fields
that you can fill in:

> -   `Task Title`{.interpreted-text role="guilabel"}: title of the
>     task.
> -   `fa-star-o`{.interpreted-text role="icon"}
>     (`Star`{.interpreted-text role="guilabel"}): click the
>     `fa-star-o`{.interpreted-text role="icon"}
>     (`star`{.interpreted-text role="guilabel"}) icon to mark the task
>     as high priority. The icon will turn yellow. Click it again to
>     remove the high priority.
> -   `Project`{.interpreted-text role="guilabel"}: the project that
>     this task belongs to.
> -   `Assignees`{.interpreted-text role="guilabel"}: the person(s) in
>     charge of handling the work on this task.
> -   `Tags`{.interpreted-text role="guilabel"}: custom labels allowing
>     to categorize and filter your tasks.
> -   `Customer`{.interpreted-text role="guilabel"}: the person or
>     company that will be billed for this task. This field only appears
>     in tasks that belong to billable projects.
> -   `Sales Order Item`{.interpreted-text role="guilabel"}: this can be
>     either the sales order that was used to create this task, or a
>     sales order that was linked to this task manually. This field only
>     appears in tasks linked to billable projects.
> -   `Allocated Time`{.interpreted-text role="guilabel"}: the amount of
>     time that the work on this task is expected to last, tracked by
>     timesheets.
> -   `Deadline`{.interpreted-text role="guilabel"}: the expected end
>     date of the task. Once this field is filled in, you can also add a
>     start date to designate the entire time frame of the tasks\'
>     duration.

::: {.tip}
::: {.title}
Tip
:::

-   You can also create new tasks by switching to the list or Gantt view
    and clicking `New`{.interpreted-text role="guilabel"}.

-   The following fields can also be edited directly from the Kanban
    view without opening the individual task:
    `fa-star-o`{.interpreted-text role="icon"} (**priority**),
    `Allocated hours`{.interpreted-text role="guilabel"},
    `Assignees`{.interpreted-text role="guilabel"}, and **task status**.
    You can also **color code** or `Set a
    Cover image`{.interpreted-text role="guilabel"} to your task by
    clicking the `fa-ellipsis-v`{.interpreted-text role="icon"}
    (**vertical ellipsis**).

-   You can use the following keyboard shortcuts in the task title to
    configure new tasks (modify the values in the examples below
    according to your needs):

    -   **30h**: to allocate 30 hours to the task.
    -   **\#tags**: to add tags to the task.
    -   **\@user**: to assign the task to a user.
    -   **!**: to star the task as high priority.

    Along with using the correct format, follow this order: the task\'s
    name, followed by the allocated time, the tags, the assignee, and
    then the priority.

    For example, if you want to create a task named \"Prepare
    workshop\", allocate 5h hours to it, add the \"School\" tag, assign
    it to Audrey and set its priority to `High`{.interpreted-text
    role="guilabel"}, enter the following task title: Prepare workshop
    5h \#school \@Audrey !

    
:::

Creating tasks from an email alias {#task_creation/email_alias}
----------------------------------

This feature allows for project tasks to be automatically created once
an email is delivered to a designated email address.

To configure it, open the Project app, then click the
`fa-ellipsis-v`{.interpreted-text role="icon"} (`vertical
ellipsis`{.interpreted-text role="guilabel"}) icon next to the desired
project\'s name. Select `Settings`{.interpreted-text role="guilabel"},
then open the `Settings`{.interpreted-text role="guilabel"} tab.

Fill in the `Create tasks by sending an email to`{.interpreted-text
role="guilabel"} field as follows:

> -   **Section of the alias before the @ symbol**: type the name of the
>     email alias, e.g. [contact]{.title-ref}, [help]{.title-ref},
>     [jobs]{.title-ref}.
> -   **Domain**: in most cases, this is filled in by default with your
>     `domain
>     <../../../general/email_communication>`{.interpreted-text
>     role="doc"}.
> -   **Accept Emails From**: refine the senders whose emails will
>     create tasks in the project.



Once configured, the email alias can be seen under the name of your
project on the Kanban dashboard.

When an email is sent to the alias, the email is automatically converted
into a project task. The following rules apply:

-   The email sender is displayed in the `Customer`{.interpreted-text
    role="guilabel"} field.
-   The email subject is displayed in the `Task Title`{.interpreted-text
    role="guilabel"} field.
-   The email body is displayed in the `Description`{.interpreted-text
    role="guilabel"} field.
-   The whole content of the email is additionally displayed in the
    **chatter**.
-   All the recipients of the email (To/Cc/Bcc) that are Odoo users are
    automatically added as **followers** of the task.

Creating tasks from a website form
----------------------------------

If you have the Website app installed in your database, you can
configure any form on your website to trigger the creation of tasks in a
project.

1.  Go to the website page where you wish to add the the form and
    `add the Form building block <websites/website/web_design/building_blocks>`{.interpreted-text
    role="ref"}.
2.  In the website editor, edit the following fields:
    -   `Action`{.interpreted-text role="guilabel"}: select
        `Create a Task`{.interpreted-text role="guilabel"}.
    -   `Project`{.interpreted-text role="guilabel"}: choose the project
        that you want the new tasks to be created in.
3.  `Customize the form <website/dynamic_content/form>`{.interpreted-text
    role="ref"}.

When the form is submitted, it automatically creates a project task. The
task\'s content is defined by the form\'s corresponding fields.

::: {.seealso}
`Dynamic website content <../../../websites/website/web_design/building_blocks/dynamic_content>`{.interpreted-text
role="doc"}
:::
