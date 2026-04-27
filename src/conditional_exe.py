phrase = """
Britannian kuningas Charles III ja kuningatar Camilla ovat saapuneet valtiovierailulle Yhdysvaltoihin. Kuningas tapaa presidentti Donald Trumpin lyhyesti jo tänään maanantaina. Yle näytti suorana, kuinka presidentti Trump ja hänen Melania-puolisonsa toivottivat kuninkaallisen parin tervetulleeksi Valkoisen talon ovella.

Vierailua vietetään tiukkojen turvatoimien keskellä, sillä viime lauantaina Valkoisen talon kirjeenvaihtajaillallisella tapahtui ammuskelu.

Kuninkaallisen parin vierailun on määrä kestää neljä päivää. Tiistaina Charles puhuu Yhdysvaltain kongressissa. Trump isännöi juhlaillalliset Valkoisessa talossa.

Britannian ja Yhdysvaltain perinteisesti läheinen suhde on viime aikoina viilentynyt, sillä Trump on arvostellut pääministeri Keir Starmeria kovin sanoin Britannian puuttuvasta tuesta sotatoimille Irania vastaan.

Valtiovierailun virallisena teemana on juhlistaa Yhdysvaltain 250-vuotista itsenäisyyttä brittien siirtomaavallasta."""

phrase_list = phrase.split(" ")
print(phrase_list)
tot = 0
for i in phrase_list:
    if i == "on":
        tot += 1
print(tot)