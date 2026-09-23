# Oferta de Destaque da Classificação da Fórmula 1 no Globoplay

- **Status:** Em Revisão
- **Data:** 24/10/2023
- **Autor / Time:** Time de Produto Globoplay (Esportes & Transmissão Live)

---

## 1. Visão Geral e Problema

Os treinos classificatórios da Fórmula 1 (geralmente realizados aos sábados) representam um dos momentos de maior pico de engajamento da categoria, pois definem a ordem de largada para a corrida principal. No entanto, análises de jornada do usuário no Globoplay apontaram dificuldades na rápida identificação e acesso à transmissão ao vivo da classificação na página inicial (Home) e no hub de Esportes.

Atualmente, a navegação até a transmissão exige múltiplos passos e navegação manual nos canais ao vivo (Sportv), resultando em:
1. Perda de audiência nos minutos iniciais críticos da classificação (Q1/Q2/Q3).
2. Subaproveitamento do momento de pico para conversão de assinantes do pacote *Globoplay + Canais ao Vivo*.
3. Experiência fragmentada e falta de contexto em tempo real sobre o status do treino.

A proposta deste PRD é estruturar a **Oferta de Destaque da Classificação da Fórmula 1**, garantindo visibilidade prioritária, atalhos diretos para a transmissão e ofertas contextuais para usuários não assinantes.

---

## 2. Porquês de Negócio e Dados (Why & Context)

- **Comportamento do Consumidor:** Dados de telemetria indicam que **42% dos espectadores de F1** acessam a plataforma nos 10 minutos que antecedem o início do treino classificatório.
- **Impacto no Player (Time to Play):** Usuários que encontram a transmissão em até 2 cliques apresentam **retenção 28% maior** durante a transmissão em relação a usuários que passam por mais de 4 etapas de navegação.
- **Oportunidade de Aquisição e Upgrade:** A classificação da F1 possui alta intenção de consumo imediato, tornando-se um gatilho valioso para conversões no fluxo de paywall para o plano *Globoplay + Canais ao Vivo* (Sportv).
- **Alinhamento Estratégico:** Fortalecer o Globoplay como o principal hub de streaming esportivo ao vivo no Brasil.

---

## 3. Métricas de Sucesso e KPIs

| Métrica | Meta / Indicador |
| :--- | :--- |
| **CTR no Card de Destaque** | Aumento de **+25%** no clique para o live streaming durante o horário do evento. |
| **Time to Play (Tempo até o vídeo)** | Redução do tempo médio de navegação para **< 5 segundos** a partir da entrada no app/web. |
| **Conversão de Assinaturas (Paywall)** | Incremento de **+10%** nas conversões/upgrades para *Globoplay + Canais ao Vivo* via oferta contextual no card. |
| **Pico de Audiência Simultânea** | Crescimento de **+15%** no *Concurrent Viewers* (CVU) durante a transmissão do treino classificatório. |

---

## 4. Escopo e Requisitos Funcionais

### 4.1. Card Hero Dinâmico de Destaque
- Exibição de um card/banner especial no topo da Home (Hero) e no Hub de Esportes durante a janela temporal do treino classificatório (a partir de 1 hora antes até o encerramento da sessão).
- Exibição do nome do Grande Prêmio (ex: *GP de São Paulo - Classificação*), localização do circuito e contagem regressiva pré-evento.

### 4.2. Badge de Status em Tempo Real
- Exibição visual de status no card:
  - `EM BREVE` (com contagem regressiva antes da sessão).
  - `AO VIVO` (durante o Q1, Q2 e Q3).
  - `ENCERRADO` (após a conclusão do treino, com redirecionamento para o VOD dos melhores momentos).

### 4.3. Redirecionamento Direto (Deep Linking)
- **Assinantes Elegíveis:** Clique no card abre imediatamente o player em tela cheia na transmissão ao vivo do Sportv/Globo.
- **Não Assinantes:** Clique no card aciona o modal da Oferta de Destaque com o gatilho de assinatura/upgrade do pacote *Globoplay + Canais ao Vivo*.

### 4.4. Mecanismo de Lembrete / Notificação
- Para usuários navegando no período `EM BREVE`, funcionalidade de ativar botão "Definir Lembrete".
- Envio de notificação Push 15 minutos antes do início do Q1 para os usuários que ativaram a opção.

---

## 5. Questões em Aberto (Open Questions) & Riscos

| ID | Questão em Aberto / Risco | Impacto | Responsável | Status / Ação |
| :--- | :--- | :--- | :--- | :--- |
| **OQ-01** | Se a classificação for transmitida em sinal aberto (TV Globo) e fechado (Sportv) simultaneamente, qual fluxo deve ser priorizado no clique? | Alto | Negócio / Direitos | Pendente de confirmação com a equipe de Direitos de Transmissão. |
| **OQ-02** | O status das etapas do treino (Q1, Q2, Q3, Bandeira Vermelha) será alimentado via API automática ou controle operacional manual? | Médio | Arquitetura de Dados / Operações | Mapear disponibilidade de dados de telemetria da F1. |
| **R-01** | Latência na atualização do status "AO VIVO" pode levar usuários a acessarem o player antes da liberação do sinal de transmissão. | Alto | Engenharia de Vídeo / Streaming | Garantir fallback de sinal ou tela de aguarde no player. |

---

## 6. Critérios de Aceite

### Cenário 1: Acesso direto à transmissão por assinante elegível (Ao Vivo)
- **Dado que** o usuário possui uma assinatura ativa do pacote *Globoplay + Canais Ao Vivo*
- **E** a sessão de classificação da F1 está acontecendo ao vivo (Status: `AO VIVO`)
- **Quando** o usuário acessa a página inicial (Home) do Globoplay
- **Então** o card de destaque da F1 deve ser exibido na posição principal do Hero Banner com a indicação "AO VIVO"
- **E** ao clicar no card, o usuário deve ser redirecionado diretamente para o player com a transmissão do canal ao vivo sem etapas intermediárias.

### Cenário 2: Acionamento da oferta de assinatura para usuário não elegível
- **Dado que** o usuário está logado com uma conta do plano *Globoplay Padrão* (sem canais ao vivo)
- **E** a classificação da F1 está sendo transmitida exclusivamente no canal Sportv
- **Quando** o usuário clica no card de destaque da F1 na Home
- **Então** o sistema deve exibir o modal de Oferta de Destaque da F1
- **E** o modal deve apresentar os benefícios do pacote *Globoplay + Canais ao Vivo* acompanhado do botão de confirmação de assinatura/upgrade.

### Cenário 3: Agendamento de lembrete pré-evento
- **Dado que** a classificação da F1 está agendada para iniciar em 2 horas (Status: `EM BREVE`)
- **E** o usuário está navegando na Home do Globoplay
- **Quando** o usuário clica no botão "Definir Lembrete" no card de destaque da F1
- **Então** o estado do botão deve mudar para "Lembrete Ativado"
- **E** uma notificação push deve ser agendada para ser enviada ao dispositivo do usuário 15 minutos antes do início do evento.
