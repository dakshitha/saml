# # # # # # from flask import Flask, request, redirect, session, render_template
# # # # # # from flask_cors import CORS
# # # # # # from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
# # # # # # from saml2.config import Config as Saml2Config
# # # # # # from saml2.client import Saml2Client
# # # # # # from urllib.parse import urlparse, parse_qs, quote
# # # # # # import logging
# # # # # # import secrets

# # # # # # app = Flask(__name__)
# # # # # # app.secret_key = secrets.token_hex(16)  # Securely generated secret key
# # # # # # CORS(app)

# # # # # # logging.basicConfig(level=logging.DEBUG)

# # # # # # # SAML Configuration
# # # # # # def saml_client():
# # # # # #     config = Saml2Config()
# # # # # #     config.load({
# # # # # #         'entityid': 'https://zitadel-test.sp/metadata',
# # # # # #         'service': {
# # # # # #             'sp': {
# # # # # #                 'name': 'SAML SP',
# # # # # #                 'endpoints': {
# # # # # #                     'assertion_consumer_service': [
# # # # # #                         ('http://127.0.0.1:5000/acs', BINDING_HTTP_POST),
# # # # # #                     ],
# # # # # #                 },
# # # # # #                 'required_attributes': ['uid'],
# # # # # #                 'optional_attributes': ['mail'],
# # # # # #             },
# # # # # #         },
# # # # # #         'metadata': {
# # # # # #             'local': ['idp_metadata.xml'],
# # # # # #         },
# # # # # #         'key_file': 'sp-key.pem',
# # # # # #         'cert_file': 'sp-cert.pem',
# # # # # #         'xmlsec_binary': '/opt/homebrew/bin/xmlsec1'  # Directly set the path to xmlsec1
# # # # # #     })
# # # # # #     return Saml2Client(config)

# # # # # # @app.route('/')
# # # # # # def index():
# # # # # #     saml_request = session.pop('saml_request', '')
# # # # # #     return render_template('index.html', saml_request=saml_request)

# # # # # # @app.route('/generate_saml_request', methods=['POST'])
# # # # # # def generate_saml_request():
# # # # # #     client = saml_client()
# # # # # #     reqid, info = client.prepare_for_authenticate()
# # # # # #     location_header = dict(info['headers'])['Location']
# # # # # #     parsed_url = urlparse(location_header)
# # # # # #     saml_request = parse_qs(parsed_url.query)['SAMLRequest'][0]
# # # # # #     logging.debug(f"SAML Request: {saml_request}")
# # # # # #     session['saml_request'] = saml_request
# # # # # #     return redirect('/')

# # # # # # @app.route('/sso', methods=['POST'])
# # # # # # def sso():
# # # # # #     saml_request = request.form['saml_request']
# # # # # #     encoded_saml_request = quote(saml_request)  # Ensure the SAML request is URL encoded
# # # # # #     redirect_url = f"https://my-instance-xtzfbc.zitadel.cloud/saml/v2/SSO?SAMLRequest={encoded_saml_request}"
# # # # # #     logging.debug(f"Redirecting to: {redirect_url}")
# # # # # #     return redirect(redirect_url)

# # # # # # @app.route('/acs', methods=['POST'])
# # # # # # def acs():
# # # # # #     logging.debug("Received POST request at /acs")
# # # # # #     logging.debug(f"Request form data: {request.form}")
# # # # # #     client = saml_client()
# # # # # #     saml_response = request.form['SAMLResponse']
# # # # # #     logging.debug(f"SAML Response: {saml_response}")
# # # # # #     try:
# # # # # #         authn_response = client.parse_authn_request_response(saml_response, BINDING_HTTP_POST)
# # # # # #         session['user_info'] = authn_response.get_identity()
# # # # # #         return render_template('response.html', saml_response=saml_response, user_info=session['user_info'])
# # # # # #     except Exception as e:
# # # # # #         logging.error(f"Error processing SAML response: {e}")
# # # # # #         return f"Error processing SAML response: {e}", 500

# # # # # # if __name__ == '__main__':
# # # # # #     app.run(debug=True, host='127.0.0.1')



