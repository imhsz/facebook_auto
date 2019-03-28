#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Charles on 19-3-16
# Function: 

import threading
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import get_db_args


def get_engine():
    args = get_db_args()
    connect_str = "{}+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(
        args['db_type'], args['user'], args['password'],
        args['host'], args['port'], args['db_name']
    )
    eng = create_engine(connect_str, encoding='utf-8')
    return eng


engine = get_engine()
Base = declarative_base()
Session = sessionmaker(bind=engine)
db_session = Session()
metadata = MetaData(get_engine())
db_lock = threading.RLock()

__all__ = ['engine', 'Base', 'db_session', 'metadata', 'db_lock']
