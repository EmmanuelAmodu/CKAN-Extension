import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from flask import Blueprint, render_template


def sample_response():
    u'''A simple view function'''
    return u'''
    <!DOCTYPE html>
        <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <title>Example Domain</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style type="text/css">
                body {
                    background-color: #f0f0f2;
                    margin: 0;
                    padding: 0;
                    font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

                }
                div {
                    width: 600px;
                    margin: 5em auto;
                    padding: 2em;
                    background-color: #fdfdff;
                    border-radius: 0.5em;
                    box-shadow: 2px 3px 7px 2px rgba(0, 0, 0, 0.02);
                }
                a:link,
                a:visited {
                    color: #38488f;
                    text-decoration: none;
                }
                @media (max-width: 700px) {
                    div {
                        margin: 0 auto;
                        width: auto;
                    }
                }
            </style>
        </head>
        <body>
            <div>
                <h1>Example CKAN Extension</h1>
                <p>This is an example CKAN extension</p>
            </div>
        </body>
    </html>
    '''

class Example_ExtensionPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'example_extension')

    # IBlueprint

    def get_blueprint(self):
        u'''Return a Flask Blueprint object to be registered by the app.'''
        # Create Blueprint for plugin
        blueprint = Blueprint(self.name, self.__module__)
        blueprint.template_folder = u'templates'
        # Add plugin url rules to Blueprint object
        blueprint.add_url_rule(
            '/sample_request', '/sample_request', sample_response)
        return blueprint
