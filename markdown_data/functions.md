# File: /content/odoo_doc17.0/fr/content/applications/productivity/spreadsheet/functions.md

Functions
=========

Spreadsheet functions are divided in the following categories:

-   `Array <functions/array>`{.interpreted-text role="ref"}
-   `Database <functions/database>`{.interpreted-text role="ref"}
-   `Date <functions/date>`{.interpreted-text role="ref"}
-   `Engineering <functions/engineering>`{.interpreted-text role="ref"}
-   `Filter <functions/filter>`{.interpreted-text role="ref"}
-   `Financial <functions/financial>`{.interpreted-text role="ref"}
-   `Info <functions/info>`{.interpreted-text role="ref"}
-   `Logical <functions/logical>`{.interpreted-text role="ref"}
-   `Lookup <functions/lookup>`{.interpreted-text role="ref"}
-   `Math <functions/math>`{.interpreted-text role="ref"}
-   `Misc <functions/misc>`{.interpreted-text role="ref"}
-   `Odoo <functions/odoo>`{.interpreted-text role="ref"}
-   `Operators <functions/operators>`{.interpreted-text role="ref"}
-   `Statistical <functions/statistical>`{.interpreted-text role="ref"}
-   `Text <functions/text>`{.interpreted-text role="ref"}
-   `Web <functions/web>`{.interpreted-text role="ref"}

::: {.note}
::: {.title}
Note
:::

Formulas containing functions that are not compatible with Excel are
replaced by their evaluated result when exporting a spreadsheet.
:::

