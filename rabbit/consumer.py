from typing import Annotated

from faststream import FastStream, Depends
from faststream.rabbit import RabbitBroker

from rabbit.constants import USER_EXCHANGE, USER_INFO_QUEUE
from rabbit.dependecies import get_user_adapter
from src.user.adapter import UserAdapter
from src.user.schemas import CreateUserSchema

broker = RabbitBroker()
app = FastStream(broker)


@broker.subscriber(queue=USER_INFO_QUEUE, exchange=USER_EXCHANGE)
async def handle(
        create_user_schema: CreateUserSchema,
        user_adapter: Annotated[UserAdapter, Depends(get_user_adapter)],
):
    await user_adapter.create_user(create_user_schema)
