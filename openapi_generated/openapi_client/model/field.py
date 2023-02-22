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


class Field(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "clazz",
        }
        
        @staticmethod
        def discriminator():
            return {
                'clazz': {
                    'BinaryField': BinaryField,
                    'CategoryField': CategoryField,
                    'CheckboxField': CheckboxField,
                    'ColumnField': ColumnField,
                    'ConstantField': ConstantField,
                    'CustomField': CustomField,
                    'DateField': DateField,
                    'DateTimeField': DateTimeField,
                    'EmptyField': EmptyField,
                    'FileField': FileField,
                    'HiddenField': HiddenField,
                    'HostFolderField': HostFolderField,
                    'ImageField': ImageField,
                    'KeyValueField': KeyValueField,
                    'LineDividerField': LineDividerField,
                    'MultiSelectField': MultiSelectField,
                    'PermissionTabField': PermissionTabField,
                    'RadioField': RadioField,
                    'RelationshipField': RelationshipField,
                    'RelationshipsTabField': RelationshipsTabField,
                    'RowField': RowField,
                    'SelectField': SelectField,
                    'StoryBlockField': StoryBlockField,
                    'TabDividerField': TabDividerField,
                    'TagField': TagField,
                    'TextAreaField': TextAreaField,
                    'TextField': TextField,
                    'TimeField': TimeField,
                    'WysiwygField': WysiwygField,
                }
            }
        
        class properties:
            clazz = schemas.StrSchema
            
            
            class fieldContentTypeProperties(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "NAME": "NAME",
                                "VALUES": "VALUES",
                                "CATEGORIES": "CATEGORIES",
                                "RELATIONSHIPS": "RELATIONSHIPS",
                                "REGEX_CHECK": "REGEX_CHECK",
                                "HINT": "HINT",
                                "REQUIRED": "REQUIRED",
                                "SEARCHABLE": "SEARCHABLE",
                                "INDEXED": "INDEXED",
                                "LISTED": "LISTED",
                                "UNIQUE": "UNIQUE",
                                "DEFAULT_VALUE": "DEFAULT_VALUE",
                                "DATA_TYPE": "DATA_TYPE",
                            }
                        
                        @schemas.classproperty
                        def NAME(cls):
                            return cls("NAME")
                        
                        @schemas.classproperty
                        def VALUES(cls):
                            return cls("VALUES")
                        
                        @schemas.classproperty
                        def CATEGORIES(cls):
                            return cls("CATEGORIES")
                        
                        @schemas.classproperty
                        def RELATIONSHIPS(cls):
                            return cls("RELATIONSHIPS")
                        
                        @schemas.classproperty
                        def REGEX_CHECK(cls):
                            return cls("REGEX_CHECK")
                        
                        @schemas.classproperty
                        def HINT(cls):
                            return cls("HINT")
                        
                        @schemas.classproperty
                        def REQUIRED(cls):
                            return cls("REQUIRED")
                        
                        @schemas.classproperty
                        def SEARCHABLE(cls):
                            return cls("SEARCHABLE")
                        
                        @schemas.classproperty
                        def INDEXED(cls):
                            return cls("INDEXED")
                        
                        @schemas.classproperty
                        def LISTED(cls):
                            return cls("LISTED")
                        
                        @schemas.classproperty
                        def UNIQUE(cls):
                            return cls("UNIQUE")
                        
                        @schemas.classproperty
                        def DEFAULT_VALUE(cls):
                            return cls("DEFAULT_VALUE")
                        
                        @schemas.classproperty
                        def DATA_TYPE(cls):
                            return cls("DATA_TYPE")
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'fieldContentTypeProperties':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "clazz": clazz,
                "fieldContentTypeProperties": fieldContentTypeProperties,
            }
    
    clazz: MetaOapg.properties.clazz
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clazz"]) -> MetaOapg.properties.clazz: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldContentTypeProperties"]) -> MetaOapg.properties.fieldContentTypeProperties: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["clazz", "fieldContentTypeProperties", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clazz"]) -> MetaOapg.properties.clazz: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldContentTypeProperties"]) -> typing.Union[MetaOapg.properties.fieldContentTypeProperties, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["clazz", "fieldContentTypeProperties", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        clazz: typing.Union[MetaOapg.properties.clazz, str, ],
        fieldContentTypeProperties: typing.Union[MetaOapg.properties.fieldContentTypeProperties, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Field':
        return super().__new__(
            cls,
            *_args,
            clazz=clazz,
            fieldContentTypeProperties=fieldContentTypeProperties,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.binary_field import BinaryField
from openapi_client.model.category_field import CategoryField
from openapi_client.model.checkbox_field import CheckboxField
from openapi_client.model.column_field import ColumnField
from openapi_client.model.constant_field import ConstantField
from openapi_client.model.custom_field import CustomField
from openapi_client.model.date_field import DateField
from openapi_client.model.date_time_field import DateTimeField
from openapi_client.model.empty_field import EmptyField
from openapi_client.model.file_field import FileField
from openapi_client.model.hidden_field import HiddenField
from openapi_client.model.host_folder_field import HostFolderField
from openapi_client.model.image_field import ImageField
from openapi_client.model.key_value_field import KeyValueField
from openapi_client.model.line_divider_field import LineDividerField
from openapi_client.model.multi_select_field import MultiSelectField
from openapi_client.model.permission_tab_field import PermissionTabField
from openapi_client.model.radio_field import RadioField
from openapi_client.model.relationship_field import RelationshipField
from openapi_client.model.relationships_tab_field import RelationshipsTabField
from openapi_client.model.row_field import RowField
from openapi_client.model.select_field import SelectField
from openapi_client.model.story_block_field import StoryBlockField
from openapi_client.model.tab_divider_field import TabDividerField
from openapi_client.model.tag_field import TagField
from openapi_client.model.text_area_field import TextAreaField
from openapi_client.model.text_field import TextField
from openapi_client.model.time_field import TimeField
from openapi_client.model.wysiwyg_field import WysiwygField
