from flask import Flask,request,render_template
from flask_mysqldb import MySQL
from src.project4.logger import logging
from src.project4.exception import CustomException
import pymysql
import pandas as pd



def read_sql_data():
    logging.info('Reading SQL database started')
    try:
        mydb = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '12345',
            db = 'mydb'
            
        )
        
        logging.info('Connection Established', mydb)
        df = pd.read_sql_query('Select * from users', mydb)
        
        
        return df
    
    except Exception as ex:
        raise CustomException(ex)