# File: /content/odoo_doc17.0/fr/content/applications/hr/fleet.md

show-content

:   

Fleet
=====

This document outlines the configurations and settings for the *Fleet*
application, for both `settings <fleet/settings>`{.interpreted-text
role="ref"} and `manufacturers <fleet/manufacturers>`{.interpreted-text
role="ref"}.

Settings {#fleet/settings}
--------

To access the settings menu, go to
`Fleet app --> Configuration --> Settings`{.interpreted-text
role="menuselection"}. Only two settings need configuration:
`End Date Contract Alert`{.interpreted-text role="guilabel"} and
`New Vehicle
Request`{.interpreted-text role="guilabel"}.

{.align-center}

### End Date Contract Alert

The `End Date Contract Alert`{.interpreted-text role="guilabel"} field
how many days before the end of a vehicle contract an alert should be
sent. The responsible people receive an email informing them a vehicle
contract is about to expire in the number of days defined in this field.

::: {.note}
::: {.title}
Note
:::

To determine who the responsible person is for a contract, open an
individual contract. The person listed as
`Responsible`{.interpreted-text role="guilabel"} under the
`Contract Information`{.interpreted-text role="guilabel"} section of the
contract is the person who will receive the alert.

To access all contracts, navigate to
`Fleet app --> Fleet --> Contracts`{.interpreted-text
role="menuselection"} and all contracts appear in the list. Click on a
`Contract`{.interpreted-text role="guilabel"} to view it.

An individual contract can also be found by navigating to
`Fleet app --> Fleet -->
Fleet`{.interpreted-text role="menuselection"} and clicking on an
individual vehicle. On the vehicle form, click the
`Contracts`{.interpreted-text role="guilabel"} smart button at the top
of the page. The contract(s) associated with this vehicle only appears
in the list. Click on an individual contract to open it. The
`Responsible`{.interpreted-text role="guilabel"} person is listed on the
contract.
:::

### New Vehicle Request

The `New Vehicle Request`{.interpreted-text role="guilabel"} field sets
a limit on how many new vehicles are requested based on fleet
availability. An employee filling out the salary configurator form
(after being offered a position), will *not* be able to request a new
car if the number of existing cars is greater than the number specified
in the `New Vehicle Request`{.interpreted-text role="guilabel"} field.
Enter the specific number limit for existing available cars in this
field.

::: {.example}
If the `New Vehicle Request`{.interpreted-text role="guilabel"} limit is
set to 20 vehicles, and there are 25 vehicles available, an employee
would not be able to request a new vehicle. If there are only 10 cars
available, then the employee would be able to request a new vehicle.
:::

Manufacturers {#fleet/manufacturers}
-------------

Odoo *Fleet* comes pre-configured with sixty-six commonly used car and
bicycle manufacturers in the database, along with their logos. To view
the pre-loaded manufacturers, go to `Fleet
app --> Configuration --> Manufacturers`{.interpreted-text
role="menuselection"}.

The manufacturers appear in an alphabetical list. Each manufacturer\'s
card lists how many specific models are configured for each particular
manufacturer. Odoo comes with forty-six preconfigured
`models <fleet/models>`{.interpreted-text role="doc"} from four major
auto manufacturers, and one major bicycle manufacturer: Audi, BMW,
Mercedes, Opel (cars), and Eddy Merckx (bicycle).

{.align-center}

### Add a manufacturer

To add a new manufacturer to the database, click
`Create`{.interpreted-text role="guilabel"}. A manufacturer form will
load. Only two pieces of information are needed, the
`Name`{.interpreted-text role="guilabel"} of the manufacturer, and the
logo. Type the name of the manufacturer in the name field, and select an
image to upload for the logo. When the information is entered, click
`Save`{.interpreted-text role="guilabel"}.

::: {.seealso}
\- `fleet/models`{.interpreted-text role="doc"} -
`fleet/new_vehicle`{.interpreted-text role="doc"} -
`fleet/service`{.interpreted-text role="doc"} -
`fleet/accidents`{.interpreted-text role="doc"}
:::

::: {.toctree titlesonly=""}
fleet/models fleet/new\_vehicle fleet/service fleet/accidents
:::
