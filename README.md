# fast-api-lms
https://www.youtube.com/watch?v=gQTRsZpR7Gw
Fast API Crash Course Code-along | Build an app with Postgres, SQL Alchemy, Async, and more

python -m venv venv
source venv/bin/activate

psql -U rich -d fastapi_lms

Create database manually with psql or dbeaver
postgresql://rich:reddpos@localhost/fastapi_lms?options=-csearch_path%3Dalembic_version"

poetry add alembic
alembic init alembic - creates alembic directory
alembic revision --autogenerate - to generate versions/<migration_file>.py
alembic upgrade head - to do the migration, runs the generated file above

ERROR [alembic.util.messaging] Can't locate revision identified by 'e11a3532ec28'
FAILED: Can't locate revision identified by 'e11a3532ec28':

alembic revision -m "initial" - to reset eveytihng

sqlalchemy.exc.NoReferencedTableError: Foreign key associated with column 'completed_content_blocks.content_block_id'
could not find table 'content_blocks' with which to generate a foreign key to target column 'id'

Needed to add schema name (public in this case) in foreign key:
user_id = Column(Integer, ForeignKey("public.users.id"), nullable=False) in models classes.

chnged gitlab to github in pre-commit-config.yaml
