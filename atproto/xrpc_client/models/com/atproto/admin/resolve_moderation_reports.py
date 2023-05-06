##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2023 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


from dataclasses import dataclass
from typing import List, Type

from atproto.xrpc_client import models
from atproto.xrpc_client.models import base


@dataclass
class Data(base.DataModelBase):

    """Input data model for :obj:`com.atproto.admin.resolveModerationReports`.

    Attributes:
        actionId: Action id.
        reportIds: Report ids.
        createdBy: Created by.
    """

    actionId: int
    createdBy: str
    reportIds: List[int]


#: Response reference to :obj:`models.ComAtprotoAdminDefs.ActionView` model.
ResponseRef: Type[models.ComAtprotoAdminDefs.ActionView] = models.ComAtprotoAdminDefs.ActionView
