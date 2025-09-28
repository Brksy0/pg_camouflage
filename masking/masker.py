import psycopg2

def mask_table(conn_params, table_name, columns):
    """
    Applies masking functions to a given table.

    conn_params: {'host':..., 'database':..., 'user':..., 'password':...}
    table_name: name of the table
    columns: dictionary {column_name: masking_function_name}
    """
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    # Create the SET clause dynamically
    set_clauses = [f"{col} = {func}({col})" for col, func in columns.items()]
    update_query = f"UPDATE {table_name} SET " + ", ".join(set_clauses) + ";"

    cur.execute(update_query)
    conn.commit()

    # Fetch and display updated rows
    cur.execute(f"SELECT * FROM {table_name};")
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()
