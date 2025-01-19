from typing import Annotated

from faststream import FastStream, Depends
from faststream.rabbit import RabbitBroker

from config import rabbit_url
from src.infrastructure.broker.constants.user import USER_EXCHANGE, USER_INFO_CREATE_QUEUE, USER_INFO_UPDATE_QUEUE
from src.infrastructure.broker.dependencies.user import get_user_adapter
from src.infrastructure.broker.adapters.user import FromBrokerToUserServiceAdapter
from src.infrastructure.broker.schemas.user import UserBrokerSchema, UpdateUserBrokerSchema

broker = RabbitBroker(url=rabbit_url)
app = FastStream(broker)


@broker.subscriber(queue=USER_INFO_CREATE_QUEUE, exchange=USER_EXCHANGE)
async def create_user(
        user_schema: UserBrokerSchema,
        user_adapter: Annotated[FromBrokerToUserServiceAdapter, Depends(get_user_adapter)],
):
    await user_adapter.create_user(user_schema)


@broker.subscriber(queue=USER_INFO_UPDATE_QUEUE, exchange=USER_EXCHANGE)
async def create_user(
        user_schema: UpdateUserBrokerSchema,
        user_adapter: Annotated[FromBrokerToUserServiceAdapter, Depends(get_user_adapter)],
):
    await user_adapter.update_user(user_schema)
