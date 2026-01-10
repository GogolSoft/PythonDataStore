# Create KV database
from kv_store.kv_store import KVStore
from table_store.table_store import TableStore

kv_db = KVStore('users_db', 'examples/kv_db/users_db/users.json')
print(kv_db.data)
kv_db.set('1', 'Tom G')
kv_db.set('2', 'John')
kv_db.set('3', 'Alex')
kv_db.set('4', 'Jane')
kv_db.save()

kv_db_memory = KVStore('users_db_memory')
kv_db_memory.set('1', 'Voytek')
kv_db_memory.set('2', 'John')
kv_db_memory.set('3', 'Alex')
kv_db_memory.set('4', 'Jane')
kv_db_memory.save()

print(kv_db_memory.keys())
print(kv_db_memory.get('3'))
print(kv_db_memory.delete('4'))
print(kv_db_memory.get('4'))
print(kv_db_memory.data)

table_db = TableStore('users_table_db', 'examples/kv_db/users_db/users_table.json')
table_db.set('1', {'name': 'Tom G', 'age': 32})
table_db.set('2', {'name': 'John H', 'age': 33})
print(table_db.data)

result_list = table_db.get_all_by_attribute('name', 'Tom G')
print(result_list)
table_db.delete('1')
result_list = table_db.get_all_by_attribute('name', 'Tom G')
print(result_list)
table_db.save()
