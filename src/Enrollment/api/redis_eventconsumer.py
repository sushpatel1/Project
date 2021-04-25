import json
import logging
import redis

from Enrollment import bootstrap, config
from Enrollment.domain import commands

logger = logging.getLogger(__name__)

r = redis.Redis(**config.get_redis_host_and_port())


def main():
    logger.info("Redis pubsub starting")
    bus = bootstrap.bootstrap()
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe("update_policy")

    for m in pubsub.listen():
        handle_pololicy(m, bus)


def handle_pololicy(m, bus):
    logger.info("handling %s", m)
    data = json.loads(m["data"])
    cmd = commands.AddMemberPolicyCommand(ref=data["policyref"])
    bus.handle(cmd)


if __name__ == "__main__":
    main()