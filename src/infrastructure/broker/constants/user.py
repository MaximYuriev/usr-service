from faststream.rabbit import RabbitExchange, RabbitQueue

USER_EXCHANGE = RabbitExchange("user")
USER_INFO_CREATE_QUEUE = RabbitQueue("user-info-create")
USER_INFO_UPDATE_QUEUE = RabbitQueue("user-info-update")
