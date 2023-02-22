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


class WorkflowStepUpdateForm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "escalationTime",
            "stepName",
            "stepOrder",
            "enableEscalation",
            "stepResolved",
        }
        
        class properties:
            stepOrder = schemas.Int32Schema
            stepName = schemas.StrSchema
            enableEscalation = schemas.BoolSchema
            escalationTime = schemas.StrSchema
            stepResolved = schemas.BoolSchema
            escalationAction = schemas.StrSchema
            __annotations__ = {
                "stepOrder": stepOrder,
                "stepName": stepName,
                "enableEscalation": enableEscalation,
                "escalationTime": escalationTime,
                "stepResolved": stepResolved,
                "escalationAction": escalationAction,
            }
    
    escalationTime: MetaOapg.properties.escalationTime
    stepName: MetaOapg.properties.stepName
    stepOrder: MetaOapg.properties.stepOrder
    enableEscalation: MetaOapg.properties.enableEscalation
    stepResolved: MetaOapg.properties.stepResolved
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stepOrder"]) -> MetaOapg.properties.stepOrder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stepName"]) -> MetaOapg.properties.stepName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enableEscalation"]) -> MetaOapg.properties.enableEscalation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["escalationTime"]) -> MetaOapg.properties.escalationTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stepResolved"]) -> MetaOapg.properties.stepResolved: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["escalationAction"]) -> MetaOapg.properties.escalationAction: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["stepOrder", "stepName", "enableEscalation", "escalationTime", "stepResolved", "escalationAction", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stepOrder"]) -> MetaOapg.properties.stepOrder: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stepName"]) -> MetaOapg.properties.stepName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enableEscalation"]) -> MetaOapg.properties.enableEscalation: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["escalationTime"]) -> MetaOapg.properties.escalationTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stepResolved"]) -> MetaOapg.properties.stepResolved: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["escalationAction"]) -> typing.Union[MetaOapg.properties.escalationAction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["stepOrder", "stepName", "enableEscalation", "escalationTime", "stepResolved", "escalationAction", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        escalationTime: typing.Union[MetaOapg.properties.escalationTime, str, ],
        stepName: typing.Union[MetaOapg.properties.stepName, str, ],
        stepOrder: typing.Union[MetaOapg.properties.stepOrder, decimal.Decimal, int, ],
        enableEscalation: typing.Union[MetaOapg.properties.enableEscalation, bool, ],
        stepResolved: typing.Union[MetaOapg.properties.stepResolved, bool, ],
        escalationAction: typing.Union[MetaOapg.properties.escalationAction, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowStepUpdateForm':
        return super().__new__(
            cls,
            *_args,
            escalationTime=escalationTime,
            stepName=stepName,
            stepOrder=stepOrder,
            enableEscalation=enableEscalation,
            stepResolved=stepResolved,
            escalationAction=escalationAction,
            _configuration=_configuration,
            **kwargs,
        )