# # # # # from flask import Flask, request, redirect, session, render_template
# # # # # from flask_cors import CORS
# # # # # from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
# # # # # from saml2.config import Config as Saml2Config
# # # # # from saml2.client import Saml2Client
# # # # # from urllib.parse import urlparse, parse_qs, quote
# # # # # import logging

# # # # # app = Flask(__name__)
# # # # # app.secret_key = 'your_secret_key'
# # # # # CORS(app)

# # # # # logging.basicConfig(level=logging.DEBUG)

# # # # # # SAML Configuration
# # # # # def saml_client():
# # # # #     config = Saml2Config()
# # # # #     config.load({
# # # # #         'entityid': 'https://zitadel-test.sp/metadata',
# # # # #         'service': {
# # # # #             'sp': {
# # # # #                 'name': 'SAML SP',
# # # # #                 'endpoints': {
# # # # #                     'assertion_consumer_service': [
# # # # #                         ('http://127.0.0.1:5000/acs', BINDING_HTTP_POST),
# # # # #                     ],
# # # # #                 },
# # # # #                 'required_attributes': ['uid'],
# # # # #                 'optional_attributes': ['mail'],
# # # # #             },
# # # # #         },
# # # # #         'metadata': {
# # # # #             'local': ['idp_metadata.xml'],
# # # # #         },
# # # # #         'key_file': 'sp-key.pem',  # Use the newly generated key
# # # # #         'cert_file': 'sp-cert.pem',  # Use the newly generated certificate
# # # # #         'xmlsec_binary': '/opt/homebrew/bin/xmlsec1',
# # # # #         'cert_data': open('zitadel_saml_cert.crt').read(),
# # # # #     })
# # # # #     return Saml2Client(config)

# # # # # @app.route('/')
# # # # # def index():
# # # # #     saml_request = session.pop('saml_request', '')
# # # # #     return render_template('index.html', saml_request=saml_request)

# # # # # @app.route('/generate_saml_request', methods=['POST'])
# # # # # def generate_saml_request():
# # # # #     client = saml_client()
# # # # #     reqid, info = client.prepare_for_authenticate()
# # # # #     location_header = dict(info['headers'])['Location']
# # # # #     parsed_url = urlparse(location_header)
# # # # #     saml_request = parse_qs(parsed_url.query)['SAMLRequest'][0]
# # # # #     logging.debug(f"SAML Request: {saml_request}")
# # # # #     session['saml_request'] = saml_request
# # # # #     return redirect('/')

# # # # # @app.route('/sso', methods=['POST'])
# # # # # def sso():
# # # # #     saml_request = request.form['saml_request']
# # # # #     encoded_saml_request = quote(saml_request)
# # # # #     redirect_url = f"https://my-instance-xtzfbc.zitadel.cloud/saml/v2/SSO?SAMLRequest={encoded_saml_request}"
# # # # #     logging.debug(f"Redirecting to: {redirect_url}")
# # # # #     return redirect(redirect_url)

# # # # # @app.route('/acs', methods=['POST'])
# # # # # def acs():
# # # # #     logging.debug("Received POST request at /acs")
# # # # #     logging.debug(f"Request form data: {request.form}")
# # # # #     client = saml_client()
# # # # #     saml_response = request.form['SAMLResponse']
# # # # #     logging.debug(f"SAML Response: {saml_response}")
# # # # #     try:
# # # # #         authn_response = client.parse_authn_request_response(saml_response, BINDING_HTTP_POST)
# # # # #         session['user_info'] = authn_response.get_identity()
# # # # #         return render_template('response.html', saml_response=saml_response, user_info=session['user_info'])
# # # # #     except Exception as e:
# # # # #         logging.error(f"Error processing SAML response: {e}")
# # # # #         return f"Error processing SAML response: {e}", 500

# # # # # if __name__ == '__main__':
# # # # #     app.run(debug=True, host='127.0.0.1')



# # # # from flask import Flask, request, redirect, session, render_template
# # # # from flask_cors import CORS
# # # # from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
# # # # from saml2.config import Config as Saml2Config
# # # # from saml2.client import Saml2Client
# # # # from urllib.parse import urlparse, parse_qs, quote
# # # # import logging
# # # # import secrets

# # # # app = Flask(__name__)
# # # # app.secret_key = secrets.token_hex(16)  # Securely generated secret key
# # # # CORS(app)

