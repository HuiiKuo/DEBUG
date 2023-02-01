from flask import Response
import json
from coder import MyEncoder


def group(data: dict, tag: list, identity: str):
    
    """
    data 是原始資料
    tag 是要被處理成陣列的屬性
    identity是識別data是否為同一組ex id
    """
    tags = []
    ret = []
    for i in range(len(tag)):
        tags.append(set())
    check_id = -1
    temp={}
    for i in data:        
        if i[identity] != check_id:                        
            if check_id != -1:                
                for j in range(len(tag)):
                    temp[tag[j]] = tags[j]
                ret.append(temp)
            check_id = i[identity]
            temp = i
            tags.clear()
            for j in range(len(tag)):
                tags.append(set())
            else:                
                temp = i
        for j in range(len(tag)):              
            tags[j].add(i[tag[j]])
    for j in range(len(tag)):
        temp[tag[j]] = tags[j]
    ret.append(temp)
    return ret
