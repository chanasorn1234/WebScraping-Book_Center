import json
class Tranformtojson:
    def __init__(self,count,author,content,text):
        self.get_txt_to_json = {
                                 "name":author,
                                "content":content,
                                 "text":text
                                }
        self.json_obj = None
        self.tname = author
        self.filename = author
        self.index = count
    def tranform(self):
        self.filename += str(self.index)+'.json'
        with open(self.tname+"\\"+self.filename,"w",encoding='utf-8') as self.json_obj  :
            self.json_obj.write(json.dumps(self.get_txt_to_json,indent=4,ensure_ascii=False))


# data = [1,"ควย","กบ","555"]
# j = Tranformtojson(data[0],data[1],data[2],data[3])
# j.tranform()



'''Test'''
# with open("test.json","r",encoding='utf-8') as file:
#     data2 = json.load(file)
#     print(data2)


