var config = {}

config.endpoint = process.env.DB_ENDPOINT;
config.primaryKey = process.env.DB_PRIMARY_KEY;
config.database = process.env.DB_NAME;
config.collection = process.env.DB_COLLECTION;

module.exports = config;