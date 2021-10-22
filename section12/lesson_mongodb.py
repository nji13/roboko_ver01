# MongoDBはドキュメント型NoSQLのデータベース

import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'data': datetime.datetime.utcnow()
}

stack2 = {
    'name': 'customer2',
    'pip': ['python', 'java'],
    'info': {'os': 'windows'},
    'data': datetime.datetime.utcnow()
}

db_stacks = db.stacks  # db_stackに find探す や delete消す などの操作ができる。
# stack_id = db_stacks.insert_one(stack1).inserted_id
# print(stack_id, type(stack_id))
# print('##########')
# from bson.objectid import ObjectId
# str_stack_id = '5f720d87f0846d2e1759209a'
# print(db_stacks.find_one({'_id': ObjectId(str_stack_id)}))
# stack_id = db_stacks.insert_one(stack2).inserted_id
# print(stack_id, type(stack_id))
# print('##########')
# for stack in db_stacks.find():
#     print(stack)
# now = datetime.datetime.utcnow()           今の時間より前に作れたデータを表示
# for stack in db_stacks.find({'data': {'$gt': now}}):
#     print(stack)
# db_stacks.find_one_and_update(          名前を書き換える
#     {'name': 'customer1'}, {'$set': {'name': 'YYY'}}
# )
# print(db_stacks.find_one({'name': 'YYY'}))
# db_stacks.delete_one({'name': 'YYY'})     削除する
# print(db_stacks.find_one({'name': 'YYY'}))