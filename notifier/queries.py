select_all_shops_to_notify = """SELECT
                bg.a_month 'date',
                sh.a_id 'shop_id',
                bg.a_budget_amount 'budget amount',
                bg.a_amount_spent 'amount spent',
                CONCAT(ROUND((a_budget_amount - bg.a_amount_spent) / bg.a_budget_amount  * 100, 2), '%') 'available'
                FROM t_shops sh
                    JOIN t_budgets bg ON sh.a_id = bg.a_shop_id
                 WHERE
                    sh.a_online AND
                    bg.a_amount_spent >= bg.a_budget_amount/2 AND
                    bg.a_amount_spent < bg.a_budget_amount AND
                    bg.a_month = (SELECT a_month FROM t_budgets ORDER BY a_month DESC LIMIT 1) AND
                    bg.notified IS FALSE
        UNION
       SELECT
                bg.a_month 'date',
                sh.a_id 'shop_id',
                bg.a_budget_amount 'budget amount',
                bg.a_amount_spent 'amount spent',
                CONCAT(ROUND((a_budget_amount - bg.a_amount_spent) / bg.a_budget_amount  * 100, 2), '%') 'available'
                FROM t_shops sh
                    JOIN t_budgets bg ON sh.a_id = bg.a_shop_id
                 WHERE
                     bg.a_amount_spent >= bg.a_budget_amount AND
                    bg.a_month = (SELECT a_month FROM t_budgets ORDER BY a_month DESC LIMIT 1)
                    AND ((bg.notified is FALSE) OR
                    ( bg.notified is TRUE
                        AND sh.a_online is TRUE
                     ))
                  """

set_shop_offline = """UPDATE t_shops 
                                       SET a_online = FALSE 
                                       WHERE a_id = %(shop_id)s AND a_online IS TRUE"""

mark_notified = """UPDATE t_budgets 
                                       SET notified = TRUE 
                                       WHERE a_shop_id = %(shop_id)s AND a_month = %(date)s"""