##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2023 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


from dataclasses import dataclass
from typing import Type

from xrpc_client import models
from xrpc_client.models import base


@dataclass
class Params(base.ParamsModelBase):

    """Parameters model for :obj:`com.atproto.admin.getModerationReport`.

    Attributes:
        id: Id.
    """

    id: int


#: Response reference to :obj:`models.ComAtprotoAdminDefs.ReportViewDetail` model.
ResponseRef: Type[models.ComAtprotoAdminDefs.ReportViewDetail] = models.ComAtprotoAdminDefs.ReportViewDetail
