# File: /content/odoo_doc17.0/fr/content/applications/hr/fleet/models.md

Vehicle models
==============

When adding a vehicle to the fleet, specify the vehicle model to
maintain updated records, which keeps track of specific details, like
maintenance schedules and parts compatibility.

Odoo comes with preconfigured car models from four major auto
manufacturers: Audi, BMW, Mercedes, and Opel.

If a new vehicle model joins the fleet, and it is not one of the
preconfigured models from these manufacturers, the model (and/or
manufacturer) **must** be `added to the
database <fleet/add-model>`{.interpreted-text role="ref"}.

Preconfigured models
--------------------

The following models are preconfigured in Odoo, and do not need to be
added to the database:

  -------------------------------------------------
  AUDI    BMW            Mercedes    Opel
  ------- -------------- ----------- --------------
  A1      Serie 1        Class A     Agilia

  A3      Serie 3        Class B     Ampera

  A4      Serie 5        Class C     Antara

  A5      Serie 6        Class CL    Astra

  A6      Serie 7        Class CLS   AstraGTC

  A7      Serie Hybrid   Class E     Combo Tour

  A8      Serie M        Class GL    Corsa

  Q3      Serie X        Class GLK   Insignia

  Q5      Serie Z4       Class M     Meriva

  Q7                     Class R     Mokka

  TT                     Class S     Zafira

                         Class SLK   Zafira Tourer

                         Class SLS   
  -------------------------------------------------

