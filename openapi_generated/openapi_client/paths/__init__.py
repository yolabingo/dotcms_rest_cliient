# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_DOTSAML_LOGIN_IDP_CONFIG_ID = "/v1/dotsaml/login/{idpConfigId}"
    V1_DOTSAML_LOGOUT_IDP_CONFIG_ID = "/v1/dotsaml/logout/{idpConfigId}"
    V1_DOTSAML_METADATA_IDP_CONFIG_ID = "/v1/dotsaml/metadata/{idpConfigId}"
    V1_FIELD_TYPES = "/v1/fieldTypes"
    AUDIT_PUBLISHING_GET_BUNDLE_ID = "/auditPublishing/get/{bundleId}"
    BUNDLE_PUBLISHER_PUBLISH = "/bundlePublisher/publish"
    BUNDLE_ALL = "/bundle/all"
    BUNDLE_ALL_FAIL = "/bundle/all/fail"
    BUNDLE_ALL_SUCCESS = "/bundle/all/success"
    BUNDLE_IDS = "/bundle/ids"
    BUNDLE_OLDERTHAN_OLDER_THAN = "/bundle/olderthan/{olderThan}"
    BUNDLE_DELETEENVIRONMENTPUSHHISTORY_PARAMS = "/bundle/deleteenvironmentpushhistory/{params}"
    BUNDLE_DELETEPUSHHISTORY_PARAMS = "/bundle/deletepushhistory/{params}"
    BUNDLE__DOWNLOAD_BUNDLE_ID = "/bundle/_download/{bundleId}"
    BUNDLE_BUNDLE_ID_MANIFEST = "/bundle/{bundleId}/manifest"
    BUNDLE__GENERATE = "/bundle/_generate"
    BUNDLE_BUNDLE_ID_ASSETS = "/bundle/{bundleId}/assets"
    BUNDLE_GETUNSENDBUNDLES_PARAMS = "/bundle/getunsendbundles/{params}"
    BUNDLE_UPDATEBUNDLE_PARAMS = "/bundle/updatebundle/{params}"
    BUNDLE = "/bundle"
    BUNDLE_SYNC = "/bundle/sync"
    CONFIG_DELETE_ENDPOINT = "/config/deleteEndpoint"
    CONFIG_DELETE_ENVIRONMENT = "/config/deleteEnvironment"
    CONFIG_REGENERATE_KEY = "/config/regenerateKey"
    CONFIG_SAVE_COMPANY_AUTH_TYPE_INFO = "/config/saveCompanyAuthTypeInfo"
    CONFIG_SAVE_COMPANY_BASIC_INFO = "/config/saveCompanyBasicInfo"
    CONFIG_SAVE_COMPANY_LOCALE_INFO = "/config/saveCompanyLocaleInfo"
    CONFIG_SAVE_COMPANY_LOGO = "/config/saveCompanyLogo"
    CLUSTER_GET_ESCONFIG_PROPERTIES_PARAMS = "/cluster/getESConfigProperties/{params}"
    CLUSTER_LICENSE_REPO_STATUS = "/cluster/licenseRepoStatus"
    CLUSTER_GET_NODES_STATUS_PARAMS = "/cluster/getNodesStatus/{params}"
    CLUSTER_REMOVE_PARAMS = "/cluster/remove/{params}"
    CLUSTER_TEST = "/cluster/test"
    CONTENT_CAN_LOCK_PARAMS = "/content/canLock/{params}"
    CONTENT_PARAMS = "/content/{params}"
    CONTENT_INDEXCOUNT_QUERY = "/content/indexcount/{query}"
    CONTENT_INDEXSEARCH_QUERY_SORTBY_SORTBY_LIMIT_LIMIT_OFFSET_OFFSET = "/content/indexsearch/{query}/sortby/{sortby}/limit/{limit}/offset/{offset}"
    CONTENT_LOCK_PARAMS = "/content/lock/{params}"
    CONTENT__SEARCH = "/content/_search"
    CONTENT_UNLOCK_PARAMS = "/content/unlock/{params}"
    ENVIRONMENT_LOADENVIRONMENTS_PARAMS = "/environment/loadenvironments/{params}"
    INTEGRITY_CHECKINTEGRITY_PARAMS = "/integrity/checkintegrity/{params}"
    INTEGRITY_CHECK_INTEGRITY_PROCESS_STATUS_PARAMS = "/integrity/checkIntegrityProcessStatus/{params}"
    INTEGRITY_DISCARDCONFLICTS_PARAMS = "/integrity/discardconflicts/{params}"
    INTEGRITY_FIXCONFLICTS_PARAMS = "/integrity/fixconflicts/{params}"
    INTEGRITY__FIXCONFLICTSFROMREMOTE = "/integrity/_fixconflictsfromremote"
    INTEGRITY__GENERATEINTEGRITYDATA = "/integrity/_generateintegritydata"
    INTEGRITY_REQUEST_ID_INTEGRITY_DATA = "/integrity/{requestId}/integrityData"
    INTEGRITY_GET_INTEGRITY_RESULT_PARAMS = "/integrity/getIntegrityResult/{params}"
    PORTLET_LAYOUT_PARAMS = "/portlet/layout/{params}"
    PORTLET_PARAMS = "/portlet/{params}"
    LICENSE_APPLY_LICENSE = "/license/applyLicense"
    LICENSE_DELETE_PARAMS = "/license/delete/{params}"
    LICENSE_FREE_PARAMS = "/license/free/{params}"
    LICENSE_ALL_PARAMS = "/license/all/{params}"
    LICENSE_PICK_PARAMS = "/license/pick/{params}"
    LICENSE_UPLOAD_PARAMS = "/license/upload/{params}"
    LICENSE_REQUEST_CODE_PARAMS = "/license/requestCode/{params}"
    LICENSE_RESET_LICENSE_PARAMS = "/license/resetLicense/{params}"
    OSGI_GET_INSTALLED_BUNDLES_PARAMS = "/osgi/getInstalledBundles/{params}"
    OSGI__PROCESS_EXPORTS_BUNDLE = "/osgi/_processExports/{bundle}"
    OSGI = "/osgi"
    V1_PUBLISHQUEUE = "/v1/publishqueue"
    RESTEXAMPLE_LAYOUT_PARAMS = "/restexample/layout/{params}"
    RESTEXAMPLE_TEST_PARAMS = "/restexample/test/{params}"
    ROLE_LOADBYID_PARAMS = "/role/loadbyid/{params}"
    ROLE_LOADBYNAME_PARAMS = "/role/loadbyname/{params}"
    ROLE_LOADCHILDREN_PARAMS = "/role/loadchildren/{params}"
    RULESENGINE_LAYOUT_PARAMS = "/rulesengine/layout/{params}"
    STRUCTURE_PATH = "/structure/{path}"
    V1_TAGS = "/v1/tags"
    V1_TAGS_TAG_ID = "/v1/tags/{tagId}"
    V1_TAGS_INODE_INODE = "/v1/tags/inode/{inode}"
    V1_TAGS_NAME_OR_ID = "/v1/tags/{nameOrId}"
    V1_TAGS_USER_USER_ID = "/v1/tags/user/{userId}"
    V1_TAGS_IMPORT = "/v1/tags/import"
    V1_TAGS_TAG_NAME_OR_ID_INODE_INODE = "/v1/tags/tag/{nameOrId}/inode/{inode}"
    TEST_RESOURCE_TEST_GET_PARAMS = "/testResource/testGet/{params}"
    TEST_RESOURCE_TEST_POST = "/testResource/testPost"
    USER_GETLOGGEDINUSER_PARAMS = "/user/getloggedinuser/{params}"
    UTIL_ENCODE_QUERY_PARAM_VALUE_PARAMS = "/util/encodeQueryParamValue/{params}"
    WIDGET_PARAMS = "/widget/{params}"
    V1_APPS = "/v1/apps"
    V1_APPS_KEY_SITE_ID = "/v1/apps/{key}/{siteId}"
    V1_APPS_KEY = "/v1/apps/{key}"
    V1_APPS_EXPORT = "/v1/apps/export"
    V1_APPS_IMPORT = "/v1/apps/import"
    V1_APITOKEN_TOKEN_ID = "/v1/apitoken/{tokenId}"
    V1_APITOKEN_USER_ID_TOKENS = "/v1/apitoken/{userId}/tokens"
    V1_APITOKEN_TOKEN_ID_JWT = "/v1/apitoken/{tokenId}/jwt"
    V1_APITOKEN_REMOTE = "/v1/apitoken/remote"
    V1_APITOKEN = "/v1/apitoken"
    V1_APITOKEN_TOKEN_ID_REVOKE = "/v1/apitoken/{tokenId}/revoke"
    V1_APITOKEN_USERS_USERID_REVOKE = "/v1/apitoken/users/{userid}/revoke"
    V1_APITOKEN_USERS_REVOKE = "/v1/apitoken/users/revoke"
    V1_AUTHENTICATION = "/v1/authentication"
    V1_AUTHENTICATION_LOG_IN_USER = "/v1/authentication/logInUser"
    V1_AUTHENTICATION_APITOKEN = "/v1/authentication/api-token"
    V1_FORGOTPASSWORD = "/v1/forgotpassword"
    V1_LOGINFORM = "/v1/loginform"
    V1_LOGOUT = "/v1/logout"
    V1_CHANGE_PASSWORD = "/v1/changePassword"
    V1_BROWSER = "/v1/browser"
    V1_BROWSER_SELECTEDFOLDER = "/v1/browser/selectedfolder"
    V1_BROWSERTREE_SITENAME_SITENAME_URI = "/v1/browsertree/sitename/{sitename}/uri"
    V1_BROWSERTREE_SITENAME_SITENAME_URI_URI = "/v1/browsertree/sitename/{sitename}/uri/{uri}"
    V1_CATEGORIES = "/v1/categories"
    V1_CATEGORIES__EXPORT = "/v1/categories/_export"
    V1_CATEGORIES_ID_OR_KEY = "/v1/categories/{idOrKey}"
    V1_CATEGORIES_CHILDREN = "/v1/categories/children"
    V1_CATEGORIES__IMPORT = "/v1/categories/_import"
    V1_CATEGORIES__SORT = "/v1/categories/_sort"
    V1_CONTAINERS__ARCHIVE = "/v1/containers/_archive"
    V1_CONTAINERS__BULKARCHIVE = "/v1/containers/_bulkarchive"
    V1_CONTAINERS__BULKDELETE = "/v1/containers/_bulkdelete"
    V1_CONTAINERS__BULKPUBLISH = "/v1/containers/_bulkpublish"
    V1_CONTAINERS__BULKUNARCHIVE = "/v1/containers/_bulkunarchive"
    V1_CONTAINERS__BULKUNPUBLISH = "/v1/containers/_bulkunpublish"
    V1_CONTAINERS_CONTAINER_ID_CONTENT_CONTENTLET_ID = "/v1/containers/{containerId}/content/{contentletId}"
    V1_CONTAINERS_CONTENT_CONTENTLET_ID = "/v1/containers/content/{contentletId}"
    V1_CONTAINERS_CONTAINER_ID_FORM_FORM_ID = "/v1/containers/{containerId}/form/{formId}"
    V1_CONTAINERS_FORM_FORM_ID = "/v1/containers/form/{formId}"
    V1_CONTAINERS_ID__COPY = "/v1/containers/{id}/_copy"
    V1_CONTAINERS = "/v1/containers"
    V1_CONTAINERS_LIVE = "/v1/containers/live"
    V1_CONTAINERS_WORKING = "/v1/containers/working"
    V1_CONTAINERS__PUBLISH = "/v1/containers/_publish"
    V1_CONTAINERS_DELETE_CONTAINER_ID_CONTENT_CONTENTLET_ID_UID_UID = "/v1/containers/delete/{containerId}/content/{contentletId}/uid/{uid}"
    V1_CONTAINERS__UNARCHIVE = "/v1/containers/_unarchive"
    V1_CONTAINERS__UNPUBLISH = "/v1/containers/_unpublish"
    V1_CONTENTRELATIONSHIPS_PARAMS = "/v1/contentrelationships/{params}"
    V1_CONTENT__CANLOCK_INODE_OR_IDENTIFIER = "/v1/content/_canlock/{inodeOrIdentifier}"
    V1_CONTENT_INODE_OR_IDENTIFIER = "/v1/content/{inodeOrIdentifier}"
    V1_CONTENT_RELATED = "/v1/content/related"
    V1_CONTENT_VERSIONS_INODE = "/v1/content/versions/{inode}"
    V1_CONTENT_VERSIONS = "/v1/content/versions"
    V1_CONTENT_RESOURCELINKS_FIELD_FIELD = "/v1/content/resourcelinks/field/{field}"
    V1_CONTENT_RESOURCELINKS = "/v1/content/resourcelinks"
    V1_CONTENTTYPE_BASE_VARIABLE_NAME__COPY = "/v1/contenttype/{baseVariableName}/_copy"
    V1_CONTENTTYPE = "/v1/contenttype"
    V1_CONTENTTYPE_ID_ID_OR_VAR = "/v1/contenttype/id/{idOrVar}"
    V1_CONTENTTYPE__FILTER = "/v1/contenttype/_filter"
    V1_CONTENTTYPE_BASETYPES = "/v1/contenttype/basetypes"
    V1_CONTENTTYPE_TYPE_ID_FIELDS = "/v1/contenttype/{typeId}/fields"
    V1_CONTENTTYPE_TYPE_ID_FIELDS_ID_FIELD_ID = "/v1/contenttype/{typeId}/fields/id/{fieldId}"
    V1_CONTENTTYPE_TYPE_ID_FIELDS_VAR_FIELD_VAR = "/v1/contenttype/{typeId}/fields/var/{fieldVar}"
    V1_CONTENTTYPE_TYPE_ID_FIELDS_ID_FIELD_ID_VARIABLES = "/v1/contenttype/{typeId}/fields/id/{fieldId}/variables"
    V1_CONTENTTYPE_TYPE_ID_FIELDS_VAR_FIELD_VAR_VARIABLES = "/v1/contenttype/{typeId}/fields/var/{fieldVar}/variables"
    V1_CONTENTTYPE_TYPE_ID_FIELDS_ID_FIELD_ID_VARIABLES_ID_FIELD_VAR_ID = "/v1/contenttype/{typeId}/fields/id/{fieldId}/variables/id/{fieldVarId}"
    V1_CONTENTTYPE_TYPE_ID_FIELDS_VAR_FIELD_VAR_VARIABLES_ID_FIELD_VAR_ID = "/v1/contenttype/{typeId}/fields/var/{fieldVar}/variables/id/{fieldVarId}"
    WS_V1_SYSTEM_EVENTS = "/ws/v1/system/events"
    WS_V1_SYSTEM_SYNCEVENTS = "/ws/v1/system/syncevents"
    V1_EXPERIMENTS_EXPERIMENT_ID_VARIANTS = "/v1/experiments/{experimentId}/variants"
    V1_EXPERIMENTS_EXPERIMENT_ID__ARCHIVE = "/v1/experiments/{experimentId}/_archive"
    V1_EXPERIMENTS = "/v1/experiments"
    V1_EXPERIMENTS_EXPERIMENT_ID = "/v1/experiments/{experimentId}"
    V1_EXPERIMENTS_EXPERIMENT_ID_GOALS_PRIMARY = "/v1/experiments/{experimentId}/goals/primary"
    V1_EXPERIMENTS_EXPERIMENT_ID_TARGETING_CONDITIONS_ID = "/v1/experiments/{experimentId}/targetingConditions/{id}"
    V1_EXPERIMENTS_EXPERIMENT_ID_VARIANTS_NAME = "/v1/experiments/{experimentId}/variants/{name}"
    V1_EXPERIMENTS_EXPERIMENT_ID__END = "/v1/experiments/{experimentId}/_end"
    V1_EXPERIMENTS_ID = "/v1/experiments/{id}"
    V1_EXPERIMENTS_IS_USER_INCLUDED = "/v1/experiments/isUserIncluded"
    V1_EXPERIMENTS_EXPERIMENT_ID__START = "/v1/experiments/{experimentId}/_start"
    V1_CONTENT_FILEASSETS_INODE_RESOURCELINK = "/v1/content/fileassets/{inode}/resourcelink"
    V1_FOLDER_CREATEFOLDERS_SITE_NAME = "/v1/folder/createfolders/{siteName}"
    V1_FOLDER_SITE_NAME = "/v1/folder/{siteName}"
    V1_FOLDER_FOLDER_ID = "/v1/folder/{folderId}"
    V1_FOLDER_BY_PATH = "/v1/folder/byPath"
    V1_FOLDER_SITE_ID_SITE_ID_PATH_PATH = "/v1/folder/siteId/{siteId}/path/{path}"
    V1_FOLDER_SITENAME_SITE_NAME_URI_URI = "/v1/folder/sitename/{siteName}/uri/{uri}"
    V1_FOLDER_ID_FILEBROWSERSELECTED = "/v1/folder/{id}/file-browser-selected"
    V1_FORM_ID_OR_VAR_SUCCESS_CALLBACK = "/v1/form/{idOrVar}/successCallback"
    V1_ESINDEX_ACTIVATE_PARAMS = "/v1/esindex/activate/{params}"
    V1_ESINDEX_CLEAR_PARAMS = "/v1/esindex/clear/{params}"
    V1_ESINDEX_CLOSE_PARAMS = "/v1/esindex/close/{params}"
    V1_ESINDEX_CREATE_PARAMS = "/v1/esindex/create/{params}"
    V1_ESINDEX_DEACTIVATE_PARAMS = "/v1/esindex/deactivate/{params}"
    V1_ESINDEX_FAILED = "/v1/esindex/failed"
    V1_ESINDEX_INDEX_NAME = "/v1/esindex/{indexName}"
    V1_ESINDEX_CACHE = "/v1/esindex/cache"
    V1_ESINDEX_ACTIVE_PARAMS = "/v1/esindex/active/{params}"
    V1_ESINDEX_CLUSTER = "/v1/esindex/cluster"
    V1_ESINDEX = "/v1/esindex"
    V1_ESINDEX_REINDEX = "/v1/esindex/reindex"
    V1_ESINDEX_INDEXLIST_PARAMS = "/v1/esindex/indexlist/{params}"
    V1_ESINDEX_OPEN_PARAMS = "/v1/esindex/open/{params}"
    V1_ESINDEX_OPTIMIZE = "/v1/esindex/optimize"
    V1_LANGUAGES_I18N = "/v1/languages/i18n"
    V1_LANGUAGES = "/v1/languages"
    V1_JVM = "/v1/jvm"
    V1_MAINTENANCE__DOWNLOAD_ASSETS = "/v1/maintenance/_downloadAssets"
    V1_MAINTENANCE__DOWNLOAD_DB = "/v1/maintenance/_downloadDb"
    V1_MAINTENANCE__DOWNLOAD_LOG_FILE_NAME = "/v1/maintenance/_downloadLog/{fileName}"
    V1_MAINTENANCE__DOWNLOAD_STARTER = "/v1/maintenance/_downloadStarter"
    V1_MAINTENANCE__DOWNLOAD_STARTER_WITH_ASSETS = "/v1/maintenance/_downloadStarterWithAssets"
    V1_MAINTENANCE__PG_DUMP_AVAILABLE = "/v1/maintenance/_pgDumpAvailable"
    V1_MAINTENANCE__SHUTDOWN = "/v1/maintenance/_shutdown"
    V1_MENU = "/v1/menu"
    V1_NOTIFICATION_DELETE = "/v1/notification/delete"
    V1_NOTIFICATION_ID_ID = "/v1/notification/id/{id}"
    V1_NOTIFICATION_GET_NEW_NOTIFICATIONS_COUNT = "/v1/notification/getNewNotificationsCount"
    V1_NOTIFICATION_GET_NOTIFICATIONS_PARAMS = "/v1/notification/getNotifications/{params}"
    V1_NOTIFICATION_MARK_AS_READ = "/v1/notification/markAsRead"
    V1_NAV_URI = "/v1/nav/{uri}"
    V1_PAGE_PAGE_ID_CONTENT = "/v1/page/{pageId}/content"
    V1_PAGE_COPY_CONTENT = "/v1/page/copyContent"
    V1_PAGE_PAGE_ID__DEEPCOPY = "/v1/page/{pageId}/_deepcopy"
    V1_PAGE_PAGE_ID_CONTENT_TREE = "/v1/page/{pageId}/content/tree"
    V1_PAGE_PAGE_ID_RENDER_VERSIONS = "/v1/page/{pageId}/render/versions"
    V1_PAGE_PAGE_ID_PERSONAS = "/v1/page/{pageId}/personas"
    V1_PAGE_JSON_URI = "/v1/page/json/{uri}"
    V1_PAGE_RENDER_URI = "/v1/page/render/{uri}"
    V1_PAGE_RENDER_HTML_URI = "/v1/page/renderHTML/{uri}"
    V1_PAGE_LAYOUT = "/v1/page/layout"
    V1_PAGE_PAGE_ID_LAYOUT = "/v1/page/{pageId}/layout"
    V1_PAGE_SEARCH = "/v1/page/search"
    V1_PERSONALIZATION_PAGEPERSONAS = "/v1/personalization/pagepersonas"
    V1_PERSONALIZATION_PAGEPERSONAS_PAGE_PAGE_ID_PERSONALIZATION_PERSONALIZATION = "/v1/personalization/pagepersonas/page/{pageId}/personalization/{personalization}"
    V1_PERSONAS = "/v1/personas"
    V1_PERSONAS_ID = "/v1/personas/{id}"
    V1_PORTLET_CUSTOM_PORTLET_ID__ADDTOLAYOUT_LAYOUT_ID = "/v1/portlet/custom/{portletId}/_addtolayout/{layoutId}"
    V1_PORTLET_CUSTOM = "/v1/portlet/custom"
    V1_PORTLET_CUSTOM_PORTLET_ID = "/v1/portlet/custom/{portletId}"
    V1_PORTLET_PORTLET_ID_PORTLET_ID = "/v1/portlet/portletId/{portletId}"
    V1_PORTLET_PORTLET_ID_PORTLET_ID_ROLE_ID_ROLE_ID = "/v1/portlet/portletId/{portletId}/roleId/{roleId}"
    V1_PORTLET_PORTLET_ID__DOESUSERHAVEACCESS = "/v1/portlet/{portletId}/_doesuserhaveaccess"
    V1_PORTLET_PORTLET_ID = "/v1/portlet/{portletId}"
    V1_PORTLET__ACTIONURL_CONTENT_TYPE_VARIABLE = "/v1/portlet/_actionurl/{contentTypeVariable}"
    V1_TOOLGROUPS_LAYOUT_ID__ADDTOUSER = "/v1/toolgroups/{layoutId}/_addtouser"
    V1_TOOLGROUPS_LAYOUT_ID__REMOVEFROMUSER = "/v1/toolgroups/{layoutId}/_removefromuser"
    V1_TOOLGROUPS_LAYOUT_ID__USER_HAS_LAYOUT = "/v1/toolgroups/{layoutId}/_userHasLayout"
    V1_PUSHPUBLISH_FILTERS_FILTER_KEY = "/v1/pushpublish/filters/{filterKey}"
    V1_PUSHPUBLISH_FILTERS = "/v1/pushpublish/filters"
    V1_RELATIONSHIPS_CARDINALITIES = "/v1/relationships/cardinalities"
    V1_RELATIONSHIPS = "/v1/relationships"
    V1_SITE_SITE_ID__ARCHIVE = "/v1/site/{siteId}/_archive"
    V1_SITE__COPY = "/v1/site/_copy"
    V1_SITE = "/v1/site"
    V1_SITE_CURRENT_SITE = "/v1/site/currentSite"
    V1_SITE_DEFAULT_SITE = "/v1/site/defaultSite"
    V1_SITE_SITE_ID = "/v1/site/{siteId}"
    V1_SITE_THUMBNAILS = "/v1/site/thumbnails"
    V1_SITE__BYNAME = "/v1/site/_byname"
    V1_SITE_SITE_ID_SETUP_PROGRESS = "/v1/site/{siteId}/setup_progress"
    V1_SITE_VARIABLE_SITE_ID = "/v1/site/variable/{siteId}"
    V1_SITE_SITE_ID__MAKEDEFAULT = "/v1/site/{siteId}/_makedefault"
    V1_SITE_SITE_ID__PUBLISH = "/v1/site/{siteId}/_publish"
    V1_SITE_VARIABLE = "/v1/site/variable"
    V1_SITE_SWITCH = "/v1/site/switch"
    V1_SITE_SWITCH_ID = "/v1/site/switch/{id}"
    V1_SITE_SITE_ID__UNARCHIVE = "/v1/site/{siteId}/_unarchive"
    V1_SITE_SITE_ID__UNPUBLISH = "/v1/site/{siteId}/_unpublish"
    V1_SITES_SITE_ID_RULEENGINE_RULES = "/v1/sites/{siteId}/ruleengine/rules"
    V1_SITES_SITE_ID_RULEENGINE_RULES_RULE_ID = "/v1/sites/{siteId}/ruleengine/rules/{ruleId}"
    V1_SITES_SITE_ID_RULEENGINE_ACTIONS = "/v1/sites/{siteId}/ruleengine/actions"
    V1_SITES_SITE_ID_RULEENGINE_ACTIONS_ACTION_ID = "/v1/sites/{siteId}/ruleengine/actions/{actionId}"
    V1_SITES_SITE_ID_RULEENGINE_RULES_RULE_ID_CONDITION_GROUPS = "/v1/sites/{siteId}/ruleengine/rules/{ruleId}/conditionGroups"
    V1_SITES_SITE_ID_RULEENGINE_RULES_RULE_ID_CONDITION_GROUPS_CONDITION_GROUP_ID = "/v1/sites/{siteId}/ruleengine/rules/{ruleId}/conditionGroups/{conditionGroupId}"
    V1_SITES_SITE_ID_RULEENGINE_RULES_RULE_ID_CONDITION_GROUPS_GROUP_ID = "/v1/sites/{siteId}/ruleengine/rules/{ruleId}/conditionGroups/{groupId}"
    V1_SITES_SITE_ID_RULEENGINE_CONDITIONS = "/v1/sites/{siteId}/ruleengine/conditions"
    V1_SITES_SITE_ID_RULEENGINE_CONDITIONS_CONDITION_ID = "/v1/sites/{siteId}/ruleengine/conditions/{conditionId}"
    V1_SITES_SITE_ID_RULEENGINE_CONDITIONS_CONDITION_ID_CONDITION_VALUES = "/v1/sites/{siteId}/ruleengine/conditions/{conditionId}/conditionValues"
    V1_SITES_SITE_ID_RULEENGINE_CONDITIONS_CONDITION_ID_CONDITION_VALUES_VALUE_ID = "/v1/sites/{siteId}/ruleengine/conditions/{conditionId}/conditionValues/{valueId}"
    V1_APPCONFIGURATION = "/v1/appconfiguration"
    V1_CONFIGURATION_CONFIG = "/v1/configuration/config"
    V1_CONFIGURATION = "/v1/configuration"
    V1_CONFIGURATION__VALIDATE_COMPANY_EMAIL = "/v1/configuration/_validateCompanyEmail"
    V1_UPGRADETASK = "/v1/upgradetask"
    V1_CACHES_PROVIDER_PROVIDER_FLUSH = "/v1/caches/provider/{provider}/flush"
    V1_CACHES_PROVIDER_PROVIDER_FLUSH_GROUP = "/v1/caches/provider/{provider}/flush/{group}"
    V1_CACHES_PROVIDER_PROVIDER_FLUSH_GROUP_ID = "/v1/caches/provider/{provider}/flush/{group}/{id}"
    V1_CACHES_PROVIDER_PROVIDER_KEYS_GROUP = "/v1/caches/provider/{provider}/keys/{group}"
    V1_CACHES_PROVIDER_PROVIDER_OBJECT_GROUP_ID = "/v1/caches/provider/{provider}/object/{group}/{id}"
    V1_CACHES_PROVIDER_PROVIDER_OBJECTS_GROUP = "/v1/caches/provider/{provider}/objects/{group}"
    V1_CACHES_PROVIDERS_GROUP = "/v1/caches/providers/{group}"
    V1_CACHES_PROVIDER_PROVIDER_GROUP = "/v1/caches/provider/{provider}/{group}"
    V1_SYSTEM_I18N_LANG_RSRC = "/v1/system/i18n/{lang}/{rsrc}"
    V1_LOGGER = "/v1/logger"
    V1_LOGGER_LOGGER_NAME = "/v1/logger/{loggerName}"
    V1_SYSTEMSTATUS_ALIVE = "/v1/system-status/alive"
    V1_SYSTEMSTATUS = "/v1/system-status"
    V1_PERMISSIONS__BYCONTENT = "/v1/permissions/_bycontent"
    V1_PERMISSIONS__BYPERMISSIONTYPE = "/v1/permissions/_bypermissiontype"
    V1_REDIS_KEY = "/v1/redis/{key}"
    V1_REDIS_HASH_KEY = "/v1/redis/hash/{key}"
    V1_REDIS_ECHO_MESSAGE = "/v1/redis/echo/{message}"
    V1_REDIS_INCR_KEY = "/v1/redis/incr/{key}"
    V1_REDIS_PING = "/v1/redis/ping"
    V1_REDIS = "/v1/redis"
    V1_REDIS_HASH = "/v1/redis/hash"
    V1_ROLES_CHECKUSERROLES_USERID_USER_ID_ROLEIDS_ROLE_IDS = "/v1/roles/checkuserroles/userid/{userId}/roleids/{roleIds}"
    V1_ROLES_LAYOUTS = "/v1/roles/layouts"
    V1_ROLES_ROLE_ID_LAYOUTS = "/v1/roles/{roleId}/layouts"
    V1_ROLES_ROLEID = "/v1/roles/{roleid}"
    V1_ROLES = "/v1/roles"
    V1_ROLES_ROLEID_ROLEHIERARCHYANDUSERROLES = "/v1/roles/{roleid}/rolehierarchyanduserroles"
    V1_ROLES__SEARCH = "/v1/roles/_search"
    V1_SYSTEM_RULEENGINE_ACTIONLETS = "/v1/system/ruleengine/actionlets"
    V1_SYSTEM_RULEENGINE_CONDITIONLETS = "/v1/system/ruleengine/conditionlets"
    V1_LOGS_FILE_NAME__TAIL = "/v1/logs/{fileName}/_tail"
    V1_TEMP_BY_URL = "/v1/temp/byUrl"
    V1_TEMP = "/v1/temp"
    V1_TEMPLATES__ARCHIVE = "/v1/templates/_archive"
    V1_TEMPLATES_TEMPLATE_ID__COPY = "/v1/templates/{templateId}/_copy"
    V1_TEMPLATES = "/v1/templates"
    V1_TEMPLATES_TEMPLATE_ID_LIVE = "/v1/templates/{templateId}/live"
    V1_TEMPLATES_TEMPLATE_ID_WORKING = "/v1/templates/{templateId}/working"
    V1_TEMPLATES__PUBLISH = "/v1/templates/_publish"
    V1_TEMPLATES__SAVEPUBLISH = "/v1/templates/_savepublish"
    V1_TEMPLATES_DRAFT = "/v1/templates/draft"
    V1_TEMPLATES__UNARCHIVE = "/v1/templates/_unarchive"
    V1_TEMPLATES__UNPUBLISH = "/v1/templates/_unpublish"
    V1_THEMES_ID_ID = "/v1/themes/id/{id}"
    V1_THEMES = "/v1/themes"
    V1_USERS_FILTER_PARAMS = "/v1/users/filter/{params}"
    V1_USERS_LOGINAS = "/v1/users/loginas"
    V1_USERS_LOGIN_AS_DATA = "/v1/users/loginAsData"
    V1_USERS_LOGOUTAS = "/v1/users/logoutas"
    V1_USERS_CURRENT = "/v1/users/current"
    V1_VERSIONABLES_VERSIONABLE_INODE__BRINGBACK = "/v1/versionables/{versionableInode}/_bringback"
    V1_VERSIONABLES_VERSIONABLE_INODE = "/v1/versionables/{versionableInode}"
    V1_VERSIONABLES_VERSIONABLE_INODE_OR_IDENTIFIER = "/v1/versionables/{versionableInodeOrIdentifier}"
    VTL_FOLDER = "/vtl/{folder}"
    VTL_FOLDER_PATH_PARAM = "/vtl/{folder}/{pathParam}"
    VTL_DYNAMIC_PATH_PARAM = "/vtl/dynamic/{pathParam}"
    VTL_DYNAMIC = "/vtl/dynamic"
    V1_WORKFLOW_STEPS = "/v1/workflow/steps"
    V1_WORKFLOW_SCHEMES_SCHEME_ID_COPY = "/v1/workflow/schemes/{schemeId}/copy"
    V1_WORKFLOW_ACTIONS_ACTION_ID = "/v1/workflow/actions/{actionId}"
    V1_WORKFLOW_STEPS_STEP_ID_ACTIONS_ACTION_ID = "/v1/workflow/steps/{stepId}/actions/{actionId}"
    V1_WORKFLOW_ACTIONLETS_ACTIONLET_ID = "/v1/workflow/actionlets/{actionletId}"
    V1_WORKFLOW_SCHEMES_SCHEME_ID = "/v1/workflow/schemes/{schemeId}"
    V1_WORKFLOW_STEPS_STEP_ID = "/v1/workflow/steps/{stepId}"
    V1_WORKFLOW_SYSTEM_ACTIONS_IDENTIFIER = "/v1/workflow/system/actions/{identifier}"
    V1_WORKFLOW_ACTIONS_ACTION_ID_CONDITION = "/v1/workflow/actions/{actionId}/condition"
    V1_WORKFLOW_SCHEMES_SCHEME_ID_EXPORT = "/v1/workflow/schemes/{schemeId}/export"
    V1_WORKFLOW_ACTIONLETS = "/v1/workflow/actionlets"
    V1_WORKFLOW_ACTIONS_ACTION_ID_ACTIONLETS = "/v1/workflow/actions/{actionId}/actionlets"
    V1_WORKFLOW_SCHEMES_SCHEME_ID_ACTIONS = "/v1/workflow/schemes/{schemeId}/actions"
    V1_WORKFLOW_SCHEMES_ACTIONS_SYSTEM_ACTION = "/v1/workflow/schemes/actions/{systemAction}"
    V1_WORKFLOW_STEPS_STEP_ID_ACTIONS = "/v1/workflow/steps/{stepId}/actions"
    V1_WORKFLOW_SCHEMES_SCHEMESCONTENTTYPES_CONTENT_TYPE_ID = "/v1/workflow/schemes/schemescontenttypes/{contentTypeId}"
    V1_WORKFLOW_CONTENTLET_INODE_ACTIONS = "/v1/workflow/contentlet/{inode}/actions"
    V1_WORKFLOW_DEFAULTACTIONS_CONTENTTYPE_CONTENT_TYPE_ID = "/v1/workflow/defaultactions/contenttype/{contentTypeId}"
    V1_WORKFLOW_DEFAULTACTIONS_SCHEMES = "/v1/workflow/defaultactions/schemes"
    V1_WORKFLOW_INITIALACTIONS_CONTENTTYPE_CONTENT_TYPE_ID = "/v1/workflow/initialactions/contenttype/{contentTypeId}"
    V1_WORKFLOW_SCHEMES = "/v1/workflow/schemes"
    V1_WORKFLOW_SCHEMES_SCHEME_ID_STEPS = "/v1/workflow/schemes/{schemeId}/steps"
    V1_WORKFLOW_CONTENTTYPES_CONTENT_TYPE_VAR_OR_ID_SYSTEM_ACTIONS = "/v1/workflow/contenttypes/{contentTypeVarOrId}/system/actions"
    V1_WORKFLOW_SCHEMES_SCHEME_ID_SYSTEM_ACTIONS = "/v1/workflow/schemes/{schemeId}/system/actions"
    V1_WORKFLOW_ACTIONS_FIRE = "/v1/workflow/actions/fire"
    V1_WORKFLOW_ACTIONS_DEFAULT_FIRE_SYSTEM_ACTION = "/v1/workflow/actions/default/fire/{systemAction}"
    V1_WORKFLOW_ACTIONS_DEFAULT_FIREMULTIPART_SYSTEM_ACTION = "/v1/workflow/actions/default/firemultipart/{systemAction}"
    V1_WORKFLOW_ACTIONS_ACTION_ID_FIRE = "/v1/workflow/actions/{actionId}/fire"
    V1_WORKFLOW_ACTIONS_ACTION_ID_FIREMULTIPART = "/v1/workflow/actions/{actionId}/firemultipart"
    V1_WORKFLOW_CONTENTLET_ACTIONS__BULKFIRE = "/v1/workflow/contentlet/actions/_bulkfire"
    V1_WORKFLOW_CONTENTLET_ACTIONS_BULK_FIRE = "/v1/workflow/contentlet/actions/bulk/fire"
    V1_WORKFLOW_CONTENTLET_ACTIONS_BULK = "/v1/workflow/contentlet/actions/bulk"
    V1_WORKFLOW_SYSTEM_ACTIONS_WORKFLOW_ACTION_ID = "/v1/workflow/system/actions/{workflowActionId}"
    V1_WORKFLOW_SCHEMES_IMPORT = "/v1/workflow/schemes/import"
    V1_WORKFLOW_REORDER_STEPS_STEP_ID_ACTIONS_ACTION_ID = "/v1/workflow/reorder/steps/{stepId}/actions/{actionId}"
    V1_WORKFLOW_REORDER_STEP_STEP_ID_ORDER_ORDER = "/v1/workflow/reorder/step/{stepId}/order/{order}"
    V1_WORKFLOW_ACTIONS = "/v1/workflow/actions"
    V1_WORKFLOW_SYSTEM_ACTIONS = "/v1/workflow/system/actions"
    V2_CONTENTTYPE_TYPE_ID_OR_VAR_NAME_FIELDS = "/v2/contenttype/{typeIdOrVarName}/fields"
    V2_CONTENTTYPE_TYPE_ID_OR_VAR_NAME_FIELDS_ID_FIELD_ID = "/v2/contenttype/{typeIdOrVarName}/fields/id/{fieldId}"
    V2_CONTENTTYPE_TYPE_ID_OR_VAR_NAME_FIELDS_VAR_FIELD_VAR = "/v2/contenttype/{typeIdOrVarName}/fields/var/{fieldVar}"
    V2_LANGUAGES_LANGUAGE_ID = "/v2/languages/{languageId}"
    V2_LANGUAGES_ID_LANGUAGEID = "/v2/languages/id/{languageid}"
    V2_LANGUAGES_LANGUAGE_KEYS = "/v2/languages/{language}/keys"
    V2_LANGUAGES_LANGUAGE_TAG = "/v2/languages/{languageTag}"
    V2_LANGUAGES_I18N = "/v2/languages/i18n"
    V2_LANGUAGES = "/v2/languages"
    V2_LANGUAGES_LANGUAGE__MAKEDEFAULT = "/v2/languages/{language}/_makedefault"
    V3_CONTENTTYPE_TYPE_ID_OR_VAR_NAME_FIELDS = "/v3/contenttype/{typeIdOrVarName}/fields"
    V3_CONTENTTYPE_TYPE_ID_OR_VAR_NAME_FIELDS_MOVE = "/v3/contenttype/{typeIdOrVarName}/fields/move"
    V3_CONTENTTYPE_TYPE_ID_OR_VAR_NAME_FIELDS_ID = "/v3/contenttype/{typeIdOrVarName}/fields/{id}"
    ES_LAYOUT_PARAMS = "/es/layout/{params}"
    ES_SEARCH = "/es/search"
    ES_RAW = "/es/raw"
    PERSONAS_LAYOUT_PARAMS = "/personas/layout/{params}"
    PERSONAS_SITES_ID = "/personas/sites/{id}"
    APPLICATION_WADL_PATH = "/application.wadl/{path}"
    APPLICATION_WADL = "/application.wadl"
