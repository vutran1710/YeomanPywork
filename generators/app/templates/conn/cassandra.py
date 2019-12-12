from logzero import logger as log
from pydantic import BaseModel
from cassandra.cluster import NoHostAvailable
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from cassandra.query import (
    dict_factory,
    BatchStatement,
    SimpleStatement,
)
from cassandra.policies import (
    WhiteListRoundRobinPolicy,
    ConstantReconnectionPolicy,
)


class CasConfig(BaseModel):
    CAS_HOST: str
    CAS_USER: str
    CAS_PWD: str
    CAS_KEYSPACE: str


class CassandraConnection:
    def __init__(self, config: CasConfig):
        self.cfg = config

        hosts = self.cfg["CAS_HOST"].split(",")
        auth_provider = PlainTextAuthProvider(self.cfg["CAS_USER"], self.cfg["CAS_PWD"])
        reconnection_policy = ConstantReconnectionPolicy(delay=2.5, max_attempts=None)
        balancing_policy = WhiteListRoundRobinPolicy(hosts)

        self.cluster = Cluster(
            hosts,
            load_balancing_policy=balancing_policy,
            auth_provider=auth_provider,
            reconnection_policy=reconnection_policy,
        )

        self.connect()
        self.prepared_statements = {}

    def connect(self):
        # https://github.com/cqlengine/cqlengine/blob/master/cqlengine/connection.py#L71 # noqa
        try:
            return self.retry()
        except NoHostAvailable:
            return self.retry()

    def retry(self):
        self.session = self.cluster.connect(self.cfg["CAS_KEYSPACE"])
        self.session.row_factory = dict_factory

    def insert(self, things):
        insert = "INSERT INTO some_table (colume_name) VALUES (%s)"    # noqa
        batch = BatchStatement()
        
        for item in things:
            batch.add(SimpleStatement(insert), (item))

        self.session.execute(batch)

    def async_insert(self, things):
        insert = "BEGIN BATCH\n" + ''.join([
            "INSERT INTO some_table (colume_name) VALUES ('{}');\n"
            .format(item) for item in things
        ]) + "APPLY BATCH"

        self.session.execute_async(insert)
