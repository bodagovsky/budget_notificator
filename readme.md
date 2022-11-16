# Stylight coding assessment - Budget notifications
Stylight at its core is a platform where fashion retailers can advertise their products. They specify a budget, i.e. an upper limit to the amount of money they are prepared to spend each month in exchange for an equivalent amount of exposure on our platform. Once that budget is exhausted, shops go _offline_ and their products are no longer advertised on Stylight until a new month begins and the advertising budget is replenished.

## General notes
This assignment assumes there is an existing system responsible for managing shop budgets. It is your task to add a feature to that system.  That includes extending the database schema to support the new feature, as well as implementing the desired behaviour.

This folder includes a file `db.sql`. It represents the current state of the database. You may use it to initialise an open-source database of your choice (SQLite, MySQL, PostgreSQL, ...). The dump was generated from a MySQL database. If you're using something else, you might need to make slight syntactical adaptations. Do not modify the provided schema. If you need to make any changes to the DB schema, please provide a separate script to perform those changes.

Please provide a readme file specifying which database system you used and which version.


## Schema
The given database schema consists of two tables: Shops and budgets.

### Shops
The table `t_shops` holds master data about all the shops in our system.

* `a_id` and `a_name` should be self-explanatory.

* `a_online`: Specifies, whether a shop's products are currently being listed on the Stylight website. `1` means they are listed, `0` means they aren't.

### Budgets
The table `t_budgets` holds all shops' monthly budgets.

* `a_shop_id`: Signifies which shop the budget is associated with.

* `a_budget_amount`: Signifies the monetary value a shop is willing to spend with Stylight in a given month.

* `a_amount_spent`: Represents how much money the shop has spent in that month.

* `a_month`: Signifies the month a budget is valid for. The _day_ component of the date is irrelevant and by convention always set to 1.

The amounts spent for the current month are continuously updated until the month ends. Assume a part of the system is already doing that. You may assume all monetary values are in the same currency.


## New Feature
The new feature request revolves around notifying shops when their monthly expenditure reaches certain thresholds. We want to notify shops when they reach 50% of the current month's budget. Once they reach 100% of the current month's budget, the shops should be notified again and set _offline_.


## Implementation
Please write a Python CLI app which when invoked checks all shops' budgets and expenditures for the current month and takes action where necessary. Shops that need to go _offline_ according to the rules in the previous section should be marked as such in the database. To simulate notifying a shop you may print a message to stdout. The message should include the current date, the shop ID, the current month's budget and the expenditure to date in absolute terms as well as as a percentage of the budget.

To accommodate this feature you most likely need to make some changes to the database schema. To do so please don't modify the schema provided in `db.sql`. Instead, provide an additional SQL script `migration.sql` which performs all schema modifications.

When receiving your solution, we will initialise a database by running `db.sql` followed by `migration.sql`. This should result in your intended database schema.


## Readme
* Please provide a readme file which specifies the database system and version you used and include instructions on how to build/run your application.
* Please make building/running your app as simple as possible.
* State the assumptions you made in your design and any changes it would entail in the rest of the system.

## Additional thoughts
Please answer the following questions in your readme:
* Does your solution avoid sending duplicate notifications?
* How does your solution handle a budget change after a notification has already been sent?
