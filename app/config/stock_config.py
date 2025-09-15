# Stock pricing configuration
# Tämä tiedosto sisältää kaikki osakehintojen laskentaan liittyvät konfiguraatioarvot
# Voit säätää näitä arvoja muuttamatta koodia!

STOCK_CONFIG = {
    # Hinnankorotuksen painokertoimet (weights)
    # Nämä määrittävät kuinka paljon kukin tekijä vaikuttaa loppuhintaan
    "price_change_weights": {
        "market_impact": 0.3,  # 30% - kuinka suuri osa markkinoista ostetaan
        "scarcity_factor": 0.2,  # 20% - kuinka harvinaisia osakkeet ovat
        "log_factor": 0.1,  # 10% - logaritminen kasvu (ei liian jyrkkä)
        "volatility": 1.0,  # 100% - satunnainen volatiliteetti (ei kerrointa = täysi vaikutus)
    },
    # Markkinoiden herkkyys - kuinka agressiivisesti hinta reagoi
    "market_sensitivity": 0.05,  # 5% - logaritmisen kasvun "aggressiivisuus"
    # Volatiliteetin alue - kuinka paljon hinta voi satunnaisesti vaihdella
    "volatility_range": 0.01,  # ±1% - satunnaisuuden määrä
    # Maksimi hinnanmuutos per kauppa - estää liian jyrkät muutokset
    "max_price_change": 0.2,  # 20% - enintään 20% muutos per kauppa
    # Normaali tarjonta - vertailupiste harvinaisuuden laskentaan
    "normal_supply": 100,  # 100 osaketta = "normaali" tarjonta
}

# Esimerkkejä eri pelityyleistä:
#
# KONSERVATIIVINEN (vakaat hinnat):
# 'market_impact': 0.4, 'scarcity_factor': 0.3, 'log_factor': 0.2, 'volatility': 0.1
#
# AGRESSIIVINEN (villit hinnat):
# 'market_impact': 0.2, 'scarcity_factor': 0.1, 'log_factor': 0.1, 'volatility': 0.6
#
# TASAPAINOINEN (kaikki tekijät yhtä tärkeitä):
# 'market_impact': 0.25, 'scarcity_factor': 0.25, 'log_factor': 0.25, 'volatility': 0.25
