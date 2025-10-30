# File: /content/odoo_doc17.0/fr/content/applications/productivity/documents.md

Documents
=========

**Odoo Documents** allows you to store, view, and manage files within
Odoo.

You can upload any file (max 64MB per file on Odoo Online) and organize
them in various workspaces.

::: {.seealso}
\-  -
[Odoo Tutorials: Documents basics
\
- [Odoo Tutorials: Using Documents with your Accounting App
\
:::

Configuration
-------------

By going to `Documents --> Configuration --> Settings`{.interpreted-text
role="menuselection"}, you can enable the centralization of files
attached to a specific area of your activity. For example, by ticking
`Human Resources`{.interpreted-text role="guilabel"}, your HR documents
are automatically available in the HR workspace, while documents related
to Payroll are automatically available in the Payroll sub-workspace. You
can change the default workspace using the dropdown menu and edit its
properties by clicking the `fa-arrow-right`{.interpreted-text
role="icon"} (`Internal link`{.interpreted-text role="guilabel"}) icon.



::: {.note}
::: {.title}
Note
:::

\- If you enable the centralization of your accounting files and
documents, it is necessary to click on `Journals`{.interpreted-text
role="guilabel"} and define each journal independently to allow
automatic synchronization.



\- If you select a new workspace, existing documents are not moved. Only
newly created documents will be found under the new workspace.
:::

Workspaces {#documents/workspaces}
----------

Workspaces are hierarchical folders having their own set of
`tags <documents/tags>`{.interpreted-text role="ref"} and
`actions <documents/workflow-actions>`{.interpreted-text role="ref"}.
Default workspaces exist, but you can create your own by going to
`Documents --> Configuration --> Workspaces`{.interpreted-text
role="menuselection"} and clicking `New`{.interpreted-text
role="guilabel"}. On the new page, fill in the following information:

-   `Name`{.interpreted-text role="guilabel"}
-   `Parent Workspace`{.interpreted-text role="guilabel"}: if you want
    to create a sub-workspace, select its `Parent
    Workspace`{.interpreted-text role="guilabel"}.

Three tabs are available: `Tags <documents/tags>`{.interpreted-text
role="ref"}, `Access Rights <documents/access-rights>`{.interpreted-text
role="ref"}, and `Description <documents/description>`{.interpreted-text
role="ref"}.

### Tags {#documents/tags}

Tags are used within workspaces to add a level of differentiation
between documents. They are organized per category, and filters can be
used to sort them.

From the `Tags`{.interpreted-text role="guilabel"} tab, click
`Add a line`{.interpreted-text role="guilabel"}, create the
`Tag Category`{.interpreted-text role="guilabel"}, and
`Name`{.interpreted-text role="guilabel"} your tags.

::: {.note}
::: {.title}
Note
:::

\- The tags of a parent workspace apply to the child workspaces
automatically; - Tags can be created and modified by going to
`Documents --> Configuration -->
Tags`{.interpreted-text role="menuselection"}; - Tags can also be
created or edited by clicking the `fa-gear`{.interpreted-text
role="icon"} (`gear`{.interpreted-text role="guilabel"}) icon on the
left panel; - An `email alias <documents/upload>`{.interpreted-text
role="ref"} can be used to automatically send received documents to a
specific workspace based on the tag assigned.
:::

### Access rights {#documents/access-rights}

To manage your workspace access rights, go to the
`Access Rights`{.interpreted-text role="guilabel"} tab. You can add
`Write Groups`{.interpreted-text role="guilabel"} that can view, create,
and edit the workspace\'s documents. You can also add
`Read Groups`{.interpreted-text role="guilabel"} that only view the
workspace\'s documents.

::: {.tip}
::: {.title}
Tip
:::

Enable `Own Documents Only`{.interpreted-text role="guilabel"} to limit
`Read Groups`{.interpreted-text role="guilabel"} and
`Write Groups`{.interpreted-text role="guilabel"} to the documents of
which they are owner.
:::

### Description {#documents/description}

You can add descriptive information to your workspace by going to the
`Description`{.interpreted-text role="guilabel"} tab.

::: {.note}
::: {.title}
Note
:::

Workspaces can also be created and edited by clicking the
`fa-gear`{.interpreted-text role="icon"} (`gear`{.interpreted-text
role="guilabel"}) icon on the left panel.
:::

Documents management {#documents/management}
--------------------

When selecting or opening a document, the right panel displays different
options, including, for example:

-   `fa-download`{.interpreted-text role="icon"}
    (`Download`{.interpreted-text role="guilabel"});
-   `fa-share-alt`{.interpreted-text role="icon"}
    (`Share this selection`{.interpreted-text role="guilabel"}): a share
    URL is copied to your clipboard;
-   `fa-retweet`{.interpreted-text role="icon"}
    (`Replace`{.interpreted-text role="guilabel"}): select a new file to
    replace the existing one. Scroll down to the bottom of the right
    panel to see the `History`{.interpreted-text role="guilabel"} and
    `restore`{.interpreted-text role="guilabel"},
    `download`{.interpreted-text role="guilabel"}, or
    `delete`{.interpreted-text role="guilabel"} the document;
-   `fa-unlock`{.interpreted-text role="icon"} (`Lock`{.interpreted-text
    role="guilabel"});
-   `fa-scissors`{.interpreted-text role="icon"}
    (`Split <documents/split>`{.interpreted-text role="ref"}).

You can also `fa-comments`{.interpreted-text role="icon"}
`Open chatter`{.interpreted-text role="guilabel"} or delete the document
by clicking the `fa-trash`{.interpreted-text role="icon"}
(`Move to trash`{.interpreted-text role="guilabel"}) icon.

::: {.note}
::: {.title}
Note
:::

Items moved to the trash are permanently deleted after 30 days.
:::

To modify the name of your file, click on `Name`{.interpreted-text
role="guilabel"}. A `Contact`{.interpreted-text role="guilabel"} or an
`Owner`{.interpreted-text role="guilabel"} can be assigned. The related
`Workspace`{.interpreted-text role="guilabel"} can be modified and it is
possible to access the related `Journal Entry`{.interpreted-text
role="guilabel"} or add `Tags`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

\- The `Contact`{.interpreted-text role="guilabel"} is a person related
to the document who only has read
`access rights <documents/access-rights>`{.interpreted-text role="ref"}
to the document, e.g., an existing supplier in your database; - The
creator of a document is automatically assigned as its
`Owner`{.interpreted-text role="guilabel"} and is granted full access
rights to it. To replace the owner of a document, select the required
user from the dropdown list in the `Owner`{.interpreted-text
role="guilabel"} field.
:::

::: {.tip}
::: {.title}
Tip
:::

An employee must be a user and the owner of a document to view it in
**My Profile**.
:::

Different `Actions <documents/workflow-actions>`{.interpreted-text
role="ref"} are available at the bottom of the right panel, depending on
the workspace where your document is stored.

### Split PDF documents {#documents/split}

Select the PDF you want to split, and click the
`fa-scissors`{.interpreted-text role="icon"}
(`scissors`{.interpreted-text role="guilabel"}) icon. A new view
displays all the pages of the document.

By default, all pages are split when you click `Split`{.interpreted-text
role="guilabel"}. To remove a split between two pages, click the
`fa-scissors`{.interpreted-text role="icon"}
(`scissors`{.interpreted-text role="guilabel"}) icon.



::: {.tip}
::: {.title}
Tip
:::

To merge documents from your dashboard, select them and click the
`fa-scissors`{.interpreted-text role="icon"}
(`scissors`{.interpreted-text role="guilabel"}) icon. Click on the
scissors between the two documents and click `Split`{.interpreted-text
role="guilabel"} to merge the documents.
:::

### Additional features

Select a workspace and click the `fa-caret-down`{.interpreted-text
role="icon"} (`down arrow`{.interpreted-text role="guilabel"}) next to
the `Upload`{.interpreted-text role="guilabel"} button to access
additional features:

#### Request

You can request files and organize them as documents to remind users to
download them.

Select the workspace where the file should be stored, click the
`fa-caret-down`{.interpreted-text role="icon"}
(`down arrow`{.interpreted-text role="guilabel"}) next to the
`Upload`{.interpreted-text role="guilabel"} button, then
`Request`{.interpreted-text role="guilabel"}. Add the
`Document Name`{.interpreted-text role="guilabel"} and select the person
you need it from in the `Request To`{.interpreted-text role="guilabel"}
field. You can also fill in the `Due Date In`{.interpreted-text
role="guilabel"}, confirm the `Workspace`{.interpreted-text
role="guilabel"} the document should belong to, and add
`Tags`{.interpreted-text role="guilabel"} and a
`Message`{.interpreted-text role="guilabel"}. Then, click
`Request`{.interpreted-text role="guilabel"}. A placeholder for the
missing document is created in the workspace.

When your document is available, click the placeholder to upload it.

You can see all missing documents by going to the **Activity** view and
the `Requested
Document`{.interpreted-text role="guilabel"} column.

::: {.tip}
::: {.title}
Tip
:::

From the `Activity`{.interpreted-text role="guilabel"} view, you can
send a **reminder email** to users from whom you are expecting a
document. Go to the `Requested Document`{.interpreted-text
role="guilabel"} column and click the `fa-ellipsis-v`{.interpreted-text
role="icon"} (`ellipsis`{.interpreted-text role="guilabel"}) icon, and
`Document Request: Reminder`{.interpreted-text role="guilabel"}. Click
on a date to see the details of a specific request. You can update it by
clicking on the `fa-pencil`{.interpreted-text role="icon"}
(`pen`{.interpreted-text role="guilabel"}) icon,
`Preview`{.interpreted-text role="guilabel"} the content of the reminder
email, or `Send Now`{.interpreted-text role="guilabel"} to send a
reminder email.


:::

#### Add a link {#documents/add-a-link}

To add a link to your documents dashboard, click
`Add a Link`{.interpreted-text role="guilabel"}, enter the
`URL`{.interpreted-text role="guilabel"}, and `Name`{.interpreted-text
role="guilabel"} it.

#### Share

You can make a document or a workspace accessible to anyone by sharing a
URL.

##### Share a document

To generate a **share link** to a document, select the document, click
the `fa-caret-down`{.interpreted-text role="icon"}
(`down arrow`{.interpreted-text role="guilabel"}) next to the
`Upload`{.interpreted-text role="guilabel"} button, and click
`Share`{.interpreted-text role="guilabel"}.

In the pop-up, you can `Name`{.interpreted-text role="guilabel"} the
share link, set a validity date by filling in the
`Valid Until`{.interpreted-text role="guilabel"} field, and if you own
more than one site, select the `Website`{.interpreted-text
role="guilabel"} you want so the right domain name is reflected in the
URL.

Click `Copy`{.interpreted-text role="guilabel"} or
`Share`{.interpreted-text role="guilabel"} to send the URL to whomever
you want.

::: {.tip}
::: {.title}
Tip
:::

You can also generate a share URL by selecting the document, going to
the right panel, and clicking the `fa-share-alt`{.interpreted-text
role="icon"} (`Share this selection`{.interpreted-text role="guilabel"})
icon.
:::

##### Share a workspace

You can share a link to a workspace and allow users to
`Download`{.interpreted-text role="guilabel"} its content or
`Download and Upload`{.interpreted-text role="guilabel"} files to it.

To do so, go to the left column of your dashboard. In the
`Workspace`{.interpreted-text role="guilabel"} section, select the
workspace to share, and possibly one or several tags that will be
automatically added to the uploaded documents. Then, click the
`fa-caret-down`{.interpreted-text role="icon"}
(`down arrow`{.interpreted-text role="guilabel"}) next to the
`Upload`{.interpreted-text role="guilabel"} button and
`Share`{.interpreted-text role="guilabel"}.

In the pop-up, a share `URL`{.interpreted-text role="guilabel"} you can
`Copy`{.interpreted-text role="guilabel"} is displayed. You can
`Name`{.interpreted-text role="guilabel"} your share link, set a
validity date by filling in the `Valid Until`{.interpreted-text
role="guilabel"} field, tick the `Include Sub Folders`{.interpreted-text
role="guilabel"} box if you want to share the workspace\'s sub-folders,
and if you own more than one site, select the
`Website`{.interpreted-text role="guilabel"} you want so the share link
reflects the right domain name.

Then, allow users to either `Download`{.interpreted-text
role="guilabel"} files from your workspace, or to `Download and
Upload <documents/upload>`{.interpreted-text role="ref"} files to it.

::: {.note}
::: {.title}
Note
:::

\- The links added to your workspace using the
`Add a Link <documents/add-a-link>`{.interpreted-text role="ref"} option
cannot be shared and are, therefore, excluded; - When tags are applied
to a shared workspace, users can exclusively access the documents
associated with those tags.
:::

###### Upload by email {#documents/upload}

Select the `Download and Upload`{.interpreted-text role="guilabel"}
option to enable users to upload their files to your workspace using an
`Email Alias`{.interpreted-text role="guilabel"}. To create the email
alias, enter its name in the `Email Alias`{.interpreted-text
role="guilabel"} field. The
`domain name <../general/email_communication>`{.interpreted-text
role="doc"} should be set by default, but you can modify it by clicking
it.

The documents sent to this email alias are uploaded to the workspace
using the chosen `tags <documents/tags>`{.interpreted-text role="ref"}.

::: {.note}
::: {.title}
Note
:::

\- By default, the `Document Owner`{.interpreted-text role="guilabel"}
is the person who uploads a file to a workspace, but you can select
another user. You can also set a `Contact`{.interpreted-text
role="guilabel"}, usually an external person, such as a partner. -
Enable `Create a new activity`{.interpreted-text role="guilabel"} to
automatically create an activity when a document is uploaded. Select the
`Activity type`{.interpreted-text role="guilabel"} from the dropdown
list and set the `Due Date In`{.interpreted-text role="guilabel"} field.
You can also add a `Summary`{.interpreted-text role="guilabel"} and a
`Responsible`{.interpreted-text role="guilabel"} person assigned to the
activity.
:::

::: {.tip}
::: {.title}
Tip
:::

Go to `Configuration --> Share & Emails`{.interpreted-text
role="menuselection"} to see and manage your share links. Select a line
and click `Delete`{.interpreted-text role="guilabel"} to disable the
URL. People who have received this link will no longer be able to access
the document(s) or workspace.
:::

#### New spreadsheet

To create a new `spreadsheet <spreadsheet>`{.interpreted-text
role="doc"}, click `New Spreadsheet`{.interpreted-text role="guilabel"}.
You can select a `Blank spreadsheet`{.interpreted-text role="guilabel"}
or an `existing template <spreadsheet/templates>`{.interpreted-text
role="doc"}.

Workflow actions {#documents/workflow-actions}
----------------

Workflow actions help manage documents and overall business operations.
These are automated actions that can be created and customized for each
workspace. With a single click you can, for example, create, move, sign,
add tags to a document, and process bills.

When a document meets the set criteria, these workflow actions appear on
the right panel.

### Create workflow actions

To update an existing workflow action or create a new one, go to
`Documents -->
Configuration --> Actions`{.interpreted-text role="menuselection"} and
click `New`{.interpreted-text role="guilabel"}.

::: {.note}
::: {.title}
Note
:::

An action applies to all **sub-workspaces** under the
`Related Workspace`{.interpreted-text role="guilabel"} you selected.
:::

### Set the conditions

Define the `Action Name`{.interpreted-text role="guilabel"} and then set
the conditions that trigger the appearance of the
`fa-play`{.interpreted-text role="icon"} (`play`{.interpreted-text
role="guilabel"}) icon on the right-side panel when selecting a file.

There are three basic types of conditions you can set:

1.  `Tags`{.interpreted-text role="guilabel"}: you can use the
    `Contains`{.interpreted-text role="guilabel"} and
    `Does not contain`{.interpreted-text role="guilabel"} conditions,
    meaning the files *must have* or *must not have* the tags set here;
2.  `Contact`{.interpreted-text role="guilabel"}: the files must be
    associated with the contact set here;
3.  `Owner`{.interpreted-text role="guilabel"}: the files must be
    associated with the owner set here.



::: {.tip}
::: {.title}
Tip
:::

If you do not set any conditions, the action button appears for all
files inside the selected workspace.
:::

#### Advanced condition type: domain

::: {.important}
::: {.title}
Important
:::

It is recommended to have some knowledge of Odoo development to
configure *Domain* filters properly.
:::

The `developer mode <developer-mode>`{.interpreted-text role="ref"}
needs to be activated to access the `Domain`{.interpreted-text
role="guilabel"} condition from the `Actions`{.interpreted-text
role="guilabel"} tab. Once done, select the `Domain`{.interpreted-text
role="guilabel"} condition type and click `New Rule`{.interpreted-text
role="guilabel"}.

To create a rule, you typically select a `field`{.interpreted-text
role="guilabel"}, an `operator`{.interpreted-text role="guilabel"}, and
a `value`{.interpreted-text role="guilabel"}. For example, if you want
to add a workflow action to all the PDF files inside a workspace, set
the `field`{.interpreted-text role="guilabel"} to *Mime Type*, the
`operator`{.interpreted-text role="guilabel"} to *contains*, and the pdf
`value`{.interpreted-text role="guilabel"}.



Click the `fa-plus`{.interpreted-text role="icon"}
(`Add New Rule`{.interpreted-text role="guilabel"}) icon and the
`fa-sitemap`{.interpreted-text role="icon"}
(`Add branch`{.interpreted-text role="guilabel"}) icon to add conditions
and sub-conditions. You can then specify if your rule should match
`all`{.interpreted-text role="guilabel"} or `any`{.interpreted-text
role="guilabel"} conditions. You can also edit the rule directly using
the `Code editor`{.interpreted-text role="guilabel"}.

### Configure the actions

Select the `Actions`{.interpreted-text role="guilabel"} tab to set up
your action. You can simultaneously:

-   **Move to Workspace**: move the file to any workspace;
-   **Create**: create one of the following items attached to the file
    in your database:
    -   **Link to record**: create a link between a document and a
        record from a specific model;
    -   **Product template**: create a product you can edit directly;
    -   **Task**: create a Project task you can edit directly;
    -   **Signature PDF template**: create a new Sign template to send
        out;
    -   **PDF to sign**: create a Sign template to sign directly;
    -   **Applicant**: create a new HR application you can edit
        directly;
    -   **Vendor bill**: create a vendor bill using OCR and AI to scrape
        information from the file content;
    -   **Customer invoice**: create an invoice using OCR and AI to
        scrape information from the file;
    -   **Vendor credit note**: create a vendor credit note using OCR
        and AI to scrape information from the file;
    -   **Credit note**: create a customer credit note using OCR and AI
        to scrape information from the file;
    -   **Miscellaneous Operations**: create an entry in the
        Miscellaneous Operations journal;
    -   **Bank Statement**: import a bank statement;
    -   **Purchase Receipt**: create a vendor receipt;
    -   **Expense**: create an HR expense.
-   **Set Contact**: add a contact to the file, or replace an existing
    contact with a new one;
-   **Set Owner**: add an owner to the file, or replace an existing
    owner with a new one;
-   **Set Tags**: add, remove, and replace any number of tags;
-   **Activities - Mark all as Done**: mark all activities linked to the
    file as done;
-   **Activities - Schedule Activity**: create a new activity linked to
    the file as configured in the action. You can choose to set the
    activity on the document owner.



Digitize documents with AI and optical character recognition (OCR)
------------------------------------------------------------------

Documents available in the Finance workspace can be digitized. Select
the document to digitize, click `Create Bill`{.interpreted-text
role="guilabel"}, `Create Customer Invoice`{.interpreted-text
role="guilabel"}, or `Create credit note`{.interpreted-text
role="guilabel"}, and then click
`Send for Digitization`{.interpreted-text role="guilabel"}.

::: {.seealso}
`AI-powered document digitization <../finance/accounting/vendor_bills/invoice_digitization>`{.interpreted-text
role="doc"}
:::
