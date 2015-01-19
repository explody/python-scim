# -*- coding: utf-8 -*-
from .core import Base
from . import attributes, types


class ProviderAttribute(attributes.Base):

    # Boolean value specifying whether the operation is supported
    supported = attributes.Singular(types.Boolean, required=True)


class Bulk(ProviderAttribute):

    # An integer value specifying the maximum number of operations.
    max_operations = attributes.Singular(types.Integer, required=True)

    # An integer value specifying the maximum payload size in bytes.
    max_payload_size = attributes.Singular(types.Integer, required=True)


class Filter(ProviderAttribute):

    # Integer value specifying the maximum number of Resources returned in a
    # response.
    max_results = attributes.Singular(types.Integer)


class AuthenticationScheme(ProviderAttribute):

    # The common authentication scheme name
    name = attributes.Singular(types.String, required=True)

    # A description of the Authentication Scheme
    description = attributes.Singular(types.String, required=True)

    # A HTTP addressable URL pointing to the Authentication Scheme's
    # specification
    spec_url = attributes.Singular(types.String)

    # A HTTP addressable URL pointing to the Authentication Scheme's usage
    # documentation
    documentation_url = attributes.Singular(types.String)


class ServiceProviderConfiguration(Base):

    # An HTTP addressable URL pointing to the Service Provider's
    # human consumable help documentation.
    documentation_url = attributes.Singular(types.String)

    # A complex type that specifies PATCH configuration options.
    patch = attributes.Complex(ProviderAttribute, required=True)

    # A complex type that specifies BULK configuration options.
    bulk = attributes.Complex(Bulk, required=True)

    # A complex type that specifies FILTER options
    filter = attributes.Complex(Filter, required=True)

    # A complex type that specifies Change Password configuration options.
    change_password = attributes.Complex(ProviderAttribute, required=True)

    # A complex type that specifies Sort configuration options
    sort = attributes.Complex(ProviderAttribute, required=True)

    # A complex type that specifies Etag configuration options
    etag = attributes.Complex(ProviderAttribute, required=True)

    # A complex type that specifies whether the XML data format is supported
    xml_data_format = attributes.Complex(ProviderAttribute, required=True)

    # A complex type that specifies supported Authentication Scheme properties
    authentication_schemes = attributes.MultiComplex(AuthenticationScheme,
                                                     required=True)
