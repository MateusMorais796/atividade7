# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.
valor_do_produto = float(input('Digite o preço do produto '))

preco_final = valor_do_produto * 1.12

print(f'O preço final do produto após a inserção do impoto é {preco_final}')