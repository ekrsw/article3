import logging
import time

# Webスクレイピング関係ライブラリ
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# access_dbをimport
from app.datamaster import access_db

# settingファイルの読込み
import settings

formatter = '%(filename)s - %(levelname)s - %(asctime)s - %(message)s'
logging.basicConfig(filename=settings.LOG_FILE, level=logging.INFO, format=formatter)
logger = logging.getLogger(__name__)

class Dynamics(object):
    """Base scraping model.
    
    method:
        
    """
    def __init__(self, headless_mode=settings.HEADLESS_MODE):
        self.headless_mode = headless_mode
    
    def constructa(self):
        if getattr(self, 'driver', None):
            self.driver.close()
            self.driver = None

        options = Options()

        # ブラウザを表示させない。
        if self.headless_mode:
            options.add_argument('--headless')
        
        # コマンドプロンプトのログを表示させない。
        options.add_argument('--disable-logging')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(options=options)

        self.driver.implicitly_wait(5)
    
    def close_driver(self):
        if getattr(self, 'driver', None):
            self.driver.close()
            self.driver = None

    def update_dynamics(self, id, kba, url, title=None, info_category=None, key_words=None, important=None, open_public_start=None, open_public_end=None, question=None, answer=None, add_comments=None):
        ctn = 0
        while True:
            try:
                self.constructa()
                self.__update(url, title, info_category, key_words, important, open_public_start, open_public_end, question, answer, add_comments)
                self.close_driver()
                access_db.update_access(id)
                logger.info(f'ID: {id} : {kba} : {url} : Success')
                break

            except Exception as e:
                ctn += 1
                if ctn > settings.RETRY_COUNT:
                    logger.info(f'ID: {id} : {kba} : {url} : {e}')
                    print('error')
                    break
                print(e)
                continue

    def __update(self, url, title=None, info_category=None, key_words=None, important=None, open_public_start=None, open_public_end=None, question=None, answer=None, add_comments=None):

        self.driver.get(url)
        time.sleep(3)

        # 公開の取り下げ
        self.driver.find_element(By.ID, 'kbarticle|NoRelationship|Form|Mscrm.Form.kbarticle.Unpublish-Medium').click()

        # iframe切り替え
        self.driver.switch_to.frame(self.driver.find_element(By.ID, 'contentIFrame'))
        
        # タイトル title
        if title is not None:
            title_el = self.driver.find_element(By.ID, 'title')
            title_el.clear()
            title_el.send_keys(title)
        
        # 情報カテゴリ info_category
        if info_category is not None:
            info_category_el = self.driver.find_element(By.ID, 'subjectid')
            info_category_el.click()
        
            # iframe切り替え
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element(By.ID, 'InlineDialog_Iframe'))
            
            if info_category == '_会計・財務':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[1]').click()
            elif info_category == '_起動トラブル':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[2]').click()
            elif info_category == '_給与・年末調整':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[3]').click()
            elif info_category == '_減価・ﾘｰｽ/資産管理':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[4]').click()
            elif info_category == '_公益・医療会計':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[5]').click()
            elif info_category == '_工事・原価':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[6]').click()
            elif info_category == '_債権・債務':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[7]').click()
            elif info_category == '_事務所管理':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[8]').click()
            elif info_category == '_人事':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[9]').click()
            elif info_category == '_税務関連':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[10]').click()
            elif info_category == '_電子申告':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[11]').click()
            elif info_category == '_販売':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[12]').click()
            elif info_category == 'Edge Tracker':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[13]').click()
            elif info_category == 'MJS-Connect関連':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[14]').click()
            elif info_category == 'インストール・MOU':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[15]').click()
            elif info_category == 'かんたん！シリーズ':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[16]').click()
            elif info_category == 'その他（システム以外）':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[17]').click()
            elif info_category == 'その他MJSシステム':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[18]').click()
            elif info_category == 'その他システム（共通）':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[19]').click()
            elif info_category == 'ハード関連(HHD)':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[20]').click()
            elif info_category == 'ハード関連（ソフトフェア）':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[21]').click()
            elif info_category == 'マイナンバー':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[22]').click()
            elif info_category == 'ワークフロー':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[23]').click()
            elif info_category == '一時受付用':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[24]').click()
            elif info_category == '運用ルール':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[25]').click()
            elif info_category == '顧客情報':
                self.driver.find_element(By.XPATH, '//*[@id="TreeContainer"]/ul/li[26]').click()

            self.driver.find_element(By.ID, 'butBegin').click()

            # iframe切り替え
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element(By.ID, 'contentIFrame'))

        # キーワード key_words
        if key_words is not None:
            key_words_el = self.driver.find_element(By.ID, 'keywords')
            key_words_el.clear()
            key_words_el.send_keys(key_words)

        # 重要 important
        if important is not None:
            self.driver.find_element(By.ID, 'rad_enjoy_important2').click()
        else:
            self.driver.find_element(By.ID, 'rad_enjoy_important1').click()

        # 公開期限（開始） open_public_start
        if open_public_start is not None:
            open_start_el = self.driver.find_element(By.XPATH, '//*[@id="enjoy_openperiod_start"]/tbody/tr/td[1]/input')
            open_start_el.clear()
            open_start_el.send_keys(open_public_start)

        # 公開期限（終了） open_public_end
        if open_public_end is not None:
            open_end_el = self.driver.find_element(By.XPATH, '//*[@id="enjoy_openperiod_end"]/tbody/tr/td[1]/input')
            open_end_el.clear()
            open_end_el.send_keys(open_public_end)

        # 質問 question
        if question is not None:
            question_el = self.driver.find_element(By.ID, 'SectionEdit0')
            question_el.clear()
            question_el.send_keys(question)

        # 回答 answer
        if answer is not None:
            answer_el = self.driver.find_element(By.ID, 'SectionEdit1')
            answer_el.clear()
            answer_el.send_keys(answer)

        # 追加コメント add_comments
        if add_comments is not None:
            add_comments_el = self.driver.find_element(By.ID, 'SectionEdit2')
            add_comments_el.clear()
            add_comments_el.send_keys(add_comments)

        # iframe切り替え
        self.driver.switch_to.default_content()

        # 承認
        self.driver.find_element(By.ID, 'kbarticle|NoRelationship|Form|Mscrm.Form.kbarticle.Publish-Medium').click()