Array {#functions/array}
-----

  Name and arguments                                 Description or link
  -------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------
  ARRAY.CONSTRAIN(input\_range, rows, columns)       Returns a result array constrained to a specific width and height (not compatible with Excel)
  CHOOSECOLS(array, col\_num, \
  CHOOSEROWS(array, row\_num, \
  EXPAND(array, rows, \
  FLATTEN(range, \[range2, \...\])                   Flattens all the values from one or more ranges into a single column (not compatible with Excel)
  FREQUENCY(data, classes)                           
  HSTACK(range1, \
  MDETERM(square\_matrix)                            
  MINVERSE(square\_matrix)                           
  MMULT(matrix1, matrix2)                            
  SUMPRODUCT(range1, \
  SUMX2MY2(array\_x, array\_y)                       
  SUMX2PY2(array\_x, array\_y)                       
  SUMXMY2(array\_x, array\_y)                        
  TOCOL(array, \
  TOROW(array, \
  TRANSPOSE(range)                                   
  VSTACK(range1, \
  WRAPCOLS(range, wrap\_count, \
  WRAPROWS(range, wrap\_count, \

Database {#functions/database}
--------

  Name and arguments                    Description or link
  ------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  DAVERAGE(database, field, criteria)   
  DCOUNT(database, field, criteria)     
  DCOUNTA(database, field, criteria)    
  DGET(database, field, criteria)       
  DMAX(database, field, criteria)       
  DMIN(database, field, criteria)       
  DPRODUCT(database, field, criteria)   
  DSTDEV(database, field, criteria)     
  DSTDEVP(database, field, criteria)    
  DSUM(database, field, criteria)       
  DVAR(database, field, criteria)       
  DVARP(database, field, criteria)      

Date {#functions/date}
----

  Name and arguments                                                    Description or link
  --------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  DATE(year, month, day)                                                
  DATEDIF(start\_date, end\_date, unit)                                 
  DATEVALUE(date\_string)                                               
  DAY(date)                                                             
  DAYS(end\_date, start\_date)                                          
  DAYS360(start\_date, end\_date, \
  EDATE(start\_date, months)                                            
  EOMONTH(start\_date, months)                                          
  HOUR(time)                                                            
  ISOWEEKNUM(date)                                                      
  MINUTE(time)                                                          
  MONTH(date)                                                           
  NETWORKDAYS(start\_date, end\_date, \
  NETWORKDAYS.INTL(start\_date, end\_date, \
  NOW()                                                                 
  SECOND(time)                                                          
  TIME(hour, minute, second)                                            
  TIMEVALUE(time\_string)                                               
  TODAY()                                                               
  WEEKDAY(date, \
  WEEKNUM(date, \
  WORKDAY(start\_date, num\_days, \
  WORKDAY.INTL(start\_date, num\_days, \
  YEAR(date)                                                            
  YEARFRAC(start\_date, end\_date, \[day\_count\_convention\])          Exact number of years between two dates (not compatible with Excel)
  MONTH.START(date)                                                     First day of the month preceding a date (not compatible with Excel)
  MONTH.END(date)                                                       Last day of the month following a date (not compatible with Excel)
  QUARTER(date)                                                         Quarter of the year a specific date falls in (not compatible with Excel)
  QUARTER.START(date)                                                   First day of the quarter of the year a specific date falls in (not compatible with Excel)
  QUARTER.END(date)                                                     Last day of the quarter of the year a specific date falls in (not compatible with Excel)
  YEAR.START(date)                                                      First day of the year a specific date falls in (not compatible with Excel)
  YEAR.END(date)                                                        Last day of the year a specific date falls in (not compatible with Excel)

Engineering {#functions/engineering}
-----------

  Name and arguments            Description or link
  ----------------------------- -----------------------------------------------------------------------------------------------------------------
  DELTA(number1, \

Filter {#functions/filter}
------

  Name and arguments                                 Description or link
  -------------------------------------------------- -------------------------------------------------------------------------------------------------------------------
  FILTER(range, condition1, \
  UNIQUE(range, \

Financial {#functions/financial}
---------

  Name and arguments                                                                                                            Description or link
  ----------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------
  ACCRINTM(issue, maturity, rate, redemption, \
  AMORLINC(cost, purchase\_date, first\_period\_end, salvage, period, rate, \
  COUPDAYS(settlement, maturity, frequency, \
  COUPDAYBS(settlement, maturity, frequency, \
  COUPDAYSNC(settlement, maturity, frequency, \
  COUPNCD(settlement, maturity, frequency, \
  COUPNUM(settlement, maturity, frequency, \
  COUPPCD(settlement, maturity, frequency, \
  CUMIPMT(rate, number\_of\_periods, present\_value, first\_period, last\_period, \
  CUMPRINC(rate, number\_of\_periods, present\_value, first\_period, last\_period, \
  DB(cost, salvage, life, period, \
  DDB(cost, salvage, life, period, \
  DISC(settlement, maturity, price, redemption, \
  DOLLARDE(fractional\_price, unit)                                                                                             
  DOLLARFR(decimal\_price, unit)                                                                                                
  DURATION(settlement, maturity, rate, yield, frequency, \
  EFFECT(nominal\_rate, periods\_per\_year)                                                                                     
  FV(rate, number\_of\_periods, payment\_amount, \
  FVSCHEDULE(principal, rate\_schedule)                                                                                         
  INTRATE(settlement, maturity, investment, redemption, \
  IPMT(rate, period, number\_of\_periods, present\_value, \
  IRR(cashflow\_amounts, \
  ISPMT(rate, period, number\_of\_periods, present\_value)                                                                      
  MDURATION(settlement, maturity, rate, yield, frequency, \
  MIRR(cashflow\_amounts, financing\_rate, reinvestment\_return\_rate)                                                          
  NOMINAL(effective\_rate, periods\_per\_year)                                                                                  
  NPER(rate, payment\_amount, present\_value, \
  NPV(discount, cashflow1, \
  PDURATION(rate, present\_value, future\_value)                                                                                
  PMT(rate, number\_of\_periods, present\_value, \
  PPMT(rate, period, number\_of\_periods, present\_value, \
  PV(rate, number\_of\_periods, payment\_amount, \
  PRICE(settlement, maturity, rate, yield, redemption, frequency, \
  PRICEDISC(settlement, maturity, discount, redemption, \
  PRICEMAT(settlement, maturity, issue, rate, yield, \
  RATE(number\_of\_periods, payment\_per\_period, present\_value, \
  RECEIVED(settlement, maturity, investment, discount, \
  RRI(number\_of\_periods, present\_value, future\_value)                                                                       
  SLN(cost, salvage, life)                                                                                                      
  SYD(cost, salvage, life, period)                                                                                              
  TBILLPRICE(settlement, maturity, discount)                                                                                    
  TBILLEQ(settlement, maturity, discount)                                                                                       
  TBILLYIELD(settlement, maturity, price)                                                                                       
  VDB(cost, salvage, life, start, end, \
  XIRR(cashflow\_amounts, cashflow\_dates, \
  XNPV(discount, cashflow\_amounts, cashflow\_dates)                                                                            
  YIELD(settlement, maturity, rate, price, redemption, frequency, \
  YIELDDISC(settlement, maturity, price, redemption, \
  YIELDMAT(settlement, maturity, issue, rate, price, \

Info {#functions/info}
----

  Name and arguments   Description or link
  -------------------- ------------------------------------------------------------------------------------------------------------
  ISERR(value)         
  ISERROR(value)       
  ISLOGICAL(value)     
  ISNA(value)          
  ISNONTEXT(value)     
  ISNUMBER(value)      
  ISTEXT(value)        
  ISBLANK(value)       
  NA()                 

Logical {#functions/logical}
-------

  Name and arguments                                                Description or link
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
  AND(logical\_expression1, \
  FALSE()                                                           
  IF(logical\_expression, value\_if\_true, \
  IFERROR(value, \
  IFNA(value, \
  IFS(condition1, value1, \
  NOT(logical\_expression)                                          
  OR(logical\_expression1, \
  TRUE()                                                            
  XOR(logical\_expression1, \

Lookup {#functions/lookup}
------

  Name and arguments                                                                                          Description or link
  ----------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
  ADDRESS(row, column, \
  COLUMN(\
  COLUMNS(range)                                                                                              
  HLOOKUP(search\_key, range, index, \
  INDEX(reference, row, column)                                                                               
  LOOKUP(search\_key, search\_array, \
  MATCH(search\_key, range, \
  ROW(\
  ROWS(range)                                                                                                 
  VLOOKUP(search\_key, range, index, \
  XLOOKUP(search\_key, lookup\_range, return\_range, \

Math {#functions/math}
----

  Name and arguments                                                                                      Description or link
  ------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------
  ABS(value)                                                                                              
  ACOS(value)                                                                                             
  ACOSH(value)                                                                                            
  ACOT(value)                                                                                             
  ACOTH(value)                                                                                            
  ASIN(value)                                                                                             
  ASINH(value)                                                                                            
  ATAN(value)                                                                                             
  ATAN2(x, y)                                                                                             
  ATANH(value)                                                                                            
  CEILING(value, \
  CEILING.MATH(number, \
  CEILING.PRECISE(number, \
  COS(angle)                                                                                              
  COSH(value)                                                                                             
  COT(angle)                                                                                              
  COTH(value)                                                                                             
  COUNTBLANK(value1, \
  COUNTIF(range, criterion)                                                                               
  COUNTIFS(criteria\_range1, criterion1, \
  COUNTUNIQUE(value1, \[value2, \...\])                                                                   Counts number of unique values in a range (not compatible with Excel)
  COUNTUNIQUEIFS(range, criteria\_range1, criterion1, \[criteria\_range2, \...\], \[criterion2, \...\])   Counts number of unique values in a range, filtered by a set of criteria (not compatible with Excel)
  CSC(angle)                                                                                              
  CSCH(value)                                                                                             
  DECIMAL(value, base)                                                                                    
  DEGREES(angle)                                                                                          
  EXP(value)                                                                                              
  FLOOR(value, \
  FLOOR.MATH(number, \
  FLOOR.PRECISE(number, \
  INT(value)                                                                                              
  ISEVEN(value)                                                                                           
  ISO.CEILING(number, \
  ISODD(value)                                                                                            
  LN(value)                                                                                               
  MOD(dividend, divisor)                                                                                  
  MUNIT(dimension)                                                                                        
  ODD(value)                                                                                              
  PI()                                                                                                    
  POWER(base, exponent)                                                                                   
  PRODUCT(factor1, \
  RAND()                                                                                                  
  RANDARRAY(\
  RANDBETWEEN(low, high)                                                                                  
  ROUND(value, \
  ROUNDDOWN(value, \
  ROUNDUP(value, \
  SEC(angle)                                                                                              
  SECH(value)                                                                                             
  SIN(angle)                                                                                              
  SINH(value)                                                                                             
  SQRT(value)                                                                                             
  SUM(value1, \
  SUMIF(criteria\_range, criterion, \
  SUMIFS(sum\_range, criteria\_range1, criterion1, \
  TAN(angle)                                                                                              
  TANH(value)                                                                                             
  TRUNC(value, \

Misc {#functions/misc}
----

  Name and arguments                     Description or link
  -------------------------------------- ---------------------------------------------------------
  FORMAT.LARGE.NUMBER(value, \[unit\])   Apply a large number format (not compatible with Excel)

Odoo {#functions/odoo}
----

  Name and arguments                                                                              Description or link
  ----------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ODOO.CREDIT(account\_codes, date\_range, \[offset\], \[company\_id\], \[include\_unposted\])    Get the total credit for the specified account(s) and period (not compatible with Excel)
  ODOO.DEBIT(account\_codes, date\_range, \[offset\], \[company\_id\], \[include\_unposted\])     Get the total debit for the specified account(s) and period (not compatible with Excel)
  ODOO.BALANCE(account\_codes, date\_range, \[offset\], \[company\_id\], \[include\_unposted\])   Get the total balance for the specified account(s) and period (not compatible with Excel)
  ODOO.FISCALYEAR.START(day, \[company\_id\])                                                     Returns the starting date of the fiscal year encompassing the provided date (not compatible with Excel)
  ODOO.FISCALYEAR.END(day, \[company\_id\])                                                       Returns the ending date of the fiscal year encompassing the provided date (not compatible with Excel)
  ODOO.ACCOUNT.GROUP(type)                                                                        Returns the account ids of a given group (not compatible with Excel)
  ODOO.CURRENCY.RATE(currency\_from, currency\_to, \[date\])                                      This function takes in two currency codes as arguments, and returns the exchange rate from the first currency to the second as float (not compatible with Excel)
  ODOO.LIST(list\_id, index, field\_name)                                                         Get the value from a list (not compatible with Excel)
  ODOO.LIST.HEADER(list\_id, field\_name)                                                         Get the header of a list (not compatible with Excel)
  ODOO.FILTER.VALUE(filter\_name)                                                                 Return the current value of a spreadsheet filter (not compatible with Excel)
  ODOO.PIVOT(pivot\_id, measure\_name, \[domain\_field\_name, \...\], \[domain\_value, \...\])    Get the value from a pivot (not compatible with Excel)
  ODOO.PIVOT.HEADER(pivot\_id, \[domain\_field\_name, \...\], \[domain\_value, \...\])            Get the header of a pivot (not compatible with Excel)
  ODOO.PIVOT.TABLE(pivot\_id, \[row\_count\], \[include\_total\], \[include\_column\_titles\])    Get a pivot table (not compatible with Excel)

Operators {#functions/operators}
---------

  Name and arguments           Description or link
  ---------------------------- -------------------------------------------------------------------------------------------------------------------
  ADD(value1, value2)          Sum of two numbers (not compatible with Excel)
  CONCAT(value1, value2)       
  DIVIDE(dividend, divisor)    One number divided by another (not compatible with Excel)
  EQ(value1, value2)           Equal (not compatible with Excel)
  GT(value1, value2)           Strictly greater than (not compatible with Excel)
  GTE(value1, value2)          Greater than or equal to (not compatible with Excel)
  LT(value1, value2)           Less than (not compatible with Excel)
  LTE(value1, value2)          Less than or equal to (not compatible with Excel)
  MINUS(value1, value2)        Difference of two numbers (not compatible with Excel)
  MULTIPLY(factor1, factor2)   Product of two numbers (not compatible with Excel)
  NE(value1, value2)           Not equal (not compatible with Excel)
  POW(base, exponent)          A number raised to a power (not compatible with Excel)
  UMINUS(value)                A number with the sign reversed (not compatible with Excel)
  UNARY.PERCENT(percentage)    Value interpreted as a percentage (not compatible with Excel)
  UPLUS(value)                 A specified number, unchanged (not compatible with Excel)

Statistical {#functions/statistical}
-----------

  Name and arguments                                                                                           Description or link
  ------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------
  AVEDEV(value1, \
  AVERAGE(value1, \
  AVERAGE.WEIGHTED(values, weights, \[additional\_values, \...\], \[additional\_weights, \...\])               Weighted average (not compatible with Excel)
  AVERAGEA(value1, \
  AVERAGEIF(criteria\_range, criterion, \
  AVERAGEIFS(average\_range, criteria\_range1, criterion1, \
  CORREL(data\_y, data\_x)                                                                                     
  COUNT(value1, \
  COUNTA(value1, \
  COVAR(data\_y, data\_x)                                                                                      
  COVARIANCE.P(data\_y, data\_x)                                                                               
  COVARIANCE.S(data\_y, data\_x)                                                                               
  FORECAST(x, data\_y, data\_x)                                                                                
  GROWTH(known\_data\_y, \[known\_data\_x\], \[new\_data\_x\], \[b\])                                          Fits points to exponential growth trend (not compatible with Excel)
  INTERCEPT(data\_y, data\_x)                                                                                  
  LARGE(data, n)                                                                                               
  LINEST(data\_y, \
  LOGEST(data\_y, \
  MATTHEWS(data\_x, data\_y)                                                                                   Compute the Matthews correlation coefficient of a dataset (not compatible with Excel)
  MAX(value1, \
  MAXA(value1, \
  MAXIFS(range, criteria\_range1, criterion1, \
  MEDIAN(value1, \
  MIN(value1, \
  MINA(value1, \
  MINIFS(range, criteria\_range1, criterion1, \
  PEARSON(data\_y, data\_x)                                                                                    
  PERCENTILE(data, percentile)                                                                                 
  PERCENTILE.EXC(data, percentile)                                                                             
  PERCENTILE.INC(data, percentile)                                                                             
  POLYFIT.COEFFS(data\_y, data\_x, order, \[intercept\])                                                       Compute the coefficients of polynomial regression of the dataset (not compatible with Excel)
  POLYFIT.FORECAST(x, data\_y, data\_x, order, \[intercept\])                                                  Predict value by computing a polynomial regression of the dataset (not compatible with Excel)
  QUARTILE(data, quartile\_number)                                                                             
  QUARTILE.EXC(data, quartile\_number)                                                                         
  QUARTILE.INC(data, quartile\_number)                                                                         
  RANK(value, data, \
  RSQ(data\_y, data\_x)                                                                                        
  SMALL(data, n)                                                                                               
  SLOPE(data\_y, data\_x)                                                                                      
  SPEARMAN(data\_y, data\_x)                                                                                   Compute the Spearman rank correlation coefficient of a dataset (not compatible with Excel)
  STDEV(value1, \
  STDEV.P(value1, \
  STDEV.S(value1, \
  STDEVA(value1, \
  STDEVP(value1, \
  STDEVPA(value1, \
  STEYX(data\_y, data\_x)                                                                                      
  TREND(known\_data\_y, \[known\_data\_x\], \[new\_data\_x\], \[b\])                                           Fits points to linear trend derived via least-squares (not compatible with Excel)
  VAR(value1, \
  VAR.P(value1, \
  VAR.S(value1, \
  VARA(value1, \
  VARP(value1, \
  VARPA(value1, \

Text {#functions/text}
----

  Name and arguments                                                                 Description or link
  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------
  CHAR(table\_number)                                                                
  CLEAN(text)                                                                        
  CONCATENATE(string1, \
  EXACT(string1, string2)                                                            
  FIND(search\_for, text\_to\_search, \
  JOIN(delimiter, value\_or\_array1, \[value\_or\_array2, \...\])                    Concatenates elements of arrays with delimiter (not compatible with Excel)
  LEFT(text, \
  LEN(text)                                                                          
  LOWER(text)                                                                        
  MID(text, starting\_at, extract\_length)                                           
  PROPER(text\_to\_capitalize)                                                       
  REPLACE(text, position, length, new\_text)                                         
  RIGHT(text, \
  SEARCH(search\_for, text\_to\_search, \
  SPLIT(text, delimiter, \
  SUBSTITUTE(text\_to\_search, search\_for, replace\_with, \
  TEXT(number, format)                                                               
  TEXTJOIN(delimiter, ignore\_empty, text1, \
  TRIM(text)                                                                         
  UPPER(text)                                                                        

Web {#functions/web}
---

  Name and arguments                Description or link
  --------------------------------- -------------------------------------------------------------------------------------------------------------------------
  HYPERLINK(url, \
