from __future__ import annotations

import logging

from pydantic import ValidationError

import d2d.contracts.exceptions as exc
from d2d.contracts import documents as doc
from d2d.providers.interface import ProviderTaskHandlers


# We use these functions to convert the JSON/ dict objects returned from
# different Prvoiders' functions to its equalavent Pydantic model
def summary_adapter(d: dict) -> doc.Summary:
    """Convert a input dictionary into structural Summary

    :param d: payload object
    :type d: dict[str, str]
    :return: Summary object parsed from input dictionary
    :rtype: Summary
    """
    try:
        return doc.Summary.model_validate(d)
    except ValidationError:
        err = exc.IncompatibleProviderOutputs("summary input is not compatible")
        logging.warning(err)
        return doc.Summary()


def metadata_adpater(d: dict) -> doc.Metadata:
    try:
        return doc.Metadata.model_validate(d)
    except ValidationError:
        err = exc.IncompatibleProviderOutputs
        logging.warning(err)
        return doc.Metadata()


def relations_adapter(d: dict) -> doc.Relations:
    try:
        return doc.Relations.model_validate(d)
    except ValidationError:
        err = exc.IncompatibleProviderOutputs
        logging.warning(err)
        return doc.Relations()


def embedding_adapter(d: dict) -> doc.Embedding:
    try:
        return doc.Embedding.model_validate(d)
    except ValidationError:
        err = exc.IncompatibleProviderOutputs
        logging.warning(err)
        return doc.Embedding()


def content_adapter(d: dict) -> doc.Content:
    try:
        return doc.Content.model_validate(d)
    except ValidationError:
        err = exc.IncompatibleProviderOutputs
        logging.warning(err)
        return doc.Content()


def obj_refs_adapter(d: dict) -> doc.ObjectReferences:
    try:
        return doc.ObjectReferences.model_validate(d)
    except ValidationError:
        err = exc.IncompatibleProviderOutputs
        logging.warning(err)
        return doc.ObjectReferences()


class TaskFunctionsAdapters(ProviderTaskHandlers[dict, doc.DocumentComponent]):
    """Mapper between provider tasks functions to the eqv pydantic object convertors

    :param ProviderInterface: _description_
    :type ProviderInterface: _type_
    """

    summary = summary_adapter
    metadata = metadata_adpater
    relations = relations_adapter
    embedding = embedding_adapter
    content = content_adapter
    obj_refs = obj_refs_adapter

