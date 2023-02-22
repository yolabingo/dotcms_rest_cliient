# coding: utf-8

"""
    dotCMS REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from dotcms_rest_client import schemas  # noqa: F401


class AdditionalParamsBean(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def pushPublish() -> typing.Type['PushPublishBean']:
                return PushPublishBean
        
            @staticmethod
            def assignComment() -> typing.Type['AssignCommentBean']:
                return AssignCommentBean
            
            
            class additionalParamsMap(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.DictSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, ],
                ) -> 'additionalParamsMap':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def pushPublishBean() -> typing.Type['PushPublishBean']:
                return PushPublishBean
        
            @staticmethod
            def assignCommentBean() -> typing.Type['AssignCommentBean']:
                return AssignCommentBean
            __annotations__ = {
                "pushPublish": pushPublish,
                "assignComment": assignComment,
                "additionalParamsMap": additionalParamsMap,
                "pushPublishBean": pushPublishBean,
                "assignCommentBean": assignCommentBean,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pushPublish"]) -> 'PushPublishBean': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignComment"]) -> 'AssignCommentBean': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additionalParamsMap"]) -> MetaOapg.properties.additionalParamsMap: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pushPublishBean"]) -> 'PushPublishBean': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignCommentBean"]) -> 'AssignCommentBean': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pushPublish", "assignComment", "additionalParamsMap", "pushPublishBean", "assignCommentBean", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pushPublish"]) -> typing.Union['PushPublishBean', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignComment"]) -> typing.Union['AssignCommentBean', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additionalParamsMap"]) -> typing.Union[MetaOapg.properties.additionalParamsMap, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pushPublishBean"]) -> typing.Union['PushPublishBean', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignCommentBean"]) -> typing.Union['AssignCommentBean', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pushPublish", "assignComment", "additionalParamsMap", "pushPublishBean", "assignCommentBean", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        pushPublish: typing.Union['PushPublishBean', schemas.Unset] = schemas.unset,
        assignComment: typing.Union['AssignCommentBean', schemas.Unset] = schemas.unset,
        additionalParamsMap: typing.Union[MetaOapg.properties.additionalParamsMap, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        pushPublishBean: typing.Union['PushPublishBean', schemas.Unset] = schemas.unset,
        assignCommentBean: typing.Union['AssignCommentBean', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AdditionalParamsBean':
        return super().__new__(
            cls,
            *_args,
            pushPublish=pushPublish,
            assignComment=assignComment,
            additionalParamsMap=additionalParamsMap,
            pushPublishBean=pushPublishBean,
            assignCommentBean=assignCommentBean,
            _configuration=_configuration,
            **kwargs,
        )

from dotcms_rest_client.model.assign_comment_bean import AssignCommentBean
from dotcms_rest_client.model.push_publish_bean import PushPublishBean
