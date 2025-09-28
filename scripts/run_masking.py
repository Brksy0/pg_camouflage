import argparse
from masking import masker

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Database masking CLI script")
    parser.add_argument("--host", required=True)
    parser.add_argument("--db", required=True)
    parser.add_argument("--user", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--table", required=True)
    parser.add_argument("--columns", required=True,
                        help='Example: "email:mask_email,phone:mask_phone,full_name:mask_name"')

    args = parser.parse_args()
    columns = dict(item.split(":") for item in args.columns.split(","))

    conn_params = {
        "host": args.host,
        "database": args.db,
        "user": args.user,
        "password": args.password
    }

    masker.mask_table(conn_params, args.table, columns)
