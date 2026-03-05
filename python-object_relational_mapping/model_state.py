#!/usr/bin/python3
"""Defines the State class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb
import sys

Base = declarative_base()

class State(Base):
	"""State class definition"""
	__tablename__ = 'states'

	id = Column(Integer, primary_key=True)
	name = Column(String(128), nullable=False)

	if __name__ == "__main__":
		"""Connect to the DB the command line arguments"""
		db = MySQLdb.connect(
			host="127.0.0.1",
			port=3306,
			user=sys.argv[1],
			passwd=sys.argv[2],
			db=sys.argv[3]
		)
		
		cur = db.cursor()

		query = ("""SELECT * FROM states
				WHERE name = %s""")

		cur.execute(query, (sys.argv[4],))

		query_rows = cur.fetchall()

		if len(query_rows) == 0:
			print("Not found")
		else:
			print(query_rows[0][0])

		cur.close()
		db.close()