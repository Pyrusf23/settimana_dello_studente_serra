"""empty message

Revision ID: feb5c427776f
Revises: 
Create Date: 2022-01-22 17:25:33.455565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'feb5c427776f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('denominazione', sa.String(length=40), nullable=False),
    sa.Column('num_posti', sa.Integer(), nullable=False),
    sa.Column('centrale_succursale', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('denominazione')
    )
    op.create_table('classi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classe_sezione', sa.String(length=40), nullable=False),
    sa.Column('centrale_succursale', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('classe_sezione')
    )
    op.create_table('materie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome_materia', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome_materia')
    )
    op.create_table('orari',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('giorno', sa.Integer(), nullable=False),
    sa.Column('ora', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('attivita',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_aula', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=80), nullable=False),
    sa.Column('descrizione', sa.String(length=100), nullable=False),
    sa.Column('responsabile', sa.String(length=50), nullable=False),
    sa.Column('num_iscritti', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_aula'], ['aule.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('orari_materie_classi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_orario', sa.Integer(), nullable=False),
    sa.Column('id_materia', sa.Integer(), nullable=False),
    sa.Column('id_classe', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_classe'], ['classi.id'], ),
    sa.ForeignKeyConstraint(['id_materia'], ['materie.id'], ),
    sa.ForeignKeyConstraint(['id_orario'], ['orari.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('utenti',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('id_classe', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_classe'], ['classi.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('attivita_orari',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_attivita', sa.Integer(), nullable=False),
    sa.Column('id_orario', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_attivita'], ['attivita.id'], ),
    sa.ForeignKeyConstraint(['id_orario'], ['orari.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('utenti_attivita',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_utente', sa.Integer(), nullable=False),
    sa.Column('id_attivita_orario', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_attivita_orario'], ['attivita_orari.id'], ),
    sa.ForeignKeyConstraint(['id_utente'], ['utenti.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('utenti_attivita')
    op.drop_table('attivita_orari')
    op.drop_table('utenti')
    op.drop_table('orari_materie_classi')
    op.drop_table('attivita')
    op.drop_table('orari')
    op.drop_table('materie')
    op.drop_table('classi')
    op.drop_table('aule')
    # ### end Alembic commands ###
