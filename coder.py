import datetime
import decimal
import json

class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        
        if isinstance(obj, bytearray):  # 返回内容如果包含bytearray类型的数据
            return str(obj, encoding='utf-8')
        elif isinstance(obj, datetime.datetime):  # 返回内容如果包含datetime类型的数据
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):  # 返回内容如果包含datetime类型的数据
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, decimal.Decimal):  # 返回内容如果包含Decimal类型的数据
            return float(obj)
        elif isinstance(obj,bytes):
            return obj.decode(encoding='utf-8')     
        elif isinstance(obj, set):
            return list(obj)   
        return json.JSONEncoder.default(self, obj)
