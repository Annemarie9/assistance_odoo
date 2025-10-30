# File: /content/odoo_doc17.0/fr/content/applications/websites/website/web_design/building_blocks.md

show-content

:   

Building blocks
===============

Building blocks let you design your website quickly by dragging and
dropping them onto your web pages. Four types of building blocks are
available depending on their use:
`Structure <building_blocks/structure>`{.interpreted-text role="doc"},
`Features <building_blocks/features>`{.interpreted-text role="doc"},
`Dynamic Content <building_blocks/dynamic_content>`{.interpreted-text
role="doc"}, and
`Inner Content <building_blocks/inner_content>`{.interpreted-text
role="doc"}.

::: {.seealso}
[Odoo Tutorial: Design your first
webpage](https://www.odoo.com/slides/slide/design-your-website-images-and-motion-6931?fullscreen=1)
:::

Adding a building block {#websites/website/web_design/building_blocks}
-----------------------

To add a building block to your website page, click
`Edit`{.interpreted-text role="guilabel"}, select the desired building
block, and drag and drop it to your page. You can add as many blocks as
needed.

To edit the content of a building block, click on it and go to the
`Customize`{.interpreted-text role="guilabel"} tab, where available
features depend on the block you selected.

Color preset and background
---------------------------

You can customize and apply color presets to building blocks. To
proceed, select a building block, go to the
`Customize`{.interpreted-text role="guilabel"} tab, click the
`Background`{.interpreted-text role="guilabel"} button, and select a
`Preset`{.interpreted-text role="guilabel"}.

When you modify a color preset, all elements using it are automatically
updated to match the new configuration.

::: {.seealso}
`Website themes <themes>`{.interpreted-text role="doc"}
:::

Layout: grid and columns
------------------------

You can choose between two layout styles for most building blocks: `grid
<building_blocks/grid>`{.interpreted-text role="ref"} or
`columns (cols) <building_blocks/cols>`{.interpreted-text role="ref"}.
To change the default layout, go to the `Customize`{.interpreted-text
role="guilabel"} tab. Under the `Banner`{.interpreted-text
role="guilabel"} section, select `Grid`{.interpreted-text
role="guilabel"} or `Cols`{.interpreted-text role="guilabel"} as the
`Layout`{.interpreted-text role="guilabel"}.

### Grid {#building_blocks/grid}

The `Grid`{.interpreted-text role="guilabel"} layout allows you to
reposition and resize elements, such as images or text, by dragging and
dropping them.



::: {.tip}
::: {.title}
Tip
:::

Position images behind the text by using the above/below icons.


:::

### Cols {#building_blocks/cols}

Choosing the `Cols`{.interpreted-text role="guilabel"} layout allows you
to determine the number of elements per line within the block. To do so,
select the block to modify, click the `Cols`{.interpreted-text
role="guilabel"} `Layout`{.interpreted-text role="guilabel"}, and adjust
the number.

By default, **on mobile devices**, one element is visible per line to
ensure that content remains easily readable and accessible on smaller
screens. To adjust the value, click the `fa-mobile`{.interpreted-text
role="icon"} (`mobile icon`{.interpreted-text role="guilabel"}) at the
top of the website editor and adapt the number of columns.



Duplicating a building block
----------------------------

You can duplicate a building block by clicking on the duplicate icon.
Once duplicated, the new block appears on your website beneath the
original one.



Reordering a building block
---------------------------

To reorder a building block, select it and click the up arrow to move it
before the previous block or click the down arrow to move it after.

You can also use the drag-and-drop icon to move a block manually.



Saving a custom building block
------------------------------

You can save a customized building block and reuse it elsewhere. To do
so, select it, navigate to the `Customize`{.interpreted-text
role="guilabel"} tab, and click the `fa-floppy-o`{.interpreted-text
role="icon"} (`floppy disk`{.interpreted-text role="guilabel"}) icon to
save it.



Saved building blocks are available in the `Custom`{.interpreted-text
role="guilabel"} section of the `Blocks`{.interpreted-text
role="guilabel"} tab. Click the `fa-pencil`{.interpreted-text
role="icon"} (`pen`{.interpreted-text role="guilabel"}) icon to edit
their name.



Visibility {#building_blocks/visibility}
----------

### Visibility on desktop/mobile

You can hide specific elements depending on the visitor\'s device. To do
so, select the element to hide, and in the `Customize`{.interpreted-text
role="guilabel"} tab, scroll down to `Visibility`{.interpreted-text
role="guilabel"}, and click the `Show/Hide on Mobile`{.interpreted-text
role="guilabel"} or the `Show/Hide on Desktop`{.interpreted-text
role="guilabel"} icon.



::: {.tip}
::: {.title}
Tip
:::

Click the `fa-mobile`{.interpreted-text role="icon"}
(`mobile`{.interpreted-text role="guilabel"}) icon at the top of the
configurator to preview how your website would look on a mobile device.


:::

### Conditional visibility

You can also hide or show building blocks using other conditions. To do
so, select an element, go to `Visibility`{.interpreted-text
role="guilabel"}, click `No condition`{.interpreted-text
role="guilabel"}, and select `Conditionally`{.interpreted-text
role="guilabel"} instead. Then, configure the condition(s) to apply by
selecting `Visible for`{.interpreted-text role="guilabel"} or
`Hidden for`{.interpreted-text role="guilabel"} and which
`Records`{.interpreted-text role="guilabel"} will be impacted.

::: {.seealso}
`Link Tracker <../reporting/link_tracker>`{.interpreted-text role="doc"}
:::

### Invisible elements

Depending on the visibility settings, some elements can become hidden
from your current view. To make a building block visible again, go to
the `Invisible Elements`{.interpreted-text role="guilabel"} section at
the bottom of the configurator and select a building block.

Mobile view customization
-------------------------

You can customize building block elements for the mobile view without
impacting the desktop view. To do so, open the website editor, click the
`fa-mobile`{.interpreted-text role="icon"} (`mobile`{.interpreted-text
role="guilabel"}) icon at the top, and select the building block
element. Then, you can:

-   reorder the elements by clicking the
    `fa-angle-left`{.interpreted-text role="icon"}
    `fa-angle-right`{.interpreted-text role="icon"}
    (`left/right arrow`{.interpreted-text role="guilabel"}) icons;
-   edit the `Cols <building_blocks/cols>`{.interpreted-text role="ref"}
    and `Visibility <building_blocks/visibility>`{.interpreted-text
    role="ref"} features in the `Customize`{.interpreted-text
    role="guilabel"} tab of the website editor.

::: {.toctree titlesonly=""}
building\_blocks/structure building\_blocks/features
building\_blocks/dynamic\_content building\_blocks/inner\_content
:::
