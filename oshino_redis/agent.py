import aioredis

from oshino import Agent


class RedisAgent(Agent):

    @property
    def host(self):
        return self._data.get("host", "localhost")

    @property
    def port(self):
        return self._data.get("port", 6379)

    @property
    def password(self):
        return self._data.get("password", None)

    async def create_connection(self):
        return await aioredis.create_redis((self.host, self.port))

    async def process(self, event_fn):
        logger = self.get_logger()
        redis = await self.create_connection()
        if self.password is not None:
            await redis.auth(self.password)
        info = await redis.info()
        for name, section in info.items():
            logger.debug("Section: {0}, data: {1}".format(name, section))
            for key, stat in section.items():
                service = "{prefix}{section}.{key}".format(prefix=self.prefix,
                                                           section=name,
                                                           key=key)
                event_fn(service=service,
                         metric_f=float(stat))
        redis.close()
