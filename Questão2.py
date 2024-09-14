def contar_as(frase):
  # Converter toda a string para minúsculas para facilitar a contagem
  frase_minuscula = frase.lower()

  # Contar as ocorrências da letra 'a' usando o método count()
  contador = frase_minuscula.count('a')

  return contador

# Solicitar a entrada do usuário
texto = input("Digite uma frase: ")

# Chamar a função e imprimir o resultado
resultado = contar_as(texto)
print(f"A letra 'a' aparece {resultado} vezes na frase.")