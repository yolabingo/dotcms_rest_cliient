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


class WorkflowSchemeImportExportObjectView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            version = schemas.StrSchema
            
            
            class schemes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WorkflowScheme']:
                        return WorkflowScheme
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['WorkflowScheme'], typing.List['WorkflowScheme']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'schemes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkflowScheme':
                    return super().__getitem__(i)
            
            
            class steps(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WorkflowStep']:
                        return WorkflowStep
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['WorkflowStep'], typing.List['WorkflowStep']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'steps':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkflowStep':
                    return super().__getitem__(i)
            
            
            class actions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WorkflowAction']:
                        return WorkflowAction
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['WorkflowAction'], typing.List['WorkflowAction']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'actions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkflowAction':
                    return super().__getitem__(i)
            
            
            class actionSteps(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            additional_properties = schemas.StrSchema
                        
                        def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                            return super().get_item_oapg(name)
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'actionSteps':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class actionClasses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WorkflowActionClass']:
                        return WorkflowActionClass
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['WorkflowActionClass'], typing.List['WorkflowActionClass']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'actionClasses':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkflowActionClass':
                    return super().__getitem__(i)
            
            
            class actionClassParams(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WorkflowActionClassParameter']:
                        return WorkflowActionClassParameter
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['WorkflowActionClassParameter'], typing.List['WorkflowActionClassParameter']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'actionClassParams':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkflowActionClassParameter':
                    return super().__getitem__(i)
            
            
            class schemeSystemActionWorkflowActionMappings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SystemActionWorkflowActionMapping']:
                        return SystemActionWorkflowActionMapping
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SystemActionWorkflowActionMapping'], typing.List['SystemActionWorkflowActionMapping']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'schemeSystemActionWorkflowActionMappings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SystemActionWorkflowActionMapping':
                    return super().__getitem__(i)
            __annotations__ = {
                "version": version,
                "schemes": schemes,
                "steps": steps,
                "actions": actions,
                "actionSteps": actionSteps,
                "actionClasses": actionClasses,
                "actionClassParams": actionClassParams,
                "schemeSystemActionWorkflowActionMappings": schemeSystemActionWorkflowActionMappings,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schemes"]) -> MetaOapg.properties.schemes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["steps"]) -> MetaOapg.properties.steps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actions"]) -> MetaOapg.properties.actions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actionSteps"]) -> MetaOapg.properties.actionSteps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actionClasses"]) -> MetaOapg.properties.actionClasses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actionClassParams"]) -> MetaOapg.properties.actionClassParams: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schemeSystemActionWorkflowActionMappings"]) -> MetaOapg.properties.schemeSystemActionWorkflowActionMappings: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "schemes", "steps", "actions", "actionSteps", "actionClasses", "actionClassParams", "schemeSystemActionWorkflowActionMappings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schemes"]) -> typing.Union[MetaOapg.properties.schemes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["steps"]) -> typing.Union[MetaOapg.properties.steps, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actions"]) -> typing.Union[MetaOapg.properties.actions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actionSteps"]) -> typing.Union[MetaOapg.properties.actionSteps, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actionClasses"]) -> typing.Union[MetaOapg.properties.actionClasses, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actionClassParams"]) -> typing.Union[MetaOapg.properties.actionClassParams, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schemeSystemActionWorkflowActionMappings"]) -> typing.Union[MetaOapg.properties.schemeSystemActionWorkflowActionMappings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "schemes", "steps", "actions", "actionSteps", "actionClasses", "actionClassParams", "schemeSystemActionWorkflowActionMappings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
        schemes: typing.Union[MetaOapg.properties.schemes, list, tuple, schemas.Unset] = schemas.unset,
        steps: typing.Union[MetaOapg.properties.steps, list, tuple, schemas.Unset] = schemas.unset,
        actions: typing.Union[MetaOapg.properties.actions, list, tuple, schemas.Unset] = schemas.unset,
        actionSteps: typing.Union[MetaOapg.properties.actionSteps, list, tuple, schemas.Unset] = schemas.unset,
        actionClasses: typing.Union[MetaOapg.properties.actionClasses, list, tuple, schemas.Unset] = schemas.unset,
        actionClassParams: typing.Union[MetaOapg.properties.actionClassParams, list, tuple, schemas.Unset] = schemas.unset,
        schemeSystemActionWorkflowActionMappings: typing.Union[MetaOapg.properties.schemeSystemActionWorkflowActionMappings, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowSchemeImportExportObjectView':
        return super().__new__(
            cls,
            *_args,
            version=version,
            schemes=schemes,
            steps=steps,
            actions=actions,
            actionSteps=actionSteps,
            actionClasses=actionClasses,
            actionClassParams=actionClassParams,
            schemeSystemActionWorkflowActionMappings=schemeSystemActionWorkflowActionMappings,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.system_action_workflow_action_mapping import SystemActionWorkflowActionMapping
from openapi_client.model.workflow_action import WorkflowAction
from openapi_client.model.workflow_action_class import WorkflowActionClass
from openapi_client.model.workflow_action_class_parameter import WorkflowActionClassParameter
from openapi_client.model.workflow_scheme import WorkflowScheme
from openapi_client.model.workflow_step import WorkflowStep
