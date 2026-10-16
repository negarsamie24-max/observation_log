
from observation import Observation


# تکراری‌ها را ذخیره نمی‌کند
def save_observations_to_db(observations, conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            observer TEXT,
            filter_name TEXT,
            exposure REAL
        )
    """)

    saved_count = 0
    duplicate_count = 0

    for obs in observations:
        cursor.execute("""
            SELECT id FROM observations
            WHERE target = ?
              AND observer = ?
              AND filter_name = ?
              AND exposure = ?
        """, (
            obs.target,
            obs.observer,
            obs.filter,
            obs.exposure
        ))

        if cursor.fetchone() is not None:
            duplicate_count += 1
            continue

        cursor.execute("""
            INSERT INTO observations
            (target, observer, filter_name, exposure)
            VALUES (?, ?, ?, ?)
        """, (
            obs.target,
            obs.observer,
            obs.filter,
            obs.exposure
        ))

        saved_count += 1

    conn.commit()

    print(f"{saved_count} new observations saved.")

    if duplicate_count > 0:
        print(f"{duplicate_count} duplicate observations skipped.")


# اطلاعات قبلی را از دیتابیس می‌خواند
def load_observations_from_db(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            observer TEXT,
            filter_name TEXT,
            exposure REAL
        )
    """)

    cursor.execute("""
        SELECT target, observer, filter_name, exposure
        FROM observations
    """)

    rows = cursor.fetchall()
    observations = []

    for row in rows:
        target, observer, filter_name, exposure = row

        obs = Observation(
            target,
            observer,
            filter_name,
            exposure
        )

        observations.append(obs)

    return observations
