import os
import sys
from gunicorn.app.wsgiapp import WSGIApplication

sys.path.insert(0, os.path.dirname(__file__))

def main():
    sys.argv[0] = 'gunicorn'
    sys.argv.append('app:app')
    WSGIApplication().run()

if __name__ == '__main__':
    main()
