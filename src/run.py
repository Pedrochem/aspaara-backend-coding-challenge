import uvicorn
import argparse
import db

def arg_parse():
    ap = argparse.ArgumentParser()
    ap.add_argument("--create_db", '-c',default=0, help = "recreates the database")
    ap.add_argument("--load_data",'-l',default=0, help = "load_data from json file into database")
    a = ap.parse_args()
    return int(a.create_db)==1, int(a.load_data)==1
    


if __name__=='__main__':
    # parsing system arguments
    create_db, load_data = arg_parse()

    # creating the database and loading the data
    if create_db:
        db.create_db(load_data)
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
