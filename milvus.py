from dotenv import load_dotenv, dotenv_values
load_dotenv()
config = dotenv_values(".env")

from pymilvus import connections, CollectionSchema, FieldSchema, DataType, Collection, db

connections.connect(
    host=config["DB_HOST"],
    port=config["DB_PORT"]
)

dbs = db.list_database()
print(dbs)

book_id = FieldSchema(
  name="book_id", 
  dtype=DataType.INT64, 
  is_primary=True, 
)
word_count = FieldSchema(
  name="word_count", 
  dtype=DataType.INT64,  
)
book_intro = FieldSchema(
  name="book_intro", 
  dtype=DataType.FLOAT_VECTOR, 
  dim=2
)
schema = CollectionSchema(
  fields=[book_id, word_count, book_intro], 
  description="Test book search"
)
collection_name = "book"
collection = Collection(
    name=collection_name, 
    schema=schema, 
    using='default', 
    shards_num=2,
    consistency_level="Strong"
)
