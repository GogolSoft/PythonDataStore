# Create KV database
from kv_store.kv_store import KVStore

kv_db = KVStore('users_db', 'examples/kv_db/users_db/users.json')
print(kv_db.data)
kv_db.set('1', 'Tom G')
kv_db.set('2', 'John')
kv_db.set('3', 'Alex')
kv_db.set('4', 'Jane')
kv_db.save()


kv_db_memory = KVStore('users_db_memory')
print(kv_db_memory.data)