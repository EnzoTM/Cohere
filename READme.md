## Projeto de recomendações de músicas e de análise de popularidade
Equipe: Inimigos do Quartus

## Modelo de recomendações de musica

Utiliza os embeddings da Cohere e um dataset proveniente de Web Scrapping para achar música que sejam semanticamente próximas e mais comuns em relação aos titulos e Hashtags providas, com o objetivo de ajudar criadores de conteúdo a melhorar sua presença nas redes sociais 

## Modelo de análise de popularidade

Utiliza os embeddings do Cohere e um modelo ML de SVM (suport vector machine) para classificar posts (Titulos, hastags e Músicas) em virais ou não. Esse modelo atingiu uma métrica de Precisão e F1 perto dos 90%, como pode ser visto no arquivo classificacao.csv no folder ./classifier_training. O objetivo desse modelo é também ajudar criadores de conteúdos na criação de material que tenha alta viralidade e engajamento pelos usuários

## Data Pipeline
Para alimentar os modelos é utilizado uma API de web_scrapping para extrair conteudos dos posts do tik-tok, esse conteúdo é processado em um dataframe (arquivo .csv) apenas com features e labels utéis para os modelos. Esse pipeline é capaz de automaticamente extrair e processar grandes quantidades de dados para treinar os modelos

## Participantes
<ul>
  <li>Caue Paiva Lira: https://github.com/caue-paiva</li>
  <li>Enzo Tonon Morente: https://github.com/EnzoTM</li>
  <li>João Pedro Alves Notari Godoy: https://github.com/joaopgodoy</li>
  <li>Letícia Barbosa Neves: https://github.com/LeticiaBN</li>
  <li>Ayrton da Costa Ganem Filho: https://github.com/A1RT0N </li>
</ul>
