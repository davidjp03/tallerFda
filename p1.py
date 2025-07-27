def sura_counter(inicio: str, fin: str, tam: int):
    inicio.lower()
    fin.lower()
    count = 0
    consonante_counts = {}
    vocals = "aeiouáéíóú"
    
    with open("RPY1_diccionario.txt", "r", encoding="utf-8") as file:
        for line in file:
            words = line.strip().lower()
            if words.startswith(inicio) and words.endswith(fin) and len(words) == tam:
                count += 1
                for letter in words:
                    if letter not in vocals and letter.isalpha() and letter != inicio and letter != fin:
                        if letter not in consonante_counts:
                            consonante_counts[letter] = 0
                        consonante_counts[letter] += 1 
                        
    max_consonante = max(consonante_counts.values(), default=0)
    consonantes_mas_frecuentes = [k for k, v in consonante_counts.items() if v == max_consonante]
    return count, consonantes_mas_frecuentes

# Example usage
print(sura_counter("ñ", "o", 5))
