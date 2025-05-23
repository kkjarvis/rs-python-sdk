# coding: utf-8

"""
Root Signals API

Root Signals JSON API provides a way to access Root Signals using provisioned API token

The version of the OpenAPI document: 1.0.0 (latest)
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated, Self

from root.generated.openapi_client.models.model_params_request import ModelParamsRequest
from root.generated.openapi_client.models.reference_variable_dynamic_datasets_request import (
    ReferenceVariableDynamicDatasetsRequest,
)


class SkillExecutionRequest(BaseModel):
    """
    SkillExecutionRequest
    """  # noqa: E501

    skill_version_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    variables: Optional[Dict[str, Annotated[str, Field(min_length=1, strict=True)]]] = None
    model_params: Optional[ModelParamsRequest] = None
    dynamic_datasets: Optional[List[ReferenceVariableDynamicDatasetsRequest]] = Field(
        default=None, description="Specify the dataset for a reference variable."
    )
    language: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = "en"
    __properties: ClassVar[List[str]] = [
        "skill_version_id",
        "variables",
        "model_params",
        "dynamic_datasets",
        "language",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SkillExecutionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of model_params
        if self.model_params:
            _dict["model_params"] = self.model_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in dynamic_datasets (list)
        _items = []
        if self.dynamic_datasets:
            for _item in self.dynamic_datasets:
                if _item:
                    _items.append(_item.to_dict())
            _dict["dynamic_datasets"] = _items
        # set to None if skill_version_id (nullable) is None
        # and model_fields_set contains the field
        if self.skill_version_id is None and "skill_version_id" in self.model_fields_set:
            _dict["skill_version_id"] = None

        # set to None if dynamic_datasets (nullable) is None
        # and model_fields_set contains the field
        if self.dynamic_datasets is None and "dynamic_datasets" in self.model_fields_set:
            _dict["dynamic_datasets"] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict["language"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SkillExecutionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "skill_version_id": obj.get("skill_version_id"),
                "variables": obj.get("variables"),
                "model_params": ModelParamsRequest.from_dict(obj["model_params"])
                if obj.get("model_params") is not None
                else None,
                "dynamic_datasets": [
                    ReferenceVariableDynamicDatasetsRequest.from_dict(_item) for _item in obj["dynamic_datasets"]
                ]
                if obj.get("dynamic_datasets") is not None
                else None,
                "language": obj.get("language") if obj.get("language") is not None else "en",
            }
        )
        return _obj
