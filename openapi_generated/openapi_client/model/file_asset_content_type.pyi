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


class FileAssetContentType(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    name = schemas.StrSchema
                    id = schemas.StrSchema
                    description = schemas.StrSchema
                    defaultType = schemas.BoolSchema
                    detailPage = schemas.StrSchema
                    fixed = schemas.BoolSchema
                    iDate = schemas.DateTimeSchema
                    system = schemas.BoolSchema
                    versionable = schemas.BoolSchema
                    multilingualable = schemas.BoolSchema
                    variable = schemas.StrSchema
                    urlMapPattern = schemas.StrSchema
                    publishDateVar = schemas.StrSchema
                    expireDateVar = schemas.StrSchema
                    modDate = schemas.DateTimeSchema
                    host = schemas.StrSchema
                    icon = schemas.StrSchema
                    sortOrder = schemas.Int32Schema
                    folder = schemas.StrSchema
                    __annotations__ = {
                        "name": name,
                        "id": id,
                        "description": description,
                        "defaultType": defaultType,
                        "detailPage": detailPage,
                        "fixed": fixed,
                        "iDate": iDate,
                        "system": system,
                        "versionable": versionable,
                        "multilingualable": multilingualable,
                        "variable": variable,
                        "urlMapPattern": urlMapPattern,
                        "publishDateVar": publishDateVar,
                        "expireDateVar": expireDateVar,
                        "modDate": modDate,
                        "host": host,
                        "icon": icon,
                        "sortOrder": sortOrder,
                        "folder": folder,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["defaultType"]) -> MetaOapg.properties.defaultType: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["detailPage"]) -> MetaOapg.properties.detailPage: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fixed"]) -> MetaOapg.properties.fixed: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["iDate"]) -> MetaOapg.properties.iDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["system"]) -> MetaOapg.properties.system: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["versionable"]) -> MetaOapg.properties.versionable: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["multilingualable"]) -> MetaOapg.properties.multilingualable: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["variable"]) -> MetaOapg.properties.variable: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["urlMapPattern"]) -> MetaOapg.properties.urlMapPattern: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["publishDateVar"]) -> MetaOapg.properties.publishDateVar: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["expireDateVar"]) -> MetaOapg.properties.expireDateVar: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["modDate"]) -> MetaOapg.properties.modDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["host"]) -> MetaOapg.properties.host: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["sortOrder"]) -> MetaOapg.properties.sortOrder: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["folder"]) -> MetaOapg.properties.folder: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "id", "description", "defaultType", "detailPage", "fixed", "iDate", "system", "versionable", "multilingualable", "variable", "urlMapPattern", "publishDateVar", "expireDateVar", "modDate", "host", "icon", "sortOrder", "folder", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["defaultType"]) -> typing.Union[MetaOapg.properties.defaultType, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["detailPage"]) -> typing.Union[MetaOapg.properties.detailPage, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fixed"]) -> typing.Union[MetaOapg.properties.fixed, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["iDate"]) -> typing.Union[MetaOapg.properties.iDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["system"]) -> typing.Union[MetaOapg.properties.system, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["versionable"]) -> typing.Union[MetaOapg.properties.versionable, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["multilingualable"]) -> typing.Union[MetaOapg.properties.multilingualable, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["variable"]) -> typing.Union[MetaOapg.properties.variable, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["urlMapPattern"]) -> typing.Union[MetaOapg.properties.urlMapPattern, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["publishDateVar"]) -> typing.Union[MetaOapg.properties.publishDateVar, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["expireDateVar"]) -> typing.Union[MetaOapg.properties.expireDateVar, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["modDate"]) -> typing.Union[MetaOapg.properties.modDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["host"]) -> typing.Union[MetaOapg.properties.host, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> typing.Union[MetaOapg.properties.icon, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["sortOrder"]) -> typing.Union[MetaOapg.properties.sortOrder, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["folder"]) -> typing.Union[MetaOapg.properties.folder, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "id", "description", "defaultType", "detailPage", "fixed", "iDate", "system", "versionable", "multilingualable", "variable", "urlMapPattern", "publishDateVar", "expireDateVar", "modDate", "host", "icon", "sortOrder", "folder", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
                defaultType: typing.Union[MetaOapg.properties.defaultType, bool, schemas.Unset] = schemas.unset,
                detailPage: typing.Union[MetaOapg.properties.detailPage, str, schemas.Unset] = schemas.unset,
                fixed: typing.Union[MetaOapg.properties.fixed, bool, schemas.Unset] = schemas.unset,
                iDate: typing.Union[MetaOapg.properties.iDate, str, datetime, schemas.Unset] = schemas.unset,
                system: typing.Union[MetaOapg.properties.system, bool, schemas.Unset] = schemas.unset,
                versionable: typing.Union[MetaOapg.properties.versionable, bool, schemas.Unset] = schemas.unset,
                multilingualable: typing.Union[MetaOapg.properties.multilingualable, bool, schemas.Unset] = schemas.unset,
                variable: typing.Union[MetaOapg.properties.variable, str, schemas.Unset] = schemas.unset,
                urlMapPattern: typing.Union[MetaOapg.properties.urlMapPattern, str, schemas.Unset] = schemas.unset,
                publishDateVar: typing.Union[MetaOapg.properties.publishDateVar, str, schemas.Unset] = schemas.unset,
                expireDateVar: typing.Union[MetaOapg.properties.expireDateVar, str, schemas.Unset] = schemas.unset,
                modDate: typing.Union[MetaOapg.properties.modDate, str, datetime, schemas.Unset] = schemas.unset,
                host: typing.Union[MetaOapg.properties.host, str, schemas.Unset] = schemas.unset,
                icon: typing.Union[MetaOapg.properties.icon, str, schemas.Unset] = schemas.unset,
                sortOrder: typing.Union[MetaOapg.properties.sortOrder, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                folder: typing.Union[MetaOapg.properties.folder, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    name=name,
                    id=id,
                    description=description,
                    defaultType=defaultType,
                    detailPage=detailPage,
                    fixed=fixed,
                    iDate=iDate,
                    system=system,
                    versionable=versionable,
                    multilingualable=multilingualable,
                    variable=variable,
                    urlMapPattern=urlMapPattern,
                    publishDateVar=publishDateVar,
                    expireDateVar=expireDateVar,
                    modDate=modDate,
                    host=host,
                    icon=icon,
                    sortOrder=sortOrder,
                    folder=folder,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                ContentType,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FileAssetContentType':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.content_type import ContentType
