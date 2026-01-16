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

MORSE_RU = {v: k for k, v in RU_MORSE.items()}

choose = int(input('1: Алфавит в морзе.\n2: Морзе в алфавит\n Ваш выбор: '))

if choose == 1:
    text = input('Введите текст.\n').lower()
    words = text.split()
    morse_words = []
    for word in words:
        morse_word = ''
        for char in word:
            morse_word += (RU_MORSE[char] + ' ')
        morse_words.append(morse_word)
  
    morse_text = '/'.join(morse_words)
    print(morse_text)
    
if choose == 2:
    morse_text = input('Введите текст на морзянке.\n')
    morse_words = morse_text.split('/')
    words = []
    for morse_word in morse_words:
        morse_letters = morse_word.split()
        word = ''
        for char in morse_letters:
            word += MORSE_RU[char]
        words.append(word)
    
    text = ' '.join(words)
    print(text)

