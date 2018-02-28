'''
CombiGenie (c) University of Manchester 2018

CombiGenie is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
import sys
import uuid

from flask import Flask, make_response

_EXCEL = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

# Configuration:
DEBUG = False
SECRET_KEY = str(uuid.uuid4())

# Create application:
APP = Flask(__name__)
APP.config.from_object(__name__)


@APP.route('/')
def root():
    '''Root.'''
    response = make_response(APP.send_static_file('CombiGenie.xlsx'))
    response.headers['Content-Type'] = _EXCEL
    response.headers['Content-Disposition'] = \
        'attachment; filename="CombiGenie.xlsx"'
    return response


def main(argv):
    '''main method.'''
    if argv:
        APP.run(host='0.0.0.0', threaded=True, port=int(argv[0]),
                use_reloader=False)
    else:
        APP.run(host='0.0.0.0', threaded=True, use_reloader=False)


if __name__ == '__main__':
    main(sys.argv[1:])
