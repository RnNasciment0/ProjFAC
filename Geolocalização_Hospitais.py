from geopy.distance import geodesic
from geopy.geocoders import Nominatim

# Sua localização atual (latitude, longitude)
minha_localizacao = (-22.9068, -43.1729)  # Exemplo: Rio de Janeiro

# Lista de hospitais com suas localizações
# Você precisaria de um banco de dados real para uma lista completa de hospitais
hospitais = {

    "Hospital Doutor Luiz Palmier": (-22.829230935588672, -43.054181482520086),

    "Hospital Estadual Alberto Torres": (-22.8385539588167, -43.018379540986224),

    "HCCOR - HOSPITAL DO CÂNCER E DO CORAÇÃO, Estr. do Pacheco, 216 A - Lagoinha, São Gonçalo": (-22.82399636712947, -42.979617854016006),

    "Upa do Pacheco": (-22.82460494834542, -42.96878357480135),

    "Posto De Saúde -  USF Emílio Ribas": (-22.82540941757022, -42.96284992476688),

    "Upa Municipal Nova CIDADE":  (-22.80931506294839, -43.02400336842124),

    "Pronto Socorro De Alcântara": (-22.818353817665596, -43.012112004867774),

    "Clínica Municipal Goncalense":  (-22.818168679439047, -43.01094783933682),

    "P.A.M - Posto de Assistência Médica do Coelho": (-22.82994514291061, -42.998788490104005),

    "Upa Santa Luzia": (-22.80555187785824, -42.98006901973282),

    "UPA 24h São Gonçalo II":  (-22.805298697497197, -42.980010045645614),

    "UPA Colubandê": (-22.835011648043178, -43.00755131609982),

    "USF LUIZ PAULO GUIMARÃES": (-22.81508757047166, -42.986719819505105),

    "Hospital Universitário Antônio Pedro":  (-22.895253209175078, -43.11206625442229),

    "Hospital Municipal Carlos Tortelly": (-22.895518245393408, -43.110314406553044),

    "Hospital Municipal Getúlio Vargas Filho": (-22.88116256565529, -43.07854828236565),

    "Hospital Estadual Azevedo Lima": (-22.880126176591293, -43.07830966725581),

    "UPA Unidade de Pronto Atendimento Mário Monteiro":  (-22.9293354692223, -43.06271133467352),

    "SES RJ UPA 24 H FONSECA": (-22.884019323510135, -43.083156871156206),

    "Hospital Municipal Oceânico Dr. Gilson Cantarino": (-22.943076722932013, -43.06159665980971),

    "Policlínica Regional do Largo da Batalha":(-22.907498891708574, -43.067384497063706),

    "Policlinica Comunitária da Engenhoca - Policlinica Regional Dr. Renato Silva": (-22.872711045281847, -43.094790844568635),

    "Hospital Municipal Dr Nelson de Sá EAP":   (-22.507563218876925, -43.19243950781399),

    "Centro de Saúde Professor Manoel José ferreira":  (-22.508451224932763, -43.16817734139856),

    "Unidade de Pronto Atendimento (UPA) - Centro":  (-22.516412110711162, -43.184061084662616),

    "Hospital Municipal Souza Aguiar": (-22.90819718835464, -43.189626828222735),

    "Hospital Getúlio Vargas": (-22.839271142629237, -43.28452894515571),

    "Hospital Municipal Salgado Filho": (-22.900498856401914, -43.277996613127655),

    "Hospital Estadual Carlos Chagas": (-22.86541065539507, -43.374015470181526),

    "Hospital Municipal Ronaldo Gazolla": (-22.825806750657595, -43.34805845876726),

    "Hospital Municipal Miguel Couto": (-22.97772144414472, -43.223690405266204),

    "Hospital Estadual Anchieta": (-22.875943637293485, -43.222243554033646),

    "Hospital Municipal Rocha Maia": (-22.953469785139312, -43.176875859471),

    "Hospital Municipal Nossa Senhora do Loreto": (-22.81465058404345, -43.225824049740034),

    "Hospital Federal de Bonsucesso": (-22.86641068783621, -43.248657121517475),

    "UPA Centro": (-22.90926555192002, -43.19066321726042),

    "UPA Botafogo 24h": (-22.949889026429634, -43.18465211340462),

    "Hospital Municipal Carlos Tortelly (antigo CPN)": (-22.89562036367323, -43.11006989833802),

    "Hospital Municipal Duque de Caxias": (-22.782603048010774, -43.31926663362164),

    "UPA Penha - Valéria Modesto dos Santos": (-22.838078319119006, -43.28719391706986),
}

# Calcule a distância entre a sua localização e cada hospital
distancias = {}
for hospital, localizacao in hospitais.items():
    distancias[hospital] = geodesic(minha_localizacao, localizacao).kilometers

# Encontre o hospital mais próximo
hospital_mais_proximo = min(distancias, key=distancias.get)

print("O hospital mais próximo é:", hospital_mais_proximo)

# Obtenha o endereço do hospital mais próximo
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.reverse(hospitais[hospital_mais_proximo], exactly_one=True)
endereco = location.address

print("Endereço:", endereco)

