'''
CombiGenie (c) University of Manchester 2018

CombiGenie is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
import os
import sys
import uuid

from flask import Flask


# Configuration:
DEBUG = True
SECRET_KEY = str(uuid.uuid4())

# Create application:
_STATIC_FOLDER = os.path.dirname(os.path.realpath(__file__))
APP = Flask(__name__, static_folder=_STATIC_FOLDER)
APP.config.from_object(__name__)


@APP.route('/')
def home():
    '''Renders homepage.'''
    return APP.send_static_file('CombiGenie.xlsx')


def main(argv):
    '''main method.'''
    if argv:
        APP.run(host='0.0.0.0', threaded=True, port=int(argv[0]),
                use_reloader=False)
    else:
        APP.run(host='0.0.0.0', threaded=True, use_reloader=False)


if __name__ == '__main__':
    main(sys.argv[1:])
