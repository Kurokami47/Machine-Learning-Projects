import sys
from flask import Flask

from housing.exception import housingexception
from housing.logger import logging

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():

    try:
        raise Exception('raising custom exception for testing')
    except Exception as e:
        housing = housingexception(e,sys) 
        logging.info(housing.error_message)
        logging.info('we are testing logging module')
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True)
