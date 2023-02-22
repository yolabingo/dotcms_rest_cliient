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


class RestRule(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            fireOn = schemas.StrSchema
            shortCircuit = schemas.BoolSchema
            priority = schemas.Int32Schema
            enabled = schemas.BoolSchema
            
            
            class conditionGroups(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def additional_properties() -> typing.Type['RestConditionGroup']:
                        return RestConditionGroup
                
                def __getitem__(self, name: typing.Union[str, ]) -> 'RestConditionGroup':
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> 'RestConditionGroup':
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: 'RestConditionGroup',
                ) -> 'conditionGroups':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class ruleActions(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.BoolSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, bool, ],
                ) -> 'ruleActions':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "name": name,
                "fireOn": fireOn,
                "shortCircuit": shortCircuit,
                "priority": priority,
                "enabled": enabled,
                "conditionGroups": conditionGroups,
                "ruleActions": ruleActions,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fireOn"]) -> MetaOapg.properties.fireOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shortCircuit"]) -> MetaOapg.properties.shortCircuit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditionGroups"]) -> MetaOapg.properties.conditionGroups: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ruleActions"]) -> MetaOapg.properties.ruleActions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "fireOn", "shortCircuit", "priority", "enabled", "conditionGroups", "ruleActions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fireOn"]) -> typing.Union[MetaOapg.properties.fireOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shortCircuit"]) -> typing.Union[MetaOapg.properties.shortCircuit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> typing.Union[MetaOapg.properties.priority, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> typing.Union[MetaOapg.properties.enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditionGroups"]) -> typing.Union[MetaOapg.properties.conditionGroups, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ruleActions"]) -> typing.Union[MetaOapg.properties.ruleActions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "fireOn", "shortCircuit", "priority", "enabled", "conditionGroups", "ruleActions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        fireOn: typing.Union[MetaOapg.properties.fireOn, str, schemas.Unset] = schemas.unset,
        shortCircuit: typing.Union[MetaOapg.properties.shortCircuit, bool, schemas.Unset] = schemas.unset,
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        enabled: typing.Union[MetaOapg.properties.enabled, bool, schemas.Unset] = schemas.unset,
        conditionGroups: typing.Union[MetaOapg.properties.conditionGroups, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        ruleActions: typing.Union[MetaOapg.properties.ruleActions, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RestRule':
        return super().__new__(
            cls,
            *_args,
            name=name,
            fireOn=fireOn,
            shortCircuit=shortCircuit,
            priority=priority,
            enabled=enabled,
            conditionGroups=conditionGroups,
            ruleActions=ruleActions,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.rest_condition_group import RestConditionGroup
