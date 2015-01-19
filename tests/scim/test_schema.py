# -*- coding: utf-8 -*-
from datetime import datetime
from scim import schema
import pprint
import inspect


class TestUser:

    def test_serialize(self):
        u = schema.User()
        u.id = '43568296982626'
        u.external_id = '42'
        u.meta.created = datetime.now()
        u.meta.attributes.append('blue')
        u.meta.attributes.append('red')
        u.name.given_name = 'Bob'
        u.preferred_language = 'en_US'
        u.active = False
        u.emails.append('bob@example.com')
        u.emails[0].primary = False

        ua = schema.Address()
        ua.street_address = "123 Main St"
        ua.locality = "Sometown"
        ua.region = "Some Province"
        ua.country = "XX"

        u.addresses.append(ua)

        d = u.serialize()

        print()
        print("Serialized:")
        pprint.pprint(d)

        assert d['id'] == u.id
        assert d['externalId'] == u.external_id
        assert d['active'] == u.active
        assert d['name']['givenName'] == u.name.given_name
        assert d['preferredLanguage'] == u.preferred_language
        assert d['meta']['created'] == u.meta.created.isoformat()
        assert len(d['meta']['attributes']) == len(u.meta.attributes)
        assert d['meta']['attributes'][0] == u.meta.attributes[0]
        assert len(d['emails']) == len(u.emails)
        assert d['emails'][0]['value'] == u.emails[0].value
        assert d['emails'][0]['primary'] == u.emails[0].primary
        assert list(d.keys())[-1] == 'meta'

    def test_deserialize(self):
        d = {}
        d['id'] = '43568296982626'
        d['externalId'] = '42'
        d['active'] = 'false'
        d['meta'] = {}
        d['meta']['created'] = datetime.now().isoformat()
        d['meta']['attributes'] = ['blue', 'red']
        d['name'] = {}
        d['name']['givenName'] = 'Bob'
        d['preferredLanguage'] = 'en_US'
        d['emails'] = [{'value': 'bob@example.com', 'primary': 'false'}]
        d['addresses'] = []
        d['addresses'].append({
                              "type": "work",
                              "streetAddress": "100 Universal City Plaza",
                              "locality": "Hollywood",
                              "region": "CA",
                              "postalCode": "91608",
                              "country": "US",
                              "formatted": "100 Universal City Plaza\n"
                                           "Hollywood, CA 91608 US",
                              "primary": True,
                              })
        d['addresses'].append({
                              "type": "work",
                              "streetAddress": "911 Universal City Plaza",
                              "locality": "Hollywood",
                              "region": "CA",
                              "postalCode": "91608",
                              "country": "US",
                              "formatted": "911 Universal City Plaza\n"
                                           "Hollywood, CA 91608 US",
                              "primary": True
                              })

        u = schema.User.deserialize(d)

        assert d['id'] == u.id
        assert d['externalId'] == u.external_id
        assert d['active'] == u.active
        assert d['name']['givenName'] == u.name.given_name
        assert d['preferredLanguage'] == u.preferred_language
        assert d['meta']['created'] == u.meta.created.isoformat()
        assert len(d['meta']['attributes']) == len(u.meta.attributes)
        assert d['meta']['attributes'][0] == u.meta.attributes[0]
        assert len(d['emails']) == len(u.emails)
        assert d['emails'][0]['value'] == u.emails[0].value
        assert d['emails'][0]['primary'] == u.emails[0].primary
        assert len(d['addresses']) == 2
        assert d['addresses'][0]['type'] == u.addresses[0].type
        assert d['addresses'][1]['streetAddress'] == \
            u.addresses[1].street_address