# # # # logging.basicConfig(level=logging.DEBUG)

# # # # # SAML Configuration
# # # # def saml_client():
# # # #     config = Saml2Config()
# # # #     config.load({
# # # #         'entityid': 'https://zitadel-test.sp/metadata',
# # # #         'service': {
# # # #             'sp': {
# # # #                 'name': 'SAML SP',
# # # #                 'endpoints': {
# # # #                     'assertion_consumer_service': [
# # # #                         ('http://127.0.0.1:5000/acs', BINDING_HTTP_POST),
# # # #                     ],
# # # #                 },
# # # #                 'required_attributes': ['uid'],
# # # #                 'optional_attributes': ['mail'],
# # # #             },
# # # #         },
# # # #         'metadata': {
# # # #             'local': ['idp_metadata.xml'],
# # # #         },
# # # #         'key_file': 'sp-key.pem',  # Use the newly generated key
# # # #         'cert_file': 'sp-cert.pem',  # Use the newly generated certificate
# # # #         'xmlsec_binary': '/opt/homebrew/bin/xmlsec1',  # Ensure this path is correct
# # # #     })
# # # #     return Saml2Client(config)

# # # # @app.route('/')
# # # # def index():
# # # #     saml_request = session.pop('saml_request', '')
# # # #     return render_template('index.html', saml_request=saml_request)

# # # # @app.route('/generate_saml_request', methods=['POST'])
# # # # def generate_saml_request():
# # # #     client = saml_client()
# # # #     reqid, info = client.prepare_for_authenticate()
# # # #     location_header = dict(info['headers'])['Location']
# # # #     parsed_url = urlparse(location_header)
# # # #     saml_request = parse_qs(parsed_url.query)['SAMLRequest'][0]
# # # #     logging.debug(f"SAML Request: {saml_request}")
# # # #     session['saml_request'] = saml_request
# # # #     return redirect('/')

# # # # @app.route('/sso', methods=['POST'])
# # # # def sso():
# # # #     saml_request = request.form['saml_request']
# # # #     encoded_saml_request = quote(saml_request)  # Ensure the SAML request is URL encoded
# # # #     redirect_url = f"https://my-instance-xtzfbc.zitadel.cloud/saml/v2/SSO?SAMLRequest={encoded_saml_request}"
# # # #     logging.debug(f"Redirecting to: {redirect_url}")
# # # #     return redirect(redirect_url)

# # # # @app.route('/acs', methods=['POST'])
# # # # def acs():
# # # #     logging.debug("Received POST request at /acs")
# # # #     logging.debug(f"Request form data: {request.form}")
# # # #     client = saml_client()
# # # #     saml_response = request.form['SAMLResponse']
# # # #     logging.debug(f"SAML Response: {saml_response}")
# # # #     try:
# # # #         authn_response = client.parse_authn_request_response(saml_response, BINDING_HTTP_POST)
# # # #         session['user_info'] = authn_response.get_identity()
# # # #         return render_template('response.html', saml_response=saml_response, user_info=session['user_info'])
# # # #     except Exception as e:
# # # #         logging.error(f"Error processing SAML response: {e}")
# # # #         return f"Error processing SAML response: {e}", 500

# # # # if __name__ == '__main__':
# # # #     app.run(debug=True, host='127.0.0.1')


# # # from flask import Flask, request, redirect, session, render_template
# # # from flask_cors import CORS
# # # from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
# # # from saml2.config import Config as Saml2Config
# # # from saml2.client import Saml2Client
# # # from urllib.parse import urlparse, parse_qs, quote
# # # import logging
# # # import secrets

# # # app = Flask(__name__)
# # # app.secret_key = secrets.token_hex(16)  # Securely generated secret key
# # # CORS(app)

# # # logging.basicConfig(level=logging.DEBUG)

