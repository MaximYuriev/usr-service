from faststream.rabbit import RabbitExchange, RabbitQueue

USER_EXCHANGE = RabbitExchange("user")
USER_INFO_QUEUE = RabbitQueue("user-info")