"""
This type stub file was generated by pyright.
"""

from typing import Callable, Dict, Optional, Sequence, Tuple, Type, Union
from google.api_core import client_options as client_options_lib, gapic_v1
from google.auth import credentials as ga_credentials
from google.ai.generativelanguage_v1beta.types import discuss_service
from .transports.base import DEFAULT_CLIENT_INFO, DiscussServiceTransport

"""
This type stub file was generated by pyright.
"""
OptionalRetry = ...
class DiscussServiceClientMeta(type):
    """Metaclass for the DiscussService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """
    _transport_registry: Dict[str, Type[DiscussServiceTransport]] = ...
    def get_transport_class(cls, label: Optional[str] = ...) -> Type[DiscussServiceTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        ...
    


class DiscussServiceClient(metaclass=DiscussServiceClientMeta):
    """An API for using Generative Language Models (GLMs) in dialog
    applications.
    Also known as large language models (LLMs), this API provides
    models that are trained for multi-turn dialog.
    """
    DEFAULT_ENDPOINT = ...
    DEFAULT_MTLS_ENDPOINT = ...
    _DEFAULT_ENDPOINT_TEMPLATE = ...
    _DEFAULT_UNIVERSE = ...
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DiscussServiceClient: The constructed client.
        """
        ...
    
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DiscussServiceClient: The constructed client.
        """
        ...
    
    from_service_account_json = ...
    @property
    def transport(self) -> DiscussServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DiscussServiceTransport: The transport used by the client
                instance.
        """
        ...
    
    @staticmethod
    def model_path(model: str) -> str:
        """Returns a fully-qualified model string."""
        ...
    
    @staticmethod
    def parse_model_path(path: str) -> Dict[str, str]:
        """Parses a model path into its component segments."""
        ...
    
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str:
        """Returns a fully-qualified billing_account string."""
        ...
    
    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        ...
    
    @staticmethod
    def common_folder_path(folder: str) -> str:
        """Returns a fully-qualified folder string."""
        ...
    
    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        ...
    
    @staticmethod
    def common_organization_path(organization: str) -> str:
        """Returns a fully-qualified organization string."""
        ...
    
    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        ...
    
    @staticmethod
    def common_project_path(project: str) -> str:
        """Returns a fully-qualified project string."""
        ...
    
    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        ...
    
    @staticmethod
    def common_location_path(project: str, location: str) -> str:
        """Returns a fully-qualified location string."""
        ...
    
    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        ...
    
    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: Optional[client_options_lib.ClientOptions] = ...):
        """Deprecated. Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        ...
    
    @property
    def api_endpoint(self):
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        ...
    
    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used by the client instance.
        """
        ...
    
    def __init__(self, *, credentials: Optional[ga_credentials.Credentials] = ..., transport: Optional[Union[str, DiscussServiceTransport, Callable[..., DiscussServiceTransport]]] = ..., client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = ..., client_info: gapic_v1.client_info.ClientInfo = ...) -> None:
        """Instantiates the discuss service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DiscussServiceTransport,Callable[..., DiscussServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the DiscussServiceTransport constructor.
                If set to None, a transport is chosen automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client.

                1. The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client when ``transport`` is
                not explicitly provided. Only if this property is not set and
                ``transport`` was not explicitly provided, the endpoint is
                determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment
                variable, which have one of the following values:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto-switch to the
                default mTLS endpoint if client certificate is present; this is
                the default value).

                2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide a client certificate for mTLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

                3. The ``universe_domain`` property can be used to override the
                default "googleapis.com" universe. Note that the ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        ...
    
    def generate_message(self, request: Optional[Union[discuss_service.GenerateMessageRequest, dict]] = ..., *, model: Optional[str] = ..., prompt: Optional[discuss_service.MessagePrompt] = ..., temperature: Optional[float] = ..., candidate_count: Optional[int] = ..., top_p: Optional[float] = ..., top_k: Optional[int] = ..., retry: OptionalRetry = ..., timeout: Union[float, object] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> discuss_service.GenerateMessageResponse:
        r"""Generates a response from the model given an input
        ``MessagePrompt``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_generate_message():
                # Create a client
                client = generativelanguage_v1beta.DiscussServiceClient()

                # Initialize request argument(s)
                prompt = generativelanguage_v1beta.MessagePrompt()
                prompt.messages.content = "content_value"

                request = generativelanguage_v1beta.GenerateMessageRequest(
                    model="model_value",
                    prompt=prompt,
                )

                # Make the request
                response = client.generate_message(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.GenerateMessageRequest, dict]):
                The request object. Request to generate a message
                response from the model.
            model (str):
                Required. The name of the model to use.

                Format: ``name=models/{model}``.

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            prompt (google.ai.generativelanguage_v1beta.types.MessagePrompt):
                Required. The structured textual
                input given to the model as a prompt.
                Given a
                prompt, the model will return what it
                predicts is the next message in the
                discussion.

                This corresponds to the ``prompt`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            temperature (float):
                Optional. Controls the randomness of the output.

                Values can range over ``[0.0,1.0]``, inclusive. A value
                closer to ``1.0`` will produce responses that are more
                varied, while a value closer to ``0.0`` will typically
                result in less surprising responses from the model.

                This corresponds to the ``temperature`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            candidate_count (int):
                Optional. The number of generated response messages to
                return.

                This value must be between ``[1, 8]``, inclusive. If
                unset, this will default to ``1``.

                This corresponds to the ``candidate_count`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            top_p (float):
                Optional. The maximum cumulative probability of tokens
                to consider when sampling.

                The model uses combined Top-k and nucleus sampling.

                Nucleus sampling considers the smallest set of tokens
                whose probability sum is at least ``top_p``.

                This corresponds to the ``top_p`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            top_k (int):
                Optional. The maximum number of tokens to consider when
                sampling.

                The model uses combined Top-k and nucleus sampling.

                Top-k sampling considers the set of ``top_k`` most
                probable tokens.

                This corresponds to the ``top_k`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.ai.generativelanguage_v1beta.types.GenerateMessageResponse:
                The response from the model.

                This includes candidate messages and
                conversation history in the form of
                chronologically-ordered messages.

        """
        ...
    
    def count_message_tokens(self, request: Optional[Union[discuss_service.CountMessageTokensRequest, dict]] = ..., *, model: Optional[str] = ..., prompt: Optional[discuss_service.MessagePrompt] = ..., retry: OptionalRetry = ..., timeout: Union[float, object] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> discuss_service.CountMessageTokensResponse:
        r"""Runs a model's tokenizer on a string and returns the
        token count.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_count_message_tokens():
                # Create a client
                client = generativelanguage_v1beta.DiscussServiceClient()

                # Initialize request argument(s)
                prompt = generativelanguage_v1beta.MessagePrompt()
                prompt.messages.content = "content_value"

                request = generativelanguage_v1beta.CountMessageTokensRequest(
                    model="model_value",
                    prompt=prompt,
                )

                # Make the request
                response = client.count_message_tokens(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.CountMessageTokensRequest, dict]):
                The request object. Counts the number of tokens in the ``prompt`` sent to a
                model.

                Models may tokenize text differently, so each model may
                return a different ``token_count``.
            model (str):
                Required. The model's resource name. This serves as an
                ID for the Model to use.

                This name should match a model name returned by the
                ``ListModels`` method.

                Format: ``models/{model}``

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            prompt (google.ai.generativelanguage_v1beta.types.MessagePrompt):
                Required. The prompt, whose token
                count is to be returned.

                This corresponds to the ``prompt`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.ai.generativelanguage_v1beta.types.CountMessageTokensResponse:
                A response from CountMessageTokens.

                   It returns the model's token_count for the prompt.

        """
        ...
    
    def __enter__(self) -> DiscussServiceClient:
        ...
    
    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        ...
    


DEFAULT_CLIENT_INFO = ...
__all__ = ("DiscussServiceClient", )
