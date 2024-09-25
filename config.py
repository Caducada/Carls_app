from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import random
import datetime

db = SQLAlchemy()


class Person(db.Model):
    ID = db.Column(
        db.BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    name = db.Column(db.String(60), unique=False, nullable=False)
    personal_code = db.Column(db.String(16), unique=True, nullable=False)
    country = db.Column(db.String(60), unique=False, nullable=False)
    city = db.Column(db.String(60), unique=False, nullable=False)
    occupation = db.Column(db.String(60), unique=False, nullable=True)
    phone_number = db.Column(db.String(16), unique=False, nullable=True)


def get_countries():
    country_string = """Afghanistan 93 Albania 355 Algeria 213 AmericanSamoa 1684 Andorra 376 Angola 244 Anguilla 1264 Antarctica 6721 Antigua 1268 Argentina 54 Armenia 374 Aruba 297 Ascension 247 Australia 61 Austria 43 Azerbaijan 994 Bahamas 1242 Bahrain 973 Bangladesh 880 Barbados 1246 Belarus 375 Belgium 32 Belize 501 Benin 229 Bermuda 1441 Bhutan 975 Bolivia 591 BosniaandHerzegovina 387 Botswana 267 Brazil 55 BritishVirginIslands 1284 Brunei 673 Bulgaria 359 BurkinaFaso 226 Burundi 257 CaboVerde 238 Cambodia 855 Cameroon 237 Canada 1 CaymanIslands 1345 Chad 235 Chile 56 China 86 Colombia 57 Comoros 269 CookIslands 682 CostaRica 506 Coted'Ivoire 225 Croatia 385 Cuba 53 Curaçao 599 Cyprus 357 CzechRepublic 420 Denmark 45 Djibouti 253 Dominica 1767 DominicanRepublic 1809 Ecuador 593 Egypt 20 ElSalvador 503 EquatorialGuinea 240 Eritrea 291 Estonia 372 Eswatini 268 Ethiopia 251 FalklandIslands 500 FaroeIslands 298 Fiji 679 Finland 358 France 33 FrenchGuiana 594 FrenchPolynesia 689 Gabon 241 Gambia 220 GazaStrip 970 Georgia 995 Germany 49 Ghana 233 Gibraltar 350 Greece 30 Greenland 299 Grenada 1473 Guadeloupe 590 Guam 1671 Guatemala 502 Guinea 224 Guinea-Bissau 245 Guyana 592 Haiti 509 Honduras 504 HongKong 852 Hungary 36 Iceland 354 India 91 Indonesia 62 Iraq 964 Iran 98 Ireland 353 Israel 972 Italy 39 Jamaica 1876 Japan 81 Jordan 962 Kazakhstan 7 Kenya 254 Kiribati 686 Kosovo 383 Kuwait 965 Kyrgyzstan 996 Laos 856 Latvia 371 Lebanon 961 Lesotho 266 Liberia 231 Libya 218 Liechtenstein 423 Lithuania 370 Luxembourg 352 Macau 853 Madagascar 261 Malawi 265 Malaysia 60 Maldives 960 Mali 223 Malta 356 MarshallIslands 692 Martinique 596 Mauritania 222 Mauritius 230 Mayotte 262 Mexico 52 Moldova 373 Monaco 377 Mongolia 976 Montenegro 382 Montserrat 1664 Morocco 212 Mozambique 258 Myanmar 95 Namibia 264 Nauru 674 Netherlands 31 Nepal 977 NewCaledonia 687 NewZealand 64 Nicaragua 505 Niger 227 Nigeria 234 Niue 683 NorfolkIsland 6723 NorthKorea 850 NorthMacedonia 389 NorthernIreland 44 Norway 47 Oman 968 Pakistan 92 Palau 680 Palestine 970 Panama 507 PapuaNewGuinea 675 Paraguay 595 Peru 51 Philippines 63 Poland 48 Portugal 351 PuertoRico 1787 Qatar 974 Reunion 262 Romania 40 Russia 7 Rwanda 250 Saint-Barthélemy 590 SaintHelena 290 SaintKitts 1869 SaintLucia 1758 SaintMartin 590 SaintPierre 508 SaintVincent 1784 Samoa 685 SaoTome 239 SaudiArabia 966 Senegal 221 Serbia 381 Seychelles 248 SierraLeone 232 SintMaarten 1721 Singapore 65 Slovakia 421 Slovenia 386 SolomonIslands 677 Somalia 252 SouthAfrica 27 SouthKorea 82 SouthSudan 211 Spain 34 SriLanka 94 Sudan 249 Suriname 597 Sweden 46 Switzerland 41 Syria 963 Taiwan 886 Tajikistan 992 Tanzania 255 Thailand 66 Timor-Leste 670 Togo 228 Tokelau 690 Tonga 676 Trinidad 1868 Tunisia 216 Turkey 90 Turkmenistan 993 CaicosIslands 1649 Tuvalu 688 Uganda 256 Ukraine 380 UnitedArabEmirates 971 UnitedKingdom 44 UnitedStatesofAmerica 1 Uruguay 598 Uzbekistan 998 Vanuatu 678 Venezuela 58 Vietnam 84 U.S.VirginIslands 1340 WallisandFutuna 681 WestBank 970 Yemen 967 Zambia 260 Zimbabwe 263""".split(
        " "
    )
    country_book = {
        country_string[i]: country_string[i + 1]
        for i in range(0, len(country_string) - 1, 2)
    }
    return country_book


def fake_people():
    fake = Faker()
    calling_codes = get_countries()
    countries = [country for country in calling_codes.keys()]
    occupations = [
        "AI Ethics Officer",
        "Human-Machine Teaming Manager",
        "Digital Detox Therapist",
        "Quantum Computing Specialist",
        "Climate Change Reversal Engineer",
        "Biofabrication Specialist",
        "Virtual Habitat Designer",
        "Space Tourism Guide",
        "Personal Data Broker",
        "Genetic Diversity Officer",
        "Smart City Infrastructure Planner",
        "Virtual Lawyer",
        "Drone Traffic Controller",
        "Augmented Reality Architect",
        "3D-Printed Food Engineer",
        "Neuro-Implant Specialist",
        "Memory Surgeon",
        "Cybersecurity Insurance Analyst",
        "AI-Powered Tutor",
        "Waste Data Analyst",
        "Unemployed"
    ]
    for _ in range(10000):
        while True:
            min_year = 1930
            max_year = datetime.datetime.now().year
            start = datetime.datetime(min_year, 1, 1, 00, 00, 00)
            years = max_year - min_year + 1
            end = start + datetime.timedelta(days=365 * years)
            random_date = start + (end - start) * random.random()
            new_code = ""
            for i in range(4):
                new_code = new_code + str(random.randint(0, 9))
            code_duplicate = Person.query.filter_by(
                personal_code=random_date.strftime("%y%m%d") + "-" + new_code
            ).first()
            if not code_duplicate:
                break
        random_country = random.choice(countries)
        random_number = ""
        for i in range(9):
            random_number += str(random.randint(0, 9))
        new_person = Person(
            name=fake.name(),
            personal_code=random_date.strftime("%y%m%d") + "-" + new_code,
            city=fake.city() + fake.city_suffix(),
            country=random_country,
            phone_number="+"+calling_codes[random_country] +"-"+ random_number,
            occupation = occupations[random.randint(0, len(occupations)-1)]
        )
        db.session.add(new_person)
        db.session.commit()
        
