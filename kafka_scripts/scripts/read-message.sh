#!/bin/bash
docker exec -it kafka1 kafka-console-consumer \
    --bootstrap-server kafka1:9092 \
    --topic vital-signs \
    --from-beginning