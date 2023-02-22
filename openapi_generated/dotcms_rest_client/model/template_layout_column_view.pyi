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


class TemplateLayoutColumnView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class containers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ContainerUUID']:
                        return ContainerUUID
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ContainerUUID'], typing.List['ContainerUUID']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'containers':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ContainerUUID':
                    return super().__getitem__(i)
            width = schemas.Int32Schema
            leftOffset = schemas.Int32Schema
            styleClass = schemas.StrSchema
            __annotations__ = {
                "containers": containers,
                "width": width,
                "leftOffset": leftOffset,
                "styleClass": styleClass,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["containers"]) -> MetaOapg.properties.containers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["leftOffset"]) -> MetaOapg.properties.leftOffset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["styleClass"]) -> MetaOapg.properties.styleClass: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["containers", "width", "leftOffset", "styleClass", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["containers"]) -> typing.Union[MetaOapg.properties.containers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["width"]) -> typing.Union[MetaOapg.properties.width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["leftOffset"]) -> typing.Union[MetaOapg.properties.leftOffset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["styleClass"]) -> typing.Union[MetaOapg.properties.styleClass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["containers", "width", "leftOffset", "styleClass", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        containers: typing.Union[MetaOapg.properties.containers, list, tuple, schemas.Unset] = schemas.unset,
        width: typing.Union[MetaOapg.properties.width, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        leftOffset: typing.Union[MetaOapg.properties.leftOffset, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        styleClass: typing.Union[MetaOapg.properties.styleClass, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplateLayoutColumnView':
        return super().__new__(
            cls,
            *_args,
            containers=containers,
            width=width,
            leftOffset=leftOffset,
            styleClass=styleClass,
            _configuration=_configuration,
            **kwargs,
        )

from dotcms_rest_client.model.container_uuid import ContainerUUID
