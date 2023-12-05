"""Moving is_ctive to user table

Revision ID: 98dfc5df0e45
Revises: 908c4e8c812e
Create Date: 2023-12-02 12:49:09.727122

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98dfc5df0e45'
down_revision: Union[str, None] = '908c4e8c812e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('completed_content_blocks_student_id_fkey', 'completed_content_blocks', type_='foreignkey')
    op.drop_constraint('completed_content_blocks_content_block_id_fkey', 'completed_content_blocks', type_='foreignkey')
    op.create_foreign_key(None, 'completed_content_blocks', 'users', ['student_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'completed_content_blocks', 'content_blocks', ['content_block_id'], ['id'], source_schema='public', referent_schema='public')
    op.add_column('content_blocks', sa.Column('type', sa.Enum('lesson', 'quiz', 'assignment', name='contenttype'), nullable=True))
    op.drop_constraint('content_blocks_section_id_fkey', 'content_blocks', type_='foreignkey')
    op.create_foreign_key(None, 'content_blocks', 'sections', ['section_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('courses_user_id_fkey', 'courses', type_='foreignkey')
    op.create_foreign_key(None, 'courses', 'users', ['user_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('profiles_user_id_fkey', 'profiles', type_='foreignkey')
    op.create_foreign_key(None, 'profiles', 'users', ['user_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_column('profiles', 'is_active')
    op.drop_constraint('sections_course_id_fkey', 'sections', type_='foreignkey')
    op.create_foreign_key(None, 'sections', 'courses', ['course_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('student_courses_student_id_fkey', 'student_courses', type_='foreignkey')
    op.drop_constraint('student_courses_course_id_fkey', 'student_courses', type_='foreignkey')
    op.create_foreign_key(None, 'student_courses', 'courses', ['course_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'student_courses', 'users', ['student_id'], ['id'], source_schema='public', referent_schema='public')
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_active')
    op.drop_constraint(None, 'student_courses', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'student_courses', schema='public', type_='foreignkey')
    op.create_foreign_key('student_courses_course_id_fkey', 'student_courses', 'courses', ['course_id'], ['id'])
    op.create_foreign_key('student_courses_student_id_fkey', 'student_courses', 'users', ['student_id'], ['id'])
    op.drop_constraint(None, 'sections', schema='public', type_='foreignkey')
    op.create_foreign_key('sections_course_id_fkey', 'sections', 'courses', ['course_id'], ['id'])
    op.add_column('profiles', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'profiles', schema='public', type_='foreignkey')
    op.create_foreign_key('profiles_user_id_fkey', 'profiles', 'users', ['user_id'], ['id'])
    op.drop_constraint(None, 'courses', schema='public', type_='foreignkey')
    op.create_foreign_key('courses_user_id_fkey', 'courses', 'users', ['user_id'], ['id'])
    op.drop_constraint(None, 'content_blocks', schema='public', type_='foreignkey')
    op.create_foreign_key('content_blocks_section_id_fkey', 'content_blocks', 'sections', ['section_id'], ['id'])
    op.drop_column('content_blocks', 'type')
    op.drop_constraint(None, 'completed_content_blocks', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'completed_content_blocks', schema='public', type_='foreignkey')
    op.create_foreign_key('completed_content_blocks_content_block_id_fkey', 'completed_content_blocks', 'content_blocks', ['content_block_id'], ['id'])
    op.create_foreign_key('completed_content_blocks_student_id_fkey', 'completed_content_blocks', 'users', ['student_id'], ['id'])
    # ### end Alembic commands ###
