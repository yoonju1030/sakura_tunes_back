from app.controller.music import music

def routes_list(app):
    app.register_blueprint(music)
    return app