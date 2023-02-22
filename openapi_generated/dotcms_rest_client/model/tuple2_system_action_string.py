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


class Tuple2SystemActionString(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class _1(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "NEW": "NEW",
                        "EDIT": "EDIT",
                        "PUBLISH": "PUBLISH",
                        "UNPUBLISH": "UNPUBLISH",
                        "ARCHIVE": "ARCHIVE",
                        "UNARCHIVE": "UNARCHIVE",
                        "DELETE": "DELETE",
                        "DESTROY": "DESTROY",
                    }
                
                @schemas.classproperty
                def NEW(cls):
                    return cls("NEW")
                
                @schemas.classproperty
                def EDIT(cls):
                    return cls("EDIT")
                
                @schemas.classproperty
                def PUBLISH(cls):
                    return cls("PUBLISH")
                
                @schemas.classproperty
                def UNPUBLISH(cls):
                    return cls("UNPUBLISH")
                
                @schemas.classproperty
                def ARCHIVE(cls):
                    return cls("ARCHIVE")
                
                @schemas.classproperty
                def UNARCHIVE(cls):
                    return cls("UNARCHIVE")
                
                @schemas.classproperty
                def DELETE(cls):
                    return cls("DELETE")
                
                @schemas.classproperty
                def DESTROY(cls):
                    return cls("DESTROY")
            _2 = schemas.StrSchema
            __annotations__ = {
                "_1": _1,
                "_2": _2,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_1"]) -> MetaOapg.properties._1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_2"]) -> MetaOapg.properties._2: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_1", "_2", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_1"]) -> typing.Union[MetaOapg.properties._1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_2"]) -> typing.Union[MetaOapg.properties._2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_1", "_2", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        _1: typing.Union[MetaOapg.properties._1, str, schemas.Unset] = schemas.unset,
        _2: typing.Union[MetaOapg.properties._2, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Tuple2SystemActionString':
        return super().__new__(
            cls,
            *_args,
            _1=_1,
            _2=_2,
            _configuration=_configuration,
            **kwargs,
        )
