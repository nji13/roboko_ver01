#キーバリュー型NoSQL
# pythonの標準データベースライブラリ、簡易的な物を素早く書き出したり取り出したりするときに使う

import dbm

with dbm.open('cache', 'c') as db:
    # db['key1'] = 'value1'
    # db['key2'] = 'value2'
    db['key3'] = 1

with dbm.open('cache', 'r') as db:
    print(db.get('key1'))
