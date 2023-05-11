from src.app import get_postgres_connection, produce_fake_record


def test_produce_fake_record_return_a_dict():
    record = produce_fake_record()

    assert isinstance(record, dict)


def test_produce_fake_record_return_expected_fields():
    expected_keys = ["first_name", "last_name", "email", "item", "item_quantity"]
    record = produce_fake_record()

    assert all(key in record for key in expected_keys)


def test_transform_dict_to_pandas():
    import json

    import pandas as pd

    record = {
        "first_name": "Campbell Stephanie",
        "last_name": "Campbell",
        "email": "marklee@example.org",
        "item": "juice",
        "item_quantity": 2,
    }

    df = pd.read_json(json.dumps(record), orient="index")

    assert isinstance(df, pd.DataFrame)


# def test_write_pandas_df_to_postgres_table():
#    import json
#
#    import pandas as pd
#
#    conn = get_postgres_connection()
#    record = {
#        "first_name": "Campbell Stephanie",
#        "last_name": "Campbell",
#        "email": "marklee@example.org",
#        "item": "juice",
#        "item_quantity": 2,
#    }
#
#    df = pd.read_json(json.dumps(record), orient="index")
#
#    result = df.to_sql("market", conn, if_exists="append", index=False)
#
#    assert result == None
#
