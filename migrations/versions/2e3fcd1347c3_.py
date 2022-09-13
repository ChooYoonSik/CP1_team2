"""empty message

Revision ID: 2e3fcd1347c3
Revises: cf93301a00d1
Create Date: 2022-09-09 00:25:01.269629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e3fcd1347c3'
down_revision = 'cf93301a00d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=100), nullable=False),
    sa.Column('region', sa.String(length=200), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    op.create_table('fridge',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product', sa.String(length=200), nullable=True),
    sa.Column('barcode', sa.Integer(), nullable=True),
    sa.Column('subclass', sa.String(length=150), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('exp_date', sa.Date(), nullable=False),
    sa.Column('adding_date', sa.DateTime(), nullable=True),
    sa.Column('modify_date', sa.DateTime(), nullable=True),
    sa.Column('remain_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_fridge_user_id_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_fridge'))
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('modify_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_question_user_id_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_question'))
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('modify_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], name=op.f('fk_answer_question_id_question'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_answer_user_id_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_answer'))
    )
    op.drop_table('recipe_ingredient')
    op.alter_column('article', 'posted_date',
               existing_type=sa.DATE(),
               nullable=False)
    op.add_column('barcode', sa.Column('exp_days', sa.Integer(), nullable=True))
    op.create_unique_constraint(op.f('uq_barcode_barcode'), 'barcode', ['barcode'])
    op.create_foreign_key(op.f('fk_barcode_b_category_id_barcode_categories'), 'barcode', 'barcode_categories', ['b_category_id'], ['b_category_id'])
    op.create_foreign_key(op.f('fk_barcode_company_id_barcode_companies'), 'barcode', 'barcode_companies', ['company_id'], ['company_id'])
    op.drop_column('barcode', 'expiry_date')
    op.create_unique_constraint(op.f('uq_barcode_categories_b_category_name'), 'barcode_categories', ['b_category_name'])
    op.create_unique_constraint(op.f('uq_barcode_companies_company_name'), 'barcode_companies', ['company_name'])
    op.create_unique_constraint(op.f('uq_ingredient_ingredient_name'), 'ingredient', ['ingredient_name'])
    op.alter_column('recipe_situation', 'situation_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.alter_column('recipe_situation', 'recipe_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_foreign_key(op.f('fk_recipe_situation_recipe_id_recipes'), 'recipe_situation', 'recipes', ['recipe_id'], ['recipe_id'])
    op.alter_column('recipes', 'recipe_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('recipes', 'recipe_desc',
               existing_type=sa.TEXT(),
               nullable=False)
    op.create_foreign_key(op.f('fk_situation_situation_id_recipe_situation'), 'situation', 'recipe_situation', ['situation_id'], ['situation_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_situation_situation_id_recipe_situation'), 'situation', type_='foreignkey')
    op.alter_column('recipes', 'recipe_desc',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('recipes', 'recipe_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.drop_constraint(op.f('fk_recipe_situation_recipe_id_recipes'), 'recipe_situation', type_='foreignkey')
    op.alter_column('recipe_situation', 'recipe_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('recipe_situation', 'situation_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.drop_constraint(op.f('uq_ingredient_ingredient_name'), 'ingredient', type_='unique')
    op.drop_constraint(op.f('uq_barcode_companies_company_name'), 'barcode_companies', type_='unique')
    op.drop_constraint(op.f('uq_barcode_categories_b_category_name'), 'barcode_categories', type_='unique')
    op.add_column('barcode', sa.Column('expiry_date', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(op.f('fk_barcode_company_id_barcode_companies'), 'barcode', type_='foreignkey')
    op.drop_constraint(op.f('fk_barcode_b_category_id_barcode_categories'), 'barcode', type_='foreignkey')
    op.drop_constraint(op.f('uq_barcode_barcode'), 'barcode', type_='unique')
    op.drop_column('barcode', 'exp_days')
    op.alter_column('article', 'posted_date',
               existing_type=sa.DATE(),
               nullable=True)
    op.create_table('recipe_ingredient',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('recipe_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ingredient_id', sa.INTEGER(), autoincrement=False, nullable=True)
    )
    op.drop_table('answer')
    op.drop_table('question')
    op.drop_table('fridge')
    op.drop_table('user')
    # ### end Alembic commands ###