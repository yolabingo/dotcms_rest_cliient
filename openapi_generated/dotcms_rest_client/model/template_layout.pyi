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


class TemplateLayout(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            width = schemas.StrSchema
            title = schemas.StrSchema
            header = schemas.BoolSchema
            footer = schemas.BoolSchema
        
            @staticmethod
            def body() -> typing.Type['Body']:
                return Body
        
            @staticmethod
            def sidebar() -> typing.Type['Sidebar']:
                return Sidebar
            
            
            class bodyRows(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TemplateLayoutRow']:
                        return TemplateLayoutRow
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TemplateLayoutRow'], typing.List['TemplateLayoutRow']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bodyRows':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TemplateLayoutRow':
                    return super().__getitem__(i)
            __annotations__ = {
                "width": width,
                "title": title,
                "header": header,
                "footer": footer,
                "body": body,
                "sidebar": sidebar,
                "bodyRows": bodyRows,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["header"]) -> MetaOapg.properties.header: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["footer"]) -> MetaOapg.properties.footer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> 'Body': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sidebar"]) -> 'Sidebar': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bodyRows"]) -> MetaOapg.properties.bodyRows: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["width", "title", "header", "footer", "body", "sidebar", "bodyRows", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["width"]) -> typing.Union[MetaOapg.properties.width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["header"]) -> typing.Union[MetaOapg.properties.header, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["footer"]) -> typing.Union[MetaOapg.properties.footer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union['Body', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sidebar"]) -> typing.Union['Sidebar', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bodyRows"]) -> typing.Union[MetaOapg.properties.bodyRows, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["width", "title", "header", "footer", "body", "sidebar", "bodyRows", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        width: typing.Union[MetaOapg.properties.width, str, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        header: typing.Union[MetaOapg.properties.header, bool, schemas.Unset] = schemas.unset,
        footer: typing.Union[MetaOapg.properties.footer, bool, schemas.Unset] = schemas.unset,
        body: typing.Union['Body', schemas.Unset] = schemas.unset,
        sidebar: typing.Union['Sidebar', schemas.Unset] = schemas.unset,
        bodyRows: typing.Union[MetaOapg.properties.bodyRows, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplateLayout':
        return super().__new__(
            cls,
            *_args,
            width=width,
            title=title,
            header=header,
            footer=footer,
            body=body,
            sidebar=sidebar,
            bodyRows=bodyRows,
            _configuration=_configuration,
            **kwargs,
        )

from dotcms_rest_client.model.body import Body
from dotcms_rest_client.model.sidebar import Sidebar
from dotcms_rest_client.model.template_layout_row import TemplateLayoutRow
