INSTALLED_APPS += ["taiga_contrib_ldap_auth_ext"]

# Multiple LDAP servers are currently not supported, see
# https://github.com/Monogramm/taiga-contrib-ldap-auth-ext/issues/16
LDAP_SERVER = os.getenv('LDAP_HOST', 'ldap://127.0.0.1')
LDAP_PORT = os.getenv('LDAP_PORT', '389')

LDAP_BIND_DN = os.getenv('LDAP_BIND_USER', 'uid=username,ou=people,dc=example,dc=com')
LDAP_BIND_PASSWORD = os.getenv('LDAP_BIND_PASS', '')

LDAP_SEARCH_BASE = os.getenv('LDAP_SEARCH_BASE', 'ou=people,dc=example,dc=com')
LDAP_SEARCH_FILTER_ADDITIONAL = os.getenv('LDAP_SEARCH_FILTER', '(memberOf=cn=taiga,ou=groups,dc=example,dc=com)')

LDAP_USERNAME_ATTRIBUTE = "uid"
LDAP_EMAIL_ATTRIBUTE = "mail"
LDAP_FULL_NAME_ATTRIBUTE = "displayName"

LDAP_SAVE_LOGIN_PASSWORD = False

LDAP_MAP_USERNAME_TO_UID = None