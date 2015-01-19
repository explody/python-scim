# -*- coding: utf-8 -*-
from .core import Base
from . import attributes, types


class Group(Base):

    # A human readable name for the Group.
    display_name = attributes.Singular(types.String)

    # A list of members of the Group.
    members = attributes.MultiValue()
