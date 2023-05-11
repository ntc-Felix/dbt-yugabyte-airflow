import psycopg2
import pytest
from fixtures.pg_credentials import db_credentials

from src.app import get_postgres_connection


def test_postgres_connection(db_credentials):
    conn = get_postgres_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    result = cursor.fetchone()
    assert "PostgreSQL" in result[0]
