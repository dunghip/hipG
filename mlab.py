import mongoengine



#mongodb://<dbuser>:<dbpassword>@ds135552.mlab.com:35552/hipgum

#v2:

#mongodb://<dbuser>:<dbpassword>@ds135519.mlab.com:35519/a-task-v2
host = "ds135552.mlab.com"
port = 35552
db_name = "hipgum"
user_name = "dunghip"
password = "hipgum"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())