# # # # SAML Configuration
# # # def saml_client():
# # #     config = Saml2Config()
# # #     config.load({
# # #         'entityid': 'https://zitadel-test.sp/metadata',
# # #         'service': {
# # #             'sp': {
# # #                 'name': 'SAML SP',
# # #                 'endpoints': {
# # #                     'assertion_consumer_service': [
# # #                         ('http://127.0.0.1:5000/acs', BINDING_HTTP_POST),
# # #                     ],
# # #                 },
# # #                 'required_attributes': ['uid'],
# # #                 'optional_attributes': ['mail'],
# # #             },
# # #         },
# # #         'metadata': {
# # #             'local': ['idp_metadata.xml'],
# # #         },
# # #         'key_file': 'sp-key.pem',  # Ensure this file exists and is correct
# # #         'cert_file': 'sp-cert.pem',  # Ensure this file exists and is correct
# # #         'xmlsec_binary': '/opt/homebrew/bin/xmlsec1',  # Ensure this path is correct
# # #     })
# # #     return Saml2Client(config)

# # # @app.route('/')
# # # def index():
# # #     saml_request = session.pop('saml_request', '')
# # #     return render_template('index.html', saml_request=saml_request)

# # # @app.route('/generate_saml_request', methods=['POST'])
# # # def generate_saml_request():
# # #     client = saml_client()
# # #     reqid, info = client.prepare_for_authenticate()
# # #     location_header = dict(info['headers'])['Location']
# # #     parsed_url = urlparse(location_header)
# # #     saml_request = parse_qs(parsed_url.query)['SAMLRequest'][0]
# # #     logging.debug(f"SAML Request: {saml_request}")
# # #     session['saml_request'] = saml_request
# # #     return redirect('/')

# # # @app.route('/sso', methods=['POST'])
# # # def sso():
# # #     saml_request = request.form['saml_request']
# # #     encoded_saml_request = quote(saml_request)  # Ensure the SAML request is URL encoded
# # #     redirect_url = f"https://my-instance-xtzfbc.zitadel.cloud/saml/v2/SSO?SAMLRequest={encoded_saml_request}"
# # #     logging.debug(f"Redirecting to: {redirect_url}")
# # #     return redirect(redirect_url)

# # # @app.route('/acs', methods=['POST'])
# # # def acs():
# # #     logging.debug("Received POST request at /acs")
# # #     logging.debug(f"Request form data: {request.form}")
# # #     client = saml_client()
# # #     saml_response = request.form['SAMLResponse']
# # #     logging.debug(f"SAML Response: {saml_response}")
# # #     try:
# # #         authn_response = client.parse_authn_request_response(saml_response, BINDING_HTTP_POST)
# # #         session['user_info'] = authn_response.get_identity()
# # #         logging.debug(f"User Info: {session['user_info']}")
# # #         return render_template('response.html', saml_response=saml_response, user_info=session['user_info'])
# # #     except Exception as e:
# # #         logging.error(f"Error processing SAML response: {e}")
# # #         return f"Error processing SAML response: {e}", 500

# # # if __name__ == '__main__':
# # #     app.run(debug=True, host='127.0.0.1')

# # from flask import Flask, request, redirect, session, render_template
# # from flask_cors import CORS
# # from saml2 import BINDING_HTTP_POST
# # from saml2.config import Config as Saml2Config
# # from saml2.client import Saml2Client
# # import logging
# # import secrets
# # from urllib.parse import urlparse, parse_qs, quote

# # app = Flask(__name__)
# # app.secret_key = secrets.token_hex(16)  # Securely generated secret key
# # CORS(app)

# # logging.basicConfig(level=logging.DEBUG)

# # # SAML Configuration
# # def saml_client():
# #     config = Saml2Config()
# #     config.load({
# #         'entityid': 'https://zitadel-test.sp/metadata',
# #         'service': {
# #             'sp': {
# #                 'name': 'SAML SP',
# #                 'endpoints': {
# #                     'assertion_consumer_service': [
# #                         ('http://127.0.0.1:5000/acs', BINDING_HTTP_POST),
# #                     ],
# #                 },
# #                 'required_attributes': ['uid'],
# #                 'optional_attributes': ['mail'],
# #             },
# #         },
# #         'metadata': {
# #             'local': ['idp_metadata.xml'],
# #         },
# #         'key_file': 'sp-key.pem',  # Use the newly generated key
# #         'cert_file': 'sp-cert.pem',  # Use the newly generated certificate
# #         'xmlsec_binary': '/opt/homebrew/bin/xmlsec1',  # Ensure this path is correct
# #         'allow_unknown_attributes': True,
# #         'debug': 1,
# #     })
# #     return Saml2Client(config)

