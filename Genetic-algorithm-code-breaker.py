from BruteForce import Brute, Force
from Cryptic import decrypt, encrypt, key_generator
from Evo import Generation

PASSWORD_LENGTH = 2
POSSIBLE = [chr(65+x) for x in range(26)]  # creats a list with "A" till "Z"

# Text originates from Wikipedia
# Text has a maximum fitness of 441 points
plain_text = """Biologie is de natuurwetenschap die zich richt op levende organismen, levensprocessen en levensverschijnselen. De biologie omvat een breed scala aan vakgebieden waarin men onderzoek doet naar fysieke structuur, chemische processen, moleculaire interacties, fysiologische mechanismen, ecologische samenhang, ontwikkeling en evolutie. Biologie erkent de cel als de fysieke basiseenheid van het leven, genen als de basiseenheid van erfelijke informatie en evolutie als het mechanisme achter het ontstaan en het uitsterven van soorten. Levende organismen zijn open systemen die in staat zijn te overleven door bruikbare omzettingen van energie en door handhaving van hun vitale toestand.
Moderne biologie is overwegend een exacte natuurwetenschap, waardoor experimentele, kwantitatieve benaderingen en causale verklaringen centraal staan. Per vakgebied worden echter verschillende onderzoeksmethoden gehanteerd: wiskundige of theoretische biologie omvat de filosofie van de biologie en gebruikt wiskundige methoden om kwantitatieve modellen te formuleren. Experimentele biologie omvat omvat beschrijvend onderzoek en empirische benaderingen, waarin de geldigheid van voorgestelde theorieën wordt getest. Veel principes uit de biologie zijn gebaseerd op de toepassing van scheikundige en natuurkundige wetten op levende systemen."""  # noqa: disable pylama warning
text = "".join(plain_text.upper().split(" "))

# Create key, and encrypted text
key = key_generator(PASSWORD_LENGTH, POSSIBLE)
print(f"The Key is:{key}")
encrypted_text = encrypt(key, text)


# Start of program
my_choise = input(
    "Whould you like to use \"{}\", \"{}\" or \"{}\"?".format(
        "genetic algorithm[g]",
        "brute force[b]",
        "stop[S]"
    ))

if my_choise.upper() in ["G", "B"]:
    if my_choise.upper() == "G":
        # Using the genetic algorithm
        gen = Generation(100, POSSIBLE, encrypted_text)
        found_key = gen.start(PASSWORD_LENGTH)
    else:
        # Using the bruteforce method
        brute = Brute(POSSIBLE, PASSWORD_LENGTH)
        force = Force(brute)
        found_key = force.start(encrypted_text)
    # print the key
    print(
        "I think it's :{}\nKey:{}".format(
            decrypt(found_key, encrypted_text), found_key))
