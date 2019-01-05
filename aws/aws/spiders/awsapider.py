# -*- coding: utf-8 -*-
import scrapy
import json
from aws.items import AwsItem
class AwsapiderSpider(scrapy.Spider):
    name = 'awsapider'
    allowed_domains = ['amazon.com']
    def start_requests(self):
        region=['us-east-1','us-east-2','us-west-1','us-west-2','ap-south-1','ap-northeast-2','ap-southeast-1','ap-southeast-2',
                'ap-northeast-1','ca-central-1','eu-central-1','eu-west-1','eu-west-2','eu-west-3','eu-north-1','sa-east-1',
                'us-gov-east-1','us-gov-west-1']
        for reg in region:
            yield scrapy.FormRequest('https://d2xn1uj035lhvj.cloudfront.net/pricing/1.0/ec2/region/'+reg+'/ondemand/linux/index.json?timestamp=1546174419535',callback=self.parse,meta={'region':reg})

    def parse(self, response):
        item=AwsItem()
        jdata=json.loads(response.body)
        prices=jdata['prices']
        item['region']=response.meta['region']

        for data in prices:
            item['price_per_hour']=data['price']['USD']
            item['name']=data['attributes']['aws:ec2:instanceType']
            item['vcpu']=data['attributes']['aws:ec2:vcpu']
            item['ecu']=data['attributes']['aws:ec2:ecu']
            item['memory_gib']=data['attributes']['aws:ec2:memory']
            item['internal_storage_gb']=data['attributes']['aws:ec2:storage']
            yield item





