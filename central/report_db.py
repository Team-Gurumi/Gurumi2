import sqlite3

def init_db(db_path='report_log.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            reporter_ip TEXT,
            hash TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_report_metadata(filename, reporter_ip, hash_value, db_path='report_log.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reports (filename, reporter_ip, hash)
        VALUES (?, ?, ?)
    ''', (filename, reporter_ip, hash_value))
    conn.commit()
    conn.close()
