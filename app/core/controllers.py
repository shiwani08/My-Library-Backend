from flask import request, jsonify
from bson import ObjectId

class BaseController:
    
    model_class = None  # To be set in child classes
    resource_name = None  # e.g., "book", "user"
    
    @classmethod
    def add(cls):
        
        try:
            data = request.get_json()
            
            # Validate required fields (override in child class if needed)
            required_fields = cls.get_required_fields()
            missing_fields = [field for field in required_fields if not data.get(field)]
            
            if missing_fields:
                return jsonify({
                    "error": f"{', '.join(missing_fields)} are required"
                }), 400
            
            # Call model's add method
            resource_id = cls.model_class.add(**data)
            
            return jsonify({
                "message": f"{cls.resource_name.capitalize()} added successfully!",
                f"{cls.resource_name}_id": resource_id,
                **data
            }), 201
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @classmethod
    def get_all(cls):
        
        try:
            # Get pagination parameters
            # page = request.args.get("page", 1, type=int)
            # limit = request.args.get("limit", 10, type=int)
            
            items = cls.model_class.get_all()
            return jsonify(items), 200
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @classmethod
    def get_by_query(cls):
        
        try:
            # Get the search field (override in child class for different fields)
            search_field = cls.get_search_field()
            search_value = request.args.get(search_field)
            
            if not search_value:
                return jsonify({
                    "error": f"{search_field.capitalize()} parameter is required"
                }), 400
            
            item = cls.model_class.get_by_field(search_field, search_value)
            
            if not item:
                return jsonify({
                    "error": f"{cls.resource_name.capitalize()} not found"
                }), 404
            
            return jsonify(item), 200
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @classmethod
    def update(cls, resource_id):
        
        try:
            data = request.get_json()
            
            # Remove None values
            update_data = {k: v for k, v in data.items() if v is not None}
            
            if not update_data:
                return jsonify({"error": "No data provided for update"}), 400
            
            updated_item = cls.model_class.update(resource_id, **update_data)
            
            if not updated_item:
                return jsonify({
                    "error": f"{cls.resource_name.capitalize()} not found"
                }), 404
            
            return jsonify({
                "message": f"{cls.resource_name.capitalize()} updated successfully!",
                cls.resource_name: updated_item
            }), 200
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @classmethod
    def delete(cls, resource_id):
        
        try:
            deleted = cls.model_class.delete(resource_id)
            
            if not deleted:
                return jsonify({
                    "error": f"{cls.resource_name.capitalize()} not found"
                }), 404
            
            return jsonify({
                "message": f"{cls.resource_name.capitalize()} deleted successfully!"
            }), 200
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @classmethod
    def get_required_fields(cls):  
        return []
    
    @classmethod
    def get_search_field(cls):
        return "title"