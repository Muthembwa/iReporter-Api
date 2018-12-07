from app import create_app, test
import os

config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app = create_app(config_name)
test = test()

if __name__ =='__main__':
    app.run 