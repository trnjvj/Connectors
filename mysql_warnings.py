import mysql.connector

STMT = "SELECT 'abc'+1"


def main(config):
    output = []
    config["get_warnings"] = True
    db = mysql.connector.Connect(**config)
    cursor = db.cursor()
    db.sql_mode = ""

    output.append("Executing '%s'" % STMT)
    cursor.execute(STMT)
    cursor.fetchall()

    warnings = cursor.fetchwarnings()
    if warnings:
        for w in warnings:
            output.append("%d: %s" % (w[1], w[2]))
    else:
        output.append("We should have got warnings.")
        raise Exception("Got no warnings")

    cursor.close()
    db.close()
    return output


if __name__ == "__main__":
    config = {
        "host": "localhost",
        "port": 3306,
        "database": "test",
        "user": "root",
        "password": "",
        "charset": "utf8",
        "use_unicode": True,
        "get_warnings": True,
    }

    out = main(config)
    print("\n".join(out))
