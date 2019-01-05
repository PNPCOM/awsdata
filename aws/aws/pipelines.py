# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from aws.items import AwsItem

class AwsPipeline(object):
    DB_IP = "localhost"
    # DB_IP = "192.168.1.17"
    DB_user = "root"
    DB_password = "root"
    DB_name = "aws"

    def __init__(self):
        try:
            db = pymysql.connect(self.DB_IP, self.DB_user, self.DB_password, charset='utf8')
            cursor = db.cursor()
            cursor.execute('CREATE DATABASE ' + self.DB_name)
        except Exception as e:
            print(e)
        try:
            connection = pymysql.connect(self.DB_IP, self.DB_user, self.DB_password, self.DB_name, charset='utf8')
            cursor = connection.cursor()
            strquery2 = "CREATE TABLE aws_data""""(Id INT NOT NULL AUTO_INCREMENT,region longtext DEFAULT NULL,name longtext DEFAULT NULL,vcpu longtext DEFAULT NULL,ecu longtext DEFAULT NULL,memory_gib longtext DEFAULT NULL,internal_storage_gb longtext DEFAULT NULL,price_per_hour longtext DEFAULT NULL,PRIMARY KEY (`Id`))"""
            cursor.execute(strquery2)
        except Exception as e:
            print(e)

    def process_item(self, item, spider):

        if isinstance(item, AwsItem):

            try:
                self.connection = pymysql.connect(self.DB_IP, self.DB_user, self.DB_password, self.DB_name,
                                                  charset='utf8')
                self.cursor = self.connection.cursor()
                self.cursor.execute(
                    "INSERT INTO aws_data(region,name,vcpu,ecu,memory_gib,internal_storage_gb,price_per_hour) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                    (item['region'], item['name'], item['vcpu'], item['ecu'],
                     item['memory_gib'], item['internal_storage_gb'], item['price_per_hour']))
                self.connection.commit()
                print 'Data inserted'
            except Exception as e:
                print e
        return item

