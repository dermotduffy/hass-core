"""Constants for Hyperion integration."""
DOMAIN = "hyperion"

COLOR_BLACK = (0, 0, 0)

CONF_AUTH_ID = "auth_id"
CONF_CREATE_TOKEN = "create_token"
CONF_INSTANCE = "instance"
CONF_PRIORITY = "priority"
CONF_MODE_ABSOLUTE = "absolute"
CONF_MODE_PRIORITY = "priority"

CONF_ROOT_CLIENT = "ROOT_CLIENT"
CONF_ON_UNLOAD = "ON_UNLOAD"

DEFAULT_MODE = CONF_MODE_ABSOLUTE
DEFAULT_NAME = "Hyperion"
DEFAULT_ORIGIN = "Home Assistant"
DEFAULT_PRIORITY = 128

SIGNAL_INSTANCES_UPDATED = f"{DOMAIN}_instances_updated_signal." "{}"
SIGNAL_INSTANCE_REMOVED = f"{DOMAIN}_instance_removed_signal." "{}"

SOURCE_IMPORT = "import"
