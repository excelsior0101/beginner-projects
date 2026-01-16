RU_MORSE = {
    'а': '.-', 'б': '-...', 'в': '.--',
    'г': '--.', 'д': '-..', 'е': '.',
    'з': '--..', 'ж': '...-', 'и': '..',
    'й': '.---', 'к': '-.-', 'л': '.-..',
    'м': '--', 'н': '-.', 'о': '---',
    'п': '.--.', 'р': '.-.', 'с': '...',
    'т': '-', 'у': '..-', 'ф': '..-.',
    'х': '....', 'ц': '-.-.', 'ч': '---.',
    'ш': '----', 'щ': '--.-', 'ь': '-..-',
    'ы': '-.--', 'э': '..-..', 'ю': '..--', 'я': '.-.-'
}

choose = int(input('1: Алфавит в морзе.\n2: Морзе в алфавит\n Ваш выбор: '))

if choose == 1:
    text = input('Введите текст.\n').lower()
    words = text.split()
    morse_words = []
    for word in words:
        morse_word = ' '
        for char in word:
            morse_word += RU_MORSE[char]
        morse_words.append(morse_word)
        
morse_text = " ".join(morse_words)

print(morse_words)    
print(morse_text)
    