import harperdb

db = harperdb.HarperDB(
    url = "*************************",
    username = '"*************************",',
    password = '"*************************",'
)

SCHEMA = 'watch_later_repo'
TABLE = 'todo_s'
TODAY_TABLE = 'todays_video'

def insert_video(video_data):
    return db.insert(SCHEMA, TABLE, [video_data])

def delete_video(video_id):
    return db.delete(SCHEMA, TABLE, [video_id])

def get_all_videos():
    try:
        # return db.sql(f"select video_id,channel,title,duration from {SCHEMA}.{TABLE}")
        return db.sql(f"select * from {SCHEMA}.{TABLE}")
    except harperdb.exceptions.HarperDBError:
        return []

def get_video_today():
    return db.sql(f"select * from {SCHEMA}.{TODAY_TABLE} where id = 0")

def update_video_today(video_data, insert=False):
    video_data['id'] = 0
    if insert:
        return db.insert(SCHEMA, TODAY_TABLE, [video_data])
    return db.update(SCHEMA, TODAY_TABLE, [video_data])
