from flask import Blueprint

class BaseRoutes:
    
    @staticmethod
    def register_standard_routes(blueprint, controller, config=None):
        
        if config is None:
            # Default configuration
            config = {
                'create': {'path': '/create', 'method': 'POST', 'handler': 'create'},
                'list': {'path': '/list', 'method': 'GET', 'handler': 'list'},
                'get': {'path': '/get', 'method': 'GET', 'handler': 'get'},
                'update': {'path': '/update/<id>', 'method': 'PUT', 'handler': 'update'},
                'delete': {'path': '/delete/<id>', 'method': 'DELETE', 'handler': 'delete'}
            }
        
        for route_config in config.values():
            path = route_config['path']
            method = route_config['method']
            handler_name = route_config['handler']
            
            handler = getattr(controller, handler_name, None)
            if handler:
                blueprint.route(path, methods=[method])(handler)