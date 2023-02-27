from flask import Flask, jsonify, request
from flask.views import MethodView
from config import dabase_config
from dotenv import load_dotenv

load_dotenv()


class AuthorRest(MethodView):
    connection = dabase_config.connection()
    cursor = connection.cursor()

    def get(self, id=0):
        if id == 0:
            self.cursor.execute("SELECT * FROM authors")
            results = self.cursor.fetchall()
            authors = []
            for result in results:
                authors.append({
                    "id": result[0],
                    "first_name": result[1],
                    "last_name": result[2]
                })
            return jsonify(authors)
        self.cursor.execute("""
            SELECT * FROM authors 
            WHERE id=%s
        """, (id))
        result = self.cursor.fetchone()
        return jsonify({
            "id": result[0],
            "first_name": result[1],
            "last_name": result[2]
        })

    def post(self):
        author = request.json
        self.cursor.execute("insert into authors(first_name, last_name) values(%s,%s)",
                            (author['first_name'], author['last_name']))
        self.connection.commit()
        return jsonify("created")

    def put(self, id):
        author = request.json
        self.cursor.execute("UPDATE authors SET first_name=%s,last_name=%s WHERE id=%s",
                            (author['first_name'], author['last_name'], id))
        self.connection.commit()
        return jsonify("updated")

    def delete(self, id):
        self.cursor.execute("DELETE FROM authors WHERE id=%s",
                            (id))
        self.connection.commit()
        return jsonify("deleted")
