# SAML Service Provider with ZITADEL Integration

This repository provides a simple SAML Service Provider (SP) setup to interact with ZITADEL as the Identity Provider (IdP). The application is built using Flask and the `pysaml2` library.

## Prerequisites

- Python 3.x
- Flask
- pysaml2
- Flask-CORS

## Setting Up

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/saml-sp-zitadel.git
cd saml-sp-zitadel
```

### 2. Install Dependencies

Make sure you have Python 3 installed. Then, create a virtual environment and install the required packages.

```bash
python3 -m venv venv
source venv/bin/activate
pip install Flask pysaml2 Flask-CORS
```

### 3. ZITADEL Configuration

You need to create a SAML app in your ZITADEL instance and upload the `sp_metadata.xml` file found in this repository. Follow these steps:

1. Log in to your ZITADEL instance.
2. Navigate to the **Applications** section.
3. Create a new **SAML Application**.
4. Upload the `sp_metadata.xml` file.
5. Obtain the IdP metadata URL or file from ZITADEL and replace the content of `idp_metadata.xml` with the provided IdP metadata.

### 4. Configuration

Ensure the paths in the `app.py` file for `key_file`, `cert_file`, and `xmlsec_binary` are correct.

## Running the Application

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

The application should now be running on `http://127.0.0.1:5000`.

### Endpoints

- `/` - Home page with options to generate a SAML request and perform SSO.
- `/generate_saml_request` - Endpoint to generate the SAML request.
- `/sso` - Endpoint to redirect to the IdP with the SAML request.
- `/acs` - Assertion Consumer Service endpoint to handle the SAML response from the IdP.

### Files

- `templates/index.html` - HTML template for the home page.
- `templates/response.html` - HTML template to display the SAML response and user information.
- `app.py` - Main application file.
- `idp_metadata.xml` - IdP metadata file.
- `sp_metadata.xml` - SP metadata file to be uploaded to ZITADEL.
- `sp-cert.pem` - SP certificate file.
- `sp-csr.pem` - SP certificate signing request file.
- `sp-key.pem` - SP private key file.

### Notes

- Ensure the `xmlsec1` binary is installed and its path is correctly specified in `app.py`.
- Keep the `sp-key.pem` file secure and do not share it publicly.

## License

This project is licensed under the MIT License.
