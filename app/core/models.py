from bson import ObjectId
from datetime import datetime
from app.core.config import mongo

class BaseModel:
    
    collection_name = None  # To be set in child classes
    
    @classmethod
    def get_collection(cls):
        
        if not cls.collection_name:
            raise NotImplementedError("collection_name must be set in child class")
        return mongo.db[cls.collection_name]
    
    @classmethod
    def serialize_id(cls, document):
        
        if document and "_id" in document:
            document["_id"] = str(document["_id"])
        return document
    
    @classmethod
    def serialize_list(cls, documents):
        return [cls.serialize_id(doc) for doc in documents]
    
    @classmethod
    def add(cls, **data):
        
        collection = cls.get_collection()
        
        # Add timestamps if not present
        if "created_at" not in data:
            data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        
        # Call before_insert hook if exists
        if hasattr(cls, 'before_insert'):
            data = cls.before_insert(data)
        
        result = collection.insert_one(data)
        return str(result.inserted_id)
    
    @classmethod
    def get_all(cls, query={}, skip=0, limit=100, sort=None):
        
        collection = cls.get_collection()
        cursor = collection.find(query).skip(skip).limit(limit)
        
        if sort:
            cursor = cursor.sort(sort)
        
        documents = list(cursor)
        return cls.serialize_list(documents)
    
    @classmethod
    def get_by_id(cls, doc_id):
        
        try:
            collection = cls.get_collection()
            document = collection.find_one({"_id": ObjectId(doc_id)})
            return cls.serialize_id(document) if document else None
        except Exception:
            return None
    
    @classmethod
    def get_by_field(cls, field_name, field_value):
        
        collection = cls.get_collection()
        document = collection.find_one({field_name: field_value})
        return cls.serialize_id(document) if document else None
    
    @classmethod
    def get_many_by_field(cls, field_name, field_value):
        
        collection = cls.get_collection()
        documents = list(collection.find({field_name: field_value}))
        return cls.serialize_list(documents)
    
    @classmethod
    def update(cls, doc_id, **update_data):
        
        try:
            collection = cls.get_collection()
            
            # Check if document exists
            document = collection.find_one({"_id": ObjectId(doc_id)})
            if not document:
                return None
            
            # Remove None values
            update_data = {k: v for k, v in update_data.items() if v is not None}
            
            if not update_data:
                return cls.serialize_id(document)
            
            # Add updated timestamp
            update_data["updated_at"] = datetime.utcnow()
            
            # Call before_update hook if exists
            if hasattr(cls, 'before_update'):
                update_data = cls.before_update(document, update_data)
            
            # Update document
            collection.update_one(
                {"_id": ObjectId(doc_id)},
                {"$set": update_data}
            )
            
            # Get updated document
            updated_document = collection.find_one({"_id": ObjectId(doc_id)})
            return cls.serialize_id(updated_document)
            
        except Exception:
            return None
    
    @classmethod
    def delete(cls, doc_id):
        
        try:
            collection = cls.get_collection()
            
            # Call before_delete hook if exists
            if hasattr(cls, 'before_delete'):
                document = collection.find_one({"_id": ObjectId(doc_id)})
                if document and not cls.before_delete(document):
                    return False
            
            result = collection.delete_one({"_id": ObjectId(doc_id)})
            return result.deleted_count > 0
        except Exception:
            return False
    
    @classmethod
    def count(cls, query={}):
        
        collection = cls.get_collection()
        return collection.count_documents(query)
    
    @classmethod
    def exists(cls, query):
        
        collection = cls.get_collection()
        return collection.find_one(query) is not None