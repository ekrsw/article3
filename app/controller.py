import datetime
from app.datamaster import access_db
from app.dynamics import Dynamics
import logging

import settings

formatter = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(filename=settings.LOG_FILE, level=logging.INFO, format=formatter)
logger = logging.getLogger(__name__)

def update_dynamics():
    df = access_db.read_access()
    dynamics = Dynamics()
    for i, row in df.iterrows():
        url = row['URL']
        title = row['タイトル']
        info_category = row['情報カテゴリ']
        key_words = row['キーワード']
        important = row['重要']
        open_public_start = row['公開期限_開始']
        open_public_end = row['公開期限_終了']
        question = row['質問']
        answer = row['回答']
        add_comments = row['追加コメント']

        dynamics.update_dynamics(url, title=title, info_category=info_category, key_words=key_words, important=important, open_public_start=open_public_start, open_public_end=open_public_end, question=question, answer=answer, add_comments=add_comments)
        access_db.update_access(row['提出ID'])
        
        logger.info(f'ID: {row["提出ID"]} : {row["記事番号"]}')
        print(f'提出ID: {row["提出ID"]} 記事番号: {row["記事番号"]} 反映完了')
        