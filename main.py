from bottle import Bottle, request, template

bottle = Bottle()

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@bottle.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    session = request.get_cookie("session-1")
    return template('cookie = {{session}}', session=session)


# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.'
