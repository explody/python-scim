# -*- coding: utf-8 -*-
from . import attributes, types
from .user import User


class Manager(attributes.Base):

    # The id of the SCIM resource representing the User's manager.
    id = attributes.Singular(types.String, 'managerId')

    # The URI of the SCIM resource representing the User's manager.
    uri = attributes.Singular(types.String, '$ref')

    # The displayName of the User's manager.
    display_name = attributes.Singular(types.String)


class EnterpriseUser(User):
    """
    Maps to the Enterprise User extension which defines attributes
    commonly used in representing users that belong to, or act on behalf
    of a business or enterprise (v2.0 § 7).
    """

    class Meta:
        schema = 'urn:scim:schemas:extension:enterprise:2.0:User'

    # Numeric or alphanumeric identifier assigned to a
    # person, typically based on order of hire or association with an
    # organization.
    employee_number = attributes.Singular(types.String)

    # Identifies the name of a cost center.
    cost_center = attributes.Singular(types.String)

    # Identifies the name of an organization.
    organization = attributes.Singular(types.String)

    # Identifies the name of a department.
    department = attributes.Singular(types.String)

    # Identifies the name of a division.
    division = attributes.Singular(types.String)

    # The User's manager.  A complex type that optionally allows
    # Service Providers to represent organizational hierarchy by
    # referencing the "id" attribute of another User.
    manager = attributes.Complex(Manager)
