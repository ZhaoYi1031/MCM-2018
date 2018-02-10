#!/usr/bin/python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from TwitterAPI import TwitterAPI
import json

result=open("realtimeSample.csv",'a')
geo_result=open("geo_result.csv",'a')
errorlog=open("error.log",'a')
consumer_key="gBBbFtbfCATXQcHpEwr6d9azm"
consumer_secret="tF9A03v5EcErAWeohNNZI6BMVhmv5Zc4OSM4gs8G2E2HodJyBC"
access_token_key="961809210349535232-zb6BjSjwBcB6y9uPOsxv37WrjOl7jE3"
access_token_secret="lf1Yxp2OHVQVZYfNEDg3rT4z7jBZWuwIOUt2xYzcEEuEk"
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

r = api.request('statuses/sample', {})#sample randomly(offical)

counter=0
for item in r:
    #error handling
    if 'limit' in item:
        errorlog.write(str('%d tweets missed' % item['limit']['track']))
    elif 'disconnect' in item:
        errorlog.write('disconnecting because %s' % item['disconnect']['reason'])
        os.system('nohup python twitter_2.py &')#start program No2
        #os.system('nohup python twitter_1.py &')#start program No1
        exit(0)

    if 'delete' not in str(item):
        try:
            if counter%5==0:#random/5
                out=(item.get('id_str','NA')+','+
                    item.get('created_at','NA')+','+
                    item.get('user','NA').get('id_str','NA')+','+item.get('user','NA').get('name','NA').replace(',','~')+','+item.get('user','NA').get('lang','NA')+','+
                    str(item.get('lang','NA')))#nullable
                result.write(out+'\n')

            if item.get('coordinates')!=None:#geo
                out=out+','+str(item['coordinates'].get('coordinates',[0,0])[0])+','+str(item['coordinates'].get('coordinates',[0,0])[1])+'\n'
                geo_result.write(out+'\n')

            counter=counter+1
        except Exception:
            errorlog.write(str(item))
    if counter%1000==0:
        print str(counter/1000)+'k'

result.close()
geo_result.close()
errorlog.write('----------\n')
errorlog.close()
print 'fatal error!'