# # @app.route('/')
# # def index():
# #     saml_request = session.pop('saml_request', '')
# #     return render_template('index.html', saml_request=saml_request)

# # @app.route('/generate_saml_request', methods=['POST'])
# # def generate_saml_request():
# #     client = saml_client()
# #     reqid, info = client.prepare_for_authenticate()
# #     location_header = dict(info['headers'])['Location']
# #     parsed_url = urlparse(location_header)
# #     saml_request = parse_qs(parsed_url.query)['SAMLRequest'][0]
# #     logging.debug(f"SAML Request: {saml_request}")
# #     session['saml_request'] = saml_request
# #     return redirect('/')

# # @app.route('/sso', methods=['POST'])
# # def sso():
# #     saml_request = request.form['saml_request']
# #     encoded_saml_request = quote(saml_request)  # Ensure the SAML request is URL encoded
# #     redirect_url = f"https://my-instance-xtzfbc.zitadel.cloud/saml/v2/SSO?SAMLRequest={encoded_saml_request}"
# #     logging.debug(f"Redirecting to: {redirect_url}")
# #     return redirect(redirect_url)

# # @app.route('/acs', methods=['POST'])
# # def acs():
# #     logging.debug("Received POST request at /acs")
# #     logging.debug(f"Request form data: {request.form}")
# #     client = saml_client()
# #     saml_response = request.form['SAMLResponse']
# #     logging.debug(f"SAML Response: {saml_response}")
# #     try:
# #         authn_response = client.parse_authn_request_response(saml_response, BINDING_HTTP_POST)
# #         session['user_info'] = authn_response.get_identity()
# #         logging.debug(f"User Info: {session['user_info']}")
# #         return render_template('response.html', saml_response=saml_response, user_info=session['user_info'])
# #     except Exception as e:
# #         logging.error(f"Error processing SAML response: {e}")
# #         return f"Error processing SAML response: {e}", 500

# # if __name__ == '__main__':
# #     app.run(debug=True, host='127.0.0.1')

# from flask import Flask, request, redirect, session, render_template
# from flask_cors import CORS
# from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
# from saml2.config import Config as Saml2Config
# from saml2.client import Saml2Client
# from saml2.s_utils import decode_base64_and_inflate
# import logging
# import secrets
# from urllib.parse import urlparse, parse_qs, quote

# app = Flask(__name__)
# app.secret_key = secrets.token_hex(16)  # Securely generated secret key
# CORS(app)

# logging.basicConfig(level=logging.DEBUG)

# # SAML Configuration
# def saml_client():
#     config = Saml2Config()
#     config.load({
#         'entityid': 'https://zitadel-test.sp/metadata',
#         'service': {
#             'sp': {
#                 'name': 'SAML SP',
#                 'endpoints': {
#                     'assertion_consumer_service': [
#                         ('http://127.0.0.1:5000/acs', BINDING_HTTP_POST),
#                     ],
#                 },
#                 'required_attributes': ['uid'],
#                 'optional_attributes': ['mail'],
#             },
#         },
#         'metadata': {
#             'local': ['idp_metadata.xml'],
#         },
#         'key_file': 'sp-key.pem',  # Use the newly generated key
#         'cert_file': 'sp-cert.pem',  # Use the newly generated certificate
#         'xmlsec_binary': '/opt/homebrew/bin/xmlsec1',  # Ensure this path is correct
#         'allow_unknown_attributes': True,
#         'debug': 1,
#     })
#     return Saml2Client(config)

# @app.route('/')
# def index():
#     saml_request = session.pop('saml_request', '')
#     return render_template('index.html', saml_request=saml_request)

# @app.route('/generate_saml_request', methods=['POST'])
# def generate_saml_request():
#     client = saml_client()
#     reqid, info = client.prepare_for_authenticate()
#     location_header = dict(info['headers'])['Location']
#     parsed_url = urlparse(location_header)
#     saml_request = parse_qs(parsed_url.query)['SAMLRequest'][0]
#     logging.debug(f"SAML Request: {saml_request}")
#     session['saml_request'] = saml_request
#     return redirect('/')

