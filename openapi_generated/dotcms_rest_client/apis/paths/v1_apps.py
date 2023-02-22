from dotcms_rest_client.paths.v1_apps.get import ApiForget
from dotcms_rest_client.paths.v1_apps.post import ApiForpost
from dotcms_rest_client.paths.v1_apps.delete import ApiFordelete


class V1Apps(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
