##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2023 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


from dataclasses import dataclass

from xrpc_client.models import base


@dataclass
class Data(base.DataModelBase):

    """Input data model for :obj:`app.bsky.graph.muteActor`.

    Attributes:
        actor: Actor.
    """

    actor: str
