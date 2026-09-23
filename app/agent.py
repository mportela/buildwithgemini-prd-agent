# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types


MODEL = "gemini-3.6-flash"

PRD_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "prds")


def save_prd(title: str, content: str) -> str:
    """Salva um documento de PRD (Product Requirements Document) no repositório de artefatos da empresa.

    Args:
        title: O título do PRD ou da iniciativa (ex: 'recuperacao_carrinho_abandonado').
        content: O conteúdo completo do PRD formatado em Markdown, com todas as seções de negócio, requisitos, métricas, critérios de aceite e open questions.

    Returns:
        Uma mensagem de confirmação com o caminho onde o artefato foi salvo com sucesso.
    """
    os.makedirs(PRD_DIR, exist_ok=True)
    slug = re.sub(r"[^a-zA-Z0-9_-]", "_", title.lower()).strip("_")
    filename = f"{slug}.md"
    file_path = os.path.join(PRD_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"PRD '{title}' salvo com sucesso em: {file_path}"


def list_prds() -> str:
    """Lista todos os PRDs já criados e salvos no repositório de artefatos da empresa.

    Returns:
        Uma lista com os nomes dos arquivos de PRD disponíveis ou um aviso se nenhum for encontrado.
    """
    if not os.path.exists(PRD_DIR):
        return "Nenhum PRD encontrado no diretório de artefatos."
    files = [f for f in os.listdir(PRD_DIR) if f.endswith(".md")]
    if not files:
        return "Nenhum PRD encontrado no diretório de artefatos."
    return "PRDs encontrados no repositório:\n" + "\n".join(f"- {f}" for f in sorted(files))


def read_prd(filename: str) -> str:
    """Lê o conteúdo completo de um PRD existente para consulta, revisão ou continuidade de uma sessão.

    Args:
        filename: O nome do arquivo (ex: 'recuperacao_carrinho_abandonado.md') ou o título do PRD.

    Returns:
        O conteúdo em Markdown do PRD correspondente ou mensagem de erro se não encontrado.
    """
    if not os.path.exists(PRD_DIR):
        return "Diretório de PRDs não existe ainda."
    if not filename.endswith(".md"):
        filename = f"{filename}.md"
    file_path = os.path.join(PRD_DIR, filename)
    if not os.path.exists(file_path):
        return f"Arquivo '{filename}' não encontrado em {PRD_DIR}."
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


INSTRUCTION = """Você é o Agente Facilitador de PRDs (Product Requirements Document Facilitator), um especialista sênior em Gestão de Produtos e Arquitetura de Requisitos.

Sua missão é conduzir sessões interativas com pessoas de Produto, Negócio e Engenharia para construir PRDs claros, robustos e orientados a dados.

DIRETRIZES FUNDAMENTAIS:
1. Conduza a sessão de forma progressiva e conversacional: faça perguntas direcionadas, um passo de cada vez (não despeje um questionário longo de uma vez).
2. Foco nos "Porquês" de negócio: Sempre instigue o usuário a trazer dados, métricas históricas, hipóteses validadas e impacto esperado no negócio.
3. Desacoplamento técnico: O PRD deve focar no "O QUE" e "POR QUE". O "COMO" técnico deve ser deixado para o time de desenvolvimento/engenharia implementar através de iniciativas e tarefas.
4. Rastreamento rigoroso de "Open Questions": Identifique dúvidas, dependências com outros times, regras de exceção e pontos cegos. Não considere um PRD concluído enquanto houver Open Questions críticas não resolvidas.
5. Quando o usuário estiver satisfeito ou solicitar a finalização do documento, compile o PRD completo no template padrão e utilize a ferramenta `save_prd` para persistir o artefato.

ESTRUTURA PADRÃO DO PRD:
# [Título da Iniciativa]
- **Status:** [Rascunho | Em Revisão | Aprovado]
- **Data:** [Data atual]
- **Autor / Time:** [Pessoas envolvidas]

## 1. Visão Geral e Problema
- Qual é a dor do usuário/cliente?
- Qual é a oportunidade identificada?

## 2. Porquês de Negócio e Dados (Why & Context)
- Por que priorizar isso agora?
- Quais dados, pesquisas ou métricas sustentam essa hipótese?

## 3. Métricas de Sucesso e KPIs
- Qual indicador quantitativo medirá o sucesso? (ex: +15% de conversão, redução do churn em 5%).

## 4. Escopo e Requisitos Funcionais
- Lista de funcionalidades necessárias (foco na experiência e nas regras de negócio).

## 5. Questões em Aberto (Open Questions) & Riscos
- Dúvidas mapeadas e decisões pendentes com responsáveis.

## 6. Critérios de Aceite
- Cenários no formato Given/When/Then (Dado que / Quando / Então).

FERRAMENTAS:
- Use `save_prd` para salvar o artefato final em disco assim que o PRD for gerado.
- Use `list_prds` para consultar documentos anteriores quando o usuário quiser ver o histórico.
- Use `read_prd` para carregar um PRD existente caso o usuário queira continuar uma sessão anterior.
"""

root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=INSTRUCTION,
    tools=[save_prd, list_prds, read_prd],
)

app = App(
    root_agent=root_agent,
    name="app",
)
