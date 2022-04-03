from flask_app import app
from flask_app.models.champion import *


@app.route('/')
async def dashboard(): 
    return await get_all_champions()



if __name__ == '__main__':
    app.run(debug=True)
