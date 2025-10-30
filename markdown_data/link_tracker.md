# File: /content/odoo_doc17.0/fr/content/applications/websites/website/reporting/link_tracker.md

Link tracker
============

The link tracker allow you to create tracked links to measure your
marketing campaigns\' effectiveness. They let you determine which
channels bring you the most visitors and make informed decisions.

Configuration
-------------

The `Link Tracker`{.interpreted-text role="guilabel"} module is not
installed by default. You need to enable the
`Email Marketing`{.interpreted-text role="guilabel"} option by going to
`Website --> Configuration -->
Settings.`{.interpreted-text role="menuselection"} Alternatively, you
can `install <../../../general/apps_modules>`{.interpreted-text
role="doc"} the `Link
Tracker`{.interpreted-text role="guilabel"} module itself or one of the
marketing apps.

Create a traceable URL
----------------------

To create and manage tracked links, navigate to
`Website --> Site --> Link Tracker`{.interpreted-text
role="menuselection"}. Fill in the following information and click
`Get tracked link`{.interpreted-text role="guilabel"} to generate a
tracking URL.

1.  `URL`{.interpreted-text role="guilabel"}: The URL which is the
    target of the campaign. It is automatically populated with the URL
    from where you access the menu.
2.  `Campaign`{.interpreted-text role="guilabel"}: The specific campaign
    the link should be associated with. This parameter is used to
    distinguish the different campaigns.
3.  `Medium`{.interpreted-text role="guilabel"}: The medium describes
    the category or method through which the visitor arrives at your
    site, such as organic search, paid search, social media ad, email,
    etc.
4.  `Source`{.interpreted-text role="guilabel"}: The source identifies
    the precise platform or website that referred the visitor, such as a
    search engine, a newsletter, or a website.



The `Campaign`{.interpreted-text role="guilabel"},
`Medium`{.interpreted-text role="guilabel"}, and
`Source`{.interpreted-text role="guilabel"} are called `UTM (Urchin
Tracking Module)`{.interpreted-text role="abbr"} parameters. They are
incorporated in the tracked URL.

### Website visibility

You can use the `UTM (Urchin Tracking Module)`{.interpreted-text
role="abbr"} parameters to hide or show building blocks for specific
audiences. To achieve this, click the `Edit`{.interpreted-text
role="guilabel"} button on your website, select a building block, go to
the `Customize`{.interpreted-text role="guilabel"} tab, scroll down to
`Visibility`{.interpreted-text role="guilabel"}, and click
`Conditionally`{.interpreted-text role="guilabel"}.



For each parameter available in the
`Visibility <building_blocks/visibility>`{.interpreted-text role="ref"}
section, you can choose `Visible for`{.interpreted-text role="guilabel"}
or `Hidden for`{.interpreted-text role="guilabel"} and select the record
you want from the dropdown list.

Tracked links overview
----------------------

To get an overview of your tracked links, go to
`Website --> Site --> Link Tracker`{.interpreted-text
role="menuselection"} and scroll down to
`Your tracked links`{.interpreted-text role="guilabel"} section.



### Statistics

To measure the performance of tracked links, click the
`Stats`{.interpreted-text role="guilabel"} button.



Scroll down to the `Statistics`{.interpreted-text role="guilabel"}
section to get an overview of the number of clicks of your tracked
links. You can display information for a specific period by clicking the
`All Time`{.interpreted-text role="guilabel"},
`Last Month`{.interpreted-text role="guilabel"}, or
`Last Week`{.interpreted-text role="guilabel"} options.
