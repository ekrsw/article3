import os
import pandas as pd
import pyodbc as pyo

import settings

# SQLクエリ
read_sql_str = '''SELECT *
    FROM T_提出
    WHERE 反映 = 0
    AND 承認区分 = '承認'
    AND 削除 = 0;
'''

class AccessDB:
    def __init__(self) -> None:
        # Accessドライバの確認
        for driver in pyo.drivers():
            if driver.startswith('Microsoft Access Driver'):
                print(driver)

        # データベース接続文字列
        self.con_str = (
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
            rf'DBQ={os.path.join(settings.DB_PATH, settings.DB_NAME)};'
        )

    def read_access(self) -> pd.DataFrame:
        # データベース接続
        con = pyo.connect(self.con_str)
        # SQLクエリを実行し、Pandas DataFrameに結果を取り込む
        df = pd.read_sql(settings.READ_SQL_QUERY, con)
        # 接続を閉じる
        con.close()
        return df
    
    def update_access(self, id) -> None:
        # データベース接続
        con = pyo.connect(self.con_str)
        # カーソルを取得
        cursor = con.cursor()
        # SQLクエリを実行
        cursor.execute(f'{settings.UPDATE_SQL_SQUERY}{id}')
        # コミット
        con.commit()
        # カーソルを閉じる
        cursor.close()
        # 接続を閉じる
        con.close()

access_db = AccessDB()