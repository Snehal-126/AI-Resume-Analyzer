import sqlite3
from datetime import datetime


class ResumeDatabase:

    def __init__(self):

        self.conn = sqlite3.connect(
            "database/resume.db",
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS resume_analysis(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            resume_name TEXT,

            match_score REAL,

            ats_score REAL,

            analysis_date TEXT
        )
        """)

        self.conn.commit()

    def insert_record(
        self,
        resume_name,
        match_score,
        ats_score
    ):

        self.cursor.execute(
            """
            INSERT INTO resume_analysis(
                resume_name,
                match_score,
                ats_score,
                analysis_date
            )
            VALUES(?,?,?,?)
            """,
            (
                resume_name,
                match_score,
                ats_score,
                datetime.now().strftime("%d-%m-%Y %H:%M")
            )
        )

        self.conn.commit()

    def get_records(self):

        self.cursor.execute(
            """
            SELECT
            resume_name,
            match_score,
            ats_score,
            analysis_date

            FROM resume_analysis

            ORDER BY id DESC
            """
        )

        return self.cursor.fetchall()