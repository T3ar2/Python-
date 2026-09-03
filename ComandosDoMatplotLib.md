# 🎨 Comandos importantes do Matplotlib

Este resumo reúne os comandos mais usados para personalizar gráficos no **Matplotlib**.

## Título do gráfico

Define o título principal.

```python
plt.title("Meu gráfico")
```

---

## Nome do eixo X

Define o nome do eixo horizontal.

```python
plt.xlabel("Eixo X")
```

---

## Nome do eixo Y

Define o nome do eixo vertical.

```python
plt.ylabel("Eixo Y")
```

---

## Mostrar o gráfico

Exibe o gráfico criado.

```python
plt.show()
```

Normalmente é usado no final:

```python
plt.plot(dados["CRIM"])
plt.show()
```

---

## Tamanho do gráfico

Define a largura e a altura da figura.

```python
plt.figure(figsize=(10, 6))
```

- `10` = largura
- `6` = altura

Exemplo:

```python
plt.figure(figsize=(10, 6))
plt.hist(dados["CRIM"].dropna(), bins=20)
plt.title("Distribuição de CRIM")
plt.show()
```

---

## Grade

Adiciona linhas de grade ao gráfico.

```python
plt.grid()
```

Exemplo:

```python
plt.scatter(dados["RM"], dados["MEDV"])
plt.title("RM x MEDV")
plt.xlabel("RM")
plt.ylabel("MEDV")
plt.grid()
plt.show()
```

---

## Legenda

Mostra a legenda das informações representadas no gráfico.

Primeiro, utilize `label`:

```python
plt.plot(dados["CRIM"], label="CRIM")
plt.plot(dados["MEDV"], label="MEDV")
```

Depois:

```python
plt.legend()
```

Exemplo completo:

```python
plt.plot(dados["CRIM"], label="CRIM")
plt.plot(dados["MEDV"], label="MEDV")

plt.title("Comparação de variáveis")
plt.xlabel("Índice")
plt.ylabel("Valor")

plt.legend()
plt.show()
```

---

## Limites do eixo X

Define quais valores serão mostrados no eixo X.

```python
plt.xlim(0, 100)
```

---

## Limites do eixo Y

Define quais valores serão mostrados no eixo Y.

```python
plt.ylim(0, 100)
```

---

## Rotacionar textos do eixo X

Pode ser útil quando os nomes das categorias são grandes.

```python
plt.xticks(rotation=45)
```

Exemplo:

```python
dados["CHAS"].value_counts().plot(kind="bar")
plt.xticks(rotation=45)
plt.show()
```

---

## Ajustar espaçamento automaticamente

Evita que títulos, nomes dos eixos ou categorias fiquem cortados.

```python
plt.tight_layout()
```

É comum utilizar antes do `plt.show()`:

```python
plt.tight_layout()
plt.show()
```

---

## Salvar o gráfico como imagem

Salva o gráfico em um arquivo.

```python
plt.savefig("grafico.png")
```

Exemplo:

```python
plt.hist(dados["CRIM"].dropna(), bins=20)
plt.title("Distribuição de CRIM")
plt.savefig("histograma_crim.png")
plt.show()
```

---

# 📌 Estrutura básica de um gráfico

```python
plt.figure(figsize=(10, 6))

plt.plot(dados["CRIM"], label="CRIM")

plt.title("Título do gráfico")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
```

---

# ⚡ Resumo rápido

| Comando | Função |
|---|---|
| `plt.title()` | Adiciona um título |
| `plt.xlabel()` | Nomeia o eixo X |
| `plt.ylabel()` | Nomeia o eixo Y |
| `plt.show()` | Exibe o gráfico |
| `plt.figure(figsize=(x, y))` | Define o tamanho do gráfico |
| `plt.grid()` | Adiciona uma grade |
| `plt.legend()` | Mostra a legenda |
| `plt.xlim()` | Define os limites do eixo X |
| `plt.ylim()` | Define os limites do eixo Y |
| `plt.xticks(rotation=45)` | Rotaciona os textos do eixo X |
| `plt.tight_layout()` | Ajusta o espaçamento |
| `plt.savefig()` | Salva o gráfico como imagem |
