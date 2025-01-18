from authorizer.auth.payloads import AccessPayload
from authorizer.auth.token import JWT


class Authorizer:
    @staticmethod
    def _get_access_token_payload(token: str) -> AccessPayload:
        payload = JWT.parse_jwt(token)
        return AccessPayload(**payload)

    @classmethod
    def get_user_id_from_token(cls, access_token: str) -> str:
        payload = cls._get_access_token_payload(access_token)
        return payload.sub
