
from flask import Flask
import sys
from storessales.logger import logging
from storessales.exeception import StoressalesExeception


app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:

        storessales=StoressalesExeception(e,sys)


        logging.info(storessales.error_message)

        logging.info("first version storessales loggging message")
    return "CI CD pipeline has been established for store sales predection"

if __name__ == "__main__":
    app.run(debug=True)
