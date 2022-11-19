
## How to build
run `docker-compose up` inside root directory
database will be launched, then migrations will be applied

## Database
MySql 8.0

## Design decision
I have decided that adding a column `notified` to the table `t_budgets` will do the trick.

When the 50 % threshold reached first time, shop is notified and `notified` flag is set to True
When shop reaches or exceeds its 100% threshold it is notified again and goes offline

## Assumptions
In my decision I have assumed that shops offline never got their notifications about being setting offline
Also, I assumed that shop can only go offline when its budget is over, so my app only notifies about 50% threshold those shops which are currently online
The last, but not least: I intentionally did not take the current timestamp to filter budgets, but took the last possible date, because I assumed that every month we have some record in db
Taking the timestamp would result in ignoring the fixtures we already have, so I wanted you to see app working with data presented in migrations

## Does your solution avoid sending duplicate notifications?
Yes, because it checks, whether the shop has already been notified, or it is online at the moment when 100% budget threshold is reached

## How does your solution handle a budget change after a notification has already been sent?
I have implemented a worker, which selects the records from database every 2 seconds, so the change will not be missed

## More thoughts
If I had such task in real life, I would have implemented the Transactional Outbox pattern as I think that it would provide the best consistency when updating database record and sending notifications
https://microservices.io/patterns/data/transactional-outbox.html
