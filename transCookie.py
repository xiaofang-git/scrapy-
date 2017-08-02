# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = '_zap=c7cbc2db-29e7-4744-bbc7-4ab038aab799; aliyungf_tc=AQAAACrS0H1PIwAA9KPufPMymPbu/0Lo; q_c1=1e32ddf99744439f8c2ce91923f5fa69|1501657218000|1501657218000; _xsrf=410868dbc02f651435cd745481168fc3; r_cap_id="NzcwYThiN2QwNDkzNDUxMWI4MDkzNzBlY2I0OTZkMzY=|1501657218|2440413f36d57b654135528c3300f491a7ae6e4c"; cap_id="ZWEyYzI2Y2NhNTNmNDA0YTg4MWQ4M2Q0NGFlZTZlMTM=|1501657218|57c57caeb23a13c394076e8f9684088b2fcca0a4"; d_c0="ABDC7VqDKAyPTsjIkE91Th56U3M7B2o5EEk=|1501657218"; __utma=51854390.1267769589.1501657219.1501657219.1501657219.1; __utmb=51854390.0.10.1501657219; __utmc=51854390; __utmz=51854390.1501657219.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20170802=1; l_n_c=1; z_c0=Mi4wQUVBQ1V1LWdad3NBRU1MdFdvTW9EQmNBQUFCaEFsVk5qUVdwV1FDcDVSWXJDeWJOU0R1ZFpjUGZMRDZ0bEIxSHh3|1501657229|7b8d35fd4e5788d4826412f40ae6d06d21a34b10; _xsrf=410868dbc02f651435cd745481168fc3'
    trans = transCookie(cookie)
    print (trans.stringToDict())