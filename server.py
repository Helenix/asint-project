from flask import Flask
import time
from istdb import ISTdb

app = Flask(__name__)

# Testes para popular a db de buildings do ist
startTime = time.time()
db = ISTdb("ISTdb")
db.__str__()
print("%s" % (time.time() - startTime))

# Routes

if __name__ == "__main__":
    app.run(debug = True)
