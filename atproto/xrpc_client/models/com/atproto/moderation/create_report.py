##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2023 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


from dataclasses import dataclass
from typing import Optional, Union

from xrpc_client import models
from xrpc_client.models import base


@dataclass
class Data(base.DataModelBase):

    """Input data model for :obj:`com.atproto.moderation.createReport`.

    Attributes:
        reasonType: Reason type.
        reason: Reason.
        subject: Subject.
    """

    reasonType: 'models.ComAtprotoModerationDefs.ReasonType'
    subject: Union['models.ComAtprotoAdminDefs.RepoRef', 'models.ComAtprotoRepoStrongRef.Main']
    reason: Optional[str] = None


@dataclass
class Response(base.ResponseModelBase):

    """Output data model for :obj:`com.atproto.moderation.createReport`.

    Attributes:
        id: Id.
        reasonType: Reason type.
        reason: Reason.
        subject: Subject.
        reportedBy: Reported by.
        createdAt: Created at.
    """

    createdAt: str
    id: int
    reasonType: 'models.ComAtprotoModerationDefs.ReasonType'
    reportedBy: str
    subject: Union['models.ComAtprotoAdminDefs.RepoRef', 'models.ComAtprotoRepoStrongRef.Main']
    reason: Optional[str] = None
