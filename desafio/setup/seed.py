import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random, datetime
from fornecedores.models import  RegistroFornecedores

def criando_fornecedor(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        id = "{}{}{}".format("TESTE",random.randrange(100000, 999999),"TESTE" )
        name = fake.name()
        companies = ["Company1","Company2", "Company3"]
        company = random.choice(companies)
        created_at = fake.date_between(start_date='-18y', end_date='today')
        amount_products = random.randrange(1,10)
        a = RegistroFornecedores(name=name,company = company,created_at=created_at,amount_products = amount_products)
        a.save()


criando_fornecedor(10)