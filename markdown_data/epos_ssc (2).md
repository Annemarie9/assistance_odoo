Self-signed certificate for ePOS printers {#epos_ssc/ePOS printers}
=========================================

To work with Odoo, some printer models that can be used without an
`IoT system </applications/general/iot>`{.interpreted-text role="doc"}
may require `the HTTPS protocol <https>`{.interpreted-text role="doc"}
to establish a secure connection between the browser and the printer.
However, trying to reach the printer\'s IP address using HTTPS leads to
a warning page on most web browsers. In that case, you can temporarily
`force the connection <epos_ssc/instructions>`{.interpreted-text
role="ref"}, which allows you to reach the page in HTTPS and use the
ePOS printer in Odoo as long as the browser window stays open.

::: {.warning}
::: {.title}
Warning
:::

The connection is lost after closing the browser window. Therefore, this
method should only be used as a **workaround** or as a pre-requisite for
the `following instructions
<epos_ssc/instructions>`{.interpreted-text role="ref"}.
:::

Generate, export, and import self-signed certificates {#epos_ssc/instructions}
-----------------------------------------------------

For a long-term solution, you must generate a **self-signed
certificate**. Then, export and import it into your browser.

::: {.important}
::: {.title}
Important
:::

**Generating** an SSL certificate should only be done **once**. If you
create another certificate, devices using the previous one will lose
HTTPS access.
:::

::: {.tabs}
::: {.tab}
Windows 10 & Linux OS

::: {.tabs}
::: {.tab}
Generate a self-signed certificate

Navigate to the ePOS\' IP address (e.g.,
[https://192.168.1.25]{.title-ref}) and force the connection by clicking
`Advanced`{.interpreted-text role="guilabel"} and
`Proceed to [IP address]
(unsafe)`{.interpreted-text role="guilabel"}.

![Warning page on Google Chrome, Windows
10](epos_ssc/browser-https-insecure.png)

Then, sign in using your printer credentials to access the ePOS printer
settings. To sign in, enter [epson]{.title-ref} in the
`ID`{.interpreted-text role="guilabel"} field and your printer serial
number in the `Password`{.interpreted-text role="guilabel"} field.

Click `Certificate List`{.interpreted-text role="guilabel"} in the
`Authentication`{.interpreted-text role="guilabel"} section, and click
`create`{.interpreted-text role="guilabel"} to generate a new
**Self-Signed Certificate**. The `Common
Name`{.interpreted-text role="guilabel"} should be automatically filled
out. If not, fill it in with the printer IP address number. Select the
years the certificate will be valid in the `Validity
Period`{.interpreted-text role="guilabel"} field, click
`Create`{.interpreted-text role="guilabel"}, and
`Reset`{.interpreted-text role="guilabel"} or manually restart the
printer.

The self-signed certificate is generated. Reload the page and click
`SSL/TLS`{.interpreted-text role="guilabel"} in the
`Security`{.interpreted-text role="guilabel"} section to ensure
**Selfsigned Certificate** is correctly selected in the
`Server Certificate`{.interpreted-text role="guilabel"} section.
:::

::: {.tab}
Export a self-signed certificate

The export process is heavily dependent on the
`OS (Operating System)`{.interpreted-text role="abbr"} and the browser.
Start by accessing your ePOS printer settings on your web browser by
navigating to its IP address (e.g., [https://192.168.1.25]{.title-ref}).
Then, force the connection as explained in the **Generate a self-signed
certificate tab**.

If you are using **Google Chrome**,

1.  click `Not secure`{.interpreted-text role="guilabel"} next to the
    search bar, and `Certificate is
    not valid`{.interpreted-text role="guilabel"};

    

2.  go to the `Details`{.interpreted-text role="guilabel"} tab and click
    `Export`{.interpreted-text role="guilabel"};

3.  add [.crt]{.title-ref} at the end of the file name to ensure it has
    the correct extension;

4.  select `Base64-encoded ASCII, single certificate`{.interpreted-text
    role="guilabel"}, at the bottom of the pop-up window;

5.  save, and the certificate is exported.

::: {.warning}
::: {.title}
Warning
:::

Make sure that the certificate ends with the extension
[.crt]{.title-ref}. Otherwise, some browsers might not see the file
during the import process.
:::

If you are using **Mozilla Firefox**,

1.  click the **lock-shaped** icon on the left of the address bar;
2.  go to `Connection not secure --> More information --> Security tab
    --> View certificate`{.interpreted-text role="menuselection"};



1.  scroll down to the `Miscellaneous`{.interpreted-text
    role="guilabel"} section;
2.  click `PEM (cert)`{.interpreted-text role="guilabel"} in the
    `Download`{.interpreted-text role="guilabel"} section;
3.  save, and the certificate is exported.
:::

::: {.tab}
Import a self-signed certificate

The import process is heavily dependent on the
`OS (Operating System)`{.interpreted-text role="abbr"} and the browser.

::: {.tabs}
::: {.tab}
Windows 10

Windows 10 manages certificates, which means that self-signed
certificates must be imported from the certification file rather than
the browser. To do so,

1.  open the Windows File Explorer and locate the downloaded
    certification file;

2.  right-click on the certification file and click `Install
    Certificate`{.interpreted-text role="guilabel"};

3.  select where to install the certificate and for whom - either for
    the `Current User`{.interpreted-text role="guilabel"} or all users
    (`Local Machine`{.interpreted-text role="guilabel"}). Then, click
    `Next`{.interpreted-text role="guilabel"};

4.  on the [Certificate Store]{.title-ref} screen, tick
    `Place all certificates in
    the following store`{.interpreted-text role="guilabel"}, click
    `Browse...`{.interpreted-text role="guilabel"}, and select
    `Trusted Root Certification Authorities`{.interpreted-text
    role="guilabel"};

    

5.  click `Finish`{.interpreted-text role="guilabel"}, accept the pop-up
    security window;

6.  restart the computer to make sure that the changes are applied.
:::

::: {.tab}
Linux

If you are using **Google Chrome**,

1.  open Chrome;
2.  go to `Settings --> Privacy and security --> Security -->
    Manage certificates`{.interpreted-text role="menuselection"};
3.  go to the `Authorities`{.interpreted-text role="guilabel"} tab,
    click `Import`{.interpreted-text role="guilabel"}, and select the
    exported certification file;
4.  accept all warnings;
5.  click `ok`{.interpreted-text role="guilabel"};
6.  restart your browser.

If you are using **Mozilla Firefox**,

1.  open Firefox;
2.  go to `Settings --> Privacy & Security --> Security --> View
    Certificates... --> Import`{.interpreted-text role="menuselection"};
3.  select the exported certification file;
4.  tick the checkboxes and validate;
5.  restart your browser.
:::
:::
:::
:::
:::

::: {.tab}
Mac OS

On Mac OS, you can secure the connection for all browsers by following
these steps:

1.  open Safari and navigate to your printer\'s IP address. Doing so
    leads to a warning page;
2.  on the warning page, go to
    `Show Details --> visit this website --> Visit
    Website`{.interpreted-text role="menuselection"}, validate;
3.  reboot the printer so you can use it with any other browser.

To generate and export an SSL certificate and send it to IOS devices,
open **Google Chrome** or **Mozilla Firefox**. Then,

::: {.tabs}
::: {.tab}
Generate a self-signed certificate

Navigate to the ePOS\' IP address (e.g.,
[https://192.168.1.25]{.title-ref}) and force the connection by clicking
`Advanced`{.interpreted-text role="guilabel"} and
`Proceed to [IP address]
(unsafe)`{.interpreted-text role="guilabel"}.

![Warning page on Google Chrome, Windows
10](epos_ssc/browser-https-insecure.png)

Then, sign in using your printer credentials to access the ePOS printer
settings. To sign in, enter [epson]{.title-ref} in the
`ID`{.interpreted-text role="guilabel"} field and your printer serial
number in the `Password`{.interpreted-text role="guilabel"} field.

Click `Certificate List`{.interpreted-text role="guilabel"} in the
`Authentication`{.interpreted-text role="guilabel"} section, and click
`create`{.interpreted-text role="guilabel"} to generate a new
**Self-Signed Certificate**. The `Common
Name`{.interpreted-text role="guilabel"} should be automatically filled
out. If not, fill it in with the printer IP address number. Select the
years the certificate will be valid in the `Validity
Period`{.interpreted-text role="guilabel"} field, click
`Create`{.interpreted-text role="guilabel"}, and
`Reset`{.interpreted-text role="guilabel"} or manually restart the
printer.

The self-signed certificate is generated. Reload the page and click
`SSL/TLS`{.interpreted-text role="guilabel"} in the
`Security`{.interpreted-text role="guilabel"} section to ensure
**Selfsigned Certificate** is correctly selected in the
`Server Certificate`{.interpreted-text role="guilabel"} section.
:::

::: {.tab}
Export a self-signed certificate

The export process is heavily dependent on the
`OS (Operating System)`{.interpreted-text role="abbr"} and the browser.
Start by accessing your ePOS printer settings on your web browser by
navigating to its IP address (e.g., [https://192.168.1.25]{.title-ref}).
Then, force the connection as explained in the **Generate a self-signed
certificate tab**.

If you are using **Google Chrome**,

1.  click `Not secure`{.interpreted-text role="guilabel"} next to the
    search bar, and `Certificate is
    not valid`{.interpreted-text role="guilabel"};

    

2.  go to the `Details`{.interpreted-text role="guilabel"} tab and click
    `Export`{.interpreted-text role="guilabel"};

3.  add [.crt]{.title-ref} at the end of the file name to ensure it has
    the correct extension;

4.  select `Base64-encoded ASCII, single certificate`{.interpreted-text
    role="guilabel"}, at the bottom of the pop-up window;

5.  save, and the certificate is exported.

::: {.warning}
::: {.title}
Warning
:::

Make sure that the certificate ends with the extension
[.crt]{.title-ref}. Otherwise, some browsers might not find the file
during the import process.
:::

If you are using **Mozilla Firefox**,

1.  click the **lock-shaped** icon on the left of the address bar;

2.  go to `Connection not secure --> More information --> Security tab
    --> View certificate`{.interpreted-text role="menuselection"};

    

3.  scroll down to the `Miscellaneous`{.interpreted-text
    role="guilabel"} section;

4.  click `PEM (cert)`{.interpreted-text role="guilabel"} in the
    `Download`{.interpreted-text role="guilabel"} section;

5.  save, and the certificate is exported.
:::
:::
:::

::: {.tab}
Android OS

To import an SSL certificate into an Android device, first create and
export it from a computer. Next, transfer the [.crt]{.title-ref} file to
the device using email, Bluetooth, or USB. Once the file is on the
device,

1.  open the settings and search for [certificate]{.title-ref};
2.  click `Certificate AC`{.interpreted-text role="guilabel"} (Install
    from device storage);
3.  select the certificate file to install it on the device.

::: {.note}
::: {.title}
Note
:::

The specific steps for installing a certificate may vary depending on
the version of Android and the device manufacturer.
:::
:::

::: {.tab}
iOS

To import an SSL certificate into an iOS device, first create and export
it from a computer. Then, transfer the [.crt]{.title-ref} file to the
device using email, Bluetooth, or any file-sharing service.

Downloading this file triggers a warning pop-up window. Click
`Allow`{.interpreted-text role="guilabel"} to download the configuration
profile, and close the second pop-up window. Then,

1.  go to the **Settings App** on the iOS device;
2.  click `Profile Downloaded`{.interpreted-text role="guilabel"} under
    the user\'s details box;
3.  locate the downloaded [.crt]{.title-ref} file and select it;
4.  click `Install`{.interpreted-text role="guilabel"} on the top right
    of the screen;
5.  if a passcode is set on the device, enter the passcode;
6.  click `Install`{.interpreted-text role="guilabel"} on the top right
    of the certificate warning screen and the pop-up window;
7.  click `Done`{.interpreted-text role="guilabel"}.



The certificate is installed, but it still needs to be authenticated. To
do so,

1.  go to
    `Settings --> General --> About > Certificate Trust Settings`{.interpreted-text
    role="menuselection"};
2.  enable the installed certificate using the **slide button**;
3.  click `Continue`{.interpreted-text role="guilabel"} on the pop-up
    window.
:::
:::

::: {.important}
::: {.title}
Important
:::

\- If you need to export SSL certificates from an operating system or
web browser that has not been mentioned, search for [export SSL
certificate]{.title-ref} + [the name of your browser or operating
system]{.title-ref} in your preferred search engine. - Similarly, to
import SSL certificates from an unmentioned OS or browser, search for
[import SSL certificate root authority]{.title-ref} + [the name of your
browser or operating system]{.title-ref} in your preferred search
engine.
:::

Check if the certificate was imported correctly
-----------------------------------------------

To confirm your printer\'s connection is secure, connect to its IP
address using HTTPS. For example, navigate to
[https://192.168.1.25]{.title-ref} in your browser. If the SSL
certificate has been applied correctly, you should no longer see a
warning page, and the address bar should display a padlock icon,
indicating that the connection is secure.
