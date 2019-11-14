import requests
import json

#response = 	requests.get("https://transit.api.here.com/v3/coverage/search.json?app_id=TF7UTu4XaqMxJVrc97CV&app_code=heZ-H7kuc2HFE8QPD_7tLQ&name=Coventry")
places ={
    "place":{
        "name":"Johnsons Excelbus",
    }
}
json_str=json.dumps(places)
resp=json.loads(json_str)
print(resp)
print(resp['place']['name'])
#jdata = json.dumps(places)
#place = {"places":{"stn""id":"100329977","name":"Coventry Rd","distance":4170520,"duration":"P48DT6H28M40S","x":-1.857469,"y":52.470047,"has_board":1,"country":"United Kingdom","ccode":"GBR","state":"England","postal":"B10 9","district":"Small Heath","street":"Wright Street","city":"Birmingham"

#("https://transit.api.here.com/v3/stations/by_name.json?method=fuzzy&center=90,90&name=Coventry&app_id=TF7UTu4XaqMxJVrc97CV&app_code=heZ-H7kuc2HFE8QPD_7tLQ&max=25")
#print(places['place'])
#data={"test1" : "1", "test2" : "2", "test3" : "3"}
#json_str = json.dumps(data)
#resp = json.loads(json_str)
#print (resp)
#print (resp['test1'])