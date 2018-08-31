import psycopg2


class XwmDbQuery:
    SERVER_PARAMETERS = None
    
    @classmethod
    def __get_server_parameters(cls):
        if not cls.SERVER_PARAMETERS:
            file = open("server_parameters", "r")
            cls.SERVER_PARAMETERS = file.read()
            file.close()
        return cls.SERVER_PARAMETERS

    @classmethod
    def make_query(cls, query):
        conn = None
        result = None

        try:
            conn = psycopg2.connect(cls.__get_server_parameters())
            cur = conn.cursor()

            cur.execute(query)
            result = cur.fetchall()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()

        return result

    @classmethod
    def get_ship_name(cls, ship_id):
        conn = None
        result_tuple = None

        try:
            conn = psycopg2.connect(cls.__get_server_parameters())
            cur = conn.cursor()

            cur.execute(
                """
                SELECT ship_name FROM ship
                WHERE ship_id = """
                + str(ship_id)
            )
            result_tuple = cur.fetchall()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()
        result = result_tuple[0][0]
        return result

    @classmethod
    def get_maneuver_dial(cls, ship_id):
        conn = None
        result_tuples = None

        try:
            conn = psycopg2.connect(cls.__get_server_parameters())
            cur = conn.cursor()

            cur.execute(
                """
                SELECT * FROM maneuver_dial
                WHERE ship_id = 
                """ + str(ship_id)
            )
            result_tuples = cur.fetchall()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()

        keys = ['ship_id', 'speed', 'maneuver_id', 'difficulty_char']

        result = []
        for values in result_tuples:
            result.append(dict(zip(keys, values)))

        return result

    @classmethod
    def get_huge_maneuver_dial(cls, ship_id):
        conn = None
        result_tuples = None

        try:
            conn = psycopg2.connect(cls.__get_server_parameters())
            cur = conn.cursor()

            cur.execute(
                """
                SELECT * FROM huge_maneuver_dial
                WHERE ship_name = 
                """ + str(ship_id)
            )
            result_tuples = cur.fetchall()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()

        keys = ['ship_id', 'speed', 'maneuver_id', 'energy']

        result = []
        for values in result_tuples:
            result.append(dict(zip(keys, values)))

        return result

    @classmethod
    def get_ship_view(cls, ship_name):
        conn = None
        result = None

        try:
            conn = psycopg2.connect(cls.__get_server_parameters())
            cur = conn.cursor()

            cur.execute(
                """
                SELECT * FROM ship_view
                WHERE ship_name = '""" + ship_name + "'"
            )
            result = cur.fetchall()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()

        return result

    @classmethod
    def get_ship_data(cls, ship_id):
        conn = None
        result = None

        try:
            conn = psycopg2.connect(cls.__get_server_parameters())
            cur = conn.cursor()

            cur.execute(
                """
                SELECT * FROM ship
                WHERE ship_id = 
                """ + str(ship_id)
            )
            result = cur.fetchall()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()

        return result

    @classmethod
    def get_pilot_list_data(cls, ship_id):
        conn = None
        result_tuples = None

        try:
            conn = psycopg2.connect(cls.__get_server_parameters())
            cur = conn.cursor()

            cur.execute(
                """
                SELECT 
                    pilot.pilot_id,
                    pilot.pilot_name,
                    pilot.variant,
                    pilot.u_name_id,
                    pilot.ship_id,
                    ship.ship_name,
                    pilot.pilot_skill,
                    pilot.elite_upgrade,
                    pilot.point_cost,
                    pilot.keywords
                FROM pilot
                    JOIN ship ON pilot.ship_id = ship.ship_id
                WHERE pilot.ship_id = 
                """ + str(ship_id)
            )
            result_tuples = cur.fetchall()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()

        keys = ['pilot_id', 'card_name', 'variant', 'unique_name_id', 'ship_id', 'ship_name',
                'pilot_skill', 'elite_upgrade', 'point_cost', 'keywords']

        result = []
        for values in result_tuples:
            result.append(dict(zip(keys, values)))

        return result

    @classmethod
    def get_action_bar(cls, ship_id):
        conn = None
        result_tuples = None

        try:
            conn = psycopg2.connect(cls.__get_server_parameters())
            cur = conn.cursor()

            cur.execute(
                """
                SELECT action_type.action_name 
                FROM action_bar
                    JOIN action_type ON action_bar.action_id = action_type.action_id
                WHERE ship_id = 
                """ + str(ship_id)
            )
            result_tuples = cur.fetchall()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()

        keys = ['action_name', 'print_name']
        result = []
        for item in result_tuples:
            values = [item[0].replace(' ', '_').lower(), item[0]]
            result.append(dict(zip(keys, values)))

        return result

    @classmethod
    def get_upgrade_bar(cls, ship_id):
        conn = None
        result_tuples = None

        try:
            conn = psycopg2.connect(cls.__get_server_parameters())
            cur = conn.cursor()

            cur.execute(
                """
                SELECT upgrade_type.upgrade_name 
                FROM upgrade_bar
                    JOIN upgrade_type ON upgrade_bar.upgrade_type_id = upgrade_type.upgrade_id
                WHERE ship_id = 
                """ + str(ship_id)
            )
            result_tuples = cur.fetchall()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()

        keys = ['upgrade_name', 'print_name']
        result = []
        for item in result_tuples:
            values = [item[0].replace(' ', '_').lower(), item[0]]
            result.append(dict(zip(keys, values)))

        return result


if __name__ == '__main__':
    action_bar = XwmDbQuery.get_upgrade_bar(2)
    print(action_bar)
