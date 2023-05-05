##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2023 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


from dataclasses import dataclass
from typing import List, Optional

from xrpc_client import models
from xrpc_client.models import base


@dataclass
class Params(base.ParamsModelBase):

    """Parameters model for :obj:`app.bsky.feed.getAuthorFeed`.

    Attributes:
        actor: Actor.
        limit: Limit.
        cursor: Cursor.
    """

    actor: str
    cursor: Optional[str] = None
    limit: Optional[int] = None


@dataclass
class Response(base.ResponseModelBase):

    """Output data model for :obj:`app.bsky.feed.getAuthorFeed`.

    Attributes:
        cursor: Cursor.
        feed: Feed.
    """

    feed: List['models.AppBskyFeedDefs.FeedViewPost']
    cursor: Optional[str] = None
