# Requirements Traceability Matrix (Requirements <-> Use Cases)

## Functional (FR)

| ID        | Requirement Description     | Associated Use Case(s)                  | Status  |
| :-------- | :-------------------------- | :-------------------------------------- | :------ |
| **FR01**  | Add new products.           | **UCb** (Add New Product), **UCa**      | Covered |
| **FR02**  | Edit product information.   | **UCc** (Edit Product Details), **UCa** | Covered |
| **FR03**  | Search for products.        | **UCd** (Search Inventory)              | Covered |
| **FR04**  | Manage product categories.  | **UCg** (Manage Categories)             | Covered |
| **FR05**  | Manage product suppliers.   | **UCf** (Manage Suppliers)              | Covered |
| **FR06**  | Process sales transaction.  | **UCh** (Process Sales Transaction)     | Covered |
| **FR07**  | Generate low-stock reports. | **UCgR** (Generate Low Stock Report)    | Covered |

## Non-Functional (NFR)

| ID        | Requirement Description     | Implementation                                             |
| :-------- | :-------------------------- | :--------------------------------------------------------- |
| **NFR01** | System availability (99.9%) | Architectural requirement                                  |
| **NFR02** | Performance (update < 0.5s) | Constraints applied to **UCh** and **UCb/UCc**             |
| **NFR03** | Role-based authorization    | Managed by **Warehouse Manager** and **Clerk** actor roles |
| **NFR04** | Audit logging               | Covered by **UCx** (Record Audit Log) included in **UCh**  |