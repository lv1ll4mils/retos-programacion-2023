import random

opciones = ["🗿", "📄", "✂️", "🦎", "🖖"]

reglas = {
    "🗿": ["✂️", "🦎"], # piedra gana a tijeras y lagarto
    "📄": ["🗿", "🖖"], # papel gana a piedra y spock
    "✂️": ["📄", "🦎"], # tijeras gana a papel y lagarto
    "🦎": ["📄", "🖖"], # lagarto gana a papel y spock
    "🖖": ["✂️", "🗿"]  # spock gana a tijeras y piedra
}