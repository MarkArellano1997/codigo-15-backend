class Config:
    SECRET_KEY = "customsecretkey"
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost:3306/codigo_15_flask"
    SQLALCHEMY_TRACKS_MODIFICATIOONS = False
    JWT_SECRET_KEY="super_secret"