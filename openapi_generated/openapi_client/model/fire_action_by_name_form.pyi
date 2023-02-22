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

from openapi_client import schemas  # noqa: F401


class FireActionByNameForm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            comments = schemas.StrSchema
            assign = schemas.StrSchema
            publishDate = schemas.StrSchema
            publishTime = schemas.StrSchema
            expireDate = schemas.StrSchema
            expireTime = schemas.StrSchema
            neverExpire = schemas.StrSchema
            whereToSend = schemas.StrSchema
            filterKey = schemas.StrSchema
            query = schemas.StrSchema
            pathToMove = schemas.StrSchema
            timezoneId = schemas.StrSchema
            
            
            class individualPermissions(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'additional_properties':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
                ) -> 'individualPermissions':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            actionName = schemas.StrSchema
            iwantTo = schemas.StrSchema
            
            
            class contentlet(
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
                ) -> 'contentlet':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "comments": comments,
                "assign": assign,
                "publishDate": publishDate,
                "publishTime": publishTime,
                "expireDate": expireDate,
                "expireTime": expireTime,
                "neverExpire": neverExpire,
                "whereToSend": whereToSend,
                "filterKey": filterKey,
                "query": query,
                "pathToMove": pathToMove,
                "timezoneId": timezoneId,
                "individualPermissions": individualPermissions,
                "actionName": actionName,
                "iwantTo": iwantTo,
                "contentlet": contentlet,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comments"]) -> MetaOapg.properties.comments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assign"]) -> MetaOapg.properties.assign: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publishDate"]) -> MetaOapg.properties.publishDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publishTime"]) -> MetaOapg.properties.publishTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expireDate"]) -> MetaOapg.properties.expireDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expireTime"]) -> MetaOapg.properties.expireTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["neverExpire"]) -> MetaOapg.properties.neverExpire: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["whereToSend"]) -> MetaOapg.properties.whereToSend: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filterKey"]) -> MetaOapg.properties.filterKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pathToMove"]) -> MetaOapg.properties.pathToMove: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezoneId"]) -> MetaOapg.properties.timezoneId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["individualPermissions"]) -> MetaOapg.properties.individualPermissions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actionName"]) -> MetaOapg.properties.actionName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iwantTo"]) -> MetaOapg.properties.iwantTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentlet"]) -> MetaOapg.properties.contentlet: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["comments", "assign", "publishDate", "publishTime", "expireDate", "expireTime", "neverExpire", "whereToSend", "filterKey", "query", "pathToMove", "timezoneId", "individualPermissions", "actionName", "iwantTo", "contentlet", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comments"]) -> typing.Union[MetaOapg.properties.comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assign"]) -> typing.Union[MetaOapg.properties.assign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publishDate"]) -> typing.Union[MetaOapg.properties.publishDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publishTime"]) -> typing.Union[MetaOapg.properties.publishTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expireDate"]) -> typing.Union[MetaOapg.properties.expireDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expireTime"]) -> typing.Union[MetaOapg.properties.expireTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["neverExpire"]) -> typing.Union[MetaOapg.properties.neverExpire, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["whereToSend"]) -> typing.Union[MetaOapg.properties.whereToSend, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filterKey"]) -> typing.Union[MetaOapg.properties.filterKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> typing.Union[MetaOapg.properties.query, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pathToMove"]) -> typing.Union[MetaOapg.properties.pathToMove, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezoneId"]) -> typing.Union[MetaOapg.properties.timezoneId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["individualPermissions"]) -> typing.Union[MetaOapg.properties.individualPermissions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actionName"]) -> typing.Union[MetaOapg.properties.actionName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iwantTo"]) -> typing.Union[MetaOapg.properties.iwantTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentlet"]) -> typing.Union[MetaOapg.properties.contentlet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["comments", "assign", "publishDate", "publishTime", "expireDate", "expireTime", "neverExpire", "whereToSend", "filterKey", "query", "pathToMove", "timezoneId", "individualPermissions", "actionName", "iwantTo", "contentlet", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        comments: typing.Union[MetaOapg.properties.comments, str, schemas.Unset] = schemas.unset,
        assign: typing.Union[MetaOapg.properties.assign, str, schemas.Unset] = schemas.unset,
        publishDate: typing.Union[MetaOapg.properties.publishDate, str, schemas.Unset] = schemas.unset,
        publishTime: typing.Union[MetaOapg.properties.publishTime, str, schemas.Unset] = schemas.unset,
        expireDate: typing.Union[MetaOapg.properties.expireDate, str, schemas.Unset] = schemas.unset,
        expireTime: typing.Union[MetaOapg.properties.expireTime, str, schemas.Unset] = schemas.unset,
        neverExpire: typing.Union[MetaOapg.properties.neverExpire, str, schemas.Unset] = schemas.unset,
        whereToSend: typing.Union[MetaOapg.properties.whereToSend, str, schemas.Unset] = schemas.unset,
        filterKey: typing.Union[MetaOapg.properties.filterKey, str, schemas.Unset] = schemas.unset,
        query: typing.Union[MetaOapg.properties.query, str, schemas.Unset] = schemas.unset,
        pathToMove: typing.Union[MetaOapg.properties.pathToMove, str, schemas.Unset] = schemas.unset,
        timezoneId: typing.Union[MetaOapg.properties.timezoneId, str, schemas.Unset] = schemas.unset,
        individualPermissions: typing.Union[MetaOapg.properties.individualPermissions, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        actionName: typing.Union[MetaOapg.properties.actionName, str, schemas.Unset] = schemas.unset,
        iwantTo: typing.Union[MetaOapg.properties.iwantTo, str, schemas.Unset] = schemas.unset,
        contentlet: typing.Union[MetaOapg.properties.contentlet, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FireActionByNameForm':
        return super().__new__(
            cls,
            *_args,
            comments=comments,
            assign=assign,
            publishDate=publishDate,
            publishTime=publishTime,
            expireDate=expireDate,
            expireTime=expireTime,
            neverExpire=neverExpire,
            whereToSend=whereToSend,
            filterKey=filterKey,
            query=query,
            pathToMove=pathToMove,
            timezoneId=timezoneId,
            individualPermissions=individualPermissions,
            actionName=actionName,
            iwantTo=iwantTo,
            contentlet=contentlet,
            _configuration=_configuration,
            **kwargs,
        )
