import psycopg2

#  connect to the data base
# db = psycopg2.connect("dbname=pythonlab5 user=belal")
# cursor = db.cursor()

# cursor.execute(
#     """
# CREATE TABLE IF NOT EXISTS employee (
#     id SERIAL PRIMARY KEY,
#     first_name VARCHAR(255) NOT NULL,
#     last_name VARCHAR(255) NOT NULL,
#     age INTEGER NOT NULL,
#     department VARCHAR(255) NOT NULL,
#     salary INTEGER NOT NULL
# )
# """
# )

# db.commit()


class DBModel:

    _primary_key: str = "id"
    _field_definations: dict = {}
    _table_name: str
    _placeholder = "%18s |"

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls._table_name = cls.__name__.lower()
        cls._create_table()

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k in self._get_fields():
                setattr(self, k, v)
            else:
                raise ValueError(f"Invalid field name {k}")

    @classmethod
    def _create_table(cls):
        table_name = cls._get_table_name()
        definations = [f"{fn} {fd}" for fn, fd in cls._get_definations().items()]

        with cls._get_connection() as conn:
            with conn.cursor() as cursor:

                cursor.execute(
                    f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
        {', '.join(definations)}
        )
        """
                )
            conn.commit()

    @classmethod
    def _get_connection(cls):
        """Get a database connection"""
        return psycopg2.connect("dbname=pythonlab5 user=belal")

    @classmethod
    def _get_table_name(cls) -> str:
        """Get the table name"""
        name = cls.__name__
        if hasattr(cls, "_table_name"):
            name = cls._table_name
        print(name)
        return name.lower()

    @classmethod
    def _get_definations(cls):
        fields_definations = cls._field_definations.copy()
        for field in cls._get_fields():
            if field in fields_definations:
                continue
            fields_definations[field] = cls._get_field_type(field)
        return fields_definations

    @classmethod
    def _get_field_type(cls, field_name: str):
        field_type = cls.__annotations__.get(field_name)
        if field_name == cls._primary_key:
            return "SERIAL PRIMARY KEY"
        if field_type == str:
            return "VARCHAR(255)"
        elif field_type == int:
            return "INTEGER"
        elif field_type == float:
            return "REAL"
        elif field_type == bool:
            return "BOOLEAN"

    @classmethod
    def _get_fields(cls):
        fields_names = [cls._primary_key]
        for attr_name in cls.__annotations__:
            if not attr_name.startswith("_"):
                fields_names.append(attr_name)
        return fields_names

    @classmethod
    def _create_instance_from_db_row(cls, row):
        """Convert database row to model instance"""

        fields = cls._get_fields()
        kwargs = {field: value for field, value in zip(fields, row)}
        return cls(**kwargs)

    @classmethod
    def get(cls, **kwargs):
        """get  table record"""
        field_name = cls._primary_key
        for k in kwargs:
            if k not in cls._get_fields():
                raise ValueError(f"Invalid field name {k}")
            field_name = k
        q = f"SELECT * FROM {cls._get_table_name()} WHERE {field_name}='{kwargs[field_name]}' ;"

        with cls._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(q)
                v = [cls._create_instance_from_db_row(row) for row in cursor.fetchall()]
                return v if len(v) > 0 else None

    @classmethod
    def get_by_pk(cls, pk):
        """get  table record"""
        with cls._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    f"SELECT * FROM {cls._get_table_name()} WHERE {cls._primary_key}='{pk}' ;"
                )

                return (
                    cls._create_instance_from_db_row(cursor.fetchone())
                    if cursor.rowcount > 0
                    else None
                )
        return None

    @classmethod
    def list_all(cls):
        """get all table records"""
        with cls._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {cls._get_table_name()};")
                v = [cls._create_instance_from_db_row(row) for row in cursor.fetchall()]
                cls._print_table_header()
                for e in v:
                    e.show(with_header=False)

    @classmethod
    def _print_table_header(cls):
        fields_names = cls._get_fields()
        placeholder = cls._placeholder * len(fields_names)
        print(placeholder % tuple(fields_names))
        print(f"{'=' * (18+2) * len(fields_names)}")

    def save(self):
        fields_names = [
            f_name for f_name in self._get_fields() if f_name != self._primary_key
        ]
        q = f"INSERT INTO {self._get_table_name()} ({', '.join(fields_names)}) VALUES ( '{("', '".join([str(getattr(self, fn)) for fn in fields_names]))}' ) ;"
        print(q)

        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.execute(q))
            conn.commit()

    def delete(self):
        """Delete the record"""
        q = f"DELETE FROM {self._get_table_name()} WHERE {self._primary_key}='{getattr(self, self._primary_key)}';"
        print(q)
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.execute(q))
            conn.commit()

    def update(self, **kwargs):
        """Update the record"""
        fields = list(kwargs.items()) if len(kwargs.items()) > 0 else None
        if fields:
            (field_name, new_value) = fields[0]
            if field_name not in self._get_fields():
                raise ValueError(f"Invalid field name {field_name}")
            q = f"UPDATE {self._get_table_name()} SET {field_name}='{new_value}' WHERE {self._primary_key}='{getattr(self, self._primary_key)}';"
            print(q)
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    print(cursor.execute(q))
                conn.commit()
            setattr(self, field_name, new_value)

    def show(self, with_header: bool = True):
        """Show the record"""
        is_manager = (
            hasattr(self, "managed_department")
            and getattr(self, "managed_department") != ""
        )
        fields_names = self._get_fields()
        placeholder = self._placeholder * len(fields_names)
        values = [getattr(self, fn) for fn in fields_names]
        if is_manager:
            values[-2] = "confidential"
        if with_header:
            self._print_table_header()
        print(placeholder % tuple(values))
        print(f"{'_' * ((20) * len(fields_names)-1)}|")


# emp = Employee._create_instance_from_db_row(
#     (
#         55,
#         "bb",
#         "elbanna",
#         22,
#         "dprt1",
#         20000,
#     )
# )

# emp.show()

# emp.save()
# Employee.list_all()
# Employee.get_by_pk(1)
# Employee.get(first_name="bb")
"""
Let the app be use command interface as follow:
        ● Print a menu for the user with the operation he can do and the key word to
        enter for running an operation, for example:
        ● For adding new employee enter “add”
        If manager press “m”/ if employee press ‘e’
        Please insert data
        Name:>>
        Age:>>
        And so on.
        ● The final option in the menu should be q for exiting the program
"""
