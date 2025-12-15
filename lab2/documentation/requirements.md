# Requirements

## Functional (FR)

| ID       | Requirement | Priority |
| :------- | :---------- | :------- |
| **FR01** | The system must allow **adding new products** to the catalog (including SKU, name, price, stock, FK for category and supplier). | High |
| **FR02** | The system must allow **editing information** about existing products (name, price, stock). | High |
| **FR03** | The system must allow **searching for products** by SKU, name, or category. | High |
| **FR04** | The system must allow **adding and editing product categories**. | Medium |
| **FR05** | The system must allow **viewing and updating information** about suppliers (company name, phone). | Medium |
| **FR06** | The system must allow **processing a sales transaction**, which includes reducing product stock and requesting processing from an external payment gateway. | High |
| **FR07** | The system must **generate a report** on low-stock items (stock < 5). | Low |

## Non-Functional (NFR)

| ID        | Requirement | Type |
| :-------- | :---------- | :--- |
| **NFR01** | System availability must be **99.9%** of the time. | Reliability |
| **NFR02** | The execution time for a stock update operation must not exceed **0.5 seconds**. | Performance |
| **NFR03** | Access to editing functions must be controlled using **role-based authorization** (Warehouse Manager vs. Operator). | Security |
| **NFR04** | The system must ensure **auditing** of all data-modifying operations (logging). | Security |