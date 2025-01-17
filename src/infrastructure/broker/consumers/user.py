from typing import Annotated

from faststream import FastStream, Depends
from faststream.rabbit import RabbitBroker

from src.infrastructure.broker.constants.user import USER_EXCHANGE, USER_INFO_QUEUE
from src.infrastructure.broker.dependencies.user import get_user_adapter
from src.infrastructure.broker.adapters.user import FromBrokerToUserServiceAdapter
from src.infrastructure.broker.schemas.user import UserBrokerSchema

broker = RabbitBroker()
app = FastStream(broker)


@broker.subscriber(queue=USER_INFO_QUEUE, exchange=USER_EXCHANGE)
async def create_user(
        user_schema: UserBrokerSchema,
        user_adapter: Annotated[FromBrokerToUserServiceAdapter, Depends(get_user_adapter)],
):
    await user_adapter.create_user(user_schema)
