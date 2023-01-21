from pandas import read_table



# OBS: você precisa por o link do google maps já com o endereço da sua casa, e o meio de transporte a pé
# fiz porque precisava achar os locais mais proximo que estava aplicando a vacina da covid sem precisar marcar horario.
def enderecos(n, endereco):
    """ Pega o endereço e o index, joga o endereço no google maps
    pega a distancia a pé da sua casa até o endereço e depois salva em uma lista
    Args:
        n (int): index
        endereco (str): endereço

    Returns:
        _str_: retorna o index, endereço e a distancia (em hr ou min) da sua casa pro local
    """
    from selenium.webdriver import Chrome
    from selenium.webdriver.common.keys import Keys
    from time import sleep
    brow = Chrome()
    brow.get('')
    sleep(3)
    brow.find_element('xpath', '//*[@id="sb_ifc51"]/input').send_keys(item)
    brow.find_element('xpath', '//*[@id="sb_ifc51"]/input').send_keys(Keys.ENTER)
    sleep(2)
    distancia = brow.find_element('xpath', '//*[@id="section-directions-trip-0"]/div[1]/div[3]/div[1]/div[1]').get_property('innerText')
    brow.close()
    return [f'{n}: {endereco}', [distancia]]


arquivo = read_table(r'enderecos.tsv')
lista = []

for index, item in enumerate(arquivo):
    print(f'{index}: {item}')
    endereco = enderecos(index, item)
    lista.append(endereco)
