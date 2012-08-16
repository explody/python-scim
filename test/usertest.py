from scim import user
import unittest
import json




class JSONTestCase(unittest.TestCase):
    def setUp(self):
        self.u = user.User(
            name=user.User.Name(
                formatted="Ms. Barbara J Jensen III",
                given="Barbara",
                family="Jensen",
                middle="Jane",
                prefix="Ms.",
                suffix="III"
                
            ),
        )
        self.u.username = "bjensen@example.com"
        self.u.display = "Babs Jensen"
        self.u.nick_name = "Babs"
        self.u.profile = "https://login.example.com/bjensen"
        self.u.emails = [
            user.User.Email(
                primary=True,
                type='work',
                value='bejensen@example.com'
            ),
            user.User.Email(
                 type='home',
                 value='babs@jensen.org'
            )
        ]
        self.u.addresses = [
            user.User.Address(
                primary=True,
                type='work',
                street='100 Universal City Plaza',
                locality='Hollywood',
                region='CA',
                code='91608',
                country='USA',
                fomrated='100 Universal City Plaza\nHollywood, CA 91608 USA'
            ),
            user.User.Address(
                type='home',
                street='456 Hollywood Blvd',
                locality='Hollywood',
                region='CA',
                code='91608',
                country='USA',
                formatted="456 Hollywood Blvd\nHollywood, CA 91608 USA"
            )
        ]
        self.u.PhoneNumber = [
            user.User.PhoneNumber(
                value="555-555-5555",
                type='work'
            ),
            user.User.PhoneNumber(
                value='444-444-4444',
                type='mobile'
            )
        ]
        self.u.Messanger = [
            user.User.Messanger(
                value='someaimhandle',
                type='aim'
            )
        ]
        self.u.Photo = [
            user.User.Photo(
                value='https://photos.example.com/profilephoto/72930000000Ccne/F',
                type='photo'
            ),
            user.User.Photo(
                value='https://photos.example.com/profilephoto/72930000000Ccne/T',
                type='thumbnail'
            )
        ]
        self.u.user_type='Employee'
        self.u.title='Tour Guide'
        self.u.language='en_US'
        self.u.locale='en_US'
        self.u.timezone='America/Los_Angeles'
        
        self.u.password='t1meMa$heen'
        self.u.Group = [
            user.User.Group(
                display='Tour Guides',
                value='00300000005N2Y6AA'
            ),
            user.User.Group(
                display='Employees',
                value='00300000005N34H78'
            ),
            user.User.Group(
                display="US Employees",
                value='00300000005N98YT1'
            )
        ]
        self.u.Certificate = [
            user.User.Certificate(
                value="""MIIDQzCCAqygAwIBAgICEAAwDQYJKoZIhvcNAQEFBQAwTjELMAkGA1UEBhMCVVMx
                EzARBgNVBAgMCkNhbGlmb3JuaWExFDASBgNVBAoMC2V4YW1wbGUuY29tMRQwEgYD
                VQQDDAtleGFtcGxlLmNvbTAeFw0xMTEwMjIwNjI0MzFaFw0xMjEwMDQwNjI0MzFa
                MH8xCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRQwEgYDVQQKDAtl
                eGFtcGxlLmNvbTEhMB8GA1UEAwwYTXMuIEJhcmJhcmEgSiBKZW5zZW4gSUlJMSIw
                IAYJKoZIhvcNAQkBFhNiamVuc2VuQGV4YW1wbGUuY29tMIIBIjANBgkqhkiG9w0B
                AQEFAAOCAQ8AMIIBCgKCAQEA7Kr+Dcds/JQ5GwejJFcBIP682X3xpjis56AK02bc
                1FLgzdLI8auoR+cC9/Vrh5t66HkQIOdA4unHh0AaZ4xL5PhVbXIPMB5vAPKpzz5i
                PSi8xO8SL7I7SDhcBVJhqVqr3HgllEG6UClDdHO7nkLuwXq8HcISKkbT5WFTVfFZ
                zidPl8HZ7DhXkZIRtJwBweq4bvm3hM1Os7UQH05ZS6cVDgweKNwdLLrT51ikSQG3
                DYrl+ft781UQRIqxgwqCfXEuDiinPh0kkvIi5jivVu1Z9QiwlYEdRbLJ4zJQBmDr
                SGTMYn4lRc2HgHO4DqB/bnMVorHB0CC6AV1QoFK4GPe1LwIDAQABo3sweTAJBgNV
                HRMEAjAAMCwGCWCGSAGG+EIBDQQfFh1PcGVuU1NMIEdlbmVyYXRlZCBDZXJ0aWZp
                Y2F0ZTAdBgNVHQ4EFgQU8pD0U0vsZIsaA16lL8En8bx0F/gwHwYDVR0jBBgwFoAU
                dGeKitcaF7gnzsNwDx708kqaVt0wDQYJKoZIhvcNAQEFBQADgYEAA81SsFnOdYJt
                Ng5Tcq+/ByEDrBgnusx0jloUhByPMEVkoMZ3J7j1ZgI8rAbOkNngX8+pKfTiDz1R
                C4+dx8oU6Za+4NJXUjlL5CvV6BEYb1+QAEJwitTVvxB/A67g42/vzgAtoRUeDov1
                +GFiBZ+GNF/cAYKcMtGcrs2i97ZkJMo="""
            )
        ]
        self.testJson = """{
  "schemas": ["urn:scim:schemas:core:1.0"],
  "id": "2819c223-7f76-453a-919d-413861904646",
  "externalId": "701984",
  "userName": "bjensen@example.com",
  "name": {
    "formatted": "Ms. Barbara J Jensen III",
    "familyName": "Jensen",
    "givenName": "Barbara",
    "middleName": "Jane",
    "honorificPrefix": "Ms.",
    "honorificSuffix": "III"
  },
  "displayName": "Babs Jensen",
  "nickName": "Babs",
  "profileUrl": "https://login.example.com/bjensen",
  "emails": [
    {
      "value": "bjensen@example.com",
      "type": "work",
      "primary": true
    },
    {
      "value": "babs@jensen.org",
      "type": "home"
    }
  ],
  "addresses": [
    {
      "type": "work",
      "streetAddress": "100 Universal City Plaza",
      "locality": "Hollywood",
      "region": "CA",
      "postalCode": "91608",
      "country": "USA",
      "formatted": "100 Universal City Plaza\nHollywood, CA 91608 USA",
      "primary": true
    },
    {
      "type": "home",
      "streetAddress": "456 Hollywood Blvd",
      "locality": "Hollywood",
      "region": "CA",
      "postalCode": "91608",
      "country": "USA",
      "formatted": "456 Hollywood Blvd\nHollywood, CA 91608 USA"
    }
  ],
  "phoneNumbers": [
    {
      "value": "555-555-5555",
      "type": "work"
    },
    {
      "value": "555-555-4444",
      "type": "mobile"
    }
  ],
  "ims": [
    {
      "value": "someaimhandle",
      "type": "aim"
    }
  ],
  "photos": [
    {
      "value": "https://photos.example.com/profilephoto/72930000000Ccne/F",
      "type": "photo"
    },
    {
      "value": "https://photos.example.com/profilephoto/72930000000Ccne/T",
      "type": "thumbnail"
    }
  ],
  "userType": "Employee",
  "title": "Tour Guide",
  "preferredLanguage":"en_US",
  "locale": "en_US",
  "timezone": "America/Los_Angeles",
  "active":true,
  "password":"t1meMa$heen",
  "groups": [
    {
      "display": "Tour Guides",
      "value": "00300000005N2Y6AA"
    },
    {
      "display": "Employees",
      "value": "00300000005N34H78"
    },
    {
      "display": "US Employees",
      "value": "00300000005N98YT1"
    }
  ],
  "x509Certificates": [
    {
      "value": "MIIDQzCCAqygAwIBAgICEAAwDQYJKoZIhvcNAQEFBQAwTjELMAkGA1UEBhMCVVMx
                EzARBgNVBAgMCkNhbGlmb3JuaWExFDASBgNVBAoMC2V4YW1wbGUuY29tMRQwEgYD
                VQQDDAtleGFtcGxlLmNvbTAeFw0xMTEwMjIwNjI0MzFaFw0xMjEwMDQwNjI0MzFa
                MH8xCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRQwEgYDVQQKDAtl
                eGFtcGxlLmNvbTEhMB8GA1UEAwwYTXMuIEJhcmJhcmEgSiBKZW5zZW4gSUlJMSIw
                IAYJKoZIhvcNAQkBFhNiamVuc2VuQGV4YW1wbGUuY29tMIIBIjANBgkqhkiG9w0B
                AQEFAAOCAQ8AMIIBCgKCAQEA7Kr+Dcds/JQ5GwejJFcBIP682X3xpjis56AK02bc
                1FLgzdLI8auoR+cC9/Vrh5t66HkQIOdA4unHh0AaZ4xL5PhVbXIPMB5vAPKpzz5i
                PSi8xO8SL7I7SDhcBVJhqVqr3HgllEG6UClDdHO7nkLuwXq8HcISKkbT5WFTVfFZ
                zidPl8HZ7DhXkZIRtJwBweq4bvm3hM1Os7UQH05ZS6cVDgweKNwdLLrT51ikSQG3
                DYrl+ft781UQRIqxgwqCfXEuDiinPh0kkvIi5jivVu1Z9QiwlYEdRbLJ4zJQBmDr
                SGTMYn4lRc2HgHO4DqB/bnMVorHB0CC6AV1QoFK4GPe1LwIDAQABo3sweTAJBgNV
                HRMEAjAAMCwGCWCGSAGG+EIBDQQfFh1PcGVuU1NMIEdlbmVyYXRlZCBDZXJ0aWZp
                Y2F0ZTAdBgNVHQ4EFgQU8pD0U0vsZIsaA16lL8En8bx0F/gwHwYDVR0jBBgwFoAU
                dGeKitcaF7gnzsNwDx708kqaVt0wDQYJKoZIhvcNAQEFBQADgYEAA81SsFnOdYJt
                Ng5Tcq+/ByEDrBgnusx0jloUhByPMEVkoMZ3J7j1ZgI8rAbOkNngX8+pKfTiDz1R
                C4+dx8oU6Za+4NJXUjlL5CvV6BEYb1+QAEJwitTVvxB/A67g42/vzgAtoRUeDov1
                +GFiBZ+GNF/cAYKcMtGcrs2i97ZkJMo="
    }
  ],
  "meta": {
    "created": "2010-01-23T04:56:22Z",
    "lastModified": "2011-05-13T04:42:34Z",
    "version": "W\/\"a330bc54f0671c9\"",
    "location": "https://example.com/v1/Users/2819c223-7f76-453a-919d-413861904646"
  }
}"""

    def runTest(self):
        
        self.userJson = json.dumps(user.User.serialize(self.u), indent=2)
        print self.userJson
        self.assertEqual(self.userJson, self.testJson,"JSON's don't match")
