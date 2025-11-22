#  add public routes

class BaseRoutes:

    @staticmethod
    def register_standard_routes(blueprint, routes):
        for path, methods, handler in routes:
            blueprint.route(path, methods=methods)(handler)
