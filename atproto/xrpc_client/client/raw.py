from atproto.xrpc_client.client.base import ClientBase
from atproto.xrpc_client.namespaces import sync_ns

# TODO(MarshalX): This file should be autogenerated!


class ClientRaw(ClientBase):
    """Group all root namespaces"""

    com: sync_ns.ComNamespace
    bsky: sync_ns.BskyNamespace

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.com = sync_ns.ComNamespace(self)
        self.bsky = sync_ns.BskyNamespace(self)
