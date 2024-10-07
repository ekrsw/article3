HEADLESS_MODE = False

DB_PATH = r'\\mjs.co.jp\datas\CSC共有フォルダ\enjoyナレッジメンテナンス\第47期\knowlage_db'
DB_NAME = 'datamaster.accdb'

# SQLクエリ
READ_SQL_QUERY = '''SELECT *
    FROM T_提出
    WHERE 反映 = 0
    AND 承認区分 = '承認'
    AND 削除 = 0;
'''

UPDATE_SQL_SQUERY = '''UPDATE T_提出
    SET 反映 = 1
    WHERE 提出ID = '''

RETRY_COUNT = 3

LOG_FILE = 'appserver.log'