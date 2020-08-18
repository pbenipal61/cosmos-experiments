def insert_vertices(client, gremlin_insert_vertices):
    for query in gremlin_insert_vertices:
        print("\tRunning this Gremlin query:\n\t{0}\n".format(query))
        callback = client.submitAsync(query)
        if callback.result() is not None:
            print("\tInserted this vertex:\n\t{0}\n".format(
                callback.result().one()))
        else:
            print("Something went wrong with this query: {0}".format(query))
    print("\n")