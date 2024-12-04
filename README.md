# Nekilnojamojo Turto Kainų Analizė su PCA (Pagrindinių Komponentų Analizė)

Šis projektas skirtas nekilnojamojo turto duomenų analizei naudojant Pagrindinių Komponentų Analizę (PCA), kad būtų galima įvertinti, kaip įvairūs nekilnojamojo turto ypatybės (pvz., kaina, plotas, kambarių skaičius ir kt.) prisideda prie kainų pokyčių. Analizė apima ir duomenų paruošimą, ir vizualizaciją, kad būtų galima geriau suprasti, kaip kiekvienas faktorius veikia kainą.

## Projekto apžvalga

1. **Duomenų įkėlimas** – duomenys įkeliami iš CSV failo.
2. **Duomenų paruošimas** – atskiriamos skaitinės ir kategorinės funkcijos.
3. **Kategorinių kintamųjų kodavimas** – naudojant `OneHotEncoder`, kategoriniai kintamieji konvertuojami į skaitines reikšmes.
4. **Duomenų skalavimas** – visi kintamieji skaluojami į tą pačią skalę, naudojant `StandardScaler`.
5. **PCA (Pagrindinių Komponentų Analizė)** – atliekama PCA, siekiant identifikuoti pagrindinius kintamuosius, kurie paaiškina didžiausią variaciją duomenyse.
6. **Vizualizacijos** – sukuriamos stulpelinės diagramos, rodančios paaiškinamąją dispersiją per komponentus, pirmų ir antrų komponentų įkrovos reikšmes.

## Reikalavimai

Norėdami vykdyti šį projektą, turite įdiegti šias bibliotekas:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Galite įdiegti visas priklausomybės naudodami šį komandą:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn

Projekto struktūra
    • housing.csv - CSV failas su nekilnojamojo turto duomenimis.
    • main.py - Python skriptas, kuris vykdo duomenų analizę ir vizualizacijas.
    • README.md - Projekto aprašymas ir instrukcijos.
Kaip naudoti
    1. Paruoškite duomenis: Užtikrinkite, kad turite housing.csv failą, kuriame yra duomenys apie nekilnojamąjį turtą. Failas turi turėti bent šiuos stulpelius: price, area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus.
    2. Paleiskite analizę: Atsidarykite main.py failą ir paleiskite jį. Jame bus atlikta šių veiksmų seką:
        ◦ Duomenų įkėlimas ir paruošimas.
        ◦ Kategorinių kintamųjų kodavimas ir skalavimas.
        ◦ PCA analizė ir rezultatų vizualizacija.
    3. Rezultatai:
        ◦ Būsime sugeneravę stulpelines diagramas, kurios parodys:
            ▪ Paaiškinamąją dispersiją per PCA komponentus.
            ▪ Pirmų ir antrų komponentų įkrovų reikšmes.
        ◦ Šios diagramos padės vizualizuoti, kaip įvairios nekilnojamojo turto ypatybės prisideda prie kainos pokyčių.
Vizualizacijos
    • PCA Explained Variance per Component: Diagramoje rodomas paaiškinamųjų komponentų prisidėjimas prie bendros variacijos.
    • Pirmų ir antrų komponentų įkrovos: Parodoma, kaip įvairios funkcijos (pvz., bedrooms, bathrooms) prisideda prie pirmų dviejų PCA komponentų.
Išvados
    • Pagrindinė analizės tikslas yra suprasti, kurie veiksniai turi didžiausią įtaką nekilnojamojo turto kainoms.
    • PCA leidžia sumažinti duomenų matmenų skaičių ir padeda geriau suprasti svarbiausias ypatybes.
Priklausomybės
Šiam projektui naudotos bibliotekos:
    • NumPy - naudojama skaitinių duomenų apdorojimui.
    • Pandas - naudojama duomenų struktūroms ir manipuliacijai duomenimis.
    • Scikit-learn - naudojama PCA ir duomenų skalavimui.
    • Matplotlib ir Seaborn - naudojamos vizualizacijoms kurti.
Licencija
Projektas yra atvirojo kodo, licencijuotas pagal MIT licenciją.

### Paaiškinimas:

- **Projekto apžvalga**: Trumpai paaiškinama, ką projektas daro ir kaip jis struktūruotas.
- **Reikalavimai**: Aprašyta, kokios bibliotekos reikalingos šiam projektui.
- **Kaip naudoti**: Instrukcijos, kaip paleisti ir naudoti projektą.
- **Vizualizacijos**: Trumpas aprašymas, ką galima tikėtis matyti iš grafiko.
- **Išvados**: Projekto tikslas ir tai, ką galima pasiekti naudojant šį metodą.
- **Priklausomybės**: Aprašytos naudojamos bibliotekos.
- **Licencija**: Atvirojo kodo licencija pagal MIT licenciją. 

Tikiuosi, kad šis `README.md` failas padės aiškiai apibūdinti jūsų projektą ir kaip jį naudoti!
