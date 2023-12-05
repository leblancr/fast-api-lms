"""empty message

Revision ID: 908c4e8c812e
Revises: 47ef9fd0d17f
Create Date: 2023-12-02 12:27:08.374803

"""
import os, json
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision: str = '908c4e8c812e'
down_revision: Union[str, None] = '47ef9fd0d17f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    users = op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    # sa.Column('role', sa.Enum('teacher', 'student', name='role'), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.add_column(
        'users',
        sa.Column('role', sa.Enum('teacher', 'student', name='role'), nullable=True),
    )
    
    with open(os.path.join(os.path.dirname(__file__), "../data/students.json")) as f:
        student_data = f.read()
        print('student_data', student_data)

    op.bulk_insert(users, json.loads(student_data))
    
    op.create_index(op.f('ix_public_users_email'), 'users', ['email'], unique=True, schema='public')
    op.create_index(op.f('ix_public_users_id'), 'users', ['id'], unique=False, schema='public')
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['public.users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_courses_id'), 'courses', ['id'], unique=False, schema='public')
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['public.users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_profiles_id'), 'profiles', ['id'], unique=False, schema='public')
    op.create_table('sections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['public.courses.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_sections_id'), 'sections', ['id'], unique=False, schema='public')
    op.create_table('student_courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('completed', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['public.courses.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['public.users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_student_courses_id'), 'student_courses', ['id'], unique=False, schema='public')
    op.create_table('content_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('type', sa.Enum('lesson', 'quiz', 'assignment', name='contenttype'), nullable=True),
    sa.Column('url', sqlalchemy_utils.types.url.URLType(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('section_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['section_id'], ['public.sections.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_content_blocks_id'), 'content_blocks', ['id'], unique=False, schema='public')
    op.create_table('completed_content_blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('content_block_id', sa.Integer(), nullable=False),
    sa.Column('url', sqlalchemy_utils.types.url.URLType(), nullable=True),
    sa.Column('feedback', sa.Text(), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['content_block_id'], ['public.content_blocks.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['public.users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_completed_content_blocks_id'), 'completed_content_blocks', ['id'], unique=False, schema='public')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_public_completed_content_blocks_id'), table_name='completed_content_blocks', schema='public')
    op.drop_table('completed_content_blocks', schema='public')
    op.drop_index(op.f('ix_public_content_blocks_id'), table_name='content_blocks', schema='public')
    op.drop_table('content_blocks', schema='public')
    op.drop_index(op.f('ix_public_student_courses_id'), table_name='student_courses', schema='public')
    op.drop_table('student_courses', schema='public')
    op.drop_index(op.f('ix_public_sections_id'), table_name='sections', schema='public')
    op.drop_table('sections', schema='public')
    op.drop_index(op.f('ix_public_profiles_id'), table_name='profiles', schema='public')
    op.drop_table('profiles', schema='public')
    op.drop_index(op.f('ix_public_courses_id'), table_name='courses', schema='public')
    op.drop_table('courses', schema='public')
    op.drop_index(op.f('ix_public_users_id'), table_name='users', schema='public')
    op.drop_index(op.f('ix_public_users_email'), table_name='users', schema='public')
    op.drop_table('users', schema='public')
    # ### end Alembic commands ###
