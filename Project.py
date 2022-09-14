from neo4j import GraphDatabase

filename = ["Dataset-V4.csv"]

def upload_data():
  driver=GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "123456"))
  session=driver.session()
  query = '''
  LOAD CSV WITH HEADERS FROM "file:///Dataset-V4.csv" AS line
  WITH line
  MERGE (Source:IP {address:line.SrcIP})
  MERGE (Destination:IP {address:line.DestIP})
  CREATE (Source)-[:connect_to {
    `attack`:line.Threat,
    `dest_port`:line.DestPort}]->(Destination)
  '''
  session.run(query).data()

def run():
  upload_data()

if __name__ == '__main__':
  run()
