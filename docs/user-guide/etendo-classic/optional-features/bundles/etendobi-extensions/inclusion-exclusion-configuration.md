---

---

# Etendo BI Inclusion/Exclusion Configuration
:octicons-package-16: Javapackage: `com.etendoerp.powerbi.inclusion.exclusion` 

## Overview

!!! info
    To be able to include this functionality, the Etendo BI Bundle must be installed. To do that, follow the instructions from [Marketplace](https://marketplace.etendo.cloud/?#/product-details?module=11372FBD87F34F80AAADBE1C9369CF83){target="_blank"}.

In order to allow users to customize and configure the information and filters in PowerBI reports, a new module has been developed that allows the creation of different configurations that facilitate the selection and exclusion of specific entities within reports.

A detailed description of the configuration window and its components is provided below.

## **Etendo BI Inclusion/Exclusion Configuration** Window:

The window consists of two main tabs: "Header" and "Lines". These tabs are used to define and adjust the filters of PowerBI reports according to the user's specific requirements.

### _Header_

![](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/etendobi-extensions/inclusion-exclusion-configuration/header-bi.png)

**Name and Description**: Text fields that allow the user to easily identify the configuration and understand its purpose.

**Type:** It indicates the type of entity to be included or excluded according to the configuration. This field provides additional information to understand the context of the configuration.  
The options are:

- Business Partner Category
- GL Item
- Product
- Product Category
- Document Type
- Account: If it is necessary to enter accounts, selecting this type enables an Element Level, Account Type and Account Tree selector (required)
- Business Partner
- Sales Representative

!!! note
    If the "Type" field is left empty, it is assumed that the line information is given by one of the auxiliary data (number, string or Yes/No fields). Moreover, in the lines tab, it is possible to combine all the options mentioned above to be included or excluded.

**From and To Date:** date fields to define the duration of the created configuration. If specified in the header, the lines acquire that defined period. If you want the lines to have different periods, set these dates in the corresponding lines.

**Has Number, Has String, Has Boolean:** These checkboxes allow the user to enable additional number, string, or yes/no value fields in the configuration lines. These auxiliary fields are used as needed in reports.

### _Lines tab_

This tab contains the configuration lines associated with the header. Each line represents an element that can be used to include or exclude entities in reports. The fields in the lines are described below:

**Line No.:** Number of the line within the configuration. This number provides a reference to identify and order the lines.

**Document Type:** If the configuration is "Document Type", it allows selecting a specific document type. This field is only displayed if the entity type is "Document Type".

**Business Partner:** If the configuration is "Business Partner", it allows selecting a business partner. This field is only displayed if the entity type is "Business Partner".

**Business Partner Category:** If the configuration is "Business Partner Category", it allows selecting a business partner category. This field is only displayed if the entity type is "Business Partner Category".

**Sales Representative:** If the configuration is "Sales Representative", it allows selecting a sales representative. This field is only displayed if the entity type is "Sales Representative".

**Account**: If the configuration is  "Account", it allows selecting an account, pre-filtered by the related fields in the header. This field is only shown if the entity type is "Account".

**Product Category:** If the configuration is "Product Category", it allows selecting a product category. This field is only displayed if the entity type is "Product Category".

**Product:** If the configuration is "Product", it allows selecting a specific product. This field is only displayed if the entity type is "Product".

**G/L Item**: If the configuration is "GL Item", it allows selecting an accounting concept. This field is only shown if the entity type is "GL Item".

**Number:** Auxiliary field for entering an additional number. This field is only shown if the "Has Number" box is checked.

**String:** Auxiliary text string. It is shown only if the "Has String" check in the header is checked.

**Yes/No:** Auxiliary Yes/No check. Displayed only if the "Has Yes/No" check in the header is checked.

## **Examples**

Etendo accounts settings to take the balances and reflect them in the financial reports in BI:

### _Configuration in Etendo_

Main categories for account configuration:

- Cash
- Banks
- Customers
- Suppliers
- Sales
- Sales Costs

#### Configuration of cash accounts:

![cash.png](../../../../../assets/user-guide/etendo-classic/optional-features/bundles/etendobi-extensions/inclusion-exclusion-configuration/cashpng.png)

#### Configuration of bank accounts:

![bank.png](../../../../../assets/legacy/bank.png)

#### Configuration of customer accounts:

![customers.png](../../../../../assets/legacy/customers.png)

#### Configuration of supplier accounts:

![suppliers.png](../../../../../assets/legacy/suppliers.png)

#### Configuration of sales accounts:

![sales.png](../../../../../assets/legacy/sales.png)

#### Configuration of sales costs accounts:

![sales_cost.png](../../../../../assets/legacy/sales_cost.png)
