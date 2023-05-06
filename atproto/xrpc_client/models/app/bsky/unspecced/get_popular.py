##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2023 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


from dataclasses import dataclass
from typing import List, Optional

from atproto.xrpc_client import models
from atproto.xrpc_client.models import base


@dataclass
class Params(base.ParamsModelBase):

    """Parameters model for :obj:`app.bsky.unspecced.getPopular`.

    Attributes:
        includeNsfw: Include nsfw.
        limit: Limit.
        cursor: Cursor.
    """

    cursor: Optional[str] = None
    includeNsfw: Optional[bool] = None
    limit: Optional[int] = None


@dataclass
class Response(base.ResponseModelBase):

    """Output data model for :obj:`app.bsky.unspecced.getPopular`.

    Attributes:
        cursor: Cursor.
        feed: Feed.
    """

    feed: List['models.AppBskyFeedDefs.FeedViewPost']
    cursor: Optional[str] = None
