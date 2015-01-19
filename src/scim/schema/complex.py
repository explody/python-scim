from . import attributes, types, formatters

class Address(attributes.BaseMultiValue):

    # The full street address component, which may include house number,
    # street name, P.O. box, and multi-line extended street address
    # information. This attribute MAY contain newlines.
    street_address = attributes.Singular(types.String)

    # The city or locality component.
    locality = attributes.Singular(types.String)

    # The state or region component.
    region = attributes.Singular(types.String)

    # The zipcode or postal code component.
    postal_code = attributes.Singular(types.String)

    # The country name component. When specified the value MUST
    # be in ISO 3166-1 alpha 2 "short" code format; e.g., the United States
    # and Sweden are "US" and "SE", respectively.
    country = attributes.Singular(types.String)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.addr_attrs = ['street_address', 'locality', 'region',
                           'postal_code', 'country']

    @property
    def formatted(self):
        return formatters.SimpleFormatter(self, self.addr_attrs, ", ")

class Name(attributes.Base):
    """The components of the User's real name.
    """

    # The full name, including all middle names, titles, and suffixes as
    # appropriate, formatted for display (e.g. Ms. Barbara Jane Jensen, III.).
    #formatted = attributes.Singular(types.String)

    # The family name of the User, or "Last Name" in
    # most Western languages (e.g. Jensen given the full name Ms.
    # Barbara Jane Jensen, III.).
    family_name = attributes.Singular(types.String)

    # The given name of the User, or "First Name" in most Western
    # languages (e.g. Barbara given the full name
    # Ms. Barbara Jane Jensen, III.).
    given_name = attributes.Singular(types.String)

    # The middle name(s) of the User (e.g. Jane given the full
    # name Ms. Barbara Jane Jensen, III.).
    middle_name = attributes.Singular(types.String)

    # The honorific prefix(es) of the User, or "Title" in most
    # Western languages (e.g. Ms. given the full name
    # Ms. Barbara Jane Jensen, III.).
    honorific_prefix = attributes.Singular(types.String)

    # The honorific suffix(es) of the User, or "Suffix" in most
    # Western languages (e.g. III. given the full name
    # Ms. Barbara Jane Jensen, III.).
    honorific_suffix = attributes.Singular(types.String)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_attrs = ['honorific_prefix', 'given_name', 'middle_name',
                           'family_name', 'honorific_suffix']

    @property
    def formatted(self):
        return formatters.SimpleFormatter(self, self.name_attrs)
