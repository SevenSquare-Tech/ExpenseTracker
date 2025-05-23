"""
This type stub file was generated by pyright.
"""

from google.auth import _helpers, credentials

"""Experimental GDCH credentials support.
"""
TOKEN_EXCHANGE_TYPE = ...
ACCESS_TOKEN_TOKEN_TYPE = ...
SERVICE_ACCOUNT_TOKEN_TYPE = ...
JWT_LIFETIME = ...
class ServiceAccountCredentials(credentials.Credentials):
    """Credentials for GDCH (`Google Distributed Cloud Hosted`_) for service
    account users.

    .. _Google Distributed Cloud Hosted:
        https://cloud.google.com/blog/topics/hybrid-cloud/\
            announcing-google-distributed-cloud-edge-and-hosted

    To create a GDCH service account credential, first create a JSON file of
    the following format::

        {
            "type": "gdch_service_account",
            "format_version": "1",
            "project": "<project name>",
            "private_key_id": "<key id>",
            "private_key": "-----BEGIN EC PRIVATE KEY-----\n<key bytes>\n-----END EC PRIVATE KEY-----\n",
            "name": "<service identity name>",
            "ca_cert_path": "<CA cert path>",
            "token_uri": "https://service-identity.<Domain>/authenticate"
        }

    The "format_version" field stands for the format of the JSON file. For now
    it is always "1". The `private_key_id` and `private_key` is used for signing.
    The `ca_cert_path` is used for token server TLS certificate verification.

    After the JSON file is created, set `GOOGLE_APPLICATION_CREDENTIALS` environment
    variable to the JSON file path, then use the following code to create the
    credential::

        import google.auth

        credential, _ = google.auth.default()
        credential = credential.with_gdch_audience("<the audience>")

    We can also create the credential directly::

        from google.oauth import gdch_credentials

        credential = gdch_credentials.ServiceAccountCredentials.from_service_account_file("<the json file path>")
        credential = credential.with_gdch_audience("<the audience>")

    The token is obtained in the following way. This class first creates a
    self signed JWT. It uses the `name` value as the `iss` and `sub` claim, and
    the `token_uri` as the `aud` claim, and signs the JWT with the `private_key`.
    It then sends the JWT to the `token_uri` to exchange a final token for
    `audience`.
    """
    def __init__(self, signer, service_identity_name, project, audience, token_uri, ca_cert_path) -> None:
        """
        Args:
            signer (google.auth.crypt.Signer): The signer used to sign JWTs.
            service_identity_name (str): The service identity name. It will be
                used as the `iss` and `sub` claim in the self signed JWT.
            project (str): The project.
            audience (str): The audience for the final token.
            token_uri (str): The token server uri.
            ca_cert_path (str): The CA cert path for token server side TLS
                certificate verification. If the token server uses well known
                CA, then this parameter can be `None`.
        """
        ...
    
    @_helpers.copy_docstring(credentials.Credentials)
    def refresh(self, request): # -> None:
        ...
    
    def with_gdch_audience(self, audience): # -> Self:
        """Create a copy of GDCH credentials with the specified audience.

        Args:
            audience (str): The intended audience for GDCH credentials.
        """
        ...
    
    @classmethod
    def from_service_account_info(cls, info): # -> Self:
        """Creates a Credentials instance from parsed service account info.

        Args:
            info (Mapping[str, str]): The service account info in Google
                format.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.oauth2.gdch_credentials.ServiceAccountCredentials: The constructed
                credentials.

        Raises:
            ValueError: If the info is not in the expected format.
        """
        ...
    
    @classmethod
    def from_service_account_file(cls, filename): # -> Self:
        """Creates a Credentials instance from a service account json file.

        Args:
            filename (str): The path to the service account json file.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.oauth2.gdch_credentials.ServiceAccountCredentials: The constructed
                credentials.
        """
        ...
    


