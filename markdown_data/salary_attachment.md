# File: /content/odoo_doc17.0/fr/content/applications/hr/payroll/salary_attachment.md

Salary attachment report
========================

*Salary attachments* in Odoo refer to a portion of an employee\'s
earnings that are designated for a specific purpose, both voluntary and
involuntary. These can include contributions to a retirement plan,
repayment of a loan, wage garnishments, or child support.

Voluntary salary attachments, such as repaying a loan, or contributing
to a charity on a monthly basis, are considered *Assignments of Salary*
in Odoo. Salary attachments that are required, such as a lawsuit
settlement repayment, or repaying a tax lien, are considered
*Attachments of Salary* in Odoo. Child support payments have their own
category, and are simply referred to as *Child Support* in Odoo.

To view this report, navigate to
`Payroll app --> Reporting --> Salary Attachment
Report`{.interpreted-text role="menuselection"}. The
`Salary Attachment Report`{.interpreted-text role="guilabel"} shows all
deductions or allocations per employee, organized by payslip, in a
default pivot table. The default filter is the end of the current year
(`Payslip End Date: (year)`{.interpreted-text role="guilabel"}). The
employees populate the rows, while the various deductions populate the
columns, organized by type of deduction, and further grouped by
individual payslip.

The default report contains **all** payslips for the current year, so
the report typically contains a large number of columns. This could make
it difficult to view all the data at once, as the report may be very
wide and require scrolling to view all the data.

To view a condensed version of salary attachments, and have all the
salary attachment columns visible on one page, click the
`fa-minus-square-o`{.interpreted-text role="icon"}
`Total`{.interpreted-text role="guilabel"} icon at the top of the
report, above the various payslips.

This presents the salary attachments for the current year, and only
displays three columns, `Attachment of Salary`{.interpreted-text
role="guilabel"}, `Assignment of Salary`{.interpreted-text
role="guilabel"}, and `Child Support.`{.interpreted-text
role="guilabel"}

Each entry displays the total amount paid for each specific type of
salary attachment, for each employee.



The report can be downloaded as an XLSX file, or
`inserted into a spreadsheet
<../../productivity/spreadsheet/insert>`{.interpreted-text role="doc"}
using the corresponding buttons at the top.

Click the `Measures`{.interpreted-text role="guilabel"} button to reveal
the options of what data is displayed.
`Assignment of salary`{.interpreted-text role="guilabel"},
`Attachment of salary`{.interpreted-text role="guilabel"}, and
`Child support`{.interpreted-text role="guilabel"} are all selected and
visible, by default, while the `Count`{.interpreted-text
role="guilabel"} option is not.

Click an option to either show or hide that particular metric. A
`fa-check`{.interpreted-text role="icon"}
`(checkmark)`{.interpreted-text role="guilabel"} icon indicates the data
is visible.

Compare to previous year
------------------------

The `Salary Attachment Report`{.interpreted-text role="guilabel"} can be
compared to the report for the previous time period or the previous
year.

To view these comparisons, click the `fa-caret-down`{.interpreted-text
role="icon"} `(down arrow)`{.interpreted-text role="guilabel"} icon in
the search bar, then click either
`Payslip End Date: Previous Period`{.interpreted-text role="guilabel"}
or `Payslip
End Date: Previous Year`{.interpreted-text role="guilabel"}, beneath the
`fa-adjust`{.interpreted-text role="icon"}
`Comparison`{.interpreted-text role="guilabel"} column.

The report updates and displays the current time period values, and the
previous time period values, as well as the
`Variation`{.interpreted-text role="guilabel"} between the two, in a
percentage.


