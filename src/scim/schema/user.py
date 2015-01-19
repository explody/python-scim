# -*- coding: utf-8 -*-
from .core import Base
from . import attributes, types
from .complex import Address, Name


class User(Base):
    """
    SCIM provides a schema for representing Users (v1.1 § 6).
    """

    # Unique identifier for the User, typically used by the user to directly
    # authenticate to the service provider.
    username = attributes.Singular(types.String, 'userName', required=True)

    # The components of the User's real name.
    name = attributes.Complex(Name)

    # The name of the User, suitable for display to end-users.
    display_name = attributes.Singular(types.String)

    # The casual way to address the user in real life, e.g. "Bob"
    # or "Bobby" instead of "Robert".
    nick_name = attributes.Singular(types.String)

    # A fully qualified URL to a page representing the User's online profile.
    profile_url = attributes.Singular(types.String)

    # The user’s title, such as “Vice President.”
    title = attributes.Singular(types.String)

    # Used to identify the organization to user relationship.
    # Typical values used might be "Contractor", "Employee",
    # "Intern", "Temp", "External", and "Unknown" but any value may be used.
    user_type = attributes.Singular(types.String)

    # Indicates the User's preferred written or spoken language.
    preferred_language = attributes.Singular(types.String)

    # Used to indicate the User's default location for purposes of
    # localizing items such as currency, date time format,
    # numerical representations, etc.
    locale = attributes.Singular(types.String)

    # The User's time zone in the "Olson" timezone database
    # format; e.g.,'America/Los_Angeles'.
    timezone = attributes.Singular(types.String)

    # A Boolean value indicating the User's administrative status.
    active = attributes.Singular(types.Boolean)

    # The User's clear text password. This attribute is intended to be used
    # as a means to specify an initial password when creating a new User or
    # to reset an existing User's password.
    #
    # This value MUST never be returned by a Service Provider in any form.
    password = attributes.Singular(types.String)

    # E-mail addresses for the User.
    emails = attributes.MultiValue()

    # Phone numbers for the User.
    phone_numbers = attributes.MultiValue()

    # Instant messaging address for the User.
    ims = attributes.MultiValue()

    # URL of a photo of the User.
    photos = attributes.MultiValue()

    # A physical mailing address for this User
    addresses = attributes.MultiComplex(Address)

    # A list of groups that the user belongs to
    groups = attributes.MultiValue()

    # A list of entitlements for the User that represent a thing the User has.
    entitlements = attributes.MultiValue()

    # A list of roles for the User that collectively represent who the
    # User is.
    roles = attributes.MultiValue()

    # A list of certificates issued to the User.
    x509_certificates = attributes.MultiValue()
