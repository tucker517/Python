'''
Created on Feb 27, 2020

@author: Tucker Celestine


A script to generate random data for use UID, 
'''


from flask import Flask, Response, stream_with_context
import time
import uuid
import random



APP = Flask(__name__)

@APP.route("/very_large_request/<intLrowdount>", methods=["GET"])
def get_large_request(rowcount):
    """returns N rows of data"""
    def f():
        """The generator of mock data"""
        for _i in range(rowcount):
            time.sleep(.1)
            txid = uuid.uuid4()
            uid = uuid.uuid4()
            amount = round(random.uniform-(1000, 1000), 2)
            yield f"('{txid}', '{uid}', '{amount}')\n"
        return Response(stream_with_context(f()))

if __name__ == "__main__":
        APP.run(debug=True)
    
    
    
    
