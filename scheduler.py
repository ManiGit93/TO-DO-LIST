import schedule, time, sqlite3
from scraper import fetch_quote

def auto_task():
    quote = fetch_quote()
    conn = sqlite3.connect("todo.db")
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (quote,))
    conn.commit()
    conn.close()

schedule.every().day.at("09:00").do(auto_task)

while True:
    schedule.run_pending()
    time.sleep(1)
