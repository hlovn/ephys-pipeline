from msilib import schema
import datajoint as dj

schema = dj.schema('FB-inactivation-pipeline')

@schema
class Animal(dj.Manual):
    definition = """
    # Animal ID
    animal_id: varchar(5)
    ---
    # Animal ID
    animal_nickname: varchar(20)
    """

@schema
class Session(dj.Manual):
    definition = """
    -> Animal
    session_datetime: datetime
    """


@schema
class SessionDirectory(dj.Manual):
    definition = """
    -> Session
    ---
    session_dir: varchar(256) # Path to the data directory for a session
    """


@schema
class SessionExperimenter(dj.Manual):
    definition = """
    -> Session
    -> Experimenter
    """

@schema
class SessionNote(dj.Manual):
    definition = """
    -> Session
    ---
    session_note: varchar(1024)
    """

@schema
class ProjectSession(dj.Manual):
    definition = """
    -> Project
    -> Session
    """


