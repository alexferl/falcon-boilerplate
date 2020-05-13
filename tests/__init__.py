from app import settings, configure

settings.parse_argv_disabled = True  # don't parse pytest's args

# set them here since some tests rely on them
configure(json_datetime_mode="DM_ISO8601", json_uuid_mode="UM_HEX")
