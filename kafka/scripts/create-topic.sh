docker exec -it broker /opt/kafka/bin/kafka-topics.sh \
    --create \
    --topic vital-signs \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 3