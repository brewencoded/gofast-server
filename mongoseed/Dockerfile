FROM mongo

COPY mongo-seed.json /tmp/mongo-seed.json

CMD mongoimport --host db --db stock --collection inventory --type json --file /tmp/mongo-seed.json --jsonArray