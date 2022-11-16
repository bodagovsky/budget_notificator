import time
import pymysql.cursors
from queries import select_all_shops_to_notify, set_shop_offline, mark_notified
from apply_migrations import apply

if __name__ == '__main__':
    apply()
    connection = pymysql.connect(host='db',
                                 user='root',
                                 password='db-q5n2g',
                                 database='stylight',
                                 autocommit=True,
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection:
        while True:
            with connection.cursor() as cursor:
                cursor.execute(select_all_shops_to_notify)
                result = cursor.fetchall()

                if len(result) == 0:
                    time.sleep(2)
                    continue
                for res in result:
                    if res['amount spent'] >= res['budget amount']:
                        cursor.execute(set_shop_offline, res)
                    cursor.execute(mark_notified, res)

                for res in result:
                    print(f"""
                    Date: {res['date']}, 
                    Shop ID: {res['shop_id']}, 
                    Current month's budget: {res['budget amount']}, 
                    Expenditure to date: {res['amount spent']}, 
                    Available budget: {res['available']}""", flush=True)

            time.sleep(2)