# @app.route('/sso', methods=['POST'])
# def sso():
#     saml_request = request.form['saml_request']
#     encoded_saml_request = quote(saml_request)  # Ensure the SAML request is URL encoded
#     redirect_url = f"https://my-instance-xtzfbc.zitadel.cloud/saml/v2/SSO?SAMLRequest={encoded_saml_request}"
#     logging.debug(f"Redirecting to: {redirect_url}")
#     return redirect(redirect_url)

# @app.route('/acs', methods=['POST'])
# def acs():
#     logging.debug("Received POST request at /acs")
#     logging.debug(f"Request form data: {request.form}")
#     client = saml_client()
#     saml_response = request.form['SAMLResponse']
#     logging.debug(f"SAML Response: {saml_response}")
#     try:
#         authn_response = client.parse_authn_request_response(saml_response, BINDING_HTTP_POST)
#         session['user_info'] = authn_response.get_identity()
#         logging.debug(f"User Info: {session['user_info']}")
#         return render_template('response.html', saml_response=saml_response, user_info=session['user_info'])
#     except Exception as e:
#         logging.error(f"Error processing SAML response: {e}")
#         return f"Error processing SAML response: {e}", 500

# if __name__ == '__main__':
#     app.run(debug=True, host='127.0.0.1')

from flask import Flask, request, redirect, session, render_template
from flask_cors import CORS
from saml2 import BINDING_HTTP_POST
from saml2.config import Config as Saml2Config
from saml2.client import Saml2Client
import logging
import secrets
from urllib.parse import urlparse, parse_qs, quote

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Securely generated secret key
CORS(app)

logging.basicConfig(level=logging.DEBUG)

# SAML Configuration
def saml_client():
    config = Saml2Config()
    config.load({
        'entityid': 'https://zitadel-test.sp/metadata',
        'service': {
            'sp': {
                'name': 'SAML SP',
                'endpoints': {
                    'assertion_consumer_service': [
                        ('http://127.0.0.1:5000/acs', BINDING_HTTP_POST),
                    ],
                },
                'required_attributes': ['uid'],
                'optional_attributes': ['mail'],
            },
        },
        'metadata': {
            'local': ['idp_metadata.xml'],
        },
        'key_file': 'sp-key.pem',
        'cert_file': 'sp-cert.pem',
        'xmlsec_binary': '/opt/homebrew/bin/xmlsec1',  # Ensure this path is correct
        'allow_unknown_attributes': True,
        'debug': 1,
    })
    return Saml2Client(config)

@app.route('/')
def index():
    saml_request = session.pop('saml_request', '')
    return render_template('index.html', saml_request=saml_request)

@app.route('/generate_saml_request', methods=['POST'])
def generate_saml_request():
    client = saml_client()
    reqid, info = client.prepare_for_authenticate()
    location_header = dict(info['headers'])['Location']
    parsed_url = urlparse(location_header)
    saml_request = parse_qs(parsed_url.query)['SAMLRequest'][0]
    logging.debug(f"SAML Request: {saml_request}")
    session['saml_request'] = saml_request
    return redirect('/')

@app.route('/sso', methods=['POST'])
def sso():
    saml_request = request.form['saml_request']
    encoded_saml_request = quote(saml_request)  # Ensure the SAML request is URL encoded
    redirect_url = f"https://my-instance-xtzfbc.zitadel.cloud/saml/v2/SSO?SAMLRequest={encoded_saml_request}"
    logging.debug(f"Redirecting to: {redirect_url}")
    return redirect(redirect_url)

@app.route('/acs', methods=['POST'])
def acs():
    logging.debug("Received POST request at /acs")
    logging.debug(f"Request form data: {request.form}")
    client = saml_client()
    saml_response = request.form['SAMLResponse']
    logging.debug(f"SAML Response: {saml_response}")
    try:
        authn_response = client.parse_authn_request_response(saml_response, BINDING_HTTP_POST)
        session['user_info'] = authn_response.get_identity()
        logging.debug(f"User Info: {session['user_info']}")
        return render_template('response.html', saml_response=saml_response, user_info=session['user_info'])
    except Exception as e:
        logging.error(f"Error processing SAML response: {e}")
        logging.exception("Exception details:")
        # Log the response for further debugging
        with open("saml_response.xml", "w") as f:
            f.write(saml_response)
        return f"Error processing SAML response: {e}", 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')

