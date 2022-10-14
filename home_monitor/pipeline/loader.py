import connections
import speed


def speed_to_csv(data):
    """
    Upload internet speeds collected with speedtest at runtime, into a dedicated csv for speedtest data
    """

    # data = speed.get_speeds()
    input_data = []
    for keys in data:
        input_data.append(data[keys])
            
    connections.toCSV(input_data, 'database/speedtest.csv')

def speed_to_sqlite(data):
    # data = speed.get_speeds()
    query = f"""
    insert into internet_speeds (timestamp, ping, upload, download)
    values ('{data["time"]}',{data["ping"]},{data["upload"]},{data["download"]});
    """

    connections.toSqlite(query)


if __name__ == "__main__":
    data = speed.get_speeds()
    speed_to_csv(data)
    speed_to_sqlite(data)
