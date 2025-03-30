from config.omnitags import read_config

def main():
    # Initialize Config and load JSON data
    config = read_config()

    # Example Outputs
    print("Database Name:", config.Aliases.get("database", "Not Found"))
    print("Table A1 Name:", config.Titles.get("tabel_a1_alias_v2", "Not Found"))
    print("Upload Path for A1:", config.VUploadPath.get("tabel_a1", "Not Found"))
    print("Flash Message for A1:", config.Views.get("tabel_a1_daftar", "Not Found"))

if __name__ == "__main__":
    main()
