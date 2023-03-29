from api.fastapi_service.osm_handler import parse_osm


def add_graph_to_db(file_path : str):
    ways, nodes = parse_osm(file_path)


if __name__ == "__main__":
    file_path = r"D:\Code\University\NIR\Urban-Topology-Analysis-Service\api\cities_osm\Нягань.osm.pbf"
    add_graph_to_db(file_path)
