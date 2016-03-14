import sys
import os
import traceback
import hashlib


from flask import Flask, request, redirect, jsonify, abort

app = Flask(__name__)

_HERE = os.path.dirname(os.path.abspath(__file__))

def save_and_getmd5(stream, dst, buffer_size=16384):
    md5 = hashlib.md5()
    with open(dst, "wb") as dst:
	while 1:
	    buffer = stream.read(buffer_size)
	    if not buf:
		break
	    dst.write(buf)
	    md5.update(buf)
    return md5.hexdigest()


@app.route('/upload', methods=['POST'])
def nginxupload():
    return jsonify({'done':True, 'md5': request.form['fileobj.md5']})


if __name__ == '__main__':    
    app.run(host='0.0.0.0', debug=True)
