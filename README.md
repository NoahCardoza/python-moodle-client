# Python 3 Moodle Client

A client for Moodle written in Python 3 because XML is disgusting.


Here is an example:

```py
from moodle import MoodleClient

email = 'noahcardoza@gmail.com'

client = MoodleClient(
  token='API_TOKEN',
  wwwroot='WWW_ROOT'
)

results = client.request('core_user_get_users_by_field', {
  'field': 'username',
  'values': [email]
})
```

This is what results should look like:

```py
[{'auth': 'manual',
  'confirmed': True,
  'customfields': [{'name': 'Firstname',
                    'shortname': 'usrfirstname',
                    'type': 'text',
                    'value': 'Noah'},
                   {'name': 'Lastname',
                    'shortname': 'usrLastname',
                    'type': 'text',
                    'value': 'Cardoza'},
                   {'name': 'User Registration Code',
                    'shortname': 'usrregistration',
                    'type': 'text',
                    'value': '1234'}],
  'department': '',
  'description': '',
  'descriptionformat': 1,
  'email': 'noahcardoza@gmail.com',
  'firstaccess': 1539986353,
  'firstname': 'Noah',
  'fullname': 'Noah Cardoza',
  'id': 55,
  'lang': 'en',
  'lastaccess': 1615601992,
  'lastname': 'Cardoza',
  'mailformat': 1,
  'profileimageurl': 'WWW_ROOT/theme/image.php/moove/core/1623890954/u/f1',
  'profileimageurlsmall': 'WWW_ROOT/theme/image.php/moove/core/1623890954/u/f2',
  'suspended': False,
  'theme': '',
  'timezone': '99',
  'username': 'noahcardoza@gmail.com'}]
```
