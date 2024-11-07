import sqlite3

class QuestionsDB:
    @staticmethod
    def instance():
        return sqlite3.connect('questions.db', check_same_thread=False)

    @staticmethod
    def execute(sql: str):
        return QuestionsDB.instance().execute(sql)

    @staticmethod
    def createTable():
        QuestionsDB.execute(
            'CREATE TABLE PLAY_QUESTIONS '
            '(questionID INT PRIMARY KEY AUTOINCREMENT, topicId INTEGER NOT NULL, question VARCHAR(150), '
            'options VARCHAR(300), answer VARCHAR(100))'
        )
        
    @staticmethod
    def getAllQuestions():
        return QuestionsDB.execute(
            "SELECT * from PLAY_QUESTIONS"
        ).fetchall()

    @staticmethod
    def resetData():
        QuestionsDB.execute("DROP TABLE IF EXISTS PLAY_QUESTIONS")
        QuestionsDB.createTable()

