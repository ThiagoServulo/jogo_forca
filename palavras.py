from random import choice
from unicodedata import normalize

palavras = ['Carnaval', 'Cachorro', 'Geladeira', 'Televisão', 'Celular', 'Veículo', 'Porteira', 'Futebol', 'Basquete',
            'Elefante', 'Gaveta', 'Gramado', 'Computador', 'Trabalho', 'Ambiente', 'Garçom', 'Martelo', 'Melancia',
            'Refrigerante', 'Calendário', 'Recompor', 'Caderno', 'Adrenalina', 'Finanças', 'Gorila', 'Hospital',
            'Igreja', 'Jaboticaba', 'Londrina', 'Morder', 'Nômade', 'Obscuro', 'Carruagem', 'Caldeirão',
            'Construtora', 'Sabonete', 'Refrigerador', 'Impressionar', 'Padeiro', 'Credibilidade', 'Casamento',
            'Perpendicular', 'Assintomático', 'Discriminação', 'Heterosexual', 'Indispensável', 'Irresponsável',
            'Possibilidade', 'Provavelmente', 'Complexo', 'Esporte', 'Generalizar', 'Conferir', 'Divertir',
            'Redundância', 'Atravessar', 'Travesseiro', 'Cobertor', 'Reinvindicar', 'Cipotânea', 'Presentear',
            'Faculdade', 'Imortal', 'Consolidar', 'Distinguir', 'Exagerado', 'Satisfação', 'Admirável', 'Apostilas',
            'Lisonjeado', 'Juramento', 'Jumento', 'Advogado', 'Engenharia', 'Profissão', 'Professora', 'Presidente',
            'Vereador', 'Farmácia', 'Sapatilha', 'Disposição', 'Óculos', 'Dificuldade', 'Deficiente', 'Carteira',
            'Documento', 'Arquivo', 'Palestra', 'Pandemia', 'Abdomen', 'Preferência', 'Eliminado', 'Foragido',
            'Fechadura', 'Girafa', 'Borboleta', 'Calculadora', 'Presente', 'Papelão', 'Alumínio', 'Plástico',
            'Ferrugem', 'Girassol', 'Júpter', 'Saturno', 'Laranja', 'Vermelho', 'Cabeça', 'Feriado', 'Sábado',
            'Domingo', 'Prateleiras', 'Diferenças', 'Entretanto', 'Privilégio', 'Ratoeira', 'Tornozeleira',
            'Extensão', 'Gratidão', 'Vagabundo', 'Esperança']


def sortear_palavra():
    palavra_sorteada = choice(palavras)
    palavra_normalizada = normalize('NFKD', palavra_sorteada).encode('ASCII', 'ignore').decode('ASCII')
    palavra_normalizada = palavra_normalizada.lower()
    palavra_sorteada = palavra_sorteada.lower()
    # print(palavra_sorteada, palavra_normalizada)
    return palavra_sorteada, palavra_normalizada
