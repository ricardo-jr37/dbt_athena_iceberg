# Função para gerar o DataFrame
def generate_consumer_cases(num_cases):
    from datetime import datetime
    import pandas as pd
    from faker import Faker
    import random
    
    # Inicializar o Faker
    data_hora_etl = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    fake = Faker('pt_BR')

    # Gerar IDs únicos aleatórios
    case_ids = [str(random.randint(-2**63, 2**63 - 1)) for _ in range(num_cases)]   
    
    data = {
        'case_id': case_ids,
        'consumer_name': [fake.name() for _ in range(num_cases)],
        'product': [fake.random_element(elements=('Geladeira', 'Celular', 'Televisão', 'Notebook', 'Máquina de Lavar', 
                                                  'Fogão', 'Micro-ondas', 'Aspirador de Pó', 'Ar Condicionado', 'Tablet')) for _ in range(num_cases)],
        'issue': [fake.random_element(elements=('Produto com defeito', 'Atraso na entrega', 'Não corresponde à descrição', 'Defeito técnico', 
                                                'Produto avariado', 'Mau atendimento', 'Garantia não cumprida', 'Cobrança indevida', 
                                                'Cancelamento de pedido', 'Suporte técnico ineficiente')) for _ in range(num_cases)],
        'date_reported': [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_cases)],
        'company': [fake.company() for _ in range(num_cases)],
        'status': [fake.random_element(elements=('Resolvido', 'Pendente', 'Em análise', 'Não resolvido')) for _ in range(num_cases)],
        'resolution_date': [fake.date_between(start_date='today', end_date='+1y') for _ in range(num_cases)],
        'violation_type': [fake.random_element(elements=('Defeito', 'Atraso', 'Descrição', 'Defeito', 'Avaria', 
                                                         'Atendimento', 'Garantia', 'Cobrança', 'Cancelamento', 'Suporte')) for _ in range(num_cases)],
        'compensation_amount': [round(fake.random_number(digits=4), 2) for _ in range(num_cases)]
    }

    df = pd.DataFrame(data)
    df['date_reported'] = pd.to_datetime(df['date_reported'])
    df['resolution_date'] = pd.to_datetime(df['resolution_date'])
    df.loc[df.status !=  'Resolvido', 'resolution_date'] = pd.NA
    df.loc[:, 'updated_at'] = data_hora_etl
    return df
