##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2023 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


from dataclasses import dataclass
from typing import Optional, Type, Union

from xrpc_client.models import base


@dataclass
class Params(base.ParamsModelBase):

    """Parameters model for :obj:`com.atproto.sync.getRepo`.

    Attributes:
        did: The DID of the repo.
        earliest: The earliest commit in the commit range (not inclusive).
        latest: The latest commit in the commit range (inclusive).
    """

    did: str
    earliest: Optional[str] = None
    latest: Optional[str] = None


#: Response raw data type.
Response: Union[Type[str], Type[bytes]] = bytes