Add a new model {#fleet/add-model}
---------------

To add a new vehicle model, navigate to
`Fleet app --> Configuration --> Models:
Models`{.interpreted-text role="menuselection"}. Click
`New`{.interpreted-text role="guilabel"}, and in a new vehicle model
form, enter the following information on the form.

::: {.note}
::: {.title}
Note
:::

Be advised, some fields are specific to Belgian based companies, so not
all fields or sections may be visible depending on the location of the
company.
:::

-   `Model name`{.interpreted-text role="guilabel"}: enter the model
    name in the field.

-   `Manufacturer`{.interpreted-text role="guilabel"}: select the
    manufacturer from the drop-down menu. If the manufacturer is not
    configured, type in the manufacturer, and click
    `Create`{.interpreted-text role="guilabel"} or `Create and
    edit..`{.interpreted-text role="guilabel"}.

    ::: {.note}
    ::: {.title}
    Note
    :::

    When the manufacturer is selected, if it is one of the default
    manufacturers in *Odoo*, the logo for the manufacturer automatically
    loads in the image box in the top-right corner.
    :::

-   `Vehicle Type`{.interpreted-text role="guilabel"}: select one of two
    preconfigured vehicle types, either `Car`{.interpreted-text
    role="guilabel"} or `Bike`{.interpreted-text role="guilabel"}, from
    the drop-down menu. The vehicle types are hardcoded in Odoo, and are
    integrated with the *Payroll* application, since vehicles can be
    part of an employee\'s benefits. Adding additional vehicle types is
    *not* possible as it affects payroll.

-   `Category`{.interpreted-text role="guilabel"}: select a category for
    the vehicle from the drop-down menu. To create a new category, type
    in the category and then click
    `Create (new category)`{.interpreted-text role="guilabel"}.

### Information tab

In the `Information`{.interpreted-text role="guilabel"} tab, specify
details about the car model, such as the car size, passenger capacity,
cost settings (applicable to the Belgium localization only), and engine
information.

#### Model section

-   `Seats Number`{.interpreted-text role="guilabel"}: enter how many
    passengers the vehicle can accommodate.
-   `Doors Number`{.interpreted-text role="guilabel"}: enter the number
    of doors the vehicle has.
-   `Color`{.interpreted-text role="guilabel"}: enter the color of the
    vehicle.
-   `Model Year`{.interpreted-text role="guilabel"}: enter the year the
    vehicle was manufactured.
-   `Trailer Hitch`{.interpreted-text role="guilabel"}: tick this
    checkbox if the vehicle has a trailer hitch installed.

#### Salary section

::: {.note}
::: {.title}
Note
:::

The `Salary`{.interpreted-text role="guilabel"} section **only** appears
for Belgian-based companies, and **only** if the company has their
localization setting set to Belgium. The cost values are all *monthly*,
with the exception of the `Catalog Value (VAT Incl.)`{.interpreted-text
role="guilabel"}.
:::

-   `Can be requested`{.interpreted-text role="guilabel"}: tick this
    checkbox if employees can request this model vehicle, if a vehicle
    is part of their employee contract.
-   `Catalog Value (VAT Incl.)`{.interpreted-text role="guilabel"}:
    enter the `MSRP (Manufacturer's Suggested Retail
    Price)`{.interpreted-text role="abbr"} for the vehicle at the time
    of purchase or lease.
-   `C02 fee`{.interpreted-text role="guilabel"}: represents the carbon
    dioxide emission fee paid to the Belgian government. This value is
    automatically calculated, based on Belgian laws and regulations, and
    **cannot** be modified. The value is based on the figure entered in
    the `CO2 Emissions`{.interpreted-text role="guilabel"} field (in the
    `Engine`{.interpreted-text role="guilabel"} section of the
    `Information`{.interpreted-text role="guilabel"} tab) on the vehicle
    form.

::: {.important}
::: {.title}
Important
:::

Modifying the `CO2 Emissions`{.interpreted-text role="guilabel"} field
adjusts the value in the `CO2 fee`{.interpreted-text role="guilabel"}
field.
:::

-   `Cost (Depreciated)`{.interpreted-text role="guilabel"}: enter the
    monthly vehicle cost, which appears in the salary configurator for
    future employees. This value impacts the gross and net salary of the
    employee assigned to the vehicle. This figure is depreciated over
    time, according to local tax laws. The
    `Cost (Depreciated)`{.interpreted-text role="guilabel"} does **not**
    depreciate automatically on the *vehicle model*, it only depreciates
    based on the *contract* linked to a specific vehicle.
-   `Total Cost (Depreciated)`{.interpreted-text role="guilabel"}: this
    value is the combination of the `Cost
    (Depreciated)`{.interpreted-text role="guilabel"} and the
    `C02 fee`{.interpreted-text role="guilabel"} fields. It also
    depreciated over time.

#### Engine

-   `Fuel Type`{.interpreted-text role="guilabel"}: select the type of
    fuel the vehicle uses from the drop-down menu. The options are
    `Diesel`{.interpreted-text role="guilabel"},
    `Gasoline`{.interpreted-text role="guilabel"},
    `Hybrid Diesel`{.interpreted-text role="guilabel"}, `Hybrid
    Gasoline`{.interpreted-text role="guilabel"},
    `Plug-in Hybrid Diesel`{.interpreted-text role="guilabel"},
    `Plug-in Hybrid Gasoline`{.interpreted-text role="guilabel"},
    `CNG`{.interpreted-text role="guilabel"}, `LPG`{.interpreted-text
    role="guilabel"}, `Hydrogen`{.interpreted-text role="guilabel"}, or
    `Electric`{.interpreted-text role="guilabel"}.
-   `CO2 Emissions`{.interpreted-text role="guilabel"}: enter the
    average carbon dioxide emissions the vehicle produces in grams per
    kilometer (g/km). This information is provided by the car
    manufacturer.
-   `CO2 Standard`{.interpreted-text role="guilabel"}: enter the
    standard amount of carbon dioxide in grams per kilometer (g/km) for
    a similar-sized vehicle.
-   `Transmission`{.interpreted-text role="guilabel"}: select
    `Manual`{.interpreted-text role="guilabel"} or
    `Automatic`{.interpreted-text role="guilabel"} transmission from the
    drop-down menu.
-   `Power`{.interpreted-text role="guilabel"}: if the vehicle is
    electric or hybrid, enter the power the vehicle uses in kilowatts
    (kW).
-   `Horsepower`{.interpreted-text role="guilabel"}: enter the
    vehicle\'s horsepower in this field.
-   `Horsepower Taxation`{.interpreted-text role="guilabel"}: enter the
    amount that is taxed, based on the size of the vehicle\'s engine.
    This is determined by local taxes and regulations, and varies
    depending on the location. It is recommended to check with the
    accounting department to ensure this value is correct.
-   `Tax Deduction`{.interpreted-text role="guilabel"}: this field
    auto-populates, according to the engine specifications, and
    **cannot** be modified. The percentage is based on the localization
    settings and local tax laws.

### Vendors tab

Specify the vendors a vehicle can be purchased from in this tab. With
proper setup, requests for quotations for vehicles can be easily created
through Odoo\'s *Purchase* app.

To add a vendor, click `Add`{.interpreted-text role="guilabel"}, which
opens an `Add: Vendors`{.interpreted-text role="guilabel"} pop-up
window, with a list of all the vendors currently in the database. Add a
vendor by ticking the checkbox next to the vendor name, then click
`Select`{.interpreted-text role="guilabel"}. There is no limit to the
number of vendors that can be added to this list.

If a vendor is not in the database, add a vendor by clicking
`New`{.interpreted-text role="guilabel"} in the bottom-left of the
`Add: Vendors`{.interpreted-text role="guilabel"} pop-up window. In the
`Create Vendors`{.interpreted-text role="guilabel"} form that appears,
enter the necessary information, then click
`Save & Close`{.interpreted-text role="guilabel"} to add the vendor, or
click `Save & New`{.interpreted-text role="guilabel"} to add the current
vendor and create another new vendor.

{.align-center}

Model category {#fleet/categories}
--------------

To best organize a fleet, it is recommended to have vehicle models
housed under a specific category, to easily see what kinds of vehicles
are in the fleet. Model categories are set on the `vehicle
model form <fleet/add-model>`{.interpreted-text role="ref"}.

Odoo does **not** come with any models preconfigured; all models
**must** be added.

To view any models currently set up in the database, navigate to
`Fleet app -->
Configuration --> Models: Categories`{.interpreted-text
role="menuselection"}. All models are displayed in a list view.

### Add a new model category

To add a new category, click the `New`{.interpreted-text
role="guilabel"} button in the top-left corner of the
`Categories`{.interpreted-text role="guilabel"} page. A new entry line
appears at the bottom of the list. Type in the new category, then either
click `Save`{.interpreted-text role="guilabel"}, or click anywhere on
the screen, to save the entry.

To reorganize how the categories appear in the list, click on the
`oi-draggable`{.interpreted-text role="icon"}
`(draggable)`{.interpreted-text role="guilabel"} icon to the left of any
desired category name, and drag the line to the desired position.

The order of the list does not affect the database in any way. However,
it may be preferable to view the vehicle categories in a specific order,
for example, by size, or the numbers of passengers the vehicle can
carry.

{.align-center}